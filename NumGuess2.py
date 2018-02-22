# Created by Daz Buttars 10/07/17
import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print "AHOY! I'am the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99. I'll give you 6 tries. "
while guess != secret and tries < 6:
    guess = input("What's yer guess? ")
    # 20 or Higher	
    if guess - secret >=  20:
        print "Way too high, landlubber!"
    # Between 5 and 20 High
    elif (guess - secret >= 5) and (guess - secret < 20):
        print "Too high, landlubber."
    # Between secret and 5 High
    elif (guess - secret > 0) and (guess - secret < 5):
	    print "Close but too high, landlubber..."
    # Between secret and 5 Low
    elif (guess - secret < 0) and (guess - secret > -5):
	    print "Close but too low, ye scurvy dog..."
    # Between 5 and 20 Low
    elif (guess - secret <= -5) and (guess - secret > -20):
	    print "Too low, ye scurvy dog."
    # 20 or Lower
    elif guess - secret <= -20:
	    print "Way too low, ye scurvy dog!"
		
    tries = tries + 1
	
if guess == secret:
    print "Avast! Ye got it! Found my secret, ye did!"
else:
    print "No more guesses! Better luck next time, matey!"
    print "The secret number was ", secret