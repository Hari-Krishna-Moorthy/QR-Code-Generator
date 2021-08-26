from pyperclip import paste as paste_clipboard 

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from qrcode import QRCode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.constants import ERROR_CORRECT_L
import os




def getQRcode(name, strs="""Get Some Text Here"""):
	if len(strs) >= 2953:
		return "Cant convert Text to QR"
	qr = QRCode(
		version = 1,
		error_correction = ERROR_CORRECT_L,
		box_size = 10,
		border = 4,
		)
	qr.add_data(strs)
	qr.make(fit = True)
	radialGradiantColorMask = RadialGradiantColorMask(
		back_color=(235,242,250), 
		center_color=(0,119,182), 
		edge_color=(3,4,94))
	radialGradiantColorMask.paint_color = "#00b4d8" #(255, 122, 255)
	img = qr.make_image(image_factory=StyledPilImage, 
		color_mask=radialGradiantColorMask,)
		# embeded_image_path="IG-logo2.png")
	img = img.convert("CMYK") # RGBA
	img = img.convert('RGB')
	img.save(name)
	# return img


if __name__ == '__main__':
	# getQRcode("qrcode_result.png", content)
	getQRcode("qrcode_result.png", paste_clipboard())
	url = os.path.join(os.path.abspath(
		os.path.join(os.sys.argv[0],os.pardir)), 'index.html' )
	os.system("open '{}' ".format(url))

	
	