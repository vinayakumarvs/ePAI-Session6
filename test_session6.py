import importlib
import inspect
import os
import re

import pytest

import session6

MANUAL_CARDS = [('2', 'spades'),
                        ('3', 'spades'),
                        ('4', 'spades'),
                        ('5', 'spades'),
                        ('6', 'spades'),
                        ('7', 'spades'),
                        ('8', 'spades'),
                        ('9', 'spades'),
                        ('10', 'spades'),
                        ('jack', 'spades'),
                        ('queen', 'spades'),
                        ('king', 'spades'),
                        ('ace', 'spades'),
                        ('2', 'clubs'),
                        ('3', 'clubs'),
                        ('4', 'clubs'),
                        ('5', 'clubs'),
                        ('6', 'clubs'),
                        ('7', 'clubs'),
                        ('8', 'clubs'),
                        ('9', 'clubs'),
                        ('10', 'clubs'),
                        ('jack', 'clubs'),
                        ('queen', 'clubs'),
                        ('king', 'clubs'),
                        ('ace', 'clubs'),
                        ('2', 'hearts'),
                        ('3', 'hearts'),
                        ('4', 'hearts'),
                        ('5', 'hearts'),
                        ('6', 'hearts'),
                        ('7', 'hearts'),
                        ('8', 'hearts'),
                        ('9', 'hearts'),
                        ('10', 'hearts'),
                        ('jack', 'hearts'),
                        ('queen', 'hearts'),
                        ('king', 'hearts'),
                        ('ace', 'hearts'),
                        ('2', 'diamonds'),
                        ('3', 'diamonds'),
                        ('4', 'diamonds'),
                        ('5', 'diamonds'),
                        ('6', 'diamonds'),
                        ('7', 'diamonds'),
                        ('8', 'diamonds'),
                        ('9', 'diamonds'),
                        ('10', 'diamonds'),
                        ('jack', 'diamonds'),
                        ('queen', 'diamonds'),
                        ('king', 'diamonds'),
                        ('ace', 'diamonds')]

README_CONTENT_CHECK_FOR = [
    'standard_deck',
    'score',
    'get_values',
    'get_suits',
    'poker_winner',
    'get_values',
    'royal_flush',
    'straight_flush',
    'four_of_a_kind',
    'full_house',
    'flush',
    'straight',
    'three_of_a_kind',
    'two_pairs',
    'one_pair'
]

LAMBDA_CONTENT_CHECK_FOR = [
        'lambda',
    'zip',
    'map'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session6)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_function_are_defined():
    content = inspect.getsource(session6)
    AllFUNCTIONSDEFINED = True
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            AllFUNCTIONSDEFINED = False
            pass
    assert AllFUNCTIONSDEFINED == True, "You have not defined all the required functions"

def test_keyword():
    LAMBDALOOKSGOOD = True
    f = open("Session6.py", "r")
    content = f.read()
    f.close()
    for c in LAMBDA_CONTENT_CHECK_FOR:
        if c not in content:
            LAMBDALOOKSGOOD = False
            pass
    assert LAMBDALOOKSGOOD == True, "You have not used 'zip', 'lambda', 'map' "


def test_annotations():
    """
    Test case to check the function typing are implemented in the function
    definition.
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert function[1].__annotations__, "Annotations not used!"

def test_doc_strings():
    """
    Test case to check the docstrings are included in the function definition.
    """
    # functions = inspect.getmembers(session6, inspect.isfunction)
    # for function in functions:
    assert session6.standard_deck(session6.vals, session6.suits).__doc__, "Docstring not used!"

def test_deck_using_normal():
    """
    Test case to check the creation of cards by normal method using loops
    `deck_using_normal_way`. Validates using the manually created cards list.
    """
    assert sorted(session6.standard_deck(session6.vals, session6.suits)) == sorted(MANUAL_CARDS), 'Manual list is matching with the manual loop'


def test_deck_using_expressions():
    """
    Test case to check the creation of cards by normal method using loops
    `deck_using_normal_way`. Validates using the manually created cards list.
    """
    assert sorted(session6.lambda_func()) == sorted(MANUAL_CARDS)

def test_onedeck_only():
    """Test to having only 52 cards
    """
    assert len(session6.standard_deck(session6.vals, session6.suits)) == 52, 'Having wrong number of cards in one deck!'


royal_flush_lists = [['diamonds-10', 'diamonds-jack', 'diamonds-queen', 'diamonds-king', 'diamonds-ace'],
                         ['clubs-10', 'clubs-jack', 'clubs-queen', 'clubs-king', 'clubs-ace'],
                         ['spades-10', 'spades-jack', 'spades-queen', 'spades-king', 'spades-ace'],
                         ['hearts-10', 'hearts-jack', 'hearts-queen', 'hearts-king', 'hearts-ace']]

straight_flush_lists = [['clubs-10','clubs-9','clubs-8','clubs-7','clubs-6'],
                      ['clubs-5','clubs-4','clubs-3','clubs-2','clubs-ace'],
                      ['diamonds-10','diamonds-9','diamonds-8','diamonds-7','diamonds-6'],
                      ['diamonds-5','diamonds-4','diamonds-3','diamonds-2','diamonds-ace'],
                      ['spades-10','spades-9','spades-8','spades-7','spades-6'],
                      ['spades-5','spades-4','spades-3','spades-2','spades-ace'],
                      ['hearts-10','hearts-9','hearts-8','hearts-7','hearts-6'],
                      ['hearts-5','hearts-4','hearts-3','hearts-2','hearts-ace']]

four_of_a_kind_lists = [['diamonds-8','clubs-8','spades-8','hearts-8','clubs-5'],
                            ['diamonds-2','clubs-2','spades-2','hearts-2','clubs-6'],
                            ['diamonds-ace','clubs-ace','spades-ace','hearts-ace','clubs-6'],
                            ['diamonds-4','clubs-4','spades-4','hearts-4','clubs-7']]


full_house_lists = [['diamonds-10','clubs-10','spades-10','hearts-6','clubs-6'],
                        ['diamonds-2','clubs-2','spades-2','hearts-3','clubs-3'],
                        ['diamonds-4','clubs-4','spades-4','hearts-5','clubs-5'],
                        ['diamonds-6','clubs-6','spades-6','hearts-7','clubs-7'],
                        ['diamonds-8','clubs-8','spades-8','hearts-9','clubs-9'],
                        ['diamonds-jack','clubs-jack','spades-jack','hearts-king','clubs-king']]


flush_lists = [['clubs-king','clubs-9','clubs-queen','clubs-ace','clubs-6'],
                   ['clubs-5','clubs-10','clubs-jack','clubs-2','clubs-4'],
                   ['diamonds-2','diamonds-9','diamonds-king','diamonds-5','diamonds-6'],
                   ['diamonds-5','diamonds-ace','diamonds-10','diamonds-2','diamonds-8'],
                   ['spades-3','spades-9','spades-4','spades-7','spades-jack'],
                   ['spades-5','spades-10','spades-9','spades-2','spades-ace'],
                   ['hearts-10','hearts-king','hearts-8','hearts-queen','hearts-6'],
                   ['hearts-5','hearts-ace','hearts-jack','hearts-2','hearts-10']]


straight_lists = [['hearts-8','spades-9','diamonds-10','clubs-jack','diamonds-queen'],
                     ['spaces-8','clubs-9','diamonds-10','hearts-jack','clubs-queen'],
                     ['spaces-3','clubs-4','diamonds-5','hearts-6','clubs-7'],
                     ['spaces-4','clubs-5','diamonds-6','hearts-7','clubs-8']]


three_of_a_kind_lists = [['diamonds-8','clubs-8','spades-8','diamonds-jack','clubs-5'],
                             ['diamonds-2','clubs-2','spades-2','diamonds-king','clubs-5'],
                             ['diamonds-3','clubs-3','spades-3','diamonds-jack','clubs-queen'],
                             ['diamonds-4','hearts-4','spades-4','diamonds-6','clubs-ace'],
                             ['diamonds-5','clubs-5','spades-5','diamonds-2','clubs-6'],
                             ['diamonds-6','hearts-6','spades-6','diamonds-3','clubs-7'],
                             ['diamonds-7','clubs-7','spades-7','diamonds-4','clubs-8']]


two_pair_lists = [['spades-queen','diamonds-queen','clubs-3','spades-3','spades-6'],
                      ['spades-ace','diamonds-ace','clubs-6','spades-6','hearts-8'],
                      ['spades-9','diamonds-9','hearts-3','diamonds-3','clubs-king'],
                      ['spades-6','diamonds-6','clubs-jack','spades-jack','diamonds-2']]

pair_lists = [['spades-queen','diamonds-queen','clubs-3','spades-7','spades-6'],
                  ['spades-ace','diamonds-2','clubs-6','spades-6','hearts-8'],
                  ['spades-9','diamonds-9','hearts-5','diamonds-3','clubs-king'],
                  ['spades-6','diamonds-6','clubs-jack','spades-king','diamonds-2']]

def test_royalflush_vs_straight_flush():
    assert session6.poker_winner(royal_flush_lists[0],straight_flush_lists[0]) == "Player1 Won", "Please check poker decide function"

def test_royalflush_vs_fourofakind():
    assert session6.poker_winner(royal_flush_lists[1],four_of_a_kind_lists[1]) == "Player1 Won", "Please check poker decide function"

def test_royalflush_vs_straight():
    assert session6.poker_winner(royal_flush_lists[2],straight_lists[2]) == "Player1 Won", "Please check poker decide function"

def test_royalflush_vs_flush():
    assert session6.poker_winner(royal_flush_lists[3],flush_lists[1]) == "Player1 Won", "Please check poker decide function"

def test_straight_flush_vs_royalflush():
    assert session6.poker_winner(straight_flush_lists[0],royal_flush_lists[3]) == "Player2 Won", "Please check poker decide function"

def test_straight_flush_vs_twopair():
    assert session6.poker_winner(straight_flush_lists[1],two_pair_lists[3]) == "Player1 Won", "Please check poker decide function"

def test_straight_flush_vs_fourofakind():    
    assert session6.poker_winner(straight_flush_lists[3],four_of_a_kind_lists[2]) == "Player1 Won", "Please check poker decide function"

def test_straight_flush_vs_pair():
    assert session6.poker_winner(straight_flush_lists[5],pair_lists[2]) == "Player1 Won", "Please check poker decide function"

def test_four_of_a_kind_vs_royalflush():
    assert session6.poker_winner(four_of_a_kind_lists[0],royal_flush_lists[2]) == "Player2 Won", "Please check poker decide function"
    
def test_four_of_a_kind_vs_straightflush():    
    assert session6.poker_winner(four_of_a_kind_lists[1],straight_flush_lists[4]) == "Player2 Won", "Please check poker decide function"
    
def test_four_of_a_kind_vs_fullhouse():    
    assert session6.poker_winner(four_of_a_kind_lists[2],full_house_lists[3]) == "Player1 Won", "Please check poker decide function"
    
def test_four_of_a_kind_vs_flush():    
    assert session6.poker_winner(four_of_a_kind_lists[3],flush_lists[3]) == "Player1 Won", "Please check poker decide function"

def test_full_house_vs_fourofakind():
    assert session6.poker_winner(full_house_lists[0],four_of_a_kind_lists[0]) == "Player2 Won", "Please check poker decide function"
    
def test_full_house_vs_royalflush():    
    assert session6.poker_winner(full_house_lists[1],royal_flush_lists[2]) == "Player2 Won", "Please check poker decide function"
    
def test_full_house_vs_threeofakind():    
    assert session6.poker_winner(full_house_lists[2],three_of_a_kind_lists[3]) == "Player1 Won", "Please check poker decide function"
    
def test_full_house_vs_straight():    
    assert session6.poker_winner(full_house_lists[5],straight_lists[1]) == "Player1 Won", "Please check poker decide function"

