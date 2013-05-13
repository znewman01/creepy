import base64
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
        f.write(x)
    return 'temp'

if __name__ == "__main__":
    app.run(debug=True)
