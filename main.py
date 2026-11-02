import qrcode

url = input("Enter WebSite URL: ")

qr = qrcode.make(url)

qr.save("my_qr.png")

print("Qr Code created successfully!")
print("Saved as my_qr.png")