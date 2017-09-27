from flask import Flask, request, jsonify, make_response
app = Flask(__name__)


@app.route('/')
def main():
    return """
    <p>get fragments: GET request to /generate endpoint with difficulty level (easy, medium, hard)</p>
    <p>validate solution: POST request to /validate endpoint with difficulty level (easy, medium, hard)</p>
    """


@app.route('/generate', methods=['GET'])
def generate():

    return request.args["level"]


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
