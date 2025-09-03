import os
import logging
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/", methods=["GET"])
def index():
    message = os.getenv("MESSAGE", "Hola Mundo")
    release = os.getenv("RELEASE", "v0")
    app.logger.info("Petición recibida en /")
    return jsonify({
        "message": message,
        "release": release
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
