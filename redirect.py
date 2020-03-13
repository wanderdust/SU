#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:44:39 2020

@author: Mariam

Incomplete Utterance
"""
from utils.su import request_su

# According to the Split utterance research paper these are the most commun split points in a dialogue:
antecedents = ['and','but','or','so','is','are','because','the','a','my','your'] 

def check(word, list):
    if word in list:
        print("Your sentence is incomplete!")
        #redirect to our utterence completion bot
    else:
        print("Your sentence is complete!")
        #redirect to Alana
        

Utterance = input("Enter your sentence : ") 

utt_list = Utterance.split()
res = len(utt_list) 
last_word = utt_list[-1]


# printing result 
print ("The number of words in the utterance is : " +  str(res))
print ("The the last word is : " +  str(last_word))

check(last_word, antecedents)


#print (Utterance) 
