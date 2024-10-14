from flask import Flask, request, jsonify
from queries import handle_queries

app = Flask(__name__)

@app.route('/vulnerable-query', methods=['POST'])
def vulnerable_query():
    user_input = request.json['input']  # external input from user
    result = handle_queries('vulnerable', user_input)

    return jsonify([dict(row) for row in result])

@app.route('/safe-query-int', methods=['GET'])
def safe_query_int():
    user_id = int(request.args.get('id'))  # input is a number
    result = handle_queries('safe-int', user_id)

    return jsonify([dict(row) for row in result])

@app.route('/safe-query-constant', methods=['GET'])
def safe_query_constant():
    result = handle_queries('safe-constant')

    return jsonify([dict(row) for row in result])

if __name__ == '__main__':
    app.run(port=4000)
