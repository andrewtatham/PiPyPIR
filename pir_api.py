from flask import Flask, jsonify

import pir_service

app = Flask(__name__)
svc = pir_service.PirService()


@app.route("/")
def pir():
    return jsonify(svc.pir())


def run():
    app.run(debug=True)


if __name__ == '__main__':
    run()
