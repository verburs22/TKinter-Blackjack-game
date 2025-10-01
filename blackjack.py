#sarah verburg 06-10

import random
import tkinter


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face = ['jack', 'queen', 'king']

    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    for suit in suits:
        #number cards per suit
        for card in range(1,11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        #face cards per suit
        for card in face:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    #pop next card oof top of deck
    next_card = deck.pop(0)
    #add card to end of deck
    deck.append(next_card)
    #add image to label and display
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    #return card face value
    return next_card


def score_hand(hand):
    # calc total score of all cards in list
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -=10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins")
    else:
        result_text.set("Draw")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins")


def initial_deal():
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0 , column=1, sticky='ew', rowspan=2)

    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2 , column=1, sticky='ew', rowspan=2)

    result_text.set("")

    dealer_hand = []
    player_hand = []

    initial_deal()


def shuffle():
    random.shuffle(deck)


def play():
    initial_deal()
    mainWindow.mainloop()



#main code

mainWindow = tkinter.Tk()

mainWindow.title("Black Jack")
mainWindow.geometry('640x480-400-250')
mainWindow.config(background='green')

main_padding = 100
mainWindow['padx'] = main_padding
mainWindow['pady'] = 50

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

#dealer
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg ="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg ="white").grid(row=1, column=0)

dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

#player
player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Player", background="green", fg ="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg ="white").grid(row=3, column=0)

player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w' )

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

cancel_button = tkinter.Button(button_frame, text="New Game", command=new_game)
cancel_button.grid(row=0, column=2)

shuffle_button = tkinter.Button(button_frame, text="Shuffle deck", command=shuffle)
shuffle_button.grid(row=0, column=3)

#load cards
cards = []
load_images(cards)
#create deck and store dealer and player hand
deck = list(cards) + list(cards) + list(cards)
shuffle()

dealer_hand = []
player_hand = []

if __name__ == '__main__':
    play()

