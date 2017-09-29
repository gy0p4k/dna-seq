from flask import Flask, request, jsonify, make_response
from generator import splitter
app = Flask(__name__)


@app.route('/')
def main():
    return """
    <p>get fragments: GET request to /generate endpoint with difficulty level (easy, medium, hard)</p>
    """


@app.route('/generate', methods=['POST'])
def generate():
    try:
        return generate_fragment(request.form["level"])
    except:
        raise


def generate_fragment(level):
    return get_json_return(splitter(get_seq(level)))


def get_seq(filename):
    with open(filename, "r") as file:
        return file.read()


def get_json_return(fragments):
    return jsonify({"fragments": fragments})


if __name__ == '__main__':
    # app.run(debug=True, use_reloader=True)
    app.run(port=5001, debug=True)
