from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "8690618479:AAHUsOxmROoY4froEmVaAFZmQtAqQpsNMI0"
CHANNEL = "@freecashxs"

@app.route("/verify", methods=["POST"])
def verify_user():
    data = request.json
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "No user_id provided"}), 400

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember"
    params = {"chat_id": CHANNEL, "user_id": user_id}
    response = requests.get(url, params=params).json()

    if response.get("ok") and response.get("result"):
        status = response["result"]["status"]
        if status in ["member", "administrator", "creator"]:
            return jsonify({"verified": True})

    return jsonify({"verified": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
