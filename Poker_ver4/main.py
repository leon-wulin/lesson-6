# -*- coding: UTF-8 -*-
#writen by leon
#writen time: 2019/10/26
from machine.standerd_machine import creat_new_deck,shuffled_deck,record_deck

deck=[]
creat_new_deck(deck)
print(deck)

record_deck(deck,'deck1.txt')

shuffled_deck(deck)
record_deck(deck,'deck2.txt')
