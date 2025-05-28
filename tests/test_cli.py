import sys
import pathlib
import subprocess

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))


def test_cli_help():
    result = subprocess.run([sys.executable, "app.py", "--help"], capture_output=True, text=True)
    assert result.returncode == 0
    assert "--mode" in result.stdout
    assert "--data-source" in result.stdout
