# Revision storage and restoration

Use the personal archive at `~/.agents/profiles/` for discovery, saving, comparison, and restoration across projects. Prepare a separate temporary tree containing:

- `common/` with the selected original files at repository-relative paths, including the resources of each skill. For an intentional common edit, preserve the original baseline revision first.
- `variants/<key>/` with only the differing files or skill resources. Keep the logical path unchanged. Unchanged resources still resolve through the common mapping.
- `manifest.json` with a `models` object: each exact model ID maps logical file paths to relative files inside this revision. Include every managed resource in each model's effective mapping. Record client scopes separately. Include concise split decisions with the relevant passage, official URL and section, model scope, and test status. Keep volatile timestamps and run logs outside the snapshot; preserve stable ordering and reuse existing decision text when evidence and content are unchanged.

Compare with the previous revision and preserve its entries outside the observed scope. Save the prepared tree with this skill's `scripts/save_revision.py PREPARED` from any working directory (run it with Python 3 using the script's actual path). The helper validates referenced files, reuses an identical latest revision, and publishes a complete new directory on change. If another writer publishes the same revision number first, reconcile against the new latest revision before retrying. Compare or restore by resolving the saved mappings, including supporting resources. Restore only the requested revision, paths, and destination after checking local edits.
