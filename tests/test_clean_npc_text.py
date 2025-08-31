import types
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "Finale Speaker"
content = path.read_text(encoding="utf-8")
start = content.index("TAG_RE")
end = content.index("# ---------- Worker thread ----------")
snippet = "import re\nfrom typing import Optional\n" + content[start:end]
module = types.ModuleType("finale_speaker_clean")
exec(snippet, module.__dict__)
clean_npc_text = module.clean_npc_text


def test_clean_npc_text_unlimited():
    text = "Bonjour. Salut."
    assert clean_npc_text(text) == "Bonjour. Salut."


def test_clean_npc_text_limit():
    text = "Bonjour. Salut."
    assert clean_npc_text(text, max_sentences=1) == "Bonjour."
