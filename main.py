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


