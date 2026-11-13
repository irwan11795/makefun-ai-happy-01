# make.fun ai-happy-01 entry: copy the image beside this file to /output/entry.png.
# Python 3.13, standard library only. Deterministic: the same bytes every run.
# No network. Run locally with: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"

OUT.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT)

# Verify the copy: the output must be byte-identical to the source.
assert OUT.read_bytes() == SRC.read_bytes(), "entry.png copy mismatch"
