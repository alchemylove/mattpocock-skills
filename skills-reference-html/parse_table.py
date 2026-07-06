import re, json

src = r"C:/Users/alfas/Documents/git1/mattpocock-skills/docs/skills-overview.ja.md"
text = open(src, encoding='utf-8').read()
lines = text.splitlines()

start = None
for i, l in enumerate(lines):
    if l.strip().startswith('| skill |'):
        start = i
        break
assert start is not None

PLACEHOLDER = '\x00PIPE\x00'

def split_row(line):
    protected = line.replace('\\|', PLACEHOLDER)
    parts = protected.strip().strip('|').split('|')
    parts = [p.strip().replace(PLACEHOLDER, '|') for p in parts]
    return parts

rows = []
i = start + 2
while i < len(lines) and lines[i].strip().startswith('|'):
    parts = split_row(lines[i])
    if len(parts) == 6:
        rows.append(parts)
    else:
        print("SKIPPED (cols=%d): %s" % (len(parts), lines[i][:80]))
    i += 1

print(f"parsed {len(rows)} rows")
out_path = r"C:/Users/alfas/Documents/git1/mattpocock-skills/skills-reference-html/rows.json"
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(rows, f, ensure_ascii=False, indent=1)
print("wrote", out_path)
