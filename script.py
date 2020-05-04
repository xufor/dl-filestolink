import re
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'x-requested-with': 'XMLHttpRequest',
    'DNT': '1',
    'Connection': 'keep-alive',
}

no_of_lines = int(input("Enter the number of messages you selected: "))
text = str()
for _ in range(13*no_of_lines + 1):
    text += input() + "\n"

links = [l[1:-1] for l in re.findall('\(....................\)', text)]

for link in links:
    if link:
        response = requests.get(link, headers=headers)
        print(r'http://www.filestolink.gq' + response.text.split('\n')[139].strip()[9:-2])
