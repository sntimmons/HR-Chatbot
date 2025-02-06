from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "HR Chatbot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName")

    if intent == "Check_Payroll":
        return jsonify({"fulfillmentText": "Your last paycheck was $1,200 on Jan 31."})

    return jsonify({"fulfillmentText": "Sorry, I didn't understand that."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

