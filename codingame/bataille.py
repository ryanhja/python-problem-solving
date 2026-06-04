from collections import deque

cardp1 = deque()
cardp2 = deque()

# Player 1
cardp1.append('AH')
cardp1.append('10D')
cardp1.append('6C')
cardp1.append('JS')
cardp1.append('4H')
cardp1.append('9D')
cardp1.append('QS')
cardp1.append('7C')
cardp1.append('AC')
cardp1.append('3D')
cardp1.append('2S')

# Player 2
cardp2.append('KS')
cardp2.append('10C')
cardp2.append('8H')
cardp2.append('4S')
cardp2.append('AD')
cardp2.append('JD')
cardp2.append('6H')
cardp2.append('9D')
cardp2.append('QS')
cardp2.append('7C')
cardp2.append('AS')

print("Player 1 card : ", cardp1)
print("Player 2 card : ", cardp2)


def evaluate(character):
    match character:
        case 'J':
            return 11
        case 'Q':
            return 12
        case 'K':
            return 13
        case 'A':
            return 14
    return int(character)


pat = False
manche = 0
mise_c1 = []
mise_c2 = []

while cardp1 and cardp2:
    manche += 1
    c1 = cardp1.popleft()
    c2 = cardp2.popleft()

    print(f"\nPlayer1 {c1} - {c2} Player2")

    if evaluate(c1.rstrip("DHCS")) > evaluate(c2.rstrip("DHCS")):
        if mise_c1 and mise_c2:
            cardp1.extend(mise_c1)
            cardp1.append(c1)
            cardp1.extend(mise_c2)
            cardp1.append(c2)

            # Empty mise
            mise_c1 = []
            mise_c2 = []
            print(f" => Round {manche} : Player1 win")
        else:
            cardp1.append(c1)
            cardp1.append(c2)
            print(f" => Round {manche} : Player1 win")

    elif evaluate(c1.rstrip("DHCS")) < evaluate(c2.rstrip("DHCS")):
        if mise_c1 and mise_c2:
            cardp2.extend(mise_c1)
            cardp2.append(c1)
            cardp2.extend(mise_c2)
            cardp2.append(c2)

            # Empty mise
            mise_c1 = []
            mise_c2 = []
            print(f" => Round {manche} : Player2 win")
        else:
            cardp2.append(c1)
            cardp2.append(c2)
            print(f" => Round {manche} : Player2 win")

    elif evaluate(c1.rstrip("DHCS")) == evaluate(c2.rstrip("DHCS")):
        manche -= 1
        print(f" => Pat")
        # Card player 1
        mise_c1.append(c1)
        for _ in range(3):
            if cardp1:
                mise_c1.append(cardp1.popleft())
            else:
                pat = True

        # Card player 2
        mise_c2.append(c2)
        for _ in range(3):
            if cardp2:
                mise_c2.append(cardp2.popleft())
            else:
                pat = True

else:
    print("\nEnd of the game")

if pat:
    print("=> ** PAT **")
else:
    if len(cardp1) > len(cardp2):
        print("=> ** The winner is PLAYER 1 **")
        print("1", manche)
    elif len(cardp2) > len(cardp1):
        print("=> ** The winner is PLAYER 2 **")
        print("2", manche)

