"""Save a prepared profile tree, reusing the latest revision on identical input."""

import argparse
import filecmp
import json
import os
import re
import shutil
import tempfile
from pathlib import Path


def same_tree(left, right):
    left_paths = {p.relative_to(left) for p in left.rglob("*")}
    right_paths = {p.relative_to(right) for p in right.rglob("*")}
    if left_paths != right_paths:
        return False
    for path in left_paths:
        a, b = left / path, right / path
        if a.is_dir() != b.is_dir():
            return False
        if a.is_file() and not filecmp.cmp(a, b, shallow=False):
            return False
    return True


def save(prepared, store):
    prepared, store = prepared.resolve(), store.resolve()
    if prepared == store or prepared in store.parents or store in prepared.parents:
        raise ValueError("Use separate preparation and archive directories.")
    if any(p.is_symlink() for p in prepared.rglob("*")):
        raise ValueError("Snapshot the selected files, not links to live files.")
    manifest = json.loads((prepared / "manifest.json").read_text())
    for models, files in manifest["models"].items():
        if not models or not files:
            raise ValueError("Each model needs a nonempty file mapping.")
        for reference in files.values():
            target = (prepared / reference).resolve()
            if Path(reference).is_absolute() or prepared not in target.parents or not target.is_file():
                raise ValueError(f"Invalid snapshot reference: {reference}")
    if not manifest["models"]:
        raise ValueError("No verified models in the manifest.")
    store.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=store) as temp:
        staged = Path(temp) / "snapshot"
        shutil.copytree(prepared, staged)
        revisions = [int(p.name[1:]) for p in store.iterdir()
                     if p.is_dir() and re.fullmatch(r"v[1-9][0-9]*", p.name)]
        latest = max(revisions, default=0)
        if latest and same_tree(staged, store / f"v{latest}"):
            return store / f"v{latest}"
        destination = store / f"v{latest + 1}"
        os.rename(staged, destination)
        return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prepared", type=Path)
    parser.add_argument("store", type=Path, nargs="?", default=Path.home() / ".agents" / "profiles",
                        help="Archive directory (default: ~/.agents/profiles)")
    args = parser.parse_args()
    print(save(args.prepared, args.store))
