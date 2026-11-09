"""Draw the Open Graph image (site/assets/og.png, 1200×630) from the site's fonts, icon and main screenshot.

    python scripts/make_og.py

Needs Playwright with Chromium (python -m pip install playwright; python -m playwright install chromium)."""
import base64
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "site" / "assets"


def data(path: Path, mime: str) -> str:
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face {{ font-family: "EB Garamond"; src: url({data(A / "fonts" / "eb-garamond.woff2", "font/woff2")}) format("woff2"); }}
html, body {{ margin: 0; width: 1200px; height: 630px; background: #06111f; overflow: hidden; }}
.logo {{ position: absolute; left: 72px; top: 82px; width: 146px; height: 146px; border-radius: 30px; }}
h1 {{ position: absolute; left: 70px; top: 262px; margin: 0; font: 400 76px/1 "EB Garamond", serif; color: #eaf4ff;
      letter-spacing: -0.5px; white-space: nowrap; }}
p {{ position: absolute; left: 73px; top: 372px; width: 420px; margin: 0; font: 400 31px/1.2 "EB Garamond", serif;
     color: #a8bdd2; }}
.bar {{ position: absolute; left: 72px; top: 480px; width: 229px; height: 7px; background: #0bbaf4; }}
.shot {{ position: absolute; left: 534px; top: 113px; width: 620px; padding: 6px; background: #0a2542; }}
.shot img {{ display: block; width: 620px; height: auto; }}
</style></head><body>
<img class="logo" src="{data(A / "apple-touch-icon.png", "image/png")}" alt="">
<h1>SciTrace-Suite</h1>
<p>Scientific software, from the measurement to the paper.</p>
<div class="bar"></div>
<div class="shot"><img src="{data(A / "img" / "main-window.webp", "image/webp")}" alt=""></div>
</body></html>"""

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    page.set_content(HTML)
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(300)
    page.screenshot(path=str(A / "og.png"))
    browser.close()
print("og.png written")
