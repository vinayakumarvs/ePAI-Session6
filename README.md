# Session 6 - First Class Functions Part - I
# EPAi Session6 assignment

#### Objective of Assignment:

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']

We should be able to achieve:

1. Write a single expression that includes lambda, zip and map functions to select create 52 cards in a deck

2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck

3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker.


4. Docstrings must, and it must mention what the function is doing

5. Write annotations for the function

6. Basics tests to ensure your code if correct (20+ combination tests (counted as 1 test) in 3, check 1/2 with a manual list of 52 cards. Overall 20 tests at minimum)

Note:
    - The code will be able to assess only a 5 card game for two players

#### Details of the functions derived and tested:

1. standard_deck:
    * The function does generate 52 cards to make one deck by using the normal expressions than the one liner using the lambda, map and zip

2. poker_winner:
    * (player_1: 'list of five cards',player_2: 'list of five cards') ->'a string':
    * Decides who won the poker game based on the set of 5 cards from a deck Inputs:
    * player_1: List of cards for player 1
    * player_2: List of cards for player 2
    * Returns: String - who won Player 1 or Player 2

3. score:
    * (player_set: 'list of five cards') ->'score based on cards':
    * Gets score based on the set of cards and poker rules
    * Inputs: player_set: List of cards for player
    * Returns: int - score based poker rules

4. get_values:
    * (player_set: 'list of five cards') ->'list of values for the cards':
    * Gets values of the five cards
    * Inputs: player_set: List of cards for player
    * Returns: list - list of value or rank of the cards

5. get_suits:
    * (player_set: 'list of five cards') ->'list of suits for the cards':
    * Gets suits of the five cards
    * Inputs: player_set: List of cards for player
    * Returns: list - list of suites of the cards

6. royal_flush:
    * (player_set: 'list of five cards') ->'bool, check for royal flush':
    * Checks if cards contains A, K, Q, J, 10, all the same suit.
    * Inputs: player_set: List of cards for player
    * Returns: bool - list of suites of the cards

7. straight_flush:
    * (player_set: 'list of five cards') ->'bool, check for straight flush':
    * Checks if Five cards in a sequence, all in the same suit. Ace can either come before 2 or come after King.
    * Inputs: player_set: List of cards for player
    * Returns: bool, check for straight flush

8. four_of_a_kind:
    * (player_set: 'list of five cards') ->'bool, check for four of a kind':
    * Checks if All four cards of the same rank.
    * Inputs: player_set: List of cards for player
    * Returns: bool, check for four of a kind

9. full_house:
    * (player_set: 'list of five cards') ->'bool, check for full house':
    * Checks if Three of a kind with a pair.
    * Inputs: player_set: List of cards for player
    * Returns: bool, check for full house

10. flush:
    * (player_set: 'list of five cards') ->'bool, check for flush':
    * Checks if Any five cards of the same suit, but not in a sequence.
    * Inputs: player_set: List of cards for player
    * Returns: bool, check for flush

11. straight:
    * (player_set: 'list of five cards') ->'bool, check for straight':
    * Checks if Five cards in a sequence, but not of the same suit.
    * Inputs: player_set: List of cards for player
    * Returns: bool, check for straight

12. three_of_a_kind:
    * (player_set: 'list of five cards') ->'bool, check for three of a kind':
    * Checks if Three cards of the same rank.
    * Inputs: player_set: List of cards for player
    * Returns: bool, check for three of a kind

13. two_pairs:
    * (player_set: 'list of five cards') ->'bool, check for two pairs':
    * Checks if Two different pairs.
    * Inputs: player_set: List of cards for player
    * Returns: bool, check for Two different pairs.

14. one_pair:
    * (player_set: 'list of five cards') ->'bool, check for one pair':
    Checks if One pair.
    * Inputs: player_set: List of cards for player
    * Returns: bool, check for One pair.
    

Various test cases have been established to check the functions are working properly.