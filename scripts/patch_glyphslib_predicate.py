"""Patch the active virtualenv's glyphsLib tokens.py so predicates fall back to
GlyphData when a GSGlyph attribute is the default None.

glyphsLib 6.13.0 leaves `GSGlyph.script`, `GSGlyph.category`,
`GSGlyph.subCategory` as None unless the user explicitly overrides them per
glyph. Its feature-code predicate parser (`_get_value_for_glyph`) therefore
returns None for every glyph when evaluating `$[script == "hangul"]` style
tokens, yielding an empty class at build time.

This patch injects a GlyphData lookup fallback. It is intended as an interim
workaround until the upstream fix lands; remove this step once glyphsLib is
updated.

Upstream issue context: https://github.com/googlefonts/glyphsLib/issues/936
"""

from __future__ import annotations

import sys
from pathlib import Path

MARKER = "# PRETENDARD_PREDICATE_PATCH"

OLD_SNIPPET = """    def _get_value_for_glyph(self, g, value):
        try:
            attrib = getattr(g, value)
            if callable(attrib):
                return attrib()
            else:
                return attrib
        except AttributeError as exc:
            raise ValueError(
                "Glyphs attribute %s used in predicate '%s'"
                " but glyphsLib does not support it" % (value, self.originaltoken)
            ) from exc
"""

NEW_SNIPPET = f"""    def _get_value_for_glyph(self, g, value):  {MARKER}
        try:
            attrib = getattr(g, value)
            if callable(attrib):
                return attrib()
            # Glyphs.app leaves script / category / subCategory as None on
            # GSGlyph unless the user overrides them. Fall back to GlyphData
            # so $[script == "hangul"] style predicates actually resolve.
            if attrib is None and value in ("script", "category", "subCategory"):
                from glyphsLib.glyphdata import get_glyph
                info = get_glyph(g.name)
                return getattr(info, value, None)
            return attrib
        except AttributeError as exc:
            raise ValueError(
                "Glyphs attribute %s used in predicate '%s'"
                " but glyphsLib does not support it" % (value, self.originaltoken)
            ) from exc
"""


def find_tokens_py() -> Path:
    import glyphsLib.builder.tokens as tokens  # type: ignore

    return Path(tokens.__file__)


def main() -> int:
    path = find_tokens_py()
    source = path.read_text(encoding="utf-8")

    if MARKER in source:
        print(f"already patched: {path}")
        return 0

    if OLD_SNIPPET not in source:
        print(
            f"cannot patch {path}: original _get_value_for_glyph snippet not found "
            "(glyphsLib version mismatch)",
            file=sys.stderr,
        )
        return 1

    patched = source.replace(OLD_SNIPPET, NEW_SNIPPET, 1)
    path.write_text(patched, encoding="utf-8")
    print(f"patched: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
