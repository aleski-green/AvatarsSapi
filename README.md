# AvatarsSapi

A collection of browser-based Sapi tools. Open `index.html` or serve this directory with `python3 -m http.server 4174 --bind 127.0.0.1`.

| Module | Entry point | Purpose |
| --- | --- | --- |
| Expressions | [index.html](index.html) | Generate individual Sapi kaomoji avatars. |
| Groups | [groups.html](groups.html) | Generate group avatars with highlighted leaders. |
| Workspace | [workspace/index.html](workspace/index.html) | Explore a clickable agent workspace with dummy data, customizable tabs, and shared computer locks. |

The Workspace module is a frontend prototype with local browser persistence. Agent execution, connected apps, schedules, and computer control are simulated. See [Workspace documentation](workspace/README.md) for interactions and scope. A portable single-file version is included at [workspace/sapi-prototype.html](workspace/sapi-prototype.html).

## Shared style

All three modules use [assets/sapi-theme.css](assets/sapi-theme.css), adapted from [sapiens4.rent](https://sapiens4.rent/): warm gray surfaces, dark navy text, Space Mono body type, Orbitron headings, magenta and violet accents, and fine borders. Generated avatar artwork keeps its existing pastel palettes and export behavior.

The generators share a module navigation bar. Workspace includes the same destinations in the grid-icon menu beside its logo. Workspace panel toggles, compact spacing, readable chat text, and shared-computer footer are retained.

Run `python3 build-prototype.py` after changing the workspace or shared theme to rebuild its portable HTML. The bundle includes both stylesheets and the workspace JavaScript; web fonts have local fallback fonts.

Verified desktop and 320px/390px layouts, expression controls, group peer creation and renaming, module navigation, workspace panel toggles, and JavaScript syntax.

## Shared group avatars

`assets/group-avatar.js` contains the Groups module’s weighted Voronoi renderer. Both the Groups editor and Workspace group identities use it; the portable workspace bundles it as well. Workspace provides All / Sapis / Groups filters and clickable `@Name` mentions that navigate to the matching individual or group conversation.
