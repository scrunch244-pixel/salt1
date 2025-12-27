import requests

GIST_ID = "e5e979572c4cb5bfe8fcf1d4d5ddb6af"
TOKEN = "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"
GIST_URL = f"https://api.github.com/gists/{GIST_ID}"
HEADERS = {"Authorization": f"token {TOKEN}"}

def load_csv_local():
    try:
        with open("expenses.csv", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "التاريخ,القسم,المبلغ,ملاحظات\n"

def save_csv_to_gist(csv_content):
    data = {
        "files": {
            "expenses.csv": {
                "content": csv_content
            }
        }
    }
    response = requests.patch(GIST_URL, headers=HEADERS, json=data)
    print(f"Response status: {response.status_code}")
    if response.status_code != 200:
        print(f"Error: {response.text}")
    return response.status_code == 200

csv_content = load_csv_local()
print("Local CSV Content:")
print(repr(csv_content))
print("Lines:", len(csv_content.split('\n')))

if save_csv_to_gist(csv_content):
    print("Successfully uploaded to Gist.")
else:
    print("Failed to upload to Gist.")
