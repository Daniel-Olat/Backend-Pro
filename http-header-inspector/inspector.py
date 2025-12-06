from flask import Flask, request, jsonify
import requests
import jwt, datetime
app = Flask(__name__)
SECRET_KEY  =  "secretkeysuper"
USERS = {}

def verify_token():
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None
    try:
        parts = auth_header.split(" ")
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return None
        token = parts[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception as e:
        print(f"Token verification error: {e}")
        return None
@app.route("/register" , methods = ["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username in USERS:
        return jsonify({"Error": "User already exists"}), 400
    USERS[username] = password
    return jsonify({"Message": "User registered successfully"}), 201
@app.route("/login" , methods = ['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username in USERS and USERS[username] == password:
        token = jwt.encode(
            {"user": username, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            SECRET_KEY,
            algorithm="HS256"
        )
        return jsonify({"token": token})
    else:
        return jsonify({"Error": "Invalid credentials"}), 401
@app.route('/inspect', methods=['GET'])
def http_inspect_url():
    try:
        payload = verify_token()
        if not payload:
            return jsonify({"Error": "Unauthorized. Please login first."}), 401
        
        url = request.args.get('url')
        if not url:
            return jsonify({"Error": "Please provide a valid url"}), 400

        try:
            response = requests.get(url)
            headers = dict(response.headers)
            return jsonify(headers)
        except Exception as e:
            return jsonify({"Error": str(e)}), 500
    except Exception as e:
        print(f"Inspect endpoint error: {e}")
        return jsonify({"Error": "Internal server error"}), 500
@app.route('/')
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)
