from flask import Flask, redirect, abort
from url import resolve_url

app = Flask(__name__)

@app.route('/<code>')
def redirect_code(code):
    long_url = resolve_url(code)
    if long_url:
        return redirect(long_url, code=302)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
