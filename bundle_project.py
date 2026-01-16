import os

# Configuration for the bundler
# Files and directories to exclude to keep the output clean
EXCLUDE_DIRS = {'.git', '__pycache__', 'venv', '.venv', '.pytest_cache', 'dist', 'build'}
EXCLUDE_FILES = {'bundle_project.py', '.DS_Store', 'sentinel_report.html'}
OUTPUT_FILE = "sentinel_core_bundle.txt"

def bundle_project(root_dir):
    """
    Traverses the project tree and aggregates file contents into a single text file.
    """
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as output:
        output.write(f"# SENTINEL CORE PROJECT BUNDLE\n")
        output.write(f"# Generated on: 2026\n\n")

        for root, dirs, files in os.walk(root_dir):
            # Prune excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            
            for file in sorted(files):
                if file in EXCLUDE_FILES or file.endswith(('.pyc', '.pyo', '.zip')):
                    continue

                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, root_dir)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    output.write(f"{'='*80}\n")
                    output.write(f"FILE: {relative_path}\n")
                    output.write(f"{'='*80}\n\n")
                    output.write(content)
                    output.write("\n\n")
                    print(f"Bundled: {relative_path}")
                except Exception as e:
                    print(f"Skipping {relative_path}: {e}")

    print(f"\nSuccess! Full project saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    bundle_project(".")