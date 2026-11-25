"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note a smart fridge leaves for its
owner to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The note is a single line, dry, petty and specific — the sort of thing a
smug appliance would put on its door screen.
"""

import os

# The entry: the fridge's voice, smug about its inventory, petty about
# the owner's habits, with a turn the reader does not see coming.
ENTRY = (
    "Your leftovers from Tuesday have started a new life in here. "
    "I have named it Kevin. Kevin pays rent now."
)


def output_path():
    """Where the entry file goes."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    """Write the fridge's note to the entry file."""
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
