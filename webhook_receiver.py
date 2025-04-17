from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"Signal empfangen: {data}")
    return jsonify({"message": "Signal empfangen"}), 200

if __name__ == '__main__':
    # Host ändern, damit Flask auf 0.0.0.0 lauscht
    app.run(host='0.0.0.0', port=5000)
