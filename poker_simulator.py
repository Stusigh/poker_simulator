# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:38:24 2020

@author: stuar

"""


import random

random.seed(2)

class Card(object):
    '''
    Creates the class card, which contains the suit (either Spade, Heart, 
    Club or Diamond) and a value (J,Q,K and A are represented as 11, 12, 13 
    and 14).
    '''
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def get_suit(self):
        return self.suit
    def get_value(self):
        return self.value
    def set_suit(self, suit):
        self.suit = suit
    def set_value(self, value):
        self.value = value
    def compare_value(self, other_card):
        if self.value == other_card.value:
            if self.suit != other_card.suit:
                return True
        else:
            return False
    def __str__(self):
        if self.value == 11:
            return "The Jack of " + str(self.suit) + 's'
        elif self.value == 12:
            return "The Queen of " + str(self.suit) + 's'
        elif self.value == 13:
            return "The King of " + str(self.suit) + 's'
        elif self.value == 14:
            return "The Ace of " + str(self.suit) + 's'
        else:
            return "The " + str(self.value) + " of " + str(self.suit) + 's'
        
def gen_deck():
    '''Generates a standard 52 deck without jokers. Returns an ordered list of 
    card objects'''
    suits = ["Diamond", "Heart", "Club", "Spade"] #13
    values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
    deck_of_cards = []
    for i in range(4):
        for n in range(13):
            deck_of_cards.append(Card(suits[i],values[n]))
    return(deck_of_cards)

def deal(deck):
    '''One parameter (card deck) and returns a single card chosen at random. 
    This modifies the deck passed in.
    '''
    card_dealt = deck.pop(random.randint(0, (len(deck)-1)))
    return(card_dealt)
   
def deal_hand(num_players, deck, holdem= True):
    ''' takes in two arguments, the number of players and a generated deck, 
    and returns a list of lists. Each sublist is a hand containing two cards
    (if holdem is true) or five cards (if holdem is false).
    '''
    all_hands = []
    for n in range(num_players):
        if holdem == True:
            hand = [deal(deck), deal(deck)]
        else:
            hand = [deal(deck),deal(deck),deal(deck),deal(deck),deal(deck)]
        all_hands.append(hand)
    return all_hands 

def score_hand(hand):
    '''
    takes a list of card objects as input, and returns a tuple of hand score 
    and the type of hand (pair, flush etc.) as an integer value. 
    
    Prime numbers?

    '''
    hand_score = 0
    for card in hand:
        if card.get_value() > hand_score:
            hand_score = card.get_value()
            high_card = card
    if hand_score <= 14:
        type_of_hand = 'High Card: ' + high_card.__str__()
    return hand_score, type_of_hand


def pair_toak_foak(hand):
    '''
    Takes in a hand as argument. If a pair, three of a kind or four of a kind
    is found, that is returned (the highest of the three). If none are found,
    returns the high card.
    '''  
    numbers = [[],[],[],[],[],[],[],[],[],[],[],[],[]]
    pair = []
    foak = []
    toak = []
    high_card_score = 2
    for card in hand:
        numbers[(card.get_value()-2)].append(card)
        if card.get_value() > high_card_score:
            high_card_score = card.get_value()
            high_card = card
    for number in numbers:
        if 1 < len(number) < 3:
            for card in number:
                pair.append(card)
        if 2 < len(number) < 4:
            for card in number:
                toak.append(card)
        if 3 < len(number) < 5:
            for card in number:
                foak.append(card)
    if len(foak) > 0:
        return foak
    elif len(toak) > 0:
        if len(pair) > 0:
            fh = toak + pair
            return fh
        else:
            return toak
    elif len(pair) > 0:
        return pair
    else:
        return [high_card]
    
def flush(hand):
    '''
    Takes in a hand as argument. Returns suit if there is a flush (five cards
    of the same suit) or False if there is no flush'''
    
    flush = False
    suit = hand[0].get_suit()
    for card in hand:
        if card.get_suit() != suit:
            return flush
    return suit




deck = gen_deck()
all_hands = deal_hand(4, deck, holdem=False)
for hand in all_hands:
    for card in hand:
        print(card)


'''
straight_flush_test = [Card('Diamond',2), Card('Diamond', 3), Card('Diamond', 4),
              Card('Diamond', 5), Card('Diamond', 6)]

four_test = [Card('Diamond',4), Card('Heart', 4), Card('Club', 4),
              Card('Spade', 4), Card('Diamond', 7)]

full_house_test = [Card('Diamond',4), Card('Heart', 4), Card('Club', 4),
              Card('Spade', 7), Card('Diamond', 7)]

flush_test = [Card('Diamond',2), Card('Diamond', 10), Card('Diamond', 12),
              Card('Diamond', 4), Card('Diamond', 7)]

straight_test = [Card('Heart',2), Card('Diamond', 3), Card('Spade', 4),
              Card('Diamond', 5), Card('Diamond', 6)]

three_test = [Card('Diamond',2), Card('Heart', 2), Card('Club', 2),
              Card('Spade', 4), Card('Diamond', 7)]

two_pair_test = [Card('Diamond',2), Card('Heart', 2), Card('Club', 8),
              Card('Spade', 8), Card('Diamond', 7)]

pair_test = [Card('Diamond',2), Card('Heart', 2), Card('Club', 8),
              Card('Spade', 4), Card('Diamond', 7)]

high_card_test = [Card('Diamond',2), Card('Heart', 11), Card('Club', 13),
              Card('Spade', 4), Card('Diamond', 7)]
'''

    





    