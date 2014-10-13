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

def computeBigramModel(U,B):
    entropy = 0
    for key in B.keys():
	print key
    
    return entropy

def computeTrigramModel(T):
    print "Function to compute the trigram model"

      
##importing tagged brown corpus from NLTK
##importingBrownCorpusFromNLTK("../corpus/taggedBrown.txt")

#taggedWords = getTaggedWordsFromFile("corpus/taggedBrown.txt")
#enWords = getWordsFromFile("corpus/en.txt")
#esWords = getWordsFromFile("corpus/es.txt")

#(U,B,T) = countNgrams(enWords,0,0)

unigramEntropy = computeUnigramModel("corpus/en.txt")
print unigramEntropy

#bigramEntropy = computeBigramModel("corpus/en.txt")
#print bigramEntropy







