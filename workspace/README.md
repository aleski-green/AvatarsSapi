# CORPORA UI lab

CORPORA provides the UI, dashboards, chats, workspaces, and settings for Sapiens4, a multi-agent organization of autonomous Sapis. This module is a frontend lab built with demo data: conversations, tasks, schedules, shared computer locks, and agent activity are simulated.

Open `index.html` through a local server, or open the portable `sapi-prototype.html`. Rebuild the portable file with `python3 build-prototype.py` from the repository root.

## Interface

- CORPORA contains All / Sapis / Groups, search, creation, chats, and the shared-computer footer.
- Group identities use the Groups module’s weighted Voronoi renderer in `assets/group-avatar.js`.
- Known names and `@Name` mentions open the matching chat and restore it if hidden. Drafts survive switching chats.
- The three header icons independently toggle the chat list, conversation, and workspace. The hamburger is a placeholder for a future menu.
- The light/dark button shares a saved preference with Expressions and Groups. Until explicitly chosen, it follows the system preference.
- Shared-computer controls open from the footer. The lock, queue, handoff, pause, and simulated autonomous execution remain available.

## Browser workspace

The heading is `@Name’s workspace`; clicking the name returns to its chat, including when only the workspace is expanded. Each Sapi/group keeps its own tabs. Existing local tab names and URLs are retained; old built-in mock screens become blank browser tabs. Existing conversations and tasks remain intact.

The content area is an unstyled iframe surface, blank by default. Add a blank tab, an HTTP(S) URL, or an HTML document. Tabs can be closed, renamed, edited, and reordered by drag or menu. The address field navigates the active tab, reload refreshes it, and the external link opens a URL outside the embed. Switching tabs/chat preserves live frames during the session; reload reconstructs them from saved URLs/HTML, not from a snapshot of guest runtime state.

Guest scripts are sandboxed without same-origin access to the shell. This is a browser-based prototype, not Electron or a native Chromium host. Some websites reject framing or require capabilities/authentication unavailable in a sandbox. Such sites can be opened through the external-link control. A native implementation should replace the iframe adapter with isolated WebContentsView instances and implement navigation/permissions in the host.

## Themes and guest pages

The shared shell theme does not inject CSS into guests. Generated documents can opt into `color-scheme: light dark` and `prefers-color-scheme` to follow the embedding color scheme while retaining their own design. Plain or hard-coded third-party pages may keep their original colors.

Cross-origin iframe CSS cannot be edited by the shell. Electron's `webContents.insertCSS()` allows a native host to add/remove an optional page override; this requires per-navigation lifecycle handling and cannot guarantee a good result on every site. Prefer a site's native theme or theme-aware generated HTML. The prototype does not claim to implement forced third-party theming.

## Scope and verification

There is no backend, LLM, real computer control, or background scheduler. Agent execution and schedules remain simulated; real supplied website content is embedded where permitted. Data persists in localStorage. Google Fonts is optional.

Verified light/dark switching, owner shortcut from an expanded workspace, per-owner tabs, tab persistence after reload, supplied HTML button interaction, URL document loading, and shared-computer controls. The new header fits narrow layouts. JavaScript syntax and diff whitespace checks pass.
