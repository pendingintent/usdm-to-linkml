#!/usr/bin/env python
"""Generate the ER diagram and documentation from output/usdm.yaml.

Writes:
  output/usdm.erdiagram.md   Mermaid ER diagram (gen-erdiagram)
  output/docs/               Markdown documentation, one page per class/slot (gen-doc)

Run ``python scripts/generate_schema.py`` first so usdm.yaml is current.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"
SCHEMA = OUTPUT / "usdm.yaml"
ERD = OUTPUT / "usdm.erdiagram.md"
DOCS = OUTPUT / "docs"

# gen-doc lists "used by" classes in Python set order, which changes between
# runs. A fixed hash seed makes the output byte-for-byte reproducible so that
# regenerating does not create spurious diffs.
ENV = {**os.environ, "PYTHONHASHSEED": "0"}


def tool(name: str) -> str:
    """Path of a LinkML CLI installed next to the running interpreter."""
    candidate = Path(sys.executable).parent / name
    return str(candidate) if candidate.exists() else name


def main() -> int:
    if not SCHEMA.exists():
        sys.exit(f"{SCHEMA} not found; run scripts/generate_schema.py first")

    print("Generating ER diagram...")
    result = subprocess.run(
        [tool("gen-erdiagram"), str(SCHEMA)],
        env=ENV, check=True, capture_output=True, text=True,
    )
    ERD.write_text(result.stdout)
    print(f"  {ERD}")

    print("Generating documentation...")
    if DOCS.exists():
        shutil.rmtree(DOCS)  # drop pages for classes/slots that no longer exist
    subprocess.run(
        [tool("gen-doc"), str(SCHEMA), "-d", str(DOCS)],
        env=ENV, check=True, capture_output=True, text=True,
    )
    print(f"  {DOCS} ({sum(1 for _ in DOCS.glob('*.md'))} pages)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
