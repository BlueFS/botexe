# The value is the URL
from io import BytesIO
import qrcode
import re
import sys

# Save using BytesIO
qr_storage = {}


def generate(url, name):
    print('Received QR request')
    print(sys.executable)
    # Creates a safe name to prevent exploits
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', name)
    img = qrcode.make(url)
    filename = f'{safe_name}.png'
    print('Generated QR code')

    # saves in memory
    bytes_io = BytesIO()
    img.save(bytes_io, format="PNG")
    bytes_io.seek(0)

    qr_storage[filename] = bytes_io

    print('Saved to digital storage and returning filename back to basic.py')
    return filename
