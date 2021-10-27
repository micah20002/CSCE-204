from random import shuffle
import sys


def deal(deck, player, dealer):
    shuffle(deck)

    for _ in range(2):
        player.append(deck.pop())
        dealer.append(deck.pop())


def score(hand):
    non_aces = [c for c in hand if c != 'Aces']
    aces = [c for c in hand if c == 'Aces']

    total = 0

    for card in non_aces:
        if card in 'JackQueenKing':
            total += 10
        else:
            total += int(card)

    for card in aces:
        if total <= 10:
            total += 11
        else:
            total += 1

    return total


def display_info(player, dealer, stand):
    print("***** Your hand: ***** \n [{}] \n Your total: ({})\n".format(']['.join(player), score(player)))
    if stand:
        print("***** Computers Hand: ***** \n[{}] \n Total: ({})\n".format(']['.join(dealer), score(dealer)))
    else:
        print("***** Computers Hand: ***** \n Total: [{}] [?]\n".format(dealer[0]))


def results(player, dealer, hand, stand):
    if score(player) == 21 and hand:
        print("Blackjack! You won!")
        sys.exit()
    elif score(player) > 21:
        print("***** Game Over: *****\n You lose!")
        sys.exit()
    if stand:
        if score(dealer) > 21:
            print("***** Game Over: *****\n You won!")
        elif score(player) > score(dealer):
            print("***** Game Over: *****\n You won!")
        elif score(player) < score(dealer):
            print("***** Game Over: *****\n You Lose!")
        sys.exit()


def hit_stand(deck, player, dealer, hand, stand):
    print("***** Your Turn: ***** \nDo you want another card? (Y)es or (N)o")
    choice = input("> ")
    hand = False
    if choice == 'y':
        player.append(deck.pop())
    elif choice == 'n':
        stand = True
        while score(dealer) <= 16:
            dealer.append(deck.pop())
        display_info(player, dealer, stand)
        results(player, dealer, hand, stand)


if __name__ == '__main__':
    deck = ['Aces', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']*4
    player = []
    dealer = []
    standing = False
    first_hand = True
    deal(deck, player, dealer)
    while True:
        display_info(player, dealer, standing)
        results(player, dealer, first_hand, standing)
        hit_stand(deck, player, dealer, first_hand, standing)