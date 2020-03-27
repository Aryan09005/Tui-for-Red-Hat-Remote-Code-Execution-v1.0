import os
import argparse
# import subprocess

def ex_it():
	print('\n\tGoodbye :)')
	print('-'*80)
	exit()

def check_ip(ip):
	check = os.system(f'ping {ip} -c 1')

	if check != 0:
		os.system('tput setab 01')
		print('cannot ping IP .Continue? (y/n)')
		os.system('tput setab 0')
		y_n = input()
		if y_n[0].lower() == 'y':
			return True
		else:
			ex_it()					

def version():
	parser = argparse.ArgumentParser()
	parser.add_argument('-v' ,'--version' ,action= 'version' ,version='Remote Execution Tool v1.0')
	args = parser.parse_args()
	# print(agrs)
	return args

def location():
	"""
	To select remote or local system
	"""
	print('Location local or remote (l/r) : ',end='')
	while(True):	
		location = input()
		if location[0].lower() == 'l':
			print('Local computer')
			ip = 0
			return location[0].lower(),0 ,''
			break
		elif location[0].lower() == 'r':
			print('Enter remote computer IP : ',end ='')
			ip = input()
			check_ip(ip)
			print('Enter the remote user for execution : ',end ='')
			user = input()
			print(f'Remote computer {ip} selected Remote user {user} selected')	
			return location[0].lower(), ip ,user
			break
		print('Location local or remote (l/r) :')

def run_cmd(locality, ch, ip= 0,user= 'root'):
	"""
	This will select from the dictionary 
	and run the command
	"""	
	choice= {
	1:'date',
	2:'ifconfig',
	3:'whoami',
	4:'adduser'
	}

	if locality[0].lower() == 'r':
		cmd = f'ssh {user}@{ip} {choice[ch]};'
	else:
		cmd = choice[ch]

	print('\n\n')	
	os.system(cmd)
	print('\n')	

os.system('tput setab 04')
print('\t\t\tTui for Red Hat Remote Code Execution v1.0')
os.system('tput setab 0')
"""
	While loop for making the menu and getting the input 
	and sending it to the run_cmd def
"""
try:
	# args = version()
	# if args.v:
		# print('Version ------------->v1.0')
	location, ip, user = location()
	if location =='r':
		print(f'remote ip {user}@{ip}')

		
	while(True):
	    print('1. Configure Server')
	    print('2. Strat Server')
	    print('3. Stop Server')
	    print('4. Enable Server')
	    print('5. Disable Server')
	    print('99. For exit')
	    print('choice :',end='')
	    ch = int(input())

	    if ch ==99:
	    	break
	    run_cmd(location,ch, ip, user)


except KeyboardInterrupt:
	print('\nExiting')    
	ex_it()
