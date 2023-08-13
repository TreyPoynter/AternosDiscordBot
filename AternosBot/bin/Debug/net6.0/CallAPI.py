# Import
import sys
from python_aternos import Client
from python_aternos import ServerStartError

# Log in
aternos = Client.from_credentials('The_Imposter2', 'Nowayamongus!') # User, Pass

servs = aternos.list_servers()

myserv = servs[0]

currServer = None
for serv in servs:
    if serv.address == 'Metrovania_2.aternos.me': # IP
        currServer = serv

serverIsStarted = False;

if currServer is not None:
   try:
        currServer.start()
        serverIsStarted = True;
   except ServerStartError as err:
        print(err.code)
        print(err.message)
        serverIsStarted = False;
else:
    print('Server not found')

if serverIsStarted:
    print(serverIsStarted, end="")

