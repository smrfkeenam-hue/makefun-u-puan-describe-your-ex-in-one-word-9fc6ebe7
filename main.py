import os

# One word for an ex: the whole relationship was a newsletter I never
# signed up for. The verdict is what anyone does with that mail.
ENTRY = "Unsubscribe"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = os.path.join(output_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
