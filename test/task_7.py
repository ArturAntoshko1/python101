import requests

token = "live_9EHBQLG1cGOptDLjg5wUzcddDAXB6nz5LHZpvTctJwJ7CCSt3qjHA5jg1XVjGYBL"
link = f"https://api.thecatapi.com/v1/images/search?api_key={token}"

response = requests.get(link).json()
print(response)
