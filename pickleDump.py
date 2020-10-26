import pickle
import os

def zapiszDane():
	with open("daneGosci.txt", "wb") as plik:
		pickle.dump(daneFosci, plik)


def odczytajDane():
	daneGosci = []
	statinfo = os.stat("daneGosci.txt")
	if (statinfo.st_size == 0):
		return daneGosci
	try:
		with open("daneGosci.txt","rb") as plik:
			daneGosci = pickle.load(plik)
	except EOFError:
		print("plik jest pusty")
	return daneGosci

zapiszDane()
odczytajDane()