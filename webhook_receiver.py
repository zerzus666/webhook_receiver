from flask import Flask, request, jsonify

app = Flask(__name__)

# Speicherort für empfangene Signale
signals = []

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    signals.append(data)
    print(f"Signal empfangen: {data}")
    return jsonify({"message": "Signal empfangen"}), 200

if __name__ == '__main__':
    app.run(port=5000)