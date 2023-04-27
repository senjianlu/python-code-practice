#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/rabbir/python-code-practice/《流程的 Python》/1-1.2/一摞 Python 风格的纸牌.py
# @DATE: 2023/04/25 周二
# @TIME: 15:18:23
#
# @DESCRIPTION: todo...


import collections


Card = collections.namedtuple("Card", ["rank", "suit"])
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck:
    """
    一摞纸牌
    """
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        # _cards 列表顺序不会变
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

def spades_high(card):
    """
    用于排序的函数
    """
    rank_value = FrenchDeck.ranks.index(card[0])
    # rank_value: 0-12
    # len(suit_values): 4
    # suit_values[card.suit]: 0-3
    return rank_value * len(suit_values) + suit_values[card.suit]


# 单体测试
if __name__ == "__main__":
    deck = FrenchDeck()
    for card in sorted(deck, key=spades_high):
        print(card, spades_high(card))
