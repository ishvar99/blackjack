import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing=True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck=[],self.player=[],self.dealer=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    # def __str__(self):
    #     str=""
    #     for card in self.deck:
    #         str += f"{card}, "
    #     return str

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        player = random.sample(self.deck, 2)
        dealer = random.sample(self.deck, 2)


class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0


    def add_card(self,card):
        self.cards.append(card)
        if(card.rank=='Ace'):
            self.aces+=1
        self.value+=values[card.rank]

    def adjust_for_ace(self):
        if(self.value>21):
            self.value=self.value-10


class Chips:

    def __init__(self):
        self.total=100
        self.bet=0

    def win_bet(self):
        self.total+=self.bet*2

    def lose_bet(self):
        self.total-=self.bet


def take_bet():
    while True:
        try:
            bet=int(input('Place a bet!'))
            if (bet > Chips().total):
                raise ValueError('Dont have enough funds!')
        except:
            print('Invalid Input!')
            continue


def hit(deck,hand):
    pick=random.choice(deck)
    hand.add_card(pick)
    if hand.aces >=1:
        hand.adjust_for_ace()


def hit_or_stand(deck,hand):
    global playing
    res=input('Do you want to hit or stand (h/s)')
    if(res=='h'):
        hit(deck,hand)
    else:
        playing=False


def show_some(player,dealer):
    print("DEALER'S HAND")
    print(dealer[0])
    print('ONE CARD HIDDEN!')
    print('\n')
    print("PLAYER'S HAND")
    for x in player:
        print(x)

def show_all(player,dealer):
    print("PLAYER'S HAND")
    for x in player:
        print(x)
    print('\n')
    for x in dealer:
        print(dealer)

def player_busts():
    print('DEALER WINS! PLAYER BUSTED')

def player_wins():
    print('PLAYER WINS! DEALER BUSTED')

def dealer_wins():
    print('DEALER WINS!')


def dealer_busts():
    print('DEALER BUSTS!PLAYER WINS!')


while True:
    print("WELCOME TO BLACKJACK!")
    d=Deck()
    h=Hand()
    d.shuffle()
    d.deal()
    c=Chips()
    take_bet()
    show_some(d.player,d.dealer)
    while playing:
        hit_or_stand(d,h)
        show_some()




