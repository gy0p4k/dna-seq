from flask import Flask, request, jsonify, make_response
from github import Github, GithubException
import os

app = Flask(__name__)


@app.route('/')
def main():
    return """
    <p>get fragments: GET request to /generate endpoint with difficulty level (easy, medium, hard)</p>
    <p>example request: \{"level": "medium"\}</p>
    <p>example response: \{"fragments": ["ACA", "GTTG", "CGTA" ...]\}</p>
    <p></p>
    <p></p>
    <p>ok?</p>
    """


@app.route('/generate', methods=['GET'])
def generate():
    return "generate"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
