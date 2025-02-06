from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "HR Chatbot is running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName")

    # Payroll Inquiry Intent
    if intent == "Check_Payroll":
        return jsonify({"fulfillmentText": "Your last paycheck was $2,500 on January 31, 2025."})

    # Salary Breakdown Intent
    elif intent == "Salary_Breakdown":
        return jsonify({"fulfillmentText": "Your monthly gross salary is $5,000, but after taxes and deductions, your net pay is $4,200."})

    # Tax Withholding Inquiry
    elif intent == "Tax_Withholding_Info":
        return jsonify({"fulfillmentText": "Your federal tax withholding is $600 per paycheck. You can update your W-4 in the HR portal."})

    # Bonus or Commission Inquiry
    elif intent == "Bonus_Commission":
        return jsonify({"fulfillmentText": "Your Q4 sales bonus of $1,200 will be deposited on February 15."})

    # Year-End Tax Documents (W-2, 1099)
    elif intent == "Year_End_Tax_Documents":
        return jsonify({"fulfillmentText": "Your W-2 form for 2024 is available in the HR portal. Log in to download."})

    # Default response for unknown intents
    return jsonify({"fulfillmentText": "I'm not sure how to help with that. Please contact HR for further assistance."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
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
        return jsonify({"fulfillmentText": "Your last paycheck was $2,500 on January 31, 2025."})

    elif intent == "Paycheck_Breakdown":
        return jsonify({"fulfillmentText": "Your last paycheck was $3,000. After $450 in taxes, $200 for insurance, and $100 for retirement, your net pay was $2,250."})

    elif intent == "Payroll_Correction":
        return jsonify({"fulfillmentText": "If your paycheck is incorrect, submit a payroll correction request in the HR portal. An HR specialist will review it within 3 business days."})

    elif intent == "Direct_Deposit_Status":
        return jsonify({"fulfillmentText": "Your last paycheck of $2,800 was deposited successfully on February 1, 2025."})

    elif intent == "Pay_Frequency":
        return jsonify({"fulfillmentText": "You are on a bi-weekly pay schedule. Your next paycheck will be on February 15, 2025."})

    elif intent == "Yearly_Salary_Projection":
        return jsonify({"fulfillmentText": "Based on your current salary of $5,000/month, your projected annual salary is $60,000."})

    return jsonify({"fulfillmentText": "I'm not sure how to help with that. Please contact HR for assistance."})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)


