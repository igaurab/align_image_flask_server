from flask import Flask, jsonify, request, send_from_directory
from align_image import align_image
import cv2
from PIL import Image as Image
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.root_path, 'output/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route('/uploads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = UPLOAD_FOLDER
    return send_from_directory(directory=uploads, filename=filename)

@app.route('/')
@app.route('/uploads')
def upload_image():
    return """
 <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post action="/alignment" enctype=multipart/form-data>
      <input type=file name=image>
      <input type=submit value=Upload>
    </form>

    """

@app.route('/alignment', methods=['POST'])
def alignment():
    file = request.files['image']

    npimg = np.frombuffer(file.read() , np.uint8)
    image =  cv2.imdecode(npimg,cv2.IMREAD_COLOR) 

    result = align_image(image)

    image_name = file.filename
    result.save(filename=app.config['UPLOAD_FOLDER'] + 'output-' + image_name)

    download_url = f"http://localhost:5000/uploads/output-{image_name}" 
    return jsonify({'data': download_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)