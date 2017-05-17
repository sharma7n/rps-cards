from collections import Counter

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from twilio.twiml.messaging_response import MessagingResponse

from tinydb import TinyDB, Query

app = Flask(__name__)
CORS(app)

db = TinyDB("cards.json")

@app.route("/")
def cards():
    return jsonify(db.all()[0])

@app.route("/sms", methods=['POST',])
def sms():
    event = Counter(request.form['Body'].upper())
    counts = db.all()[0]
    counts['rock'] = max(counts['rock'] - event['R'], 0)
    counts['paper'] = max(counts['paper'] - event['P'], 0)
    counts['scissors'] = max(counts['scissors'] - event['S'], 0)
    
    db.update(counts, Query().id == "1")
    
    response = MessagingResponse()
    msg = "Remaining: {} rock, {} paper, {} scissors.".format(
        counts['rock'], counts['paper'], counts['scissors'])

    response.message(msg)
    return str(response)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True)