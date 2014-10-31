values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
reverse = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"}

def getKey1(item):
    return item[0]

def getKey2(item):
    return item[1]

def getValue(hand):
    value = ""
    if len(hand) < 5:
        return value
    ###########################################Straight Flush###########################################
    last = 0
    last2 = ""
    straight = 1
    simtree = 1
    hand = sorted(hand, key=getKey1)
    hando = sorted(hand, key=getKey2)
    for card in range(1,len(hand)+1):
        if hando[-card][0] == last-1:
            straight += 1
        elif hando[-card][0] == last:
            None
        else:
            straight = 1
        if hando[-card][0] == last:
            None
        elif hando[-card][1] == last2:
            simtree += 1
        else:
            simtree = 1
        if straight == 5 and simtree == 5:
            return "Straight Flush"
        last = hando[-card][0]
        last2 = hando[-card][1]
    ###############################################Poker###############################################
    last = 0
    straight = 1
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last:
            straight += 1
        else:
            straight = 1
        if straight == 4:
            return "Poker"
        last = hand[-card][0]
    #############################################Full House#############################################
    last = 0
    straight = 1
    condition = ""
    condition2 = ""
    num = 0
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last:
            straight += 1
        else:
            straight = 1
        if straight == 3 and condition2 != "Triad":
            if num == hand[-card][0]:
                condition2 = "Triad"
            condition = "Triad"
            num = hand[-card][0]
        elif straight == 2 and condition2 != "Pair" and num != hand[-card][0]:
            condition = "Pair"
            num = hand[-card][0]
        if condition != "":
            if (condition == "Pair" and condition2 == "Triad") or (condition == "Triad" and condition2 == "Pair"):
                return "Full House"
            condition2 = condition
            condition = ""
        last = hand[-card][0]
    ###############################################Flush###############################################
    last2 = ""
    simtree = 1
    for card in range(1,len(hand)+1):
        if hando[-card][1] == last2:
            simtree += 1
        else:
            simtree = 1
        if simtree == 5:
            return "Flush"
        last2 = hando[-card][1]
    #############################################Straight##############################################
    last = 0
    straight = 1
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last-1:
            straight += 1
        else:
            straight = 1
        if straight == 5:
            return "Straight"
        last = hand[-card][0]
    ###########################################Three of a kind###########################################
    last = 0
    straight = 1
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last:
            straight += 1
        else:
            straight = 1
        if straight == 3:
            return "Three of a kind"
        last = hand[-card][0]
    ###############################################Two Pair###############################################
    last = 0
    straight = 1
    condition = ""
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last:
            straight += 1
        else:
            straight = 1
        if straight == 2 and condition == "Pair":
            return "Two Pair"
        if straight == 2:
            condition = "Pair"
        last = hand[-card][0]
    ###############################################One Pair###############################################
    last = 0
    straight = 1
    for card in range(1,len(hand)+1):
        if hand[-card][0] == last:
            straight += 1
        else:
            straight = 1
        if straight == 2:
            return "One Pair"
        last = hand[-card][0]
    ###############################################High Card###############################################
    return "High Card"

def makeString(hand):
    htype = getValue(hand)
    string = ""
    for card in hand:
        string += (reverse[card[0]]+card[1]) + " "
    string = string[:-1]
    if htype != "":
        string += (" " + htype + "\n")
    else:
        string += ("\n")
    return string

def winner(stats):
    stats = stats[:-1]
    if stats.find("Straight Flush") != -1:
        pos = stats.find("Straight Flush")
        return stats[0:pos+14] + " (winner)" + stats[pos+14::]
    elif stats.find("Poker") != -1:
        pos = stats.find("Poker")
        return stats[0:pos+5] + " (winner)" + stats[pos+5::]
    elif stats.find("Full House") != -1:
        pos = stats.find("Full House")
        return stats[0:pos+10] + " (winner)" + stats[pos+10::]
    elif stats.find("Flush") != -1:
        pos = stats.find("Flush")
        return stats[0:pos+5] + " (winner)" + stats[pos+5::]
    elif stats.find("Straight") != -1:
        pos = stats.find("Straight")
        return stats[0:pos+8] + " (winner)" + stats[pos+8::]
    elif stats.find("Three of a kind") != -1:
        pos = stats.find("Three of a kind")
        return stats[0:pos+15] + " (winner)" + stats[pos+15::]
    elif stats.find("Two Pair") != -1:
        pos = stats.find("Two Pair")
        return stats[0:pos+8] + " (winner)" + stats[pos+8::]
    elif stats.find("One Pair") != -1:
        pos = stats.find("One Pair")
        return stats[0:pos+8] + " (winner)" + stats[pos+8::]
    elif stats.find("High Card") != -1:
        pos = stats.find("High Card")
        return stats[0:pos+9] + " (winner)" + stats[pos+9::]
    return stats

def order(players):
    result = ""
    for player in players:
        cards = []
        trees = []
        hand = []
        sub = []
        sub2 = []
        current = ""
        for card in player[::3]:
            cards.append(card)
        for tree in player[1::3]:
            trees.append(tree)
        for a,b in zip(cards,trees):
            hand.append(a+b)
        for item,tree in zip(hand,trees):
            sub = []
            sub.append(values[item[0]])
            sub.append(tree)
            sub2.append(sub)
        current = makeString(sub2)
        result += current
    result = winner(result)
    return result

    raise NotImplementedError

    def GetRankedGame(hands):
        players = hands.split("\n")
        return order(players)

    raise NotImplementedError
if __name__ == '__main__':
    print("Captura un mano por linea y una linea en blanco para terminar:")
    hands = ""
    line = input()
    while(line != ""):
        hands += line + "\n"
        line = input()
    print(GetRankedGame(hands))