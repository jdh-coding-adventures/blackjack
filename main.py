import functions as F

# initialize deck
deck = F.Decks()
deck = deck.create_deck(1)

# initialize players
# players
players = ["player_1", "dealer"]

player_1 = F.Player(name="player_1", type="person")
dealer = F.Player(name="dealer", type="system")

player_obj = [player_1, dealer]

# # deal
for i in range(len(player_obj)):
    for obj in player_obj:
        obj.draw_card(deck=deck, hand=obj.hand)

for p in player_obj:
    if p.name == "dealer":
        print(f"{p.hand[0]}")
    else:
        score = p.add_score(p.hand)
        print(f"{p.hand} Total: {str(score)}")

for player in player_obj:
    while player.state:
        print(f"{player.name}'s turn...")
        player.add_score(player.hand)

        if player.score >= 21:
            player.state = False
            break

        if player.name != "dealer":
            request = int(input("Press 1 to HIT, and 2 to STAY."))
        elif player.score < 17 and player.name == "dealer":
            request = 1
        else:
            request = 2

        if request == 1:
            player.draw_card(deck, player.hand)
            player.add_score(player.hand)
            print(player.hand, f" Total: {str(player.score)}")
        elif request == 2:
            player.state = False
            break

print(f"Dealer's hand - {dealer.hand} - Total: {dealer.score}")
print(f"Player's hand - {player_1.hand} - Total: {player_1.score}")

if 21 <= dealer.score > player_1.score:
    print(f"Dealer Wins!! {str(dealer.score)}")
elif 21 <= player_1.score > dealer.score:
    print(f"Player Wins!! {str(player_1.score)}")
elif player_1.score > 21 > dealer.score:
    print(f"Player BUST, Dealer Wins!! {str(dealer.score)}")
elif dealer.score > 21 > player_1.score:
    print(f"Dealer BUST, Player wins!! {str(player_1.score)}")
else:
    print("What are you missing???")
