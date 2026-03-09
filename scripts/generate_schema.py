#!/usr/bin/env python
"""Generate LinkML schema from USDM models."""

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from usdm_to_linkml import USDMToLinkMLConverter


def main():
    """Generate the LinkML schema."""
    output_path = Path(__file__).parent.parent / "output" / "usdm.yaml"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print("Converting USDM models to LinkML schema...")
    converter = USDMToLinkMLConverter()
    converter.convert()
    converter.save(str(output_path))

    print(f"Generated LinkML schema: {output_path}")
    print(f"  - {len(converter.schema['classes'])} classes")
    print(f"  - {len(converter.schema['slots'])} slots")

    return 0


if __name__ == "__main__":
    sys.exit(main())
