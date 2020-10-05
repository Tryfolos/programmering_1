#this is a comment you know. 

import time

maxpoäng = 50

print("Hur många poäng du behöver för varje betyg:")
print("e = 25")
print("d = 30")
print("c = 35")
print("b = 40")
print("a = 45")

time.sleep(1)


while True:
	resultat = float(input("Hur många poäng fick du på provet?"))

	if resultat < 25:
		print("Ditt betyg är F")

	if resultat >= 25 and resultat < 30:
		print("Ditt betyg är E")

	if resultat >= 30 and resultat < 35:
		print("Ditt betyg är D")

	if resultat >= 35 and resultat < 40:
		print("Ditt betyg är C")

	if resultat >= 40 and resultat < 45:
		print("Ditt betyg är B")

	if resultat >= 45 and resultat < 51:
		print("Ditt betyg är A")
	
	if resultat >= 51:
		print("Man kan inte har mer än 50 poäng!")

	time.sleep(1)