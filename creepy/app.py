import base64
from face import face_blit
import cv
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    im_string = request.form['image']
    # chop off
    base64_im = im_string[im_string.index(',')+1:]
    bin_im = base64.b64decode(base64_im)
    #TODO this is super janky
    with open('tmp.png', 'w') as f:
        f.write(bin_im)
    src_image = cv.LoadImageM('tmp.png')
    dst_image = cv.LoadImageM('img/chris.jpg')
    dst_image = face_blit(src_image, dst_image)
    cv.SaveImage('out.jpg', dst_image)
    with open('out.jpg') as f:
        return base64.b64encode(f.read())

if __name__ == "__main__":
    app.run(debug=True)
