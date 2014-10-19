# -*- coding: utf-8 -*-
#!/pkg/ldc/bin/python2.5
#-----------------------------------------------------------------------------
# Name:        main.py
#
#-----------------------------------------------------------------------------
from auxiliar import *
from math import log


def computeUnigramModel(pathfile):
    enWords = getWordsFromFile(pathfile)
    (U,B,T) = countNgrams(enWords,0,0)
    entropy = 0
    length = Decimal(len(enWords));
    
    for key in U.keys():
        U[key] = Decimal(U[key]/length)
        entropy += (U[key]*Decimal(log(U[key], 2)))
        
    return -1*entropy

def computeBigramModel(pathfile):
    enWords = getWordsFromFile(pathfile)
    (U,B,T) = countNgrams(enWords,0,0)
    length = float(len(enWords))
    
    prob = {}  #[ p(x), p(y|x) ]
    for key in U.keys():
		pX = U[key]/length
		prob[key] = [pX, 0.0]
		
    for bkey in B.keys():
        # bkey[0] = x
        # bkey[1] = y
        # tupleCountOfXAnfY / uniCountOfX
		pYIX = B[bkey] / float(U[bkey[0]])
		prob[bkey[0]][1] += pYIX * log(pYIX, 2)

    entropy = 0.0
    for val in prob.values():
        #entropy += p(x)  * p(x|y)
		entropy += val[0] * val[1]
    
    return -1*entropy

def computeTrigramModel(pathfile):
    X = 0;
    Y = 1;
    Z = 2;
    enWords = getWordsFromFile(pathfile)
    (U,B,T) = countNgrams(enWords,0,0)
    length = float(len(enWords))
    
    ### Compute and sum p(z|xy)
    probsZ_XY = {}
    for tKey, tCount in T.items():
        bKey = (tKey[X], tKey[Y])
        bCount = float(B[bKey])
        pZ_XY = tCount / bCount
        
        if bKey in probsZ_XY:
            probsZ_XY[bKey] += pZ_XY * log(pZ_XY,2)
        else:
            probsZ_XY[bKey] = pZ_XY * log(pZ_XY,2)
    
    ### Compute and sum p(x|y)
    probsYX = {}	
    for bkey, bCount in B.items():
        uKey = tKey[X]
        uCount = float(U[uKey])
        pYX = B[bkey] / uCount

        if uKey in probsYX:
            probsYX[uKey] += pYX * probsZ_XY.get(bkey, 0)
        else:
            probsYX[uKey] = pYX * probsZ_XY.get(bkey, 0)
    
    ### Compute p(x)
    entropy = 0.0
    for key in U.keys():
 		pX = U[key]/length
 		entropy += pX * probsYX.get(key, 0)

    return -1*entropy

      
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

print("--")

trigramEntropy = computeTrigramModel("corpus/taggedBrown.en")
print trigramEntropy







