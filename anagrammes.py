


def liste_anagrammes(mot) :
	if len(mot)==1 : return [mot]

	liste=[]
	for anagr in liste_anagrammes(mot[1:]) :
		for k in range(len(mot)) :
			liste.append(anagr[:k]+mot[0]+anagr[k:])
	return liste
	


