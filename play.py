#! /usr/bin/env python

import random 

class player:
  hand = {}
  tableau = {}

class state:
  deck = [] 
  discard = []
  players = []

def _popcard(state, cardid):
  for player in state.players:
    if cardid in player.hand:
      return player.hand.pop(cardid)
    if cardid in player.tableau:
      return player.tableau.pop(cardid)

def totableau(state, playernum, cardid):
  state.players[playernum].tableau[cardid] = _popcard(state,cardid)

def draw(state, playernum, numcards):
  if numcards > len(state.deck):
    state.discard = state.discard + state.deck
    state.deck = state.discard
    random.shuffle(state.deck)
    state.discard = []
  cards = {}
  for num in range(0,numcards):
    card = state.deck.pop(0)
    state.players[playernum].hand[card['id']] = card

def todiscard(state, cardid):
  state.discard.append(_popcard(state, cardid))

def setupGame(cards, numplayers):
  game = state()
  for i in range(numplayers):
    game.players.append(player())

  random.shuffle(cards)
  for idx, card in enumerate(cards):
    card['id'] = idx
    game.deck.append(card)
  return game

if __name__ == '__main__':
  setupGame()
