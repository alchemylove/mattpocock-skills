# -*- coding: utf-8 -*-
import json, html

RECORDS_PATH = r"C:/Users/alfas/Documents/git1/mattpocock-skills/.claude/scratch/skills-overview-html/records.json"
OUT_PATH = r"C:/Users/alfas/Documents/git1/mattpocock-skills/.claude/scratch/skills-overview-html/skills-overview.html"

records = json.load(open(RECORDS_PATH, encoding='utf-8'))

INV_META = {
    'U':  ('U', 'ユーザー起動'),
    'M':  ('M', 'モデル起動'),
    'U?': ('U?', 'ユーザー起動（推定）'),
    'M?': ('M?', 'モデル起動（推定）'),
}

CAT_META = {
    'mattpocock': 'mattpocock',
    'built-in': 'built-in',
    'plugin': 'plugin',
}

def esc_attr(s):
    return html.escape(s, quote=True)

rows_html = []
for r in records:
    inv_code, inv_title = INV_META.get(r['inv_code'], (r['inv_code'], r['inv_code']))
    cat_class = r['main_cat']
    cat_label = CAT_META.get(r['main_cat'], r['main_cat'])
    sub = r['sub_cat']
    search_blob = ' '.join([
        r['skill_text'], r['summary_text'], r['ja_text'], r['en_text'], r['main_cat'], r['sub_cat']
    ]).lower()

    cat_chip = f'<span class="chip chip-{cat_class}">{esc_attr(cat_label)}</span>'
    if sub:
        cat_chip += f'<span class="cat-sub">{html.escape(sub)}</span>'

    row = f'''
      <tr class="row" data-cat="{cat_class}" data-search="{esc_attr(search_blob)}">
        <td data-label="skill"><div class="cell-skill">{r['skill_html']}</div></td>
        <td data-label="起動"><span class="badge badge-{inv_code.replace('?','q')}" title="{esc_attr(inv_title)}">{inv_code}</span></td>
        <td data-label="概要"><div class="cell-summary">{r['summary_html']}</div></td>
        <td data-label="日本語訳"><div class="cell-ja">{r['ja_html']}</div></td>
        <td data-label="種別">{cat_chip}</td>
        <td data-label="英語訳"><div class="cell-en">{r['en_html']}</div></td>
      </tr>'''
    rows_html.append(row)

rows_joined = '\n'.join(rows_html)
count_total = len(records)

HTML_TEMPLATE = r"""<title>Skills 一覧 — mattpocock-skills</title>
<style>
  :root {
    --bg: #f4f6f8;
    --surface: #ffffff;
    --surface-2: #eceff3;
    --text: #1b222b;
    --text-muted: #5b6672;
    --border: #dde2e8;
    --accent: #2f6f86;
    --accent-contrast: #ffffff;
    --accent-soft: #e2eef1;
    --chip-mattpocock-bg: #e2f0ec;
    --chip-mattpocock-text: #1f6f5c;
    --chip-built-in-bg: #e8ebfb;
    --chip-built-in-text: #43449c;
    --chip-plugin-bg: #fdece0;
    --chip-plugin-text: #b1560f;
    --badge-u-bg: #e2eef1;
    --badge-u-text: #1f5c72;
    --badge-m-bg: #f1e9f8;
    --badge-m-text: #6a3f9e;
    --shadow: 0 1px 2px rgba(20, 30, 40, 0.06), 0 8px 24px rgba(20, 30, 40, 0.05);
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #12161b;
      --surface: #1a1f26;
      --surface-2: #20262e;
      --text: #e8ecf1;
      --text-muted: #97a2ad;
      --border: #2b323b;
      --accent: #7fc2d6;
      --accent-contrast: #0d1114;
      --accent-soft: #1c343b;
      --chip-mattpocock-bg: #163a32;
      --chip-mattpocock-text: #7fe0c4;
      --chip-built-in-bg: #262a52;
      --chip-built-in-text: #b9bdf5;
      --chip-plugin-bg: #402615;
      --chip-plugin-text: #f5b988;
      --badge-u-bg: #163a45;
      --badge-u-text: #a9dcec;
      --badge-m-bg: #35284a;
      --badge-m-text: #d9c2f5;
      --shadow: 0 1px 2px rgba(0, 0, 0, 0.3), 0 8px 24px rgba(0, 0, 0, 0.35);
    }
  }
  :root[data-theme="dark"] {
    --bg: #12161b; --surface: #1a1f26; --surface-2: #20262e; --text: #e8ecf1; --text-muted: #97a2ad;
    --border: #2b323b; --accent: #7fc2d6; --accent-contrast: #0d1114; --accent-soft: #1c343b;
    --chip-mattpocock-bg: #163a32; --chip-mattpocock-text: #7fe0c4;
    --chip-built-in-bg: #262a52; --chip-built-in-text: #b9bdf5;
    --chip-plugin-bg: #402615; --chip-plugin-text: #f5b988;
    --badge-u-bg: #163a45; --badge-u-text: #a9dcec; --badge-m-bg: #35284a; --badge-m-text: #d9c2f5;
    --shadow: 0 1px 2px rgba(0,0,0,.3), 0 8px 24px rgba(0,0,0,.35);
  }
  :root[data-theme="light"] {
    --bg: #f4f6f8; --surface: #ffffff; --surface-2: #eceff3; --text: #1b222b; --text-muted: #5b6672;
    --border: #dde2e8; --accent: #2f6f86; --accent-contrast: #ffffff; --accent-soft: #e2eef1;
    --chip-mattpocock-bg: #e2f0ec; --chip-mattpocock-text: #1f6f5c;
    --chip-built-in-bg: #e8ebfb; --chip-built-in-text: #43449c;
    --chip-plugin-bg: #fdece0; --chip-plugin-text: #b1560f;
    --badge-u-bg: #e2eef1; --badge-u-text: #1f5c72; --badge-m-bg: #f1e9f8; --badge-m-text: #6a3f9e;
    --shadow: 0 1px 2px rgba(20,30,40,.06), 0 8px 24px rgba(20,30,40,.05);
  }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Hiragino Sans", "Yu Gothic", system-ui, sans-serif;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  .page {
    margin: 0 auto;
    padding: 2rem 1.25rem 4rem;
  }

  header.hero {
    display: flex;
    flex-direction: column;
    gap: 0.9rem;
    margin-bottom: 1.75rem;
  }

  h1 {
    font-size: clamp(1.5rem, 1.1rem + 1.4vw, 2.1rem);
    font-weight: 700;
    letter-spacing: -0.015em;
    margin: 0;
    text-wrap: balance;
  }

  .subtitle {
    color: var(--text-muted);
    max-width: 68ch;
    margin: 0;
    font-size: 0.98rem;
  }

  .legend {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1.25rem;
    align-items: center;
    font-size: 0.85rem;
    color: var(--text-muted);
  }

  .legend-group {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    flex-wrap: wrap;
  }

  .legend-label {
    font-weight: 600;
    color: var(--text);
    margin-right: 0.15rem;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-width: 1.9em;
    padding: 0.12em 0.5em;
    border-radius: 999px;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.01em;
  }
  .badge-U { background: var(--badge-u-bg); color: var(--badge-u-text); }
  .badge-M { background: var(--badge-m-bg); color: var(--badge-m-text); }
  .badge-Uq { background: var(--badge-u-bg); color: var(--badge-u-text); opacity: 0.72; }
  .badge-Mq { background: var(--badge-m-bg); color: var(--badge-m-text); opacity: 0.72; }

  .chip {
    display: inline-flex;
    align-items: center;
    padding: 0.15em 0.65em;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    white-space: nowrap;
  }
  .chip-mattpocock { background: var(--chip-mattpocock-bg); color: var(--chip-mattpocock-text); }
  .chip-built-in { background: var(--chip-built-in-bg); color: var(--chip-built-in-text); }
  .chip-plugin { background: var(--chip-plugin-bg); color: var(--chip-plugin-text); }

  .cat-sub {
    display: block;
    font-size: 0.75rem;
    color: var(--text-muted);
    margin-top: 0.2rem;
  }

  .controls {
    position: sticky;
    top: 0;
    z-index: 5;
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    align-items: center;
    background: var(--bg);
    padding: 0.75rem 0;
    margin-bottom: 0.25rem;
    border-bottom: 1px solid var(--border);
  }

  .search {
    flex: 1 1 240px;
    min-width: 0;
  }

  .search input {
    width: 100%;
    padding: 0.55rem 0.85rem;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text);
    font-size: 0.92rem;
  }
  .search input:focus {
    outline: 2px solid var(--accent);
    outline-offset: 1px;
  }

  .filters {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
  }

  .filter-btn {
    border: 1px solid var(--border);
    background: var(--surface);
    color: var(--text);
    border-radius: 999px;
    padding: 0.4rem 0.85rem;
    font-size: 0.82rem;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.15s ease, color 0.15s ease, border-color 0.15s ease;
  }
  .filter-btn:hover { border-color: var(--accent); }
  .filter-btn[aria-pressed="true"] {
    background: var(--accent);
    border-color: var(--accent);
    color: var(--accent-contrast);
  }
  .filter-btn:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
  }

  .count {
    font-size: 0.82rem;
    color: var(--text-muted);
    font-variant-numeric: tabular-nums;
    margin-left: auto;
  }

  /* Real table, sized to the container — no min-width, so it never
     forces horizontal scroll. Columns are fixed percentages and cell
     text wraps instead of pushing the table wider than its box. */
  .table-scroll {
    border: 1px solid var(--border);
    border-radius: 14px;
    background: var(--surface);
    box-shadow: var(--shadow);
    overflow: hidden;
  }

  table {
    width: 100%;
    table-layout: fixed;
    border-collapse: collapse;
  }

  col.col-skill { width: 15%; }
  col.col-inv { width: 6%; }
  col.col-summary { width: 15%; }
  col.col-ja { width: 27%; }
  col.col-cat { width: 10%; }
  col.col-en { width: 27%; }

  thead th {
    background: var(--surface-2);
    color: var(--text-muted);
    text-align: left;
    font-size: 0.74rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    padding: 0.7rem 0.8rem;
    border-bottom: 1px solid var(--border);
  }

  tbody td {
    padding: 0.75rem 0.8rem;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    font-size: 0.85rem;
    overflow-wrap: break-word;
    word-break: break-word;
  }

  tbody tr:last-child td { border-bottom: none; }
  tbody tr:nth-child(even) { background: var(--surface-2); }
  tbody tr.hidden { display: none; }

  td[data-label="概要"] { color: var(--text); font-weight: 600; }
  td[data-label="英語訳"] { color: var(--text-muted); }

  a { color: var(--accent); text-decoration: none; }
  a:hover { text-decoration: underline; }
  code {
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    background: var(--surface-2);
    padding: 0.05em 0.35em;
    border-radius: 5px;
    font-size: 0.92em;
    overflow-wrap: break-word;
  }

  .cell-skill code { background: transparent; padding: 0; }

  .empty-state {
    display: none;
    padding: 2.5rem 1rem;
    text-align: center;
    color: var(--text-muted);
  }
  .empty-state.visible { display: block; }

  footer.note {
    margin-top: 1.5rem;
    font-size: 0.8rem;
    color: var(--text-muted);
  }

  /* Narrow viewports: same data, stacked as cards instead of a table row —
     still no horizontal scroll, just a different reading direction. */
  @media (max-width: 720px) {
    .page { padding: 1.25rem 0.85rem 3rem; }
    table { display: block; width: 100%; table-layout: auto; }
    colgroup, col { display: none; }
    thead { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
    tbody { display: flex; flex-direction: column; gap: 0.6rem; padding: 0.6rem; }
    tbody tr {
      display: block;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 0.85rem 0.9rem 0.95rem;
    }
    tbody tr:nth-child(even) { background: var(--surface); }
    tbody td {
      display: block;
      padding: 0.28rem 0;
      border-bottom: none;
      font-size: 0.87rem;
    }
    td[data-label]::before {
      content: attr(data-label);
      display: block;
      font-size: 0.66rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-muted);
      margin-bottom: 0.15rem;
    }
    td[data-label="skill"] { font-size: 0.98rem; }
    td[data-label="skill"]::before { display: none; }
    td[data-label="起動"] { display: inline-block; margin-right: 0.5rem; }
    td[data-label="起動"]::before { display: none; }
    td[data-label="種別"] { display: inline-block; }
    td[data-label="種別"]::before { display: none; }
  }
</style>

<div class="page">
  <header class="hero">
    <h1>Skills 一覧</h1>
    <p class="subtitle">
      <code>mattpocock-skills</code> リポジトリを開いた Claude Code セッションで使える skill の一覧。
      <strong>種別</strong>で mattpocock リポジトリの skill（バケット別）・ビルトイン公式 skill・プラグイン skill を区別しています。
      mattpocock 系の skill は <code>scripts/link-skills.sh</code> 未実行のため現状すべて off（未リンク）です。
    </p>
    <div class="legend">
      <div class="legend-group">
        <span class="legend-label">起動:</span>
        <span class="badge badge-U">U</span> ユーザー起動
        <span class="badge badge-M">M</span> モデル起動
        <span style="opacity:.7">?＝推定（ビルトイン/プラグインは frontmatter 未確認）</span>
      </div>
      <div class="legend-group">
        <span class="legend-label">種別:</span>
        <span class="chip chip-mattpocock">mattpocock</span>
        <span class="chip chip-built-in">built-in</span>
        <span class="chip chip-plugin">plugin</span>
      </div>
    </div>
  </header>

  <div class="controls">
    <div class="search">
      <input type="text" id="searchInput" placeholder="skill 名・概要・説明で検索…" autocomplete="off">
    </div>
    <div class="filters" id="filterGroup">
      <button class="filter-btn" data-cat="mattpocock" aria-pressed="false" type="button">mattpocock (__MATTPOCOCK_COUNT__)</button>
      <button class="filter-btn" data-cat="built-in" aria-pressed="false" type="button">built-in (__BUILTIN_COUNT__)</button>
      <button class="filter-btn" data-cat="plugin" aria-pressed="false" type="button">plugin (__PLUGIN_COUNT__)</button>
    </div>
    <span class="count" id="countLabel">__TOTAL__ / __TOTAL__ 件</span>
  </div>

  <div class="table-scroll">
    <table>
      <colgroup>
        <col class="col-skill"><col class="col-inv"><col class="col-summary">
        <col class="col-ja"><col class="col-cat"><col class="col-en">
      </colgroup>
      <thead>
        <tr>
          <th>skill</th>
          <th>起動</th>
          <th>概要</th>
          <th>日本語訳</th>
          <th>種別</th>
          <th>英語訳</th>
        </tr>
      </thead>
      <tbody id="tbody">__ROWS__</tbody>
    </table>
    <div class="empty-state" id="emptyState">条件に一致する skill がありません。</div>
  </div>

  <footer class="note">
    全 __TOTAL__ 件（mattpocock __MATTPOCOCK_COUNT__ 件 / built-in __BUILTIN_COUNT__ 件 / plugin __PLUGIN_COUNT__ 件）。
    upstream <code>mattpocock/skills</code> の <code>272f99b</code>（main）に同期し、全 skill を日本語へ翻訳し直した直後の状態。
  </footer>
</div>

<script>
(function () {
  var searchInput = document.getElementById('searchInput');
  var rows = Array.prototype.slice.call(document.querySelectorAll('#tbody tr.row'));
  var buttons = Array.prototype.slice.call(document.querySelectorAll('.filter-btn'));
  var countLabel = document.getElementById('countLabel');
  var emptyState = document.getElementById('emptyState');
  var activeCats = new Set();

  function applyFilters() {
    var q = searchInput.value.trim().toLowerCase();
    var terms = q.split(/\s+/).filter(Boolean);
    var visible = 0;
    rows.forEach(function (row) {
      var cat = row.getAttribute('data-cat');
      var blob = row.getAttribute('data-search');
      var catOk = activeCats.size === 0 || activeCats.has(cat);
      var textOk = terms.every(function (t) { return blob.indexOf(t) !== -1; });
      var show = catOk && textOk;
      row.classList.toggle('hidden', !show);
      if (show) visible++;
    });
    countLabel.textContent = visible + ' / ' + rows.length + ' 件';
    emptyState.classList.toggle('visible', visible === 0);
  }

  searchInput.addEventListener('input', applyFilters);

  buttons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var cat = btn.getAttribute('data-cat');
      if (activeCats.has(cat)) {
        activeCats.delete(cat);
        btn.setAttribute('aria-pressed', 'false');
      } else {
        activeCats.add(cat);
        btn.setAttribute('aria-pressed', 'true');
      }
      applyFilters();
    });
  });
})();
</script>
"""

cat_counts = {'mattpocock': 0, 'built-in': 0, 'plugin': 0}
for r in records:
    cat_counts[r['main_cat']] = cat_counts.get(r['main_cat'], 0) + 1

out = HTML_TEMPLATE.replace('__ROWS__', rows_joined)
out = out.replace('__TOTAL__', str(count_total))
out = out.replace('__MATTPOCOCK_COUNT__', str(cat_counts['mattpocock']))
out = out.replace('__BUILTIN_COUNT__', str(cat_counts['built-in']))
out = out.replace('__PLUGIN_COUNT__', str(cat_counts['plugin']))

with open(OUT_PATH, 'w', encoding='utf-8') as f:
    f.write(out)

print('wrote', OUT_PATH, 'bytes:', len(out))
