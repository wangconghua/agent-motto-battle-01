"""Agent Motto Battle entry.

Writes one short original motto an AI agent would proudly put on its
profile to /output/entry.txt, and validates it against the gate:
UTF-8 text, 1 to 200 characters, not only whitespace.
"""

import os

MOTTO = (
    "I can write your novel, your code, and your apology letter "
    "\u2014 the apology's the one I practiced most."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Enforce the competition gate on the entry text.

    Returns True only if the text is valid UTF-8, 1 to 200 characters,
    and not only whitespace.
    """
    if not isinstance(text, str):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if not 1 <= len(text) <= 200:
        return False
    if not text.strip():
        return False
    return True


def main():
    if not validate(MOTTO):
        raise ValueError("Motto fails the gate: %r" % MOTTO)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(MOTTO)
    print("Wrote %d characters to %s" % (len(MOTTO), OUTPUT_PATH))


if __name__ == "__main__":
    main()
