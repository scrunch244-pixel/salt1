import requests

GIST_ID = "e5e979572c4cb5bfe8fcf1d4d5ddb6af"
TOKEN = "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"
GIST_URL = f"https://api.github.com/gists/{GIST_ID}"
HEADERS = {"Authorization": f"token {TOKEN}"}

def load_csv_from_gist():
    response = requests.get(GIST_URL)
    if response.status_code == 200:
        gist_data = response.json()
        if 'files' in gist_data and 'expenses.csv' in gist_data['files']:
            csv_content = gist_data['files']['expenses.csv']['content']
            return csv_content
        else:
            return "التاريخ,القسم,المبلغ,ملاحظات\n"
    else:
        return "التاريخ,القسم,المبلغ,ملاحظات\n"

csv_content = load_csv_from_gist()
print("CSV Content from Gist:")
print(repr(csv_content))
print("Lines:", len(csv_content.split('\n')))
