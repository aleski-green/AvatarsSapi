# Sapi workspace prototype

A clickable three-panel agent workspace with sample data. Open the portable `sapi-prototype.html` directly. The editable source is split into `index.html`, `styles.css`, and `app.js`. To serve the source locally, use `python3 -m http.server 4173 --bind 127.0.0.1` from this directory.

The interface shares [the repository theme](../assets/sapi-theme.css), based on [sapiens4.rent](https://sapiens4.rent/): warm gray surfaces, dark navy monospace text, geometric headings, fine borders, and magenta/violet accents. Pastel kaomoji avatars retain the original generator’s expressions and radial lighting. Rebuild the portable HTML from the repository root with `python3 build-prototype.py`.

## Explore

- Use the three header icons to show or hide the chat list, chat, and workspace independently. Panel visibility saves locally.
- The CORPORA footer shows only the shared computer, its current controller, or its last user when available.

- Switch between All, Sapis (individual agents), and Groups; search, create a Sapi or group, or adjust autonomy.
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

## Compact layout update

The header uses `sapi*4 ◠‿◠ AI`, with workspace branding and promotional copy removed. The sidebar keeps CORPORA, view tabs, search, add-agent control, conversations, and shared-computer status. Chat text is 15px, previews 13px, and the desktop header is 48px high. All three panes fit side by side at a 968px viewport. Below 900px, remaining panels reflow without shrinking the text.

Verified panel visibility and restoration, persistence after reload, readable font sizes, and horizontal fit at 968px, 390px, and 320px.

## Group identities and mentions

Groups use the same weighted Voronoi renderer as the Groups editor, shared in `assets/group-avatar.js`. Designers is a group; Jared, Aaron, SlackTwin, and Scout are individual Sapis. This classification is separate from an agent’s earlier personal/team scope. Existing local data is migrated without resetting conversations or workspace tabs.

Known names and `@Name` mentions in conversations, activity details, documents, task owners, and computer ownership/queues open the matching chat. Mentions reveal a hidden chat panel and switch the list filter when necessary. The computer footer has separate controls for opening the computer and opening its current or last controller’s chat. Conversation drafts are retained when switching chats.
