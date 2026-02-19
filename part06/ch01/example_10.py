import requests

robots = requests.get("https://example.com/robots.txt")
print(robots.text)
