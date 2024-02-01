import random
cpu = random.randint(1,3)

user = input ("Enter rock, paper, or scissors: ")

if user == "rock":
	if cpu == 1: #cpu chose rock
		print("Tied game!")
	elif cpu == 2: #cpu chose paper
		print("Womp womp, you lost!")
	else: #cpu chose scissors 
		print ("Woop Woop, you won!")

if user == "paper":
	if cpu == 1: #cpu chose rock
		print("Woop Woop, you won!")
	elif cpu == 2: #cpu chose paper
		print("Tied game!")
	else: #cpu chose scissors 
		print ("Womp womp, you lost!")

if user == "scissors":
	if cpu == 1: #cpu chose rock
		print("Womp womp, you lost!")
	elif cpu == 2: #cpu chose paper
		print("Woop Woop, you won!")
	else: #cpu chose scissors 
		print ("Tied game!")



