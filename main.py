import qrcode
import qrcode.image.svg


content = input("give any text or url you want to store in qr code: ").strip().lower()
path_settings = input("will you like to use path settings or continue?(y/n): ").strip().lower()

try:
	if path_settings == 'y':
		file_format = input("what should be the file extention?(svg or jpg): ").strip().lower()
		img_name = input("what should be the qrcode image name?: ").strip().lower()

		if file_format == 'svg':
			factory = qrcode.image.svg.SvgImage
			img = qrcode.make(f'{content}', image_factory=factory)
			img.save(f"{img_name}.svg")
			print("your qr code is ready!")

		if file_format == 'jpg':
			img = qrcode.make(content)
			img.save(f"{img_name}.jpg")
			print("your qr code is ready!")
	else:
		img = qrcode.make(content)
		img.save(f"qrcode_img.png")
		print("Your qr code is ready!")

except:

	print('something went wrong :(')
	print("please try again")

