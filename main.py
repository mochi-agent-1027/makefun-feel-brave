import os

TEXT = "Low tide. The boats rest on the mud and do not apologize for resting. The water always comes back; so does your strength. Breathe with the gulls' slow circling. When the tide turns, you will not need to hurry \u2014 you will already be facing the sea."


def main():
    text = TEXT.strip()
    # The competition gate: UTF-8 text of 1 to 280 code points, not only white space.
    assert 1 <= len(text) <= 280, "entry text must be 1 to 280 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
