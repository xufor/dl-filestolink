import re
import requests
from sys import stdin as si

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'x-requested-with': 'XMLHttpRequest',
    'DNT': '1',
    'Connection': 'keep-alive',
}

print("=========================HOW TO USE==========================")
print("=> Paste the selected messages from @filestolink telegram bot")
print("=> Press Enter")
print("=> Press Ctrl+D")
print("=============================================================")

text = str()
while True:
    try:
        text += input()
    except EOFError:
        break

links = [l[1:-1] for l in re.findall('\(....................\)', text)]

if len(links) > 0:
    for link in links:
        if link:
            response = requests.get(link, headers=headers)
            #print(response.text)
            response = response.text.split('\n')
            for index in range(len(response)):
                position = response[index].find('id="video-fully-responsive"')
                if(position != -1):
                    print(r'http://www.filestolink.gq' + response[index+1].strip()[13:-20])
                    break
                position = response[index].find('class="filename"')
                if(position != -1 and response[index+2].strip() != "<div id='vidiv'>"):
                    print(r'http://www.filestolink.gq' + response[index+2].strip()[9:-2])
                    break
