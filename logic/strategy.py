from models.bet import Bet
from models.table import Table
from models.card import Card
from typing import List


# raise multiplier if four cards of the same suit
def check_flush(card1: Card, card2: Card, comm_cards: List[Card]) -> bool:
    all_cards = [card1, card2]
    all_cards.extend(comm_cards)

    counter: int = 0
    if len(all_cards) == 5:
        for i in range(1, len(all_cards)):
            if all_cards[i - 1].suit == all_cards[i].suit:
                counter += 1
            if counter == 5:
                return True

    return False


def checkStraight(card1: Card, card2: Card, comm_Cards: List[Card]):
    cards = [card1, card2]
    cards.extend(comm_Cards)
    ranks = [card.rank.value for card in cards]

    # Sort the ranks
    ranks.sort(key=lambda x: cards.rank[x].value)

    # Check for consecutive ranks
    for i in range(len(ranks) - 1):
        if cards.rank[cards.rank[i]].value + 1 != cards.rank[ranks[i + 1]].value:
            return False

    return True


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
    player = table.players[table.activePlayer]
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
            multiplier = 1.5
            # Full House
            if matchesInCommunityCards == 2:
                multiplier = 4
        # three of a kind
        case 2:
            multiplier = 2
            # Full House
            if matchesInCommunityCards >= 2:
                multiplier = 4
        # four of a kind
        case 3:
            multiplier = 10
        case _:
            multiplier = 1

    # if checkStraight(card1, card2, cCards):
    #     multiplier = 5

    if check_flush(card1, card2, cCards):
        return player.stack

    if multiplier == 1:
        # print(int(0.5 * player.stack))
        return int(0.5 * player.stack)

    # print(multiplier, " ", table.minimumBet)
    return int(multiplier * table.minimumBet)


def strat_Willy(table: Table) -> int:
    cards = []
    for player in table.players:
        for pcard in player.cards:
            cards.append(pcard)
    card1: Card = cards[0]
    card2: Card = cards[1]

    matches = 0
    if card1.rank.value == card2.rank.value:
        matches += 1

    suits = 0
    if card1.suit.value == card2.suit.value:
        suits = 1

    if len(table.communityCards) >= 3:
        for card in table.communityCards:
            if (
                card.rank.value == card1.rank.value
                or card.rank.value == card2.rank.value
            ):
                matches += 1
            if (
                card.suit.value == card1.suit.value
                or card.suit.value == card2.suit.value
            ):
                suits += 1

    if suits == 5:
        return table.minimumBet

    if matches > 2:
        return table.minimumBet
    if matches == 1:
        if int(card1.rank.value) < 10 and int(card2.rank.value) < 10:
            return 20
        else:
            return table.minimumBet
    else:
        return 0
        # amount = table.minimumBet
        # if amount+player.bet <= table.smallBlind:
        #     return amount
        # else:
        #     return 0


def decide(table: Table) -> Bet:
    # call first strategy
    # strat1_bet = strat_1(table)
    # chips = strat_0(table)
    # chips = strat_Willy(table)
    player = table.players[table.activePlayer]
    if table.round < 8:
        amount = table.minimumBet
    else:
        amount = table.minimumRaise

    chip = strat_Willy(table)

    return Bet(chip)
