"""Guards for the generated documentation in output/docs/."""

import shutil
import subprocess
from collections import defaultdict
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent


def _tracked_docs():
    if shutil.which("git") is None:
        pytest.skip("git not available")
    result = subprocess.run(
        ["git", "ls-files", "output/docs"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if result.returncode != 0:
        pytest.skip("not a git checkout")
    return result.stdout.split()


def test_docs_paths_do_not_collide_on_case_insensitive_filesystems():
    """gen-doc emits both Code (class) and code (slot) pages; they must not
    share a folder, or macOS/Windows checkouts silently lose pages."""
    files = _tracked_docs()
    if not files:
        pytest.skip("no tracked docs")
    by_lower = defaultdict(list)
    for f in files:
        by_lower[f.lower()].append(f)
    clashes = {k: v for k, v in by_lower.items() if len(v) > 1}
    assert not clashes, f"case-colliding doc paths: {clashes}"


def test_docs_are_split_by_page_type():
    files = _tracked_docs()
    if not files:
        pytest.skip("no tracked docs")
    folders = {Path(f).parts[2] for f in files if len(Path(f).parts) > 3}
    assert {"classes", "slots"} <= folders
