from random import shuffle


class Card:
    def __init__(self, cardNumber):
        self.cardNumber = cardNumber
        
    def get_face_value(self):
        number = self.cardNumber % 13 
        if(number < 9):
            return str(number+2)
        return ["A","K","Q","J"][12-number]   
    
    def get_suite(self):
        return ["H","C","D","S"][int(self.cardNumber/13)]
    
    def __str__(self):
        return f"{self.get_face_value()}{self.get_suite()} ";

class CardDeck:
    def __init__(self, total_decks = 1):
        #add the numbers 0 to 52 to our cards once for every deck requested
        self._cards = [Card(i%52) for i in range(0,52*total_decks)]
        
    def shuffle(self):
        shuffle(self._cards)
                
    def cut(self):
        #Choose an index in the center of the deck to cut.
        #This could be made random, or just left as taking the middle index
        cut_index = len(self._cards) // 2
        first_half = self._cards[:cut_index]
        second_half = self._cards[cut_index:]
        self._cards = second_half + first_half
        
    def add_another_deck(self, other_deck):
        #You don't know how many cards are in other_deck
        #So loop until you run out of new cards
        while True:
            new_card = other_deck.draw_card()
            
            #When draw_card returns None, the deck must be empty, so we're done
            if new_card == None:
                break
            self.place_card_on_top(new_card)        
        
    def draw_card(self):
        #Don't let the user draw a card from an empty deck
        if len(self._cards) == 0:
            return None
        
        return self._cards.pop(0)
    
    def peek_at_first_card(self):
        #Don't let the user peek a card that doesn't exist
        if len(self._cards) == 0:
            return None
        
        return self._cards[0]
    
    def place_card_on_top(self, card):
        self._cards.insert(0, card)
        
    def display_all_cards(self):
        for card in self._cards:
            print(str(card), end = "\t")

print("Two 52 card decks combined into a mega deck:")
deck = CardDeck(2)
deck.display_all_cards()

print("\n\nA deck where 46 cards have been draw. Leaving just 6:")
deck = CardDeck(1)
for i in range(46):
    deck.draw_card()    
deck.display_all_cards()

print("\n\nCutting the 6-card deck down the centre:")
deck.cut()
deck.display_all_cards()