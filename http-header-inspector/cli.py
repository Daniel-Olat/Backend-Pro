import requests

def main_cli():
  action = input("Enter r to register , l to login if you have an account: ").strip().lower()
  username = input("Enter username: ").strip()
  password = input("Enter password: ").strip()
  
  if action == "r":
        resp = requests.post("http://127.0.0.1:5000/register", json={"username": username, "password": password})
        try:
          print(resp.json())
        except ValueError:
          print("Server did not return JSON. Raw response:", resp.text)
      
  login_resp = requests.post("http://127.0.0.1:5000/login", json={"username": username, "password": password})
  if login_resp.status_code != 200:
        print("Login failed:", login_resp.json())
        return
      
  token = login_resp.json().get("token")
  url = input("Enter a valid URL: ").strip()
  

  try:
    response = requests.get("http://127.0.0.1:5000/inspect", params={'url': url},headers={"Authorization": f"Bearer {token}"}, timeout=10)
    if response.status_code == 200:
      headers = response.json()
      print("URL Headers:")
      for key, value in headers.items():
        print(f"{key}: {value}")
    else:
      try:
        err = response.json()
      except Exception:
        err = response.text
      print('Error:', err)

  except Exception as e:
    print("Failed to connect:", e)
    
    
if __name__ == "__main__":
  main_cli()