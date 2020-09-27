import itertools
import random

class cards_deck:

    # def deal_card (self):
    #     suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
    #     value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    #     suit = random.choice(suit_list)
    #     value = random.choice(value_list)
    #     card = suit + " " + value
    #     return card

    def shuffle (self, deck):
        random.shuffle(deck)

        for card in deck:
            print(card)

        return deck

    def deal_card(self, deck):
        card = random.choice(deck)
        print("\nYour card is")
        print(card)
        return card

    def remove_card(self, deck, card):
        # print(deck)
        # print(card)
        # print(isinstance(deck, (list)))
        deck.remove(card)
        deck_removed = deck
        # print(deck_removed)
        return deck_removed

'Create the deck'
suit_list = ["Hearts", "Diamonds", "Clubs", "Spades"]
value_list = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = list(itertools.product(suit_list, value_list))

d = cards_deck()

'Shuffle, deal card and remove it from deck until the end'
for i in range(1, 52, 1):
    deck1 = d.shuffle(deck)
    card1 = d.deal_card(deck1)
    deck2 = d.remove_card(deck1, card1)
    print("The new deck is now:")
    print(deck2)