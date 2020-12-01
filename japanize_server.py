from flask import jsonify, Flask

import japanize

app = Flask(__name__, static_folder="static")


@app.route("/", defaults={"names": None})
@app.route("/<names>")
def root(names):
    if names:
        return jsonify(list(map(japanize.transform, names.split(" "))))
    else:
        return app.send_static_file("index.html")
