from pathlib import Path

import app


def test_check_repository_reports_all_required_files(tmp_path):
    (tmp_path / "README.md").write_text("# Demo project\n", encoding="utf-8")
    (tmp_path / "tests").mkdir()
    (tmp_path / "requirements.txt").write_text("pytest\n", encoding="utf-8")

    found, missing = app.check_repository(tmp_path)

    assert "README.md" in found
    assert "tests folder" in found
    assert "requirements.txt" in found
    assert missing == []


def test_check_repository_reports_missing_files(tmp_path):
    found, missing = app.check_repository(tmp_path)

    assert "README.md" not in found
    assert "tests folder" not in found
    assert "requirements.txt" not in found

    assert "README.md" in missing
    assert "tests folder" in missing
    assert "requirements.txt" in missing
