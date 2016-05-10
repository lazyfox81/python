#!/usr/bin/python
import os

def get_vocabulary(dat_f):
    words={}
    with open(dat_f, "r", encoding='utf-8') as in_f:
        for line in in_f:
            word, words[word] = line.strip().split(':')
    return words

def thumb_dictionary(dic):
    for word in dic:
        start = input()
        if start == 'q':
            break
        else:
            print (word, end=" ")
            input()
            print (dic[word], end=" ")
    print()
        
if __name__ == '__main__':
    data_file = os.environ['HOME'] + "/python/vocabulary_data.txt"
    words = get_vocabulary(data_file)
    thumb_dictionary(words)
