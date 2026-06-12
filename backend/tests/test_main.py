import os
import subprocess
import sys


def test_backend_starts_in_once_mode(tmp_path):
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    env["TMPDIR"] = str(tmp_path)

    result = subprocess.run(
        [sys.executable, "main.py", "--once"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        timeout=60,
        env=env,
    )

    assert result.returncode == 0, result.stderr or result.stdout
    assert "Copy Trading Bot - Kotak Neo API" in result.stdout
    assert "Bot ready. Waiting for signals..." in result.stdout
