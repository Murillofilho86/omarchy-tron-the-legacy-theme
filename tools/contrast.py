#!/usr/bin/env python3
"""WCAG 2.x contrast check for colors.toml.

Usage: python3 tools/contrast.py [path/to/colors.toml]

Checks the text/background pairs the Omarchy 4.5 templates actually produce
(terminal, btop, neovim, selection, search highlights). Exits 1 if any required
pair fails. Pairs marked "info" are reported but never fail the run.
"""
import sys
import tomllib
from pathlib import Path


def lum(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))
    lin = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def ratio(a: str, b: str) -> float:
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "colors.toml"
    c = tomllib.loads(path.read_text())

    surfaces = ["background", "dark_background", "lighter_background"]
    # (foreground key, background keys, minimum ratio, required?, note)
    checks = []
    for fg in ("foreground", "bright_foreground", "light_foreground", "muted"):
        checks.append((fg, surfaces, 4.5, True, "text"))
    checks.append(("accent", surfaces, 4.5, True, "accent text/indicators"))
    for fg in (
        "red", "green", "yellow", "orange", "blue", "magenta", "cyan", "brown",
        "bright_red", "bright_green", "bright_yellow", "bright_blue", "bright_magenta", "bright_cyan",
    ):
        checks.append((fg, ["background", "lighter_background"], 4.5, True, "ANSI/syntax text"))
    checks += [
        ("selection_foreground", ["selection_background"], 4.5, True, "selected text"),
        ("accent", ["selection"], 4.5, True, "btop selected row"),
        ("background", ["yellow", "red", "foreground", "bright_foreground"], 4.5, True, "search match / footer / cursor"),
        ("dark_foreground", surfaces, 3.0, False, "disabled text (WCAG exempts disabled controls)"),
    ]

    failures = 0
    print(f"{'foreground':22s} {'on':20s} {'ratio':>6s}  {'min':>4s}  result")
    print("-" * 70)
    for fg, bgs, minimum, required, note in checks:
        for bg in bgs:
            r = ratio(c[fg], c[bg])
            ok = r >= minimum
            tag = "pass" if ok else ("FAIL" if required else "info")
            if not ok and required:
                failures += 1
            print(f"{fg:22s} {bg:20s} {r:6.2f}  {minimum:4.1f}  {tag}  {c[fg]} / {c[bg]}  ({note})")

    print()
    print("Non-text elements (UI components need 3:1):")
    inactive = "#" + c["hyprland_inactive_border"].split("(")[1][:6]
    for name, fg, bg, minimum in (("active border / bg", c["accent"], c["background"], 3.0),
                                  ("inactive border / bg", inactive, c["background"], 0.0)):
        note = "pass" if ratio(fg, bg) >= minimum else "below 3:1"
        if name.startswith("inactive"):
            note = "info, discreet by design (rendered at 67% alpha)"
        print(f"  {name:22s} {ratio(fg, bg):5.2f}  {note}")

    print()
    print(f"{failures} required pair(s) failed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
