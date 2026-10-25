
from pathlib import Path
import shutil

# Folder containing files to organize
SOURCE_DIR = Path("test_files")

# File extension categories
FILE_CATEGORIES = {
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp"],
}

def get_category(file_path):
    """Return the category for a file based on its extension."""
    for category, extensions in FILE_CATEGORIES.items():
        if file_path.suffix.lower() in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    """Avoid overwriting a file with the same name."""
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_destination = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )

        if not new_destination.exists():
            return new_destination

        counter += 1


def organize_files():
    if not SOURCE_DIR.exists() or not SOURCE_DIR.is_dir():
        print("Error: Source folder does not exist.")
        return

    moved_count = 0
    skipped_count = 0

    for file_path in SOURCE_DIR.iterdir():
        # Skip directories
        if not file_path.is_file():
            continue

        category = get_category(file_path)
        category_folder = SOURCE_DIR / category
        category_folder.mkdir(exist_ok=True)

        destination = get_unique_path(
            category_folder / file_path.name
        )

        try:
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name} -> {category}/")
            moved_count += 1

        except (PermissionError, OSError) as error:
            print(f"Could not move {file_path.name}: {error}")
            skipped_count += 1

    print("\n===== ORGANIZATION SUMMARY =====")
    print(f"Files moved: {moved_count}")
    print(f"Files skipped: {skipped_count}")


if __name__ == "__main__":
    organize_files()
