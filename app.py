from flask import Flask, send_file, request
import qrcode
from io import BytesIO

app = Flask(__name__)


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
        return """
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta http-equiv="x-ua-compatible" content="ie=edge">
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
            <title>ez-qrcode-generator</title>
          </head>
          <body>
            <div class="container">
              <form method="post">
                  <div class="form-group">
                      <label for="text_input">String to convert:</label>
                      <input type="text" id="text_input" name="text_input" class="form-control" placeholder="Type Something">
                  </div>
                  <button type="submit" class="btn btn-primary">Submit</button>
              </form>
            </div>

            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
          </body>
        </html>
        """


if __name__ == "__main__":
    app.run(debug=True)
