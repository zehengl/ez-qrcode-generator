import os
from base64 import b64encode
from io import BytesIO

import qrcode
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from whitenoise import WhiteNoise

from forms import TextInputForm

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


def generate_qrcode_bytes(text_input):
    if not text_input:
        return None

    img = qrcode.make(text_input)
    img_io = BytesIO()
    img.save(img_io, "png")
    img_io.seek(0)
    img_bytes = b64encode(img_io.getvalue()).decode("utf-8")
    img_io.close()

    return img_bytes


@app.route("/", methods=["get", "post"])
def index():
    form = TextInputForm(request.form)
    img_bytes = generate_qrcode_bytes(form.text_input.data)

    return render_template("index.html", form=form, img_bytes=img_bytes)


if __name__ == "__main__":
    app.run(debug=True)
