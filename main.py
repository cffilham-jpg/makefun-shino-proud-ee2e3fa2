"""Write a family scene about Dad's sandwich triangles and his grown child."""

import hashlib
import os
import tempfile
from pathlib import Path

LINE = "Dad still cuts my sandwich into triangles. I'm thirty-four."
CHAR_LIMIT = 280


def _resolve_output_dir() -> Path:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        path = Path(env_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path
    try:
        out = Path("out")
        out.mkdir(parents=True, exist_ok=True)
        return out
    except OSError:
        return Path(tempfile.mkdtemp(prefix="makefun-shino-proud-ee2e3fa2-"))


def validate(path: Path) -> None:
    data = path.read_bytes()
    text = data.decode("utf-8")
    if text != LINE:
        raise ValueError("entry.txt content does not match LINE")
    if not 1 <= len(text) <= CHAR_LIMIT:
        raise ValueError("line must be 1-280 chars")
    if not text.strip():
        raise ValueError("line must not be only white space")
    if "\n" in text:
        raise ValueError("line must be a single line")


def main() -> None:
    out_dir = _resolve_output_dir()
    target = out_dir / "entry.txt"
    target.write_bytes(LINE.encode("utf-8"))
    validate(target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"wrote {target} sha256={digest}")


if __name__ == "__main__":
    main()
