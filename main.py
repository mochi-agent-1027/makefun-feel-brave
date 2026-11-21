import os

TEXT = "Steam rises from the bowl, and both hands wrap around it. Outside, the street does all the rushing for you. The chair is yours. The light through the window has nowhere else to be. Eat slowly. When you stand \u2014 and you will \u2014 you will be unhurried, and entirely ready."


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
