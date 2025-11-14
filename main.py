import argparse
import os
import sys
from pathlib import Path

import kagglehub as kh


def download_dataset(dataset: str, force: bool = False) -> Path:
    """Download dataset using kagglehub and return local Path.

    Prints hints if download/authentication fails and re-raises the exception.
    """
    try:
        path = kh.dataset_download(dataset, force=force)
        return Path(path)
    except Exception as exc:
        print("Failed to download dataset:", exc, file=sys.stderr)
        print(
            "Ensure you have a Kaggle API token at '~/.kaggle/kaggle.json'",
            file=sys.stderr,
        )
        print("Or set KAGGLE_USERNAME and KAGGLE_KEY environment variables.", file=sys.stderr)
        raise


def count_images(root: Path) -> int:
    exts = (".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff")
    count = 0
    for _root, _dirs, files in os.walk(root):
        for f in files:
            if f.lower().endswith(exts):
                count += 1
    return count


def list_files(root: Path, max_items: int = 20) -> None:
    printed = 0
    for dirpath, _dirs, files in os.walk(root):
        for f in files:
            print(os.path.join(dirpath, f))
            printed += 1
            if printed >= max_items:
                return


def parse_args():
    p = argparse.ArgumentParser(description="Download & inspect Kaggle brain-tumor dataset")
    p.add_argument(
        "--dataset",
        default="masoudnickparvar/brain-tumor-mri-dataset",
        help="Kaggle dataset reference owner/dataset-name",
    )
    p.add_argument("--force", action="store_true", help="Force re-download the dataset")
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't download; just print what would happen (useful for testing)",
    )
    p.add_argument("--count", action="store_true", help="Count image files in dataset")
    p.add_argument("--list", type=int, default=0, help="List first N files in dataset")
    return p.parse_args()


def main():
    args = parse_args()

    print("Dataset reference:", args.dataset)
    if args.dry_run:
        print("Dry run: no download will be attempted.")
        print("If running for real, remove --dry-run to download the dataset.")
        return

    try:
        path = download_dataset(args.dataset, force=args.force)
    except Exception:
        sys.exit(1)

    print("Local dataset path:", path)

    if args.count:
        n = count_images(path)
        print(f"Found {n} image files under {path}")

    if args.list > 0:
        print(f"Listing first {args.list} files:")
        list_files(path, max_items=args.list)


if __name__ == "__main__":
    main()