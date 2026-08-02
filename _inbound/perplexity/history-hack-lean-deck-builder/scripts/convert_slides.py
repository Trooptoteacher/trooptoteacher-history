from PIL import Image
import glob, os, re

SRC = "/tmp/deckrender"
DST = "/home/user/workspace/hh-web/public/data/us-history/tcap-decks/unit-1-lean/slides"
os.makedirs(DST, exist_ok=True)

pngs = sorted(glob.glob(f"{SRC}/hi-*.png"),
              key=lambda p: int(re.search(r'hi-(\d+)\.png', p).group(1)))
for p in pngs:
    n = int(re.search(r'hi-(\d+)\.png', p).group(1))
    im = Image.open(p).convert("RGB")
    out = os.path.join(DST, f"deckimg-{n:03d}.jpg")
    im.save(out, "JPEG", quality=88, optimize=True)
    print(f"{out}  {im.size}  {os.path.getsize(out)//1024}KB")
