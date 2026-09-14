# Sapi workspace prototype

A clickable three-panel agent workspace with sample data. Open the portable `sapi-prototype.html` directly. The editable source is split into `index.html`, `styles.css`, and `app.js`. To serve the source locally, use `python3 -m http.server 4173 --bind 127.0.0.1` from this directory.

The visual system follows the supplied [Sapi avatar generator](https://github.com/aleski-green/AvatarsSapi/tree/codex/sapi-kaomoji-expressions): ink `#151719`, warm paper `#f1ede3`, golden haze `#fdd997`, pastel backgrounds, outlined circular kaomoji, bold typography, and offset shadows. Avatars use the generator’s expressions and radial lighting treatment in CSS.

## Explore

- Switch between personal and team agents, search, create a Sapi, or adjust its autonomy.
- Send a chat message. Status, computer, and document prompts have sample responses; other prompts create demo tasks. Autonomous tasks execute after a short simulated delay.
- Inspect Tasks, Log, and Cron. Create and run a task or schedule; pause and edit schedules.
- Add, close, rename, and rearrange workspace tabs. Drag tabs, or use the tab menu’s move buttons. Website tabs save bookmarks and open externally.
- Take the shared computer lock, pause its session, add agents to the queue, or hand control to the next agent. Finishing a task hands off the lock if that agent is the current controller.
- Edit and export the kickoff document, inspect sample pull requests, post to a mock Slack channel, and toggle demo connections.
- Use the AP menu to reset local data.

## Scope

No backend, language model, actual computer control, account connection, or scheduled background execution is included. All work and external application screens are simulated. Data persists in browser local storage. Schedule runs are triggered with **Run now**; website tabs are bookmarks rather than embedded remote browsers. Google Fonts is optional; system fonts provide a fallback.

The left panel provides identity and team scope, the middle panel provides instructions and execution history, and the right panel preserves the user’s working context in customizable tabs. A single computer owner and an explicit queue make shared control visible without requiring confirmation for every agent action.

## Verification

Checked in the browser: computer takeover, release, handoff, and pause/resume; autonomous chat-to-task completion; creating an agent; adding, renaming, and moving tabs; document editing and persistence after reload; creating, pausing, and manually running schedules. Inspected desktop and phone layouts and checked horizontal fit at 320px and 390px. JavaScript syntax validation passed, with no browser console errors in the checked flows.
