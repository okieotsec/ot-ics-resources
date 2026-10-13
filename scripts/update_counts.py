# SPDX-License-Identifier: MIT
"""Refresh derived counts without changing resource review dates."""
import json
from catalog import ROOT, load

data = load()
data['counts'] = {
    'free': sum(r['cost_group'] == 'free' for r in data['resources']),
    'paid': sum(r['cost_group'] == 'paid' for r in data['resources']),
    'total': len(data['resources']),
}
(ROOT / 'resources.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Refreshed counts:', data['counts'])
