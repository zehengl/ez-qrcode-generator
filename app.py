from io import BytesIO

import qrcode
from flask import Flask, render_template, request, send_file
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")


def serve_image(img):
    img_io = BytesIO()
    img.save(img_io, "png")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/png")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        img = qrcode.make(request.form["text_input"])
        return serve_image(img)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
