from tinydb import TinyDB

db = TinyDB("cards.json")

NUM_PLAYERS = 30

db.purge()
db.insert({
    'rock': NUM_PLAYERS * 4,
    'paper': NUM_PLAYERS * 4,
    'scissors': NUM_PLAYERS * 4,
})