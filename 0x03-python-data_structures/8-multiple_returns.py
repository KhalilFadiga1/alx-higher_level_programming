#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        senLength = len(sentence)
    else:
        senLength = 0
    return (senLength, sentence if not sentence else sentence[0])
