import os
import hashlib
from flask import Flask, render_template, request, send_from_directory
import qrcode

app = Flask(__name__)
QR_CODE_DIR = os.path.join('static', 'qrcodes')

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code_filename = None
    if request.method == 'POST':
        data = request.form.get('data')
        if data:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            
            hashed_data = hashlib.md5(data.encode()).hexdigest()
            qr_code_filename = f"{hashed_data}.png"
            
            img.save(os.path.join(QR_CODE_DIR, qr_code_filename))

    return render_template('index.html', qr_code_filename=qr_code_filename)

@app.route('/static/qrcodes/<filename>', methods=['GET'])
def get_qrcode(filename):
    return send_from_directory(QR_CODE_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)