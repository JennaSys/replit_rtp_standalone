from flask import Flask


STATIC_DIR = './dist/dev'

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='/')


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

