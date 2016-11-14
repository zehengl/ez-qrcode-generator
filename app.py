from flask import Flask, send_file, request
import qrcode
from StringIO import StringIO

app = Flask(__name__)


def serve_image(img):
    img_io = StringIO()
    img.save(img_io, 'png')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img = qrcode.make(request.form['password'])
        return serve_image(img)
    else:
        return """
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta http-equiv="x-ua-compatible" content="ie=edge">

            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/css/bootstrap.min.css" integrity="sha384-AysaV+vQoT3kOAXZkl02PThvDr8HYKPZhNT5h/CXfBThSRXQ6jW5DO2ekP5ViFdi" crossorigin="anonymous">
          </head>
          <body>
            <form method="post">
                <div class="form-group">
                    <label for="exampleInputEmail1">String to convert:</label>
                    <input type="text" name="password" class="form-control" placeholder="Type Something">
                    <input type="submit" value="Submit">
                </div>              
            </form>

            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="sha384-3ceskX3iaEnIogmQchP8opvBy3Mi7Ce34nWjpBIwVTHfGYWQS9jwHDVRnpKKHJg7" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.3.7/js/tether.min.js" integrity="sha384-XTs3FgkjiBgo8qjEjBk0tGmf3wPrWtA6coPfQDfFEY8AnYJwjalXCiosYRBIBZX8" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.5/js/bootstrap.min.js" integrity="sha384-BLiI7JTZm+JWlgKa0M0kGRpJbF2J8q+qreVrKBC47e3K6BW78kGLrCkeRX6I9RoK" crossorigin="anonymous"></script>
          </body>
        </html>
        """

if __name__ == '__main__':
    app.run(debug=True)
