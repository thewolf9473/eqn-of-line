from datetime import date
a =int(input("input your age/birthdate:  "))
b=int(input("input the year in which you want to know:  "))
if a>b:
	print("error! you were not born in this year.")
elif a>200:
	print("You will turn 100 in ",100+a)
	current_age=b-a
	print(f"your age in {b} will be {current_age}")
else:
	current_year = int(date.today().year)
	print("You will turn 100 in ",(current_year-a+100))
	current_age=b-(current_year-a)
	print(f"your age in {b} will be {current_age}")


