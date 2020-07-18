from spellchecker import SpellChecker
from wordsegment import load, segment


def spell_correct(word):
    spell = SpellChecker()
    load()
    correct_spelling = ''
    words = word.split(' ')
    for wd in words:
        correct_spelling = correct_spelling + spell.correction(wd) + ' '
    correct_spelling = ' '.join(segment(correct_spelling))

    return correct_spelling
