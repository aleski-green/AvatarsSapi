#!/usr/bin/env python3
"""Bundle the workspace source and shared theme into the portable HTML."""
from pathlib import Path

root = Path(__file__).resolve().parent
workspace = root / 'workspace'
html = (workspace / 'index.html').read_text()
for href, path in [('styles.css', workspace / 'styles.css'), ('../assets/sapi-theme.css', root / 'assets/sapi-theme.css')]:
    html = html.replace(f'<link rel="stylesheet" href="{href}">', '<style>\n' + path.read_text() + '\n</style>')
html = html.replace('<script src="app.js"></script>', '<script>\n' + (workspace / 'app.js').read_text() + '\n</script>')
(workspace / 'sapi-prototype.html').write_text(html)
print('Built workspace/sapi-prototype.html')
