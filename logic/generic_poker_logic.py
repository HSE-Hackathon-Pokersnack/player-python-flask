from datacontracts import Card, PokerHandEnum
from models import card


def RateHandOnly(cardsOnHand) -> str:
    card_first = card(cardsOnHand[0])
    card_second = card(cardsOnHand[1])

    if card_first.rank > card_second.rank:
        card_temp = card_first
        card_first = card_second
        card_second = card_temp

    return card_first.rank + " " + card_second.rank


def GenerateResponse() -> str:
    return ""


cards = [{"rank": "2", "suit": "HEARTS"}, {"rank": "9", "suit": "CLUBS"}]

print(RateHandOnly(cards))
