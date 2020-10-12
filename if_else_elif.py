import time
import sys

print("Du ska vara på ditt jobb klockan 8:00")
time.sleep(2)


while True:
	print("Klockan är 05:00 på morgonen.")
	time.sleep(2)
	svar = input("Vill du vakna?")
	if svar == "ja":
		print("Nu är du vaken. Men det är ju så tidigt?")
		sys.exit()
		time.sleep(2)
	if svar == "nej":
		print("Du sover lite till.")
		time.sleep(2)


	print("Klockan är nu 05:30 på morgonen.")
	time.sleep(2)
	svar = input("Vill du vakna?")
	if svar == "ja":
		print("Nu är du vaken.Men du kunde sovit lite till.")
		sys.exit()
		time.sleep(2)
	if svar == "nej":
		print("Du fortsätter sova.")
		time.sleep(2)


	print("Klockan är nu 06:00 på morgonen.")
	time.sleep(2)
	svar = input("Vill du vakna?")
	if svar == "ja":
		print("Nu är du vaken. Ha det bra.")
		sys.exit()
		time.sleep(2)
	if svar == "nej":
		print("Du sover nu vidare.")
		time.sleep(2)


	print("Klockan är nu 06:30 på morgonen.")
	time.sleep(2)
	svar = input("Vill du vakna?")
	if svar == "ja":
		print("Nu är du vaken. Ha en bra dag!")
		sys.exit()
		time.sleep(2)
	if svar == "nej":
		print("Du sover nu vidare. Men kom ihåg att inte sova för länge.")
		time.sleep(2)


	print("Klockan är nu 07:00 på morgonen.")
	time.sleep(2)
	svar = input("Vill du vakna?")
	if svar == "ja":
		print("Nu är du vaken. Men gör dig klar snabbt.")
		sys.exit()
		time.sleep(2)
	if svar == "nej":
		print("Du sover nu vidare. Men det kommer bli stressigt senare.")
		time.sleep(2)


	print("Klockan är nu 07:30 på morgonen.")
	time.sleep(2)
	svar = input("Vill du vakna?")
	if svar == "ja":
		print("Nu är du vaken nu. Men skynda till jobbet!")
		sys.exit()
		time.sleep(2)
	if svar == "nej":
		print("Du sover nu vidare. Men du kommer missa jobbet.")
		time.sleep(2)


	print("Klockan är nu 08:00 på morgonen.")
	time.sleep(2)
	svar = input("Vill du vakna?")
	if svar == "ja":
		print("Nu är du vaken. Men du måste springa till jobbet för att inte få sparken!")
		sys.exit()
		time.sleep(2)
	if svar == "nej":
		print("Du sover nu vidare. Men du är sen till jobbet!")
		time.sleep(2)

		sys.exit()
