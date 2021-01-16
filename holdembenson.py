# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:38:24 2020

@author: stuar
"""
import random

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
            hand = deal(deck), deal(deck)
        else:
            hand = deal(deck),deal(deck),deal(deck),deal(deck),deal(deck)
        all_hands.append(hand)
    return all_hands 

def deal_flop(deck):
    burn_card = deck.pop(random.randint(0, (len(deck)-1)))
    flop = deal(deck),deal(deck),deal(deck)
    return flop

def deal_turn(deck):
    burn_card = deck.pop(random.randint(0, (len(deck)-1)))
    turn = deal(deck)
    return turn

def deal_river(deck):
    burn_card = deck.pop(random.randint(0, (len(deck)-1)))
    river = deal(deck)
    return river

def pair_toak_foak(hand):
    '''
    Takes in a hand as argument. Returns strings pair, three of a kind, four
    of a kind, and high card.
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
        return 'Four of a kind'
    elif len(toak) > 0:
        if len(pair) > 0:
            fh = toak + pair
            return 'Full house'
        else:
            return 'Three of a kind'
    elif len(pair) > 2:
        return 'Two pair'
    elif len(pair) > 0:
        return 'Pair'
    else:
        return 'High card'
    
def flush(hand):
    '''
    Takes in a hand as argument. Returns string flush if there is a flush.
    '''
    flush = False
    suit = hand[0].get_suit()
    for card in hand:
        if card.get_suit() != suit:
            return flush
    return 'Flush'

def straight(hand):
    '''
    Takes in a hand as argument. Returns string straight if there is a straight.
    '''
    straight = False
    values = []
    for card in hand:
        values.append(card.get_value())
    values.sort()
    try:
        for i in range(5):
            if values[i] + 1 != (values[i +1]):
                return straight
    except IndexError:
        return 'Straight'
    
def score_hand(hand):
    if straight(hand) == 'Straight' and flush(hand) == 'Flush':
        return 'Straight flush'
    elif pair_toak_foak(hand) == 'Four of a Kind':
        return 'Four of a kind'
    elif pair_toak_foak(hand) == 'Full House':
        return 'Full house'
    elif flush(hand) == 'Flush':
        return 'Flush'
    elif straight(hand) == 'Straight':
        return 'Straight'
    else:
        return pair_toak_foak(hand)

def play_a_round(num_players):
    deck = gen_deck()
    all_hands = deal_hand(num_players, deck)
    player_hand = all_hands[0]
    flop = deal_flop(deck)
    turn = deal_turn(deck)
    river = deal_river(deck)
    total_hand = []
    total_hand.append(turn)
    total_hand.append(river)
    for card in player_hand:
        total_hand.append(card)
    for card in flop:
        total_hand.append(card)
    return(score_hand(total_hand))



def benson_poker(num_rounds):
    pairs = 0
    twopairs = 0
    trips = 0
    straights = 0
    flushes = 0
    fullhouses=0
    quads=0
    straightflushes=0
    high_card = 0
    for i in range(num_rounds):
        outcome = play_a_round(4)
        if outcome == 'Pair':
            pairs += 1
        elif outcome == 'Two pair':
            twopairs += 1
        elif outcome == 'Three of a kind':
            trips += 1
        elif outcome == 'Straight':
            straights += 1
        elif outcome == 'Flush':
            flushes += 1
        elif outcome == 'Full house':
            fullhouses += 1
        elif outcome== 'Four of a kind':
            quads += 1
        elif outcome == 'Straight flush':
            straightflushes += 1
        else:
            high_card += 1

    print("In " + str(num_rounds) + " hands, there were:\n -------------")
    
    print(str(high_card) + ' High Cards.')
    pairscent = (pairs * 100)/num_rounds
    print(str(pairscent) + ' %')
    
    print(str(pairs) + ' Pairs.')
    pairscent = (pairs * 100)/num_rounds
    print(str(pairscent) + ' %')
    
    print(str(twopairs)+ ' Two pairs.')
    pairscent = (twopairs * 100)/num_rounds
    print(str(pairscent) + ' %')
    
    print(str(trips)+ ' Three of a kind.')
    pairscent = (trips * 100)/num_rounds
    print(str(pairscent) + ' %')
    
    print(str(straights)+ ' Straights')
    pairscent = (straights * 100)/num_rounds
    print(str(pairscent) + ' %')
    
    print(str(flushes)+ ' Flushes')
    pairscent = (flushes * 100)/num_rounds
    print(str(pairscent) + ' %')
    
    print(str(fullhouses) + ' Full Houses')
    pairscent = (fullhouses * 100)/num_rounds
    print(str(pairscent) + ' %')
    
    print(str(quads) + ' Four of a kind')
    pairscent = (quads * 100)/num_rounds
    print(str(pairscent) + ' %')
    
    print(str(straightflushes) + ' Straight Flushes')
    pairscent = (straightflushes * 100)/num_rounds
    print(str(pairscent) + ' %')

    
    
    
benson_poker(1000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    