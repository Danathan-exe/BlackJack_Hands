Letterc = [  #creating arrays for the Letter options.
    'a', 'j', 'k', 'q'
]
#input the two cards
while True:
    card1 = input("what is your first card?  ")
    try:
        card1 = int(card1)
    except:
        card1 = card1.lower()

    if type(card1) == int:
        if card1 > 10:
            print("This number is too high. Please enter a new number.")
        else:
            break
    else:
        if card1 in Letterc:
            break
        else:
            print(
                "This is not a correct card letter. Please enter from letters: A, J, K, or Q"
            )

while True:
    card2 = input("what is your second card. ")
    try:
        card2 = int(card2)
    except:
        card2 = card2.lower()

    if type(card2) == int:
        if card2 > 10:
            print("This number is too high. Please enter a new number.")
        else:
            break
    else:
        if card2 in Letterc:
            break
        else:
            print(
                "This is not a correct card letter. Please enter from letters: A, J, K, or Q"
            )

print(bool(card1))

while True:
    try:
        card1 = int(card1)
        break

    except:
        card1 = card1.lower()
        break
#setting the card Value for A

while True:
    try:
        card2 = int(card2)
        break
    except:
        card2 = card2.lower()
        break
#setting the card Value for A

# while True:
# if type(card1) == int
if card1 in Letterc:
    # if the card is an ace, the player can select 11 or 1
    if card1 == 'a':
        ls = [1, 11]
        # loop until they select 11 or 1 to assure proper rules
        while True:
            card1val = int(
                input("Do you want your ace (card #1) to be an 11 or a 1?"))
            if card1val not in ls:
                print("This was not a 1 or an 11. Please try again.")
            else:
                break
    else:
        card1val = 10
else:
    card1val = card1

#setting the card Value for A
if card2 in Letterc:
    # if the card is an ace, the player can select 11 or 1
    if card2 == 'a':
        ls = [1, 11]
        # loop until they select 11 or 1 to assure proper rules
        while True:
            card2val = int(
                input("Do you want your ace (card #2) to be an 11 or a 1?"))
            if card2val not in ls:
                print("This was not a 1 or an 11. Please try again.")
            else:
                break
    else:
        card2val = 10
else:
    card2val = card2

score = card1val + card2val
print("Your score is: " + str(score))

#statements per total
#if score is less than 16 statement
if score <= 16:
  print("Hit!")
#statement for split (when both cards are 8)
if card1 == 8 and card2 == 8:
    print("Split!")
#statement for hit.
if (score == 17 and (card1 == 'a' or card2 == 'a')):
    print("Hit!")
#statement for stay.
if (score == 17 and (card1 != 'a' and card2 != 'a')) or score == 20 or score == 18 or score == 19:
    print("Stay")
#prints if score is equel to 21
if score == 21:
    print("Blackjack!")
