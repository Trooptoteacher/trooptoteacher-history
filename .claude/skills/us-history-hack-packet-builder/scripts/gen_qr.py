"""Generate a branded QR code (navy modules, gold finder eyes) to the App Store listing."""
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image

APP_URL = "https://apps.apple.com/us/app/u-s-history-hack-1877-present/id6757368709"
OUT = "/home/user/workspace/tpt_launch/assets/app_qr.png"

NAVY = (10, 31, 60)
WHITE = (255, 255, 255)

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=18,
    border=2,
)
qr.add_data(APP_URL)
qr.make(fit=True)

img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(radius_ratio=1.0),
    color_mask=SolidFillColorMask(front_color=NAVY, back_color=WHITE),
).convert("RGB")

img.save(OUT)
print("WROTE", OUT, img.size)
