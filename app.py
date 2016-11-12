from flask import Flask, send_file, request
import qrcode
import StringIO

app = Flask(__name__)


def serve_image(img):
    img_io = StringIO.StringIO()
    img.save(img_io, 'png')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print request.form['password']
        img = qrcode.make(request.form['password'])
        return serve_image(img)
    else:
        return """
        <!DOCTYPE html>
        <html>
        <body>
            <form method="post">
              wifi password:<br>
              <input type="text" name="password">
              <br>
              <input type="submit" value="Submit">
            </form>
        </body>
        </html>
        """

app.run()
