import pandas as pd 

words = pd.read_csv("subdhkosh.csv") 

########search##############
############################
def search():
	string =""
	guess = []
	i =0
	j=0
	l_inc_pos = input("Enter positionally incorrect letters: ") #letter incorrect position
	l_inc = input("Enter incorrect letters: ")#letter incorrect
	l_inc_pos = l_inc_pos.upper() 
	l_inc = l_inc.upper()
	while i < 12478:
		string=words.iat[i,0]
		if(string.find(l_inc_pos[0])!=-1):
			guess.append(words.iat[i,0])
		i+=1
	j=0
	i=0
	while j<len(l_inc_pos):
	#print(j)
		i=0
		while i<len(guess):
			string=guess[i]
			if(string.find(l_inc_pos[j])==-1): #if I can't find the letter I delete it from guess array 
				guess.remove(guess[i])
				i-=1
			i+=1
		j+=1
	
	#############################
	#############################
	#######parsing incorrect#####
	#############################
	j=0
	i=0
	string=""
	#print(l_inc)
	while j<len(l_inc):
	#print(j)
		i=0
		while i<len(guess):
			string=guess[i]
			if(string.find(l_inc[j])!=-1): #if I CAN find the letter I delete it from guess array 
				guess.remove(guess[i])
				i-=1 #since the element if removed we need to decreament the index
			i+=1
		j+=1



	i=0
	while(i<len(guess)):
		print(guess[i])
		i+=1
############################
############################

#############################
#######run it again?#####
#############################
k=0
run=""

while(run.upper()==""):
	if(k==0):
		run = input("Search? y/n: ") 
		if(run.upper()=="Y"):
			search()
			run=""
	else:
		run = input("Search again? y/n: ")
		if(run.upper()=="Y"):
			search()
			run=""
	k+=1

if(run.upper()!="Y"):
	print("program terminated")




	



