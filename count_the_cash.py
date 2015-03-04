import random

def maina_count_the_cash_simulation(loops):
	''''
	This function serves to demonstrate that you must always change your initial choice immediately after maina reveals which of the 3 numbers is not correct
	
	My simulation demonstrated that those who 'STICK THEIR ORIGINAL ANSWER' will win only 33% of the time, while those who switch to the other remaining option have a 67% chance
	
	ASSUMPTIONS:
	- Currently we are assuming Maina will never tell you if your initial answer is incorrect, If that ever happens, its okay, but it's not part of the scenario we are simulating
	- We to simplify the math, we imagine 2 callers are doing the challenge and both start with the same initial answer, 1 caller always sticks to her answers, the other always switches. Lets roll and see who wins the most of the times
	This is a classic problem known as the MONTY HALL PROBLEM
	'''
	initial_choice_correct=0
	changed_choice_correct=0
	total=0
	for k in range(loops):
		total+=1
		true_correct_choice = int(random.random()*3)+1 #The secret true choice, a number between 1 and 3
		choose = int(random.random()*3)+1# The caller guesses, a number between 1 and 3
		changed_to = None
		
		#Maina makes things interesting by revealing one wrong choice, now you are left with 2 options
		if choose == true_correct_choice:		
			#If your first guess was spot on, Maina will try to confuse you by  offering that one of the 2 other numbers is known to be incorrect
			#We choose one of the 2 other numbers randomly
			revealed_wrong_choice=true_correct_choice+int(random.random()*2)+1 #The revealed number is one of the 2 numbers excluding the true correct choice
			revealed_wrong_choice = revealed_wrong_choice%3 if revealed_wrong_choice>3 else revealed_wrong_choice
		else:		
			#If Maina knows your initial guess is wrong, he offers to let you know the other incorrect choice, leaving you with your current wrong initial choice, and the true correct choice
			revealed_wrong_choice = [choice for choice in (1,2,3) if choice not in (true_correct_choice, choose)][0]
		
		#THe SWITCHER been who she is, obviosly steers away from her original answer as well as the revealed wrong answer
		changed_to = [choice for choice in (1,2,3) if choice not in (revealed_wrong_choice, choose)][0]
		
		#Only 2 possible scenarios left: 
		if true_correct_choice == choose:
			#The Stucker WON
			initial_choice_correct+=1
		elif true_correct_choice == changed_to:
			#The Switcher WON
			changed_choice_correct+=1

	print "STUCKERS WON %s %% of the time" % (float(initial_choice_correct)/total*100)
	print "SWITCHERS WON %s %% of the time" % (float(changed_choice_correct)/total*100)
	
if __name__ == "__main__":
	maina_count_the_cash_simulation(10000)