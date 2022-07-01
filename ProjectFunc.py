from itertools import islice
from matplotlib import cm
from numpy import NaN
from sqlalchemy import Integer
from termcolor import colored
import pandas as pd

def lcs(X, Y):
	X, Y = X.lower(), Y.lower()
	m = len(X)
	n = len(Y)
	bX = [0]*len(X)
	bY = [0]*len(Y)
	L = [[None]*(n + 1) for i in range(m + 1)]

	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
				bX[i-1] = max(bX) + 1
				bY[j-1] = max(bY) + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	return L[m][n]

def selectionSort(df, size):
   
    for step in range(size):
        idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if df.iloc[i]['longest'] > df.iloc[idx]['longest']:
                idx = i
            elif (df.iloc[i]['longest'] == df.iloc[idx]['longest'] and 
                     df.iloc[i]['firstSameIndex'] < df.iloc[idx]['firstSameIndex']):
                idx = i
            elif (df.iloc[i]['longest'] == df.iloc[idx]['longest'] and 
                     df.iloc[i]['firstSameIndex'] == df.iloc[idx]['firstSameIndex'] and 
                     df.iloc[i]['len'] < df.iloc[idx]['len']):
                idx = i
         
        # put min at the correct position
        (df.iloc[step], df.iloc[idx]) = (df.iloc[idx], df.iloc[step])
    return df

def DictionaryLcs(UserInput, sentences):
    DictLcs = {}
    for sen in sentences:
        DictLcs[sen] = lcs(sen, UserInput)
    return dict(sorted(DictLcs.items(), key=lambda item: item[1], reverse=True))

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return dict(islice(iterable, n))

def DictionarySimilarSort(UserInput, sentences):
    dfSimilar = pd.DataFrame({'sen':[], 'longest':[], 'len':[], 'firstSameIndex':[]})
    for sen in sentences:
        dfSimilar.loc[len(dfSimilar.index)] = [sen, 
                        len(longestSubstringFinder(UserInput, sen)), 
                        len(sen), 
                        sen.lower().index(UserInput.lower()) if UserInput.lower() in sen.lower() else NaN]
    # dfSimilar = dfSimilar.sort_values(by='longest', ascending=False)
    # dfSimilar = dfSimilar.sort_values(by=['firstSameIndex', 'len'], ascending=True, na_position='last')
    dfSimilar = selectionSort(dfSimilar, 5)
    return dfSimilar.sen






























def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0
            match = ''
            while ((i+lcs_temp < len1) and (j+lcs_temp<len2) and string1[i+lcs_temp].lower() == string2[j+lcs_temp].lower()):
                match += string2[j+lcs_temp]
                lcs_temp += 1
            if len(match) > len(answer):
                answer = match
    return answer

def setColor(UserInput, sentences):
    ColorSens = []
    for sen in sentences:
        CommonSen = longestSubstringFinder(UserInput, sen)
        ColorSen = sen.split(CommonSen)
        ColorSen.insert(len(ColorSen) - 1, colored(CommonSen, 'red'))
        ColorSens.append(''.join(ColorSen))
    return ColorSens