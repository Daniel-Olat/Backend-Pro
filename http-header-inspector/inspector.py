from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/inspect', methods=['GET'])
def http_inspect_url():
    url = request.args.get('url')
    if not url:
        return jsonify({"Error": "Please provide a valid url"}), 400  # To handle bad requests

    try:
        response = requests.get(url)
        headers = dict(response.headers)
        return jsonify(headers)
    except Exception as e:
        return jsonify({"Error": str(e)}), 500  # To Handle server error.
@app.route('/')
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
