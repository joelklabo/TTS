#!/usr/bin/env python3

# Change this to the IP address of your 21 Bitcoin Computer.
# You can find this with `sudo hostname --ip-address`
SERVER_IP_ADDRESS='10.244.195.231'

# Import methods from the 21 Bitcoin Library
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

# Configure your Bitcoin wallet. 
username = Config().username
wallet = Wallet()
requests = BitTransferRequests(wallet, username)

# Send text to the endpoint
def send_text(text):
  # tell the user what text they're sending
  print('You sent {0}'.format(text))

  # 402-payable endpoint URL and request
  tts_url = 'http://' + SERVER_IP_ADDRESS + ':5000/tts?text={0}'
  speech = requests.get(url=tts_url.format(text))

  # save the received audio file to disk
  speech_output = open('speech.wav', 'wb')
  speech_output.write(speech.content)
  speech_output.close()

# Read the text to speechify from the CLI
if __name__ == '__main__':
  from sys import argv
  send_text(argv[1])
