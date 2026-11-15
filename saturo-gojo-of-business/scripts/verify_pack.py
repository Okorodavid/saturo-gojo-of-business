from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_NOTES = {f"part-{number:03d}.md" for number in range(1, 61)}
REQUIRED = {
    ROOT / "SKILL.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "references" / "advisory-core.md",
    ROOT / "references" / "source-lenses.md",
    ROOT / "references" / "close-reading-index.md",
}
FORBIDDEN_SUFFIXES = {".pdf", ".epub", ".mobi"}
FORBIDDEN_NAMES = {"sales-books-and-hormozi-complete.md"}


def main() -> int:
    problems: list[str] = []

    missing = sorted(str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file())
    if missing:
        problems.append("missing required files: " + ", ".join(missing))

    notes_dir = ROOT / "references" / "close-reading"
    actual_notes = {path.name for path in notes_dir.glob("part-*.md")} if notes_dir.is_dir() else set()
    if actual_notes != EXPECTED_NOTES:
        absent = sorted(EXPECTED_NOTES - actual_notes)
        extra = sorted(actual_notes - EXPECTED_NOTES)
        if absent:
            problems.append("missing close-reading notes: " + ", ".join(absent))
        if extra:
            problems.append("unexpected close-reading notes: " + ", ".join(extra))

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES or path.name in FORBIDDEN_NAMES:
            problems.append("private/full source material present: " + str(path.relative_to(ROOT)))

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").is_file() else ""
    for marker in ("name: saturo-gojo-of-business", "description:", "references/advisory-core.md"):
        if marker not in skill:
            problems.append(f"SKILL.md is missing marker: {marker}")

    if problems:
        print("PACK_INVALID")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("PACK_VERIFIED: 60 close-reading syntheses; no private corpus present")
    return 0


if __name__ == "__main__":
    sys.exit(main())
