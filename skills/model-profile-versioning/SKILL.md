---
name: model-profile-versioning
description: Discover the user's available Codex models and reconcile personal instructions and skills with current official model guidance. Invoke without arguments to preserve shared defaults and version only justified per-file differences.
---

# Model Profile Versioning

A bare invocation runs the workflow below. Treat the selectable models as peers: a newly available model does not supersede setups still used by other sessions.

## Discover the setup

- Identify the current session model from session metadata or status if exposed. Record its source separately from the selectable models; a configured default is not proof of the current model.
- For each relevant client and account, use its model picker or its authenticated Codex app-server `model/list` (initialize the connection, omit hidden entries and follow every `nextCursor`). Compare desktop and CLI inventories only when both are accessible. Record client-specific availability. A public model catalog, an old local cache, a subscription name, and a CLI default do not establish access in the app.
- If only part of the inventory is visible, continue with confirmed models. Preserve previous mappings for clients or models not observed this time. If no model is verifiable, inspect the shared baseline, report the missing signal, and stop before writing a speculative revision. Do not require the user to name a model on an ordinary invocation.
- Resolve this installed skill's real path to find its owning repository even when invoked from another project. Inspect the managed global instructions and personal skills, supporting files, local registrations, active overrides, and the personal revision archive at `~/.agents/profiles/`. Compare installed copies with repository sources. If they diverge, preserve both and identify the discrepancy before choosing a baseline. Exclude unrelated workspace instructions, vendor skills, credentials, and transient files.

## Review the shared instructions and skill boundaries

Before considering model-specific variants, compare global rules, skill triggers, workflows, and deliverables. For each overlap, identify who needs the behavior and when. Keep universal response preferences in the global instructions. Keep task-specific decisions close to the skill that makes them. Preserve explicit user preferences even when general prompting advice favors a different default.

Merge skills only when the same requests reliably need the same workflow and outcome. For related tasks with distinct outcomes, clarify triggers and use a short handoff where necessary. Split independently invocable jobs when one skill tries to own both. If one job merely has extensive examples or occasional operational details, move those details into a linked reference. Length alone does not justify a new skill.

Check representative requests against the revised boundaries, retain resource links and installed names where possible, and report which overlaps were removed and why any proposed split or merge was made. Apply common improvements independently of access to a model inventory.

## Decide per file using official evidence

Fetch current OpenAI prompting, migration, or skill guidance for the confirmed models. Start with the provider's current model guide and follow applicable exact-model or family references. Retain the official page and section and identify which model the advice actually covers. If exact guidance is unavailable, reuse the common file and explain the uncertainty. Never assume that model names, release order, or a recommendation for one family establish a difference for another.

For each relevant passage ask: which existing instruction is affected, what behavior must it preserve, and would the same wording satisfy all confirmed models? Keep one common file when it works across models. Apply a generally useful simplification to the common candidate. Write a variant only when official guidance supports a concrete difference and the common wording would lose an intended behavior or conflict with an applicable recommendation. Share identical variants among compatible models. Observed failures inform testing; distinguish them from provider guidance. A short global instruction can stay shared even when one skill needs a variant.

## Save and compare revisions

Follow [revision storage and restoration](references/revisions.md) to preserve the original before common edits, publish a complete revision, compare inventories, or restore selected files. Include supporting resources and check repeat runs reuse identical revisions.

## Activation and reporting

An archive is not a Codex instruction discovery location. Preserve concurrent sessions: never swap a shared global file or retarget a personal skill symlink when selecting a model-specific variant. Verify the client-specific selection mechanism before claiming activation. An explicitly selected isolated workspace or launch environment can be an option only after verifying the effective instructions AND skill lookup in that environment, including collisions with user-wide skills. A CLI configuration profile or a model picker alone is not evidence of such routing. If isolated routing is unavailable, keep the common installation active and report the variants as saved only.

Report confirmed models by client, current model if known, shared files, concrete deviations with official sources, revision reused or created, and verified activation or remaining limitations. When possible test representative behavior using identical inputs. File checks and scenario fixtures verify version handling; they do not establish model quality.

Official discovery references: [model/list](https://learn.chatgpt.com/docs/app-server#list-models-modellist), [instruction lookup](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [skill lookup](https://learn.chatgpt.com/docs/build-skills).
