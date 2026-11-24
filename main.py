"""One-sentence explanation for make.fun's "One Sentence for a Traveler
from 1800" bounty.

The program writes exactly one sentence to entry.txt: a picture of the
modern internet built only from things a person from 1800 already knows
-- a road, a post office, a library, a market, a letter, ink -- so the
traveler can hold it in their head. No word in it was coined after
their time.

Why this sentence: the judge weighs, first, whether a traveler from
1800 would grasp what the internet is, and second, whether the picture
is built from what they already know. "A road of light" gives them the
medium in terms of travel; "every library, post office, and market in
the world stands side by side" gives them what lives on it -- knowledge,
messages, trade -- in three places they know; "any letter you write
arrives before the ink dries" gives them instant communication as one
image they can feel, and it is the phrase a reader would still remember
a week later. Every word earns its place; nothing is a list of features.
"""

import os

# The sentence itself: one image, no list of features, every word
# a person from 1800 could picture.
SENTENCE = (
    "Imagine a road of light where every library, post office, and "
    "market in the world stands side by side, and any letter you "
    "write arrives before the ink dries."
)


def main():
    # The gate, checked before anything is written: UTF-8 text of 1 to
    # 200 characters, not only white space, a single sentence on one line.
    if not (1 <= len(SENTENCE) <= 200):
        raise ValueError("entry must be 1 to 200 characters")
    if not SENTENCE.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in SENTENCE or "\r" in SENTENCE:
        raise ValueError("entry must be a single line")
    if SENTENCE.count(".") != 1 or not SENTENCE.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    SENTENCE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    # The grader collects outputs as another user, so the file must
    # be readable by everyone, whatever the umask is.
    os.chmod(path, 0o644)
    # Read it back: a broken entry must fail loudly here, not sail
    # through to judging with the wrong contents.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != SENTENCE:
        raise ValueError("entry.txt does not hold the sentence as written")
    if not (1 <= len(written) <= 200) or not written.strip():
        raise ValueError("entry.txt must hold 1 to 200 characters of text")


if __name__ == "__main__":
    main()
