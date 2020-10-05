#variabler
årskort = 2500
biljett = 25

biljett = float(input("Vad är priset för en biljett? "))

antal_besök = float(input("Hur många gånger besöker du gymmet på ett år? "))

årskort = float(input("Vad är priset för ett årskort? "))


if biljett * antal_besök < årskort:
	print("Årskort är INTE värt det för dig!")
else:
	print("Årskort ÄR värt det för dig!")

