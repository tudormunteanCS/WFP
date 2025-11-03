import msal
import requests
import os


TENANT_ID_ENDAVA = "0b3fc178-b730-4e8b-9843-e81259237b77"
CLIENT_ID_ENDAVA = "4a0b27f7-9b96-4d5c-9279-01f2049a00aa"
CLIENT_SECRET_ENDAVA = os.getenv("CLIENT_SECRET_ENDAVA")
AUTH = f"https://login.microsoftonline.com/{TENANT_ID_ENDAVA}"
SCOPE = ["https://graph.microsoft.com/.default"]

app = msal.ConfidentialClientApplication(CLIENT_ID_ENDAVA, authority=AUTH, client_credential=CLIENT_SECRET_ENDAVA)
token = app.acquire_token_for_client(scopes=SCOPE)["access_token"]
headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

GRAPH_API_URL = "https://graph.microsoft.com/v1.0/sites/endava.sharepoint.com:/sites/RomaniaWFPSpace:/drive/root/children"

response = requests.get(GRAPH_API_URL, headers=headers)
json_response = response.json()
print("Response:", json_response)