
import requests

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}
response = requests.post("https://api.openai.com/v1/images/generations", json={
    "prompt": "circular icon with padding around background, cute snake, flat vector graphic",
    "n": 1,
    "size": "256x256"
  }, headers=headers)

print(response.text)