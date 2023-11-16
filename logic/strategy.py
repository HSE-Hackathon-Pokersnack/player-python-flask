from models.bet import Bet
from models.table import Table


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)
    multiplier = 1
    matches = 0
    player = Table.players[Table["activePlayer"]]
    card1 = player["cards"][0]
    card2 = player["cards"][1]
    commmunityCards = Table["communityCards"]

    if card1["rank"] == card2["rank"]:
        matches += 1

    for card in commmunityCards:
        if card["rank"] == card1["rank"] or card["rank"] == card2["rank"]:
            matches += 1

    match matches:
        case 1:
            multiplier = 2
        case 2:
            multiplier = 5
        case 3:
            multiplier = 50

    return Bet(multiplier * Table["minimumBet"])
