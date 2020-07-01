#!/usr/bin/env python

import json

DATA = "data.json" #pour l'instant le dictionnaire n'est qu'un fichier json. Plus tard l'appli pourra être branchée sur un api


def main():
    data = json.load(open(DATA))
    word = input("Type a word : \n")
    definitions = checkWord(word, data)
    for definition in definitions:
        print(definition)


def checkWord(word, data):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return ['No word "{}" in the dictionnary.'.format(word)]

if __name__ == "__main__":
    main()