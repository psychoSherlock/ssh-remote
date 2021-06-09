from subprocess import run as shell
import substring
from urllib.parse import urlparse
from sys import exit

print(f'Collecting data..')

ngrokData = shell('curl https://api.cl1p.net/55hserver', shell=True, capture_output=True).stdout.decode()
host = urlparse(ngrokData).hostname
port = urlparse(ngrokData).port

if host==None:
    print('NO Data found. Start the server first')
    exit()
else:
    print(f'Command: ssh {host} -p {port} -l ')
