# -*- coding: utf-8 -*-
import json, re, html

ROWS_PATH = r"C:/Users/alfas/AppData/Local/Temp/claude/C--Users-alfas-Documents-git1-mattpocock-skills/e679f719-93f4-4bf9-b294-3a7af8074a0a/scratchpad/rows.json"
OUT_PATH = r"C:/Users/alfas/AppData/Local/Temp/claude/C--Users-alfas-Documents-git1-mattpocock-skills/e679f719-93f4-4bf9-b294-3a7af8074a0a/scratchpad/skills-overview.html"

rows = json.load(open(ROWS_PATH, encoding='utf-8'))

LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
CODE_RE = re.compile(r'`([^`]+)`')
BR_TOKEN = '\x00BR\x00'

def inline_md(text, base_href_prefix=None):
    # protect literal <br> already in source
    text = text.replace('<br>', BR_TOKEN)
    # extract & protect markdown links first (label, href) -> tokens
    links = []
    def link_sub(m):
        links.append((m.group(1), m.group(2)))
        return f'\x01LINK{len(links)-1}\x01'
    text = LINK_RE.sub(link_sub, text)
    # extract & protect inline code
    codes = []
    def code_sub(m):
        codes.append(m.group(1))
        return f'\x01CODE{len(codes)-1}\x01'
    text = CODE_RE.sub(code_sub, text)
    # escape remaining plain text
    text = html.escape(text, quote=False)
    # restore code spans (escaped)
    for i, c in enumerate(codes):
        text = text.replace(f'\x01CODE{i}\x01', f'<code>{html.escape(c, quote=False)}</code>')
    # restore links (escaped label; href passed through, mostly relative repo paths)
    for i, (label, href) in enumerate(links):
        full_href = href
        text = text.replace(f'\x01LINK{i}\x01', f'<a href="{html.escape(full_href, quote=True)}" target="_blank" rel="noopener">{html.escape(label, quote=False)}</a>')
    text = text.replace(BR_TOKEN, '<br>')
    return text

CATEGORY_RE = re.compile(r'^([a-zA-Z\-]+)(?:（(.+)）)?$')

def parse_category(cat):
    m = CATEGORY_RE.match(cat.strip())
    if not m:
        return cat, None
    main, sub = m.group(1), m.group(2)
    return main, sub

CAT_LABELS = {
    'mattpocock': 'mattpocock',
    'built-in': 'built-in',
    'plugin': 'plugin',
}

INV_LABELS = {
    'U': ('U', 'ユーザー起動'),
    'M': ('M', 'モデル起動'),
    'U?': ('U?', 'ユーザー起動（推定）'),
    'M?': ('M?', 'モデル起動（推定）'),
}

records = []
for r in rows:
    skill_raw, inv, summary_raw, ja_raw, cat_raw, en_raw = r
    main_cat, sub_cat = parse_category(cat_raw)
    inv_code = inv.strip()
    records.append({
        'skill_html': inline_md(skill_raw),
        'skill_text': re.sub(r'[\[\]`]', '', LINK_RE.sub(lambda m: m.group(1), skill_raw)),
        'inv_code': inv_code,
        'summary_html': inline_md(summary_raw),
        'summary_text': CODE_RE.sub(r'\1', summary_raw),
        'ja_html': inline_md(ja_raw),
        'ja_text': CODE_RE.sub(r'\1', ja_raw),
        'en_html': inline_md(en_raw),
        'en_text': CODE_RE.sub(r'\1', en_raw).replace('<br>', ' '),
        'main_cat': main_cat,
        'sub_cat': sub_cat or '',
    })

print(f"built {len(records)} records")

# ---- category counts for legend ----
from collections import Counter
main_counts = Counter(r['main_cat'] for r in records)
print(main_counts)

with open(r"C:/Users/alfas/AppData/Local/Temp/claude/C--Users-alfas-Documents-git1-mattpocock-skills/e679f719-93f4-4bf9-b294-3a7af8074a0a/scratchpad/records.json", 'w', encoding='utf-8') as f:
    json.dump(records, f, ensure_ascii=False, indent=1)
print("wrote records.json")
