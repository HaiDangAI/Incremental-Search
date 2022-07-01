from ReadSentences import sentences
from ProjectFunc import *
from Present import *

def wait(): input()

def getSimilarSens(typed):
    five_sens = take(5, DictionaryLcs(typed, sentences).items())
    SimilarSens = DictionarySimilarSort(typed, list(five_sens))
    return SimilarSens

if __name__ == '__main__':
    while True:
        UserInput = input('\nEnter string: ')
        if not UserInput: break
        five_sens = take(5, DictionaryLcs(UserInput, sentences).items())
        SimilarSens = DictionarySimilarSort(UserInput, list(five_sens))
        print('Suggestion:')
        for sen in setColor(UserInput, SimilarSens):
            print('\t'+sen)