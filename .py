#just alot of variables

score = 0
ques1 = 0
ques2 = 0
ques3 = 0
ques4 = 0
ques5 = 0
ques_2 = 0
ques_3 = 0
ques_4 = 0
ques_5 = 0
#-------------------------------------------------#
print("hi welcome to my quiz")
ans = input("would you like to start yes or no?: ")

if ans.lower() == ("yes"):
	question_1 = input("n = 8 n² x 4 = ")
if question_1.lower() == "256":
	score += 20
	print("good job! you have the score of", score)
else:
	ques += 1
	print("incorrect sorry!")
if score == 20:
	question_2 = input("when did the us gain independence? ")
if question_2.lower() == "1776":
	score += 20
	print("great your score is", score)
else:
	ques2 += 1
	print("sorry but you got that question wrong")
if ques1 == 1:
	question2 = input("when did the us gain independence?")
	if question2.lower() == "1776":
		score += 20
		ques_2 += 1
		print("great your score is", score)
else:
	ques_2 += 1
	print("sorry but you got that question wrong")
if ques_2 == 1:
	question3 = input("can you add lists in python?")
	if question3.lower() == "yes":
		ques4 += 1
		print("Correct your score is", score)
		score += 20
else:
	ques_4 += 1
	print("sorry but you got that wrong")
	
if ques2 == 1:
	question_3 = input("can you add lists in python?")
	if question_3.lower() == 'yes':
		ques4 +=1
		print("you got that correct your score is", score)
else:
	ques_4 += 1
	print("Sorry but you got that question wrong")
