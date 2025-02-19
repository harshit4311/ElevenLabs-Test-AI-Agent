import os
import requests

api_key = os.getenv("ELEVENLABS_API_KEY")  # Ensure it's correctly loaded
headers = {"xi-api-key": api_key}

response = requests.get("https://api.elevenlabs.io/v1/voices", headers=headers)
print(response.json())  # Should return the list of voices
