# Import libraries met Tarot kaarten, twee libraries om de betekenis van de kaarten te scheiden. Eén voor wanneer ze
# rechtop worden getrokken en één voor wanneer ze ondersteboven worden getrokken uit reverse, de LuckyOrUnlucky
# module om te bepalen of een kaart wel of niet geluk brengt en de random module zodat we deze kunnen gebruiken.
from reversed import Tarot_r
from upright import Tarot_u
from LuckyOrUnlucky import Luck_Unlucky
import random

# Om één deck te creëren voegen we de verschillende kaarten samen, we willen hier alleen de namen van de kaarten
# hebben zodat we later de betekenis op kunnen vragen. Daarom vragen we alleen de keys op, omdat dit later handig is
# converteren we ze gelijk naar lijsten.
deck_A = list(Tarot_u.keys())
deck_B = list(Tarot_r.keys())

# Om alle kaarten en hun betekenis in één stapel te hebben zodat we de index kunnen gebruiken maken we hier een
# apart tuple van
deck_meaning = {}
deck_meaning.update(Tarot_u)
deck_meaning.update(Tarot_r)

# In deze lijst komen alle kaarten gekoppeld aan een waarde van 1, 0 of -1 om te bepalen of ze wel of geen geluk brengen
Luck_or_not = Luck_Unlucky


# Om te voorkomen dat steeds de eerste kaart van de stapel pakken is er een uitgebreide functie gecreëerd die bepaald
# welke kaart van welke stapel wordt gepakt. Hieronder zien we het begin van dit proces door middel van een coinflip
# bepalen we of we van stapel A of B pakken
def reversed_upright():
    flipped_coin = random.randint(0, 1)
    if flipped_coin == 0:
        return "A"
    if flipped_coin == 1:
        return "B"


# Deze functie bepaald welke kaarten we trekken en voegt deze kaarten aan de stapel toe die hij ons daarna terug geeft
def draw_cards(cards_to_draw):
    card_total = 0
    card_pile = []
    while card_total < cards_to_draw:
        deck_type = reversed_upright()
        if card_total <= cards_to_draw:
            if deck_type == "A":
                card_pile.append(random.choice(deck_A))
            if deck_type == "B":
                card_pile.append(random.choice(deck_B))
        if card_total == cards_to_draw:
            break
        card_total += 1
    return card_pile


# Zodat we de betekenis van de kaarten kunnen opvragen hebben we ook een functie geschreven die je kunt aanroepen.
# Deze functie zoekt de betekenis bij de key die we hem geven vanuit de vorige functie(Deze is geschikt voor 3 kaarten).
def card_meaning3(card_list):
    reading1 = [card_list[0], ]
    reading2 = [card_list[1], ]
    reading3 = [card_list[2], ]
    reading1.append(deck_meaning.get(card_list[0]))
    reading2.append(deck_meaning.get(card_list[1]))
    reading3.append(deck_meaning.get(card_list[2]))
    return [reading1, reading2, reading3]


# Deze is geschikt voor 5 kaarten.
def card_meaning5(card_list):
    reading1 = [card_list[0], ]
    reading2 = [card_list[1], ]
    reading3 = [card_list[2], ]
    reading4 = [card_list[3], ]
    reading5 = [card_list[4], ]
    reading1.append(deck_meaning.get(card_list[0]))
    reading2.append(deck_meaning.get(card_list[1]))
    reading3.append(deck_meaning.get(card_list[2]))
    reading4.append(deck_meaning.get(card_list[3]))
    reading5.append(deck_meaning.get(card_list[4]))
    return [reading1, reading2, reading3, reading4, reading5]


# Deze functie is om te bepalen of de drie kaart lezing veel of weinig geluk geeft
def card_luck3(card_list):
    are_you_lucky = []
    luck_list = []
    are_you_lucky.append(Luck_or_not.get(card_list[0]))
    are_you_lucky.append(Luck_or_not.get(card_list[1]))
    are_you_lucky.append(Luck_or_not.get(card_list[2]))
    for i in are_you_lucky:
        luck_list += i
    luck_total = (sum(luck_list))
    if luck_total == 0:
        return "Your future is undecided"
    elif luck_total <= 1:
        return "It's your lucky day!"
    else:
        return "Better luck next time"


# Deze doet hetzelfde voor 5 kaarten
def card_luck5(card_list):
    are_you_lucky = []
    luck_list = []
    are_you_lucky.append(Luck_or_not.get(card_list[0]))
    are_you_lucky.append(Luck_or_not.get(card_list[1]))
    are_you_lucky.append(Luck_or_not.get(card_list[2]))
    are_you_lucky.append(Luck_or_not.get(card_list[3]))
    are_you_lucky.append(Luck_or_not.get(card_list[4]))
    for i in are_you_lucky:
        luck_list += i
    luck_total = (sum(luck_list))
    if luck_total == 0:
        return "Your future is undecided"
    elif luck_total <= 1:
        return "It's your lucky day!"
    else:
        return "Better luck next time"


# Door de hiervoor geschreven functies te combineren kunnen we een volledige lezing genereren
def full_reading3(cards_to_draw, name):
    cards_drawn = draw_cards(cards_to_draw)
    cards_read = card_meaning3(cards_drawn)
    luck = card_luck3(cards_drawn)
    reading =   "Welcome to your reading " + name + ",\n" \
                "The cards selected for you today are " + cards_drawn[0] + ", " + cards_drawn[1] + " and " + cards_drawn[2] + ".\n"\
                "I will tell you about the first card of you're reading " + str(cards_read[0][0]) + ", " + str(cards_read[0][1][0]) + "\n" \
                "The second card I've drawn for you means this: " + str(cards_read[1][0]) + ", " + str(cards_read[1][1][0]) + "\n" \
                "The last card predicts this for you: " + str(cards_read[2][0]) + ", " + str(cards_read[2][1][0]) + "\n" \
                "If you wonder about you future all I have to say is this " + luck + "."
    reading_neat = str(reading)
    reading_neater = reading_neat.rstrip()
    f = open("C:\\Users\\anouk\\OneDrive\\Documents\\Tarot lezingen\\reading.txt", "w")
    f.write(reading_neater)
    f.close()
    return reading_neater


# Dit is de volledige lezing voor 5 kaarten
def full_reading5(cards_to_draw, name):
    cards_drawn = draw_cards(cards_to_draw)
    cards_read = card_meaning5(cards_drawn)
    luck = card_luck5(cards_drawn)
    reading =   "Welcome to your reading " + name + ",\n" \
                "The cards selected for you today are " + cards_drawn[0] + ", " + cards_drawn[1] + " and " + cards_drawn[2] + ".\n"\
                "I will tell you about the first card of you're reading " + str(cards_read[0][0]) + ", " + str(cards_read[0][1][0]) + "\n" \
                "The second card I've drawn for you means this: " + str(cards_read[1][0]) + ", " + str(cards_read[1][1][0]) + "\n" \
                "The third card tells me: " + str(cards_read[2][0]) + ", " + str(cards_read[2][1][0]) + "\n" \
                "The fourth card is rather surprising it means: " + str(cards_read[3][0]) + ", " + str(cards_read[3][1][0]) + "\n" \
                "The last card predicts this for you: " + str(cards_read[4][0]) + ", " + str(cards_read[4][1][0]) + "\n" \
                "If you wonder about you future all I have to say is this " + luck + "."
    reading_neat = str(reading)
    reading_neater = reading_neat.rstrip()
    f = open("C:\\Users\\anouk\\OneDrive\\Documents\\Tarot lezingen\\reading.txt", "w")
    f.write(reading_neater)
    f.close()
    return reading_neater


#print(full_reading3(3, "Robin"))
#print(full_reading5(5, "Anouk"))


