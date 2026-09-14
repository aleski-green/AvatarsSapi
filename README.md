# AvatarsSapi

A collection of browser-based Sapi tools. Open `index.html` or serve this directory with `python3 -m http.server 4174 --bind 127.0.0.1`.

| Module | Entry point | Purpose |
| --- | --- | --- |
| Expressions | [index.html](index.html) | Generate individual Sapi kaomoji avatars. |
| Groups | [groups.html](groups.html) | Generate group avatars with highlighted leaders. |
| Workspace | [workspace/index.html](workspace/index.html) | Explore a clickable agent workspace with dummy data, customizable tabs, and shared computer locks. |

The Workspace module is a frontend prototype with local browser persistence. Agent execution, connected apps, schedules, and computer control are simulated. See [Workspace documentation](workspace/README.md) for interactions and scope. A portable single-file version is included at [workspace/sapi-prototype.html](workspace/sapi-prototype.html).
