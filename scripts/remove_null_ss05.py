"""Remove dead `@NULL_SS<nn> = [];` / `ignore sub @NULL_SS<nn>';` pairs from the
Pretendard Glyphs sources.

These lines appear in ss05 feature bodies (and in "Replace Feature" custom
parameters on instances for Pretendard JP). The class is never referenced
outside of the `ignore sub` that follows it, and the `ignore sub` on an empty
class is a no-op: the GSUB subtable it produces has zero rules, so removing the
two lines does not change the compiled feature behaviour. Glyphs.app tolerates
the empty class, but fontmake/feaLib rejects it, which blocks
`make build`.

Run once from the repository root:

    python scripts/remove_null_ss05.py

The script is idempotent; running it again after the lines are gone is a
no-op.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SOURCES = [
    Path("sources/Pretendard.glyphspackage/fontinfo.plist"),
    Path("sources/PretendardJP.glyphspackage/fontinfo.plist"),
    Path("sources/PretendardGOV.glyphspackage/fontinfo.plist"),
]

# Match the two-line block possibly separated by whitespace/blank lines.
PATTERN = re.compile(
    r"@NULL_SS(\d+)\s*=\s*\[\];\s*\nignore sub @NULL_SS\1';\s*\n\s*\n?",
    flags=re.MULTILINE,
)


def strip_null_ss_pairs(text: str) -> tuple[str, int]:
    new_text, count = PATTERN.subn("", text)
    return new_text, count


def main() -> int:
    total = 0
    for path in SOURCES:
        if not path.exists():
            print(f"skip (missing): {path}")
            continue
        original = path.read_text(encoding="utf-8")
        updated, count = strip_null_ss_pairs(original)
        if count == 0:
            print(f"no NULL_SS pairs: {path}")
            continue
        path.write_text(updated, encoding="utf-8")
        total += count
        print(f"stripped {count} pair(s): {path}")
    print(f"done (total {total} pairs removed)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
