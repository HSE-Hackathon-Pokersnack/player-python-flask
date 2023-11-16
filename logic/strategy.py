from models.bet import Bet
from models.table import Table
from models.card import Card
from typing import List


def check_flush(card1, card2, comm_cards) -> bool:
    all_cards = [card1, card2]
    all_cards.append(comm_cards)
    counter: int = 0

    for i in range(1, len(all_cards)):
        if all_cards[i - 1].suit == all_cards[i].suit:
            counter += 1
        if counter == 5:
            return True

    return False


# Philip: "Reimt sich ja: 'Ist schon Witzig mit 70 :D !!!'"
def strat_0(table: Table) -> int:
    bet = 0
    if table.minimumBet <= 70:
        bet = 70
    else:
        bet = table.minimumBet

    if table.minimumBet > 200:
        bet = 0
    return bet


def strat_1(table: Table) -> int:
    player = table.players[2]
    multiplier = 1
    matches = 0
    matchesInCommunityCards = 0
    card1 = player.cards[0]
    card2 = player.cards[1]
    cCards = table.communityCards

    for i in range(len(cCards)):
        for i2 in range(len(cCards)):
            if cCards[i].rank == cCards[i2].rank:
                matchesInCommunityCards += 1

    if card1.rank == card2.rank:
        matches += 1

    for card in cCards:
        if card.rank == card1.rank or card.rank == card2.rank:
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

    if check_flush(card1, card2, cCards):
        multiplier = 50

    return multiplier * table.minimumBet


def checkStraight(card1: Card, card2: Card, comm_Cards: List[Card]):
    result = 0
    return result


def decide(table: Table) -> Bet:
    # call first strategy
    # strat1_bet = strat_1(table)
    chips = strat_0(table)
    return Bet(chips)
