import pandas as pd 

words = pd.read_csv("subdhkosh.csv") 
# Preview the first 5 lines of the loaded data 
rows, columns = words.shape
#print(columns)
#print(rows)
#print(type(words.iat[1,0]))


#print(l_inc_pos)
#print(l_inc_pos[0])
#print(words.iat[12477,0])

############################
############################
def search():
	string =""
	guess = []
	correct = []
	i =0
	j=0
	l_inc_pos = input("Enter positionally incorrect letters: ") #letter incorrect position
	l_inc = input("Enter incorrect letters: ")#letter incorrect
	l_pos = input("Do you know the green letters? y/n")
	if(l_pos.upper()=="Y"):
		string1 = input("First letter?")
		correct.append(string1.upper())
		string1 = input("Second letter?")
		correct.append(string1.upper())
		string1 = input("Third letter?")
		correct.append(string1.upper())
		string1 = input("Fourth letter?")
		correct.append(string1.upper())
		string1 = input("Fifth letter?")
		correct.append(string1.upper())

	l_inc_pos = l_inc_pos.upper() 
	l_inc = l_inc.upper()
	while i < 12478:
		string=words.iat[i,0]
		if(string.find(l_inc_pos[0])!=-1):
			guess.append(words.iat[i,0])
		i+=1
	# print("********")
    # print(guess)
	# print(len(guess))
	# print(len(l_inc_pos))
	# print(" ")
	# l_inc_pos=l_inc_pos[1:]
	# print(l_inc_pos)
	#print("********")
	#############################
	j=0
	i=0
	while j<len(l_inc_pos):
	#print(j)
		i=0
		while i<len(guess):
			string=guess[i]
			#l_inc_pos=l_inc_pos.capitalize()
			#print(string)
			#print(i)
			#print(l_inc_pos[j])
			#result=string.find(l_inc_pos[j])
			#print(string.find(l_inc_pos[j]))
			if(string.find(l_inc_pos[j])==-1): #if I can't find the letter I delete it from guess array 
				guess.remove(guess[i])
				i-=1
			i+=1
		j+=1
	#print(guess)
	#print(" ")
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
			#print("*****")
			#l_inc_pos=l_inc_pos.capitalize()
			#print(string)
			#print(i)
			#print(l_inc_pos[j])
			#print(string.find(l_inc_pos[j]))
			#print("*****")
			if(string.find(l_inc[j])!=-1): #if I CAN find the letter I delete it from guess array 
				guess.remove(guess[i])
				i-=1 #since the element if removed we need to decreament the index
			i+=1
		j+=1
	j=0
	i=0
	string1=""
	while j<5:
		# print(str(j))
		i=0
		while i<len(guess):
			#print(correct)
			string1=guess[i]
			if(correct[j]==""):
				pass
			else :
				# print(string1[j])
				# print(correct[j])
				if(string1[j]!=correct[j]):
					guess.remove(guess[i])
					i-=1
			i+=1
		j+=1
	#################vowel %##############
	vowel = [0]*5 
	i=0
	j=0
	string2=""
	while i<len(guess):
		j=0
		while j<5:
			string2=guess[i]
			if(string2[j]=="A"):
				vowel[0]+=1
			elif (string2[j]=='E'):
				vowel[1]+=1
			elif (string2[j]=='I'):
				vowel[2]+=1
			elif (string2[j]=='O'):
				vowel[3]+=1
			elif (string2[j]=="U"):
				vowel[4]+=1
			# string2=guess[i]
			# print(string2[j])
			
			j+=1

		i+=1
	j=0
	sum=0
	sum=vowel[0]+vowel[1]+vowel[2]+vowel[3]+vowel[4]
	print("Chances of A "+str(vowel[0]/sum*100))
	print("Chances of E "+str(vowel[1]/sum*100))
	print("Chances of I "+str(vowel[2]/sum*100))
	print("Chances of O "+str(vowel[3]/sum*100))
	print("Chances of U "+str(vowel[4]/sum*100))
	######################################

	i=0
	while(i<len(guess)):
		print(guess[i])
		i+=1

def freq_API():
	
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




	



