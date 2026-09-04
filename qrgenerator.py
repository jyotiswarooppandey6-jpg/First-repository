import qrcode

import qrcode

data = "vastugonahoiya.vercel.app"

qr = qrcode.make(data)
qr.save("my_qr.png")

print("QR ban gaya: /public/my_qr.png")