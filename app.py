from flask import Flask
from flask.globals import request
from PIL import Image
from io import BytesIO
from flask.helpers import send_file

app = Flask(__name__)
##hola que tal
##$dsd
@app.route('/')
def hello_world():
    return "hello world  +1 +2 +4 +5 ++6"

@app.route('/primerapi')
def prueb():
    return "hola pee apisito"

@app.route('/samanta')
def doc():
    return "Espero que te encuentres bien, te comparto este detalle bebesitaaa, espero que nos podamos ver más adelante"

@app.route('/cat.jpg')
def cat():
    width = request.args.get('width')
    height = request.args.get('height')

    size = (int(width), int(height))

    img = Image.open('gato.jpg')
    img.thumbnail(size)
    img_io = BytesIO()
    img.save(img_io, "JPEG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")
