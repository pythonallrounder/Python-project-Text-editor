import PIL
from PIL import Image
import pyqrcode
from pyzbar.pyzbar import decode


qr = pyqrcode.create('Hello Arooj')
qr.png("mylife.png",scale=8)
