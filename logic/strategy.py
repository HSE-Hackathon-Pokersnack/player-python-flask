from models.bet import Bet
from models.table import Table


def Givebet():
    player = Table.players[3]
    multiplier = 1
    matches = 0
    matchesInCommunityCards = 0
    card1 = player["cards"][0]
    card2 = player["cards"][1]
    commmunityCards = Table["communityCards"]
    commmunityCard1 = commmunityCards[0]
    commmunityCard2 = commmunityCards[1]
    commmunityCard3 = commmunityCards[2]

    if commmunityCard1 == commmunityCard2:
        matchesInCommunityCards += 1
    if commmunityCard2 == commmunityCard3:
        matchesInCommunityCards += 1
    if commmunityCard1 == commmunityCard3:
        matchesInCommunityCards += 1

    if card1["rank"] == card2["rank"]:
        matches += 1

    for card in commmunityCards:
        if card["rank"] == card1["rank"] or card["rank"] == card2["rank"]:
            matches += 1

    match matches:
        # pair
        case 1:
            multiplier = 2
            # Full House
            if matchesInCommunityCards == 2:
                multiplier = 10
        # three of a kind
        case 2:
            multiplier = 5
            # Full House
            if matchesInCommunityCards >= 1:
                multiplier = 10
        # four of a kind
        case 3:
            multiplier = 50
        case _:
            multiplier = 1
    return 1


def decide(table: Table) -> Bet:
    return Bet(70)
