import pyshorteners
import pyqrcode
import png
from pyqrcode import QRCode

long_url = input("Enter the URL to shorten: 
need = input("Do you require QR code for the shortened link:'Y' / 'N'")

# TinyURL shortener service
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
need.lower()
try:
    if need == 'y':
        url = pyqrcode.create(short_url)
        url.png('myqr.png', scale=6)


finally:
    print("The Shortened URL is: " + short_url)