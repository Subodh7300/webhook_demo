from flask import Flask, request

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        if request.headers['key'] == "UZw3KfpfGU2QpMFEOWhQNSmnXyhOGD6G" and request.headers['Content-Type'] == "application/json":
            return {"success": True}, 200, "OK"
        else:
            return {"success": False}, 400, "Bad request"
    except:
        return {"success": False}, 500, "Authentication error"


if __name__ == "__main__":
    app.run()
