from sys import exit
import random # to get randoms for make_game
import time # for delaying the printing of the text to screen
# from sys import argv # this was used for test()

# A short game.  I used to time to make the text more naturally appear on the screen
# as it's played. I'm not sure it's a 'fun' game. Enjoy responsibly. 


def demon():
	# this is the Demon encounter
	print "\nA DEMON emerges from a crevice in the wall."
	print "He's kinda bummed you're here." 
	print "What's the best course of action?" 
	time.sleep(1)
	choice = raw_input("run, search, or fight?> ")
	demon_battle = True
	
	while demon_battle == True:
		if choice == 'run':
			time.sleep(1)
			print "Who wants to fight a demon? Not you!"
			demon_battle = False
			run_away()
		elif choice == 'search':
			time.sleep(1)
			print "\nWhat exactly are you looking for?"
			print "The Demon is like, right in front of you...\n"
			time.sleep(1)
			print "The Demon reaches into your chest and removes your"
			print "still-beating heart."
			time.sleep(2)
			greeting("You're dead!",2)
			greeting("GAME OVER", 1)
			exit(0)
		elif choice == 'fight':
			time.sleep(1)
			print "\nYou punch the demon in the face."
			time.sleep(1)
			print "Dude goes down a like a ton of bricks."
			print "You totally kicked his ass!"
			time.sleep(1)
			print "You venture forth..."
			time.sleep(2)
			demon_battle = False
		else:
			time.sleep(1)
			print "\nYou don't know how to type. What are you doing?"
			print "In life, as in this game, there are no 2nd chances."
			print "You auto-decide that fighting is a better choice..."
			time.sleep(1)
			choice = 'fight'

def champion():
	# Champion encounter
	print "\nA CHAMPION with a big-ass sword approaches."
	print "He's visibly upset with your presence." 
	
	time.sleep(.5)
	choice = raw_input("run, search, or fight?> ")
	
	champ_battle = True
	while champ_battle == True:
		if choice == 'run':
			time.sleep(1)
			print "Who wants to fight a Champion? Not you!"
			run_away()
			champ_battle = False
		elif choice == 'search':
			time.sleep(1)
			print "\nYou look around. Nothing to see, here."
			time.sleep(1)
			print "The Champion comes closer as you browse the area."
			time.sleep(1)
			print "His breath is terrible so you decide it's time to go..."
			time.sleep(1)
			run_away()
			champ_battle = False
		elif choice == 'fight':
			time.sleep(1)
			print "\nYou grab a large rock and chuck it at the Champion."
			print "The rock strikes the champion in the noggin'."
			time.sleep(2)
			print "He yelps, drops, his sword, and craps his pants."
			time.sleep(2)
			print "Not bad, brave adventurer, not bad at all..."
			champ_battle = False
		else:
			time.sleep(1)
			print "\nThat's really not a valid move..."
			print "I've got an idea: how about you run? Yeah. Lets."
			run_away()
			champ_battle = False

def theif():
	# Theif encounter 
	print "\nUh, yeah, your wallet is totally gone."
	print "You'll have to cancel your credit cards, etc."
	print "You've obviously encountered a THEIF!."
	print "What do you do? There's nobody to fight!"
	
	choice = raw_input("search or run> ")
	theif_battle = True
	
	while theif_battle == True:
		if choice == 'run':
			print "\nWhat's your driver license going to do to protect you here? Nothing."
			theif_battle = False
			time.sleep(1)
			run_away()
		elif choice == 'search':
			time.sleep(1)
			print "\nYou search the area and see a little dude crouched"
			print "behind a rock.  You yell for him to show himself..."
			time.sleep(2)
			print "When he appears, you kick him in the balls, get your"
			print "wallet from his pocket."
			time.sleep(1)
			give_mercy = raw_input("Spare the Theif's life (yes or no)? >")
			
			if give_mercy == 'yes':
				print "The sneaky fucker stabs you in the back"
				print "as you try to make an exit."
				time.sleep(1)
				greeting("You're kind... and dead!",2)
				greeting("GAME OVER", 1)
				exit(0)
			elif give_mercy == 'no':
				time.sleep(1)
				print "You drive your foot into the theif's skull."
				time.sleep(2)
				print "The Theif is dead.  You're cold af."
				theif_battle = False
			else:
				greeting("Bad move, you're toast!",2)
				greeting("GAME OVER", 1)
				exit(0)
		else:
			time.sleep(1)
			print "\nIt's obvious you're having trouble with instructions..."
			print "In times like this, it's usually better to gtfo..."
			theif_battle = False
			time.sleep(2)
			run_away()
	
def dragon():
	# dragon battle. 
	print "\nA DRAGON slithers from a hole in the ground."
	print "It's not enthusiastic about your existence."
	time.sleep(2)
	print "Combat is not an option... can an ant participate"
	print "in combat with a grown human? Can you even?"
	
	time.sleep(1)
	choice = raw_input("run or run?> ")
	
	if choice == 'run':
		print "\nThat's a good call, holmes - go!"
		run_away()
	else:
		print "\nAre you kidding? It's a dragon.  It's massive."
		time.sleep(1)
		print "The dragon bites your head off.  Your headless body"
		print "drops to the floor in a heap. Gross!"
		time.sleep(1)
		greeting("You're dead!",2)
		greeting("GAME OVER", 1)
		exit(0)

def make_game():
	# create a list of up to 4 'encounters' during game
	game_size = random.randint(2,4)
	encounters = ['demon', 'champion', 'theif', 'dragon']
	game = random.sample(encounters, game_size)
	'''
	Example outputs for make_game(),random samples of game:
	['champion', 'theif']
	['demon', 'dragon', 'champion', 'theif']
	['champion', 'dragon', 'theif']
	'''
	return game

def run_away():
	# select a random 'run' phrase and print
	run_phrase = random.randint(1,3)
	time.sleep(1)
	if run_phrase == 1:
		print "You hit the bricks and escaped!"
	elif run_phrase == 2:
		print "You flailed your arms and escaped with finesse!"
	elif run_phrase == 3:
		print "You high-tailed it outta there! Phew!"
	else: 
		exit(0)
		
def greeting(phrase, i):
	# full boarder if i is included in function call
	if i == 1:
		print "*"*49
		print "*"*((50-len(phrase))/2) + phrase + "*"*((50-len(phrase))/2)
		print "*"*49
	else:
		print "*"*((50-len(phrase))/2) + phrase + "*"*((50-len(phrase))/2)
		
def start():
	
	greeting("Shit's about to get real...", 1)
	print "\nYou've come to a scary-ish place"
	print "You may encounter up to 4 creatures\n"
	time.sleep(1)
	game = make_game()
	counter = 0
	
	for i in game:
		encounter = i # select first randomly generated encounter
		end_of_game = len(game)
		if encounter == "demon":
			counter += 1
			demon()
		elif encounter == "theif":
			counter += 1
			theif()
		elif encounter == "champion":
			counter += 1
			champion()
		elif encounter == "dragon":
			counter += 1
			dragon()
		else:
			exit(0)
		
		# prints the "What's next" after every move except last move
		if end_of_game != counter:
			greeting("\nWhat's next?!\n", 2)
			time.sleep(2)
		#print counter
	greeting("You survived!", 2)
	greeting("GAME OVER", 1)


start()

'''
script, filename = argv
def test():
# this was used to see the ouputs of 'make_game()' 
# note that the .txt file was in the directory already.
	test = []
	test1 = []
	test2 = []
	test= make_game()
	test1 = make_game()
	test2 = make_game()
	print test
	print test1
	print test2

	x = test
	x1 = test1
	x2 = test2

	txt = open(filename, 'w')
	txt.write(str(x)+'\n')
	txt.write(str(x1)+'\n')
	txt.write(str(x2))
	txt.close()
'''
