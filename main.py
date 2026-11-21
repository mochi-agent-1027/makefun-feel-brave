import os

TEXT = 'Rain on the window, and nowhere to be until it stops. The tea is warm. The list can wait. One breath in, one breath out, slower than the clock. What comes next is only one thing — and you have carried heavier mornings than this.'

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
