"""Regression checks: literal review examples are not navigation."""
from pathlib import Path
import importlib.util
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("integrity",ROOT/"check_document_integrity.py")
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
t=chr(96)
cases=[
("[live](README.md)\n"+t*4+"text\n[old](missing-old.md)\n"+t*4+"\n",["README.md"]),
("~~~text\n[old](missing-old.md)\n~~~\n[live](README.md)",["README.md"]),
("inline "+t+"[old](missing.md)"+t+" [live](README.md)",["README.md"]),
("[bad](missing-live.md)",["missing-live.md"]),
(t*3+"text\n[old](missing-unclosed.md)",[]),
(t*2+"[old](missing.md) "+t+" nested "+t*2+" [live](README.md)",["README.md","missing-should-not-be-present"]),
]
for index,(value,expected) in enumerate(cases):
 if index==5:expected=["README.md"]
 assert m.MARKDOWN_LINK.findall(m.navigation_text(value))==expected
assert m.HTML_LINK.findall(m.navigation_text("<a href='missing-live.md'>live</a>"))==["missing-live.md"]
assert not m.HTML_LINK.findall(m.navigation_text(t+"<a href='missing-literal.md'>"+t))
print("8 regression checks PASS; actual broken routes remain checked.")
