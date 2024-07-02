from flask import Flask, render_template, request, jsonify, send_from_directory
import cv2
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def apply_theme(image, theme):
    if theme == 'charcoal':
        return charcoal_sketch(image)
    elif theme == 'sepia':
        return sepia_tone(image)
    elif theme == 'grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        return None

def charcoal_sketch(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_image = 255 - blurred_image
    charcoal_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    return charcoal_sketch

def sepia_tone(image):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    sepia_image = cv2.transform(image, kernel)
    return sepia_image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    theme = request.form['theme']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    nparr = np.fromstring(file.read(), np.uint8)
    original_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    processed_image = apply_theme(original_image, theme)

    if processed_image is None:
        return jsonify({'error': 'Invalid theme'})

    original_img_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'original_image.jpg')
    cv2.imwrite(original_img_filename, original_image)

    processed_img_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_image.jpg')
    cv2.imwrite(processed_img_filename, processed_image)

    return render_template('view_image.html', original_img_filename=original_img_filename, processed_img_filename=processed_img_filename)

if __name__ == '__main__':
    app.run(debug=True)
