# This is a grade calculator.


grade = int(input("Enter Grade:"))

if grade >= 55:
    print("you passed!")
else:
  print("you failed.")


# This is a pH calculator.
 
pH = int(input("Enter Value Between 1-14:"))

if pH > 7:
    print ("Basic")
elif pH < 7:
    print ("Acidic")
else:
    print ("Neutral")       


# This is a magic 8-ball


import random

question = input("Question:     ")

random_number = random.randint(1, 9)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2: 
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"  

print (answer)