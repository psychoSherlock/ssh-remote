# Starts the server and sends the ngrok url to remote text share

from os import system as shell
from subprocess import run
from time import sleep as wait
import sys

def startSSH():
    print("💀 Starting local ssh server")
    shell('sudo service ssh start')
    print("☠️  Local ssh server started")
    return


def sendData():

    ngrokServer = run('curl -s localhost:4040/api/tunnels | jq -r .tunnels[0].public_url', capture_output=True, shell=True) # Capturing ngrok url from local webserver started by ngrok on port 4040 and piping it to json to get public url
    ngrokServer = ngrokServer.stdout.decode() # Decoding subprocess output
    data = str(ngrokServer)

    print(f'💀 Sending data {data}')
    shell(f'curl -H "Content-Type: text/html; charset=UTF-8" -X POST --data "{data}" https://api.cl1p.net/55hserver ')
    print(f'Data Sent....')

    return

def stopSSH():
    print('👻 Stopping local ssh server...')
    shell('sudo service ssh stop')
    
    print("👻 Clearing remote data..") # For clearing left alone ngrok url
    run('curl -s https://api.cl1p.net/55hserver > /dev/null', shell=True)
    
    print('👻 Killing ngrok and stopping port forward')
    shell("killall ngrok")
    print("💩 Quitting..")
    return

try:
    startSSH()

    # Enabling port forwd on another terminal
    print('☠️  Starting port forward..')
    shell('x-terminal-emulator -e ./ngrok.sh')
    print('🤖 Port Forward enabled..')
    wait(4)


    # Sending ngrok url
    ngrokServer = run('curl -s localhost:4040/api/tunnels | jq -r .tunnels[0].public_url', capture_output=True, shell=True) # Capturing ngrok url from local webserver started by ngrok on port 4040 and piping it to json to get public url
    ngrokServer = ngrokServer.stdout.decode() # Decoding subprocess output
    data = str(ngrokServer)

    print(f'☠️  Sending data {data}')
    shell(f'curl -s -H "Content-Type: text/html; charset=UTF-8" -X POST --data "{data}" https://api.cl1p.net/55hserver ')
    print(f'☠️  Data Sent....')



    input('💩 Started port forwarding...\nPress CTRL + C to quit \n')
    stopSSH()
    sys.exit()

except KeyboardInterrupt:
    stopSSH()
    sys.exit()
