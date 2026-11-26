"""Write the internet in one word to the output file.

The entry is a single word that describes the whole internet: "feral".
The internet is untamed, unmoderated, and runs on its own wild logic —
a word that is funny by itself, true of the internet as a whole, and
surprising enough that it is not the first word anyone reaches for.

This program writes exactly that word and nothing else: no network
access, no randomness, and no dependence on the time or date, so every
run produces the same bytes. The word is 5 characters long, inside the
bounty gate of 1 to 30 characters, and it is a single word with no
spaces, hyphens, or punctuation.

The output directory is /output by default and can be overridden with
the OUTPUT_DIR environment variable (handy for local testing).
"""

import hashlib
import os
import sys

WORD = "feral"


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = (WORD + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"Wrote {len(data)} bytes to {path} (sha256 {digest})")
    print(f"Word: {WORD!r} ({len(WORD)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
