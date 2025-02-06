from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Your HR Chatbot is running."

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    question = req.get('queryResult', {}).get('queryText', '').lower()

    responses = {
        "how many pto days do i have?": "You have 15 PTO days remaining.",
        "how do i get alumni access?": "You can use your old username. A temporary password has been sent to your email.",
        "how can hr employees get records?": "HR employees can request records through the HRIS system."
    }

    answer = responses.get(question, "I'm not sure about that. Please contact HR for more details.")
    return jsonify({'fulfillmentText': answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName")

    # Example HR response
    if intent == "Check_Payroll":
        return jsonify({"fulfillmentText": "Your last paycheck was $1,200 on Jan 31."})

    return jsonify({"fulfillmentText": "Sorry, I didn't understand that."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)

