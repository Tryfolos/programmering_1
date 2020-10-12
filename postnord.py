#Avgör om brevet är tillåtet eller inte

import time


print("Minimummått för brev är:")
print("Längd: 140mm")
print("Bredd: 90mm")


print("")
time.sleep(2)

print("Maximummåttet för brev är:")
print("Längd: 600mm")
print("Tjocklek: 100mm")
print("Bredd+Längd+Tjocklek: 900mm")

print("")

time.sleep(1)

print("Alla svar måste anges i millimeter och ska bara innehålla siffror.")

print("")

time.sleep(2)

längd = input("Vad längden på ditt brev?:")
tjock = input("Vad är tjockleken på ditt brev?:")
bredd = input("Vad är bredden på ditt brev?:")

if float(längd) >= 140 and float(längd) <= 600:
	if float(bredd) >= 90 and float(tjock) <= 100:
		if float(längd) + float(bredd) + float(tjock) <= 900:
			print("Ditt brev är godkänt!")
		else:
			print("Ditt brev är inte godkänt")
	else:
		print("Ditt brev är inte godkänt")
else:
	print("Ditt brev är inte godkänt")

time.sleep(1)