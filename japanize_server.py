from flask import jsonify, Flask

import japanize

app = Flask(__name__, static_folder="static")


@app.route("/api/japanize/<names>")
def japanize_api(names):
    return jsonify(list(map(japanize.transform, names.split(" "))))


@app.route("/")
def root():
    return app.send_static_file("index.html")


if __name__ == '__main__':
    app.run(debug=True)
