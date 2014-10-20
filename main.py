# -*- coding: utf-8 -*-
#!/pkg/ldc/bin/python2.5
#-----------------------------------------------------------------------------
# Name:        main.py
#
#-----------------------------------------------------------------------------
from auxiliar import *
from math import log


def computeUnigramEntropy(ngrams):
    (U,B,T) = ngrams
    entropy = 0.0
    
    # Count total amount of words
    length = 0.0
    for count in U.values():
        length += count
    
    for key in U.keys():
        U[key] = Decimal(U[key]/length)
        entropy += (U[key]*Decimal(log(U[key], 2)))
        
    return -1*entropy

def computeBigramEntropy(ngrams):
    (U,B,T) = ngrams
    
    # Count total amount of words
    length = 0.0
    for count in U.values():
        length += count
    
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

def computeTrigramEntropy(ngrams):
    X = 0;
    Y = 1;
    Z = 2;
    (U,B,T) = ngrams
    
    # Count total amount of words
    length = 0.0
    for count in U.values():
        length += count
    
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

def countSmoothNgrams(tw, smoothX, smoothY, inic,end=0):
    if end == 0:
        end = len(tw)
        
    WORD = 0 
    
    U={}
    B={}
    T={}
    
    U[(tw[inic][smoothX])]=1
    if ( tw[inic+1][smoothX] ) not in U:
        U[( tw[inic+1][smoothX] )]=1
    else:
        U[( tw[inic+1][smoothX] )]+=1
        
    B[(tw[inic][smoothX],tw[inic+1][WORD])]=1
    for i in range(inic+2,end):
        # Unigram
        if (tw[i][smoothX]) not in U:
            U[(tw[i][smoothX])]=1
        else:
            U[(tw[i][smoothX])]+=1
            
        # Bigram
        if (tw[i-1][smoothX],tw[i][smoothY]) not in B:
            B[(tw[i-1][smoothX],tw[i][smoothY])] = 1
        else:
            B[(tw[i-1][smoothX],tw[i][smoothY])] +=1
            
        # Trigram
        if (tw[i-2][smoothX],tw[i-1][smoothY],tw[i][WORD]) not in T:
            T[(tw[i-2][smoothX],tw[i-1][smoothY],tw[i][WORD])] = 1
        else:
            T[(tw[i-2][smoothX],tw[i-1][smoothY],tw[i][WORD])] +=1
    return (U,B,T)


taggedWords = getTaggedWordsFromFile("corpus/taggedBrown.txt")
allWordsCount = len(taggedWords)

# Full Corpus
entropy = computeTrigramEntropy( countSmoothNgrams(taggedWords,1,0,0,0) )
perplexity = pow(2, entropy)
print perplexity

# Half Corpus
entropy = computeTrigramEntropy( countSmoothNgrams(taggedWords,1,0,0,allWordsCount/2) )
perplexity = pow(2, entropy)
print perplexity

# Quarter Corpus
entropy = computeTrigramEntropy( countSmoothNgrams(taggedWords,1,0,0,allWordsCount/4) )
perplexity = pow(2, entropy)
print perplexity
