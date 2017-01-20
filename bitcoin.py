# coding: utf8

import os
import time
import json
from pprint import pprint

def display_info(dir, info):
	print("Checking info")
	os.system("bitcoin-cli -datadir=" +str(dir)+" getinfo > test"+str(dir))
	with open('test'+ str(dir)) as data_file:
		data =json.load(data_file)
	print("user " + str(dir) + " has currently " + str(data[info]) + " "+ info)
	os.system("rm test" + str(dir))

def mine_blocks(dir, n_blocks):
	print("Now mining " + str(n_blocks) +" blocks")
	os.system("bitcoin-cli -datadir=" + str(dir) + " generate " + str(n_blocks) + " > /dev/null")

def start_bitcoin():
	print("Starting 2 bitcoin users")
	os.system("bitcoind -datadir=1 -daemon > /dev/null")
	os.system("bitcoind -datadir=2 -daemon > /dev/null")

def stop_bitcoin():
	os.system("bitcoin-cli -datadir=1  stop")
	os.system("bitcoin-cli -datadir=2  stop")

def newaddress(dir):
	os.system("bitcoin-cli -datadir="+str(dir)+" getnewaddress > address")
	f = open('address', 'r')
	address = f.read()
	f.close
	os.system("rm address")
	return address

def sendbitcoin(dir, address, amount):
	os.system("bitcoin-cli -datadir="+str(dir)+' sendtoaddress "' + address + '" '  + str(amount))



print "Welcome to this bitcoin test program"
os.system("echo Hello World")

start_bitcoin()

time.sleep(10)
display_info(1, "blocks")
#pprint(data)
mine_blocks(1, 100)
display_info(1, "blocks")
display_info(1, "balance")

address1 = newaddress(1)
print "Address of user 1 : " + address1
address2 = newaddress(2)

sendbitcoin(1, address2, 10)
mine_blocks(1,1)

display_info(1,"balance")
display_info(2,"balance")

stop_bitcoin()