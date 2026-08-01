#!/usr/bin/env python3
"""Convert the markdown agent files in agents/ into Codex subagent TOML.

Usage:  python3 scripts/agents-to-codex-toml.py [outdir]

Default outdir is ~/.codex/agents. roster.md is copied through as-is — it is a
lookup table for the orchestrators, not an agent.
"""
import json
import pathlib
import re
import shutil
import sys

SRC = pathlib.Path(__file__).resolve().parent.parent / "agents"
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "~/.codex/agents").expanduser()


def field(meta: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", meta, re.M)
    return m.group(1).strip() if m else ""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for src in sorted(SRC.glob("*.md")):
        if src.name == "roster.md":
            shutil.copy(src, OUT / "roster.md")
            continue
        text = src.read_text()
        m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
        meta, body = (m.group(1), m.group(2).strip()) if m else ("", text.strip())

        description = f'{field(meta, "name")} — {field(meta, "role")}. {field(meta, "summary")}'
        if "'''" in body:
            sys.exit(f"{src}: body contains ''' and cannot be embedded in a TOML literal string")

        (OUT / f"{src.stem}.toml").write_text(
            f'name = "{src.stem}"\n'
            f"description = {json.dumps(description.strip(' —.') + '.')}\n"
            f"developer_instructions = '''\n{body}\n'''\n"
        )
        count += 1
    print(f"Wrote {count} agent TOML files + roster.md to {OUT}")


if __name__ == "__main__":
    main()
