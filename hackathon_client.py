import os
import google.auth
import json
import requests
from dotenv import load_dotenv, find_dotenv

# load environment variables
_=load_dotenv(find_dotenv())

# read environment variables
PROJECT_ID = os.getenv('PROJECT_ID_INT')
LOCATION = os.getenv('AGENT_LOCATION')
REASONING_ENGINE_ID = os.getenv('REASONING_ENGINE_ID')

# agent client code
def call_tmf_aiva_agent(query_str, token):
  """Makes a POST request to the specified Reasoning Engine endpoint."""
  # Set the headers and data
  headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json; charset=utf-8",
  }

  # Create the JSON payload from the query_str
  json_input = {"input": {"input": f"{query_str}"}}

  # Construct the URL
  url = f"https://{LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{REASONING_ENGINE_ID}:query"

  # Send the POST request
  r = requests.post(url, headers=headers, data=json.dumps(json_input))
  return r.json()

## Generate user default auth token
credentials, _ = google.auth.default()
request = google.auth.transport.requests.Request()
credentials.refresh(request)
token = credentials.token

query = "Describe ODF?"

agent_response = call_tmf_aiva_agent(query, token)

print(agent_response)