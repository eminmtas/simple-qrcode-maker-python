import qrcode

qr_code = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=7,
    border=1,
)

qr_code.add_data('https://github.com/eminmtas')
qr_code.make(fit=True)

image = qr_code.make_image(fill_color='red', back_color='white')
image.save('newqrcode.png')