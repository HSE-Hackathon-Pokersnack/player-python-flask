from models.card import Card
from models.player import Player
from typing import List


class Table:
    communityCards: List[Card] = []
    players: List[Player] = []
    round: int
    smallBlind: int
    minimumBet: int
    minimumRaise: int
    pot: int
    activePlayer: int
    currentDealer: int

    def __init__(self, table: dict):
        # self.communityCards = table["communityCards"]
        for card in table["communityCards"]:
            self.communityCards.append(Card(card))
        for player in table["players"]:
            self.players.append(Player(player))
        self.round = table["round"]
        self.smallBlind = table["smallBlind"]
        self.minimumBet = table["minimumBet"]
        self.minimumRaise = table["minimumRaise"]
        self.pot = table["pot"]
        self.activePlayer = table["activePlayer"]
        self.currentDealer = table["currentDealer"]
