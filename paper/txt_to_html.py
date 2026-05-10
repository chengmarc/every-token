"""
Converts tokens/cl100k_base.txt to a print-ready HTML file.
Open the output in a browser and Ctrl+P -> Save as PDF.
"""

from pathlib import Path

src  = Path(__file__).parent / "../tokens/cl100k_base.txt"
dest = Path(__file__).parent / "appendix.html"

lines = src.read_text(encoding="utf-8").splitlines()

entries = []
for line in lines:
    parts = line.split(None, 1)
    if len(parts) == 2:
        tid, display = parts[0].strip(), parts[1].strip()
        # escape HTML special chars
        display = (display
                   .replace("&", "&amp;")
                   .replace("<", "&lt;")
                   .replace(">", "&gt;"))
        entries.append(f'<span class="entry">[{tid}] {display}</span>')

body = "\n".join(entries)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Appendix A: Complete Token Listing</title>
<style>
  @page {{
    size: letter;
    margin: 1.5cm;
  }}
  body {{
    font-family: 'Cascadia Mono', 'Courier New', 'MS Gothic',
                 'Malgun Gothic', 'Microsoft YaHei', monospace;
    font-size: 7pt;
    line-height: 1.4;
    columns: 2;
    column-gap: 1cm;
  }}
  h1 {{
    column-span: all;
    font-size: 14pt;
    margin-bottom: 0.5cm;
    font-family: serif;
  }}
  .entry {{
    display: inline;
    white-space: pre;
  }}
  .entry::after {{
    content: "  ";
    white-space: pre;
  }}
</style>
</head>
<body>
<h1>Appendix A: Complete Token Listing</h1>
{body}
</body>
</html>
"""

dest.write_text(html, encoding="utf-8")
print(f"Done -> {dest}")
print("Open in Chrome/Edge, Ctrl+P, 'Save as PDF', uncheck headers/footers.")
