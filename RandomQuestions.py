import random as r

questions = ['1. Question 0?',
			 '2. Question 1?',
			 '3. Question 2?',
			 '4. Question 3?',
			 '5. Question 4?',
			 '6. Question 5?',
			 '7. Question 6?',
			 '8. Question 7?',
			 '9. Question 8?',
			 '10. Question 9?',
		    ]

userChoice = 'y'
end = 'n'
while userChoice != 'n':
	if len(questions) == 0:
		print("No questions left!")
		break

	random_item = r.choice(questions)
	print(random_item)
	questions.remove(random_item)
	
	print("Next question? y/n : ")
	userChoice = input()

	if userChoice != 'y' and userChoice != 'n':
		print("Neither 'y' or 'n' was entered, let's take a break!")
		break