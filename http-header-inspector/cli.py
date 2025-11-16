import requests

def main_cli():
  url = input("Enter a valid URL: ")
  url = url.strip()

  try:
    response = requests.get("http://127.0.0.1:5000/inspect", params={'url': url}, timeout=10)
    if response.status_code == 200:
      headers = response.json()
      print("URL Headers:")
      for key, value in headers.items():
        print(f"{key}: {value}")
    else:
      # Attempt to show JSON error body, otherwise fallback to text
      try:
        err = response.json()
      except Exception:
        err = response.text
      print('Error:', err)

  except Exception as e:
    print("Failed to connect:", e)
    
    
if __name__ == "__main__":
  main_cli()