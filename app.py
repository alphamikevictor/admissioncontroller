from flask import Flask, escape, request

app = Flask("Admission Controller")

@app.route("/", methods=['POST'])
def controller():
    content = request.json
    app.logger.info("HOLA")
    app.logger.info(content)
    return {
        "ok": True
    }