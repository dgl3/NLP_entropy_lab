# -*- coding: utf-8 -*-
#!/pkg/ldc/bin/python2.5
#-----------------------------------------------------------------------------
# Name:        main.py
#
#-----------------------------------------------------------------------------
from auxiliar import *

def computeUnigramModel(pathfile):
    enWords = getWordsFromFile(pathfile)
    (U,B,T) = countNgrams(enWords,0,0)
    entropy = 0
    length = Decimal(len(enWords));
    
    for key in U.keys():
	U[key] = Decimal(U[key]/length)
        entropy += (U[key]*Decimal(log(U[key])))
        
    return -1*entropy

def computeBigramModel(pathfile):
    enWords = getWordsFromFile(pathfile)
    (U,B,T) = countNgrams(enWords,0,200)
    entropy = 0.0
    length = float(len(enWords));
    bilength = 0.0    

    for val in B.values():
	bilength += val

    for key in U.keys():
	pX = U[key]/length
        
	
 	sumatory = 0.0
	for bkey in B.keys():
		if bkey[0] == key:
			print bkey[0], bkey[1]
			# .. later remove this entry from dict
			pYX = B[bkey]/bilength
			pY = U[bkey[1]]/length
			pXIY = pYX/pY
			sumatory += pXIY * log(pXIY)

	entropy += pX*sumatory
	
    
    return -1*entropy

def computeTrigramModel(T):
    print "Function to compute the trigram model"

      
##importing tagged brown corpus from NLTK
##importingBrownCorpusFromNLTK("../corpus/taggedBrown.txt")

#taggedWords = getTaggedWordsFromFile("corpus/taggedBrown.txt")
#enWords = getWordsFromFile("corpus/en.txt")
#esWords = getWordsFromFile("corpus/es.txt")

#(U,B,T) = countNgrams(enWords,0,0)

#unigramEntropy = computeUnigramModel("corpus/en.txt")
#print unigramEntropy

bigramEntropy = computeBigramModel("corpus/en.txt")
print bigramEntropy







