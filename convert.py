import os
from pathlib import Path

# ==========================
# CONFIG
# ==========================

SOURCE_DIR = Path(".")
OUTPUT_FILE = Path("ai_bundle.txt")

MAX_CHUNK_SIZE = 250_000  # ~250KB безопасный размер блока

ALLOWED_EXTENSIONS = {
    ".html", ".htm",
    ".css",
    ".js",
    ".txt",
    ".xml",
    ".asc",
    ".md",
    ".json",
    ".yml",
    ".yaml",
}

EXCLUDED_EXTENSIONS = {
    ".mp4", ".png", ".jpg", ".jpeg", ".gif",
    ".webp", ".ico",
    ".pdf", ".zip", ".tar", ".gz",
}

# ==========================
# FUNCTIONS
# ==========================

def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in EXCLUDED_EXTENSIONS:
        return False
    if path.suffix.lower() in ALLOWED_EXTENSIONS:
        return True
    return False


def split_content(content: str):
    parts = []
    current = ""
    current_size = 0

    for line in content.splitlines(keepends=True):
        line_size = len(line.encode("utf-8"))

        if current_size + line_size > MAX_CHUNK_SIZE:
            parts.append(current)
            current = line
            current_size = line_size
        else:
            current += line
            current_size += line_size

    if current:
        parts.append(current)

    return parts


# ==========================
# MAIN
# ==========================

with open(OUTPUT_FILE, "w", encoding="utf-8") as bundle:

    for root, dirs, files in os.walk(SOURCE_DIR):
        root_path = Path(root)

        for file in files:
            source_file = root_path / file

            if source_file == OUTPUT_FILE:
                continue

            if not is_text_file(source_file):
                continue

            relative_path = source_file.relative_to(SOURCE_DIR)

            try:
                with open(source_file, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                parts = split_content(content)

                for idx, part in enumerate(parts, 1):
                    bundle.write("\n" + "="*80 + "\n")
                    bundle.write(f"FILE: {relative_path}\n")
                    bundle.write(f"PART: {idx}/{len(parts)}\n")
                    bundle.write("="*80 + "\n\n")
                    bundle.write(part)
                    bundle.write("\n\n")

                print(f"[OK] {relative_path}")

            except Exception as e:
                print(f"[ERROR] {relative_path}: {e}")

print("\nГотово. Создан файл:", OUTPUT_FILE)