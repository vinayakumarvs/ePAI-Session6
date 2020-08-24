import itertools
import random
from collections import defaultdict

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

order_dict = {x:y+1 for x,y in zip(vals,range(len(vals)))}

def lambda_func(vals : 'list of values'= vals,suits :'List containing suits'= suits) -> list:
    '''Lambda function for listing down all the cards '''
    return list(map(lambda x : x ,zip(vals*len(suits), suits*len(vals))))
# deck_s = map(lambda x:x, zip(vals * len(suits), suits * len(vals)))


def standard_deck(vals: 'card values', suits: 'suites')-> list:
    """
    standard_deck function creates a deck of cards using for loops.

    Returns:
        list of cards in one deck
    """
    deck = []
    for suit in suits:
        for val in vals:
            deck.append((val, suit))
    return deck

def score(player: 'list of five cards') ->'score based on cards':
    """ Gets score based on the set of cards and poker rules
    Inputs: 
        player: List of cards for player
    Returns:
        int - score based poker rules
    """
    if royal_flush(player):
        return 100

    if straight_flush(player):
        return 99

    if four_of_a_kind(player):
        return 98

    if full_house(player):
        return 97

    if flush(player):
        return 96

    if straight(player):
        return 95

    if three_of_a_kind(player):
        return 94

    if two_pairs(player):
        return 93

    if one_pair(player):
        return 92

    return max(get_values(player))

def get_values(player: 'list of five cards') ->'list of values for the cards':
    """ Gets values of the five cards
    Inputs: 
        player: List of cards for player
    Returns:
        list - list of value or rank of the cards
    """
    return list(map(lambda x: order_dict[x.split("-")[1]],player))

def get_suits(player: 'list of five cards') ->'list of suits for the cards':
    """ Gets suits of the five cards
    Inputs: 
        player: List of cards for player
    Returns:
        list - list of suites of the cards
    """
    return list(map(lambda x: x.split("-")[0],player))

def flush(player: 'list of five cards') ->'bool, check for flush':
    """ Checks if Any five cards of the same suit, but not in a sequence.
    Inputs: 
        player: List of cards for player
    Returns:
        bool, check for flush
    """
    suits = get_suits(player)
    if len(set(suits))==1:
        return True
    else:
        return False

def straight(player: 'list of five cards') ->'bool, check for straight':
    """ Checks if Five cards in a sequence, but not of the same suit.
    Inputs: 
        player: List of cards for player
    Returns:
        bool, check for straight
    """
    values = get_values(player)
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    value_range = max(values) - min(values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return True
    else: 
        #check straight with low Ace
        if set(values) == set([13, 1, 2, 3, 4]):
            return True
        return False


def royal_flush(player: 'list of five cards') ->'bool, check for royal flush':
    """ Checks if cards contains A, K, Q, J, 10, all the same suit.
    Inputs: 
        player: List of cards for player
    Returns:
        bool - list of suites of the cards
    """
    values = get_values(player)
    if flush(player) and sum(values) == 55:
        return True
    else:
        return False

def straight_flush(player: 'list of five cards') ->'bool, check for straight flush':
    """ Checks if Five cards in a sequence, all in the same suit. Ace can either come before 2 
    or come after King.
    Inputs: 
        player: List of cards for player
    Returns:
        bool, check for straight flush
    """
    if flush(player) and straight(player):
        return True
    else:
        return False

def four_of_a_kind(player: 'list of five cards') ->'bool, check for four of a kind':
    """ Checks if All four cards of the same rank.
    Inputs: 
        player: List of cards for player
    Returns:
        bool, check for four of a kind
    """
    values = get_values(player)
    value_counts = defaultdict(lambda:0)
    for v in values: 
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return True
    return False

def full_house(player: 'list of five cards') ->'bool, check for full house':
    """ Checks if Three of a kind with a pair.
    Inputs: 
        player: List of cards for player
    Returns:
        bool, check for full house
    """
    values = get_values(player)
    value_counts = defaultdict(lambda:0)
    for v in values: 
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def three_of_a_kind(player: 'list of five cards') ->'bool, check for three of a kind':
    """ Checks if Three cards of the same rank.
    Inputs: 
        player: List of cards for player
    Returns:
        bool, check for three of a kind
    """
    values = get_values(player)
    value_counts = defaultdict(lambda:0)
    for v in values: 
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return True
    else:
        return False

def two_pairs(player: 'list of five cards') ->'bool, check for two pairs':
    """ Checks if Two different pairs.
    Inputs: 
        player: List of cards for player
    Returns:
        bool, check for Two different pairs.
    """
    values = get_values(player)
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return True
    else:
        return False

def one_pair(player: 'list of five cards') ->'bool, check for one pair':
    """ Checks if One pair.
    Inputs: 
        player: List of cards for player
    Returns:
        bool, check for One pair.
    """
    values = get_values(player)
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return True
    else:
        return False

def poker_winner(player_1: 'list of five cards',player_2: 'list of five cards') ->'a string':
    """ Decides who won the poker game based on the set of 5 cards from a deck
    Inputs: 
        player_1: List of cards for player 1
        player_2: List of cards for player 2
    Returns:
        String - who won Player 1 or Player 2
    """
    if type(player_1)!=list or type(player_2)!=list:
        raise TypeError("Give the cards in list")
    if len(player_1)!=5 or len(player_2)!=5 :
        raise ValueError("Only set of 5 cards are accepted")

    if score(player_1) > score(player_2):
        return "Player1 Won"
    elif score(player_1) == score(player_2):
        return "Draw"
    else:
        return "Player2 Won"