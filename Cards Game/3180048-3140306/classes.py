from random import randint
from main import*
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def play(self, object):
        while True:
            try:
                x, y = map(int, input("Δώστε γραμμή και στήλη κάρτας: ").split())
                if object.deck[x - 1][y - 1].situation:
                    print("ο συνδυασμος  αντιστοιχει σε ανοιχτη καρτα!")
                    continue
                else:
                    object.change_situation(x, y, True)  # αλλαζει προσωρινα σε φανερη η καρτα που επελεξε
                    object.show_deck()  # εμφανιση της τραπουλας
            except:
                print("Κατι πηγε στραβα.Δοκιμαστε παλι")
                continue
            break
        return x, y


class Computer(Player):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def play(self, object):
        if self.level == 1:
            number = 4
        elif self.level == 2:
            number = 10
        else:
            number = 13
        while True:
            x = randint(1, 4)
            y = randint(1, number)
            if not object.deck[x - 1][y - 1].situation:
                break
        object.change_situation(x, y, True)
        object.show_deck()
        return x, y


class Card:
    def __init__(self, number, symbol, value):
        self.number = number
        self.symbol = symbol
        self.value = value
        self.situation = True

    def show(self):
        if self.number == "10":
            return "  " + self.number + self.symbol	
        else:
            return "  " + self.number + self.symbol + " "

    def hide(self):
        return "  X  "


class Deck_of_cards:
    def __init__(self, level):
        list_of_symbols = ["\u2663", "\u2660", "\u2666", "\u2665"]
        if level == 1:
            self.list_of_numbers = ["10", "J", "Q", "K"]
            list_of_value = [10, 10, 10, 10]
        elif level == 2:
            self.list_of_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
            list_of_value = [i for i in range(1, 11)]
        else:
            self.list_of_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
            list_of_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        self.deck = [[0 for i in range(len(self.list_of_numbers))] for j in range(4)]
        for i in range(4):
            for j in range(len(self.list_of_numbers)):
                self.deck[i][j] = Card(self.list_of_numbers[j], list_of_symbols[i], list_of_value[j])

    def show_deck(self):
        for i in range(len(self.list_of_numbers) + 1):
            if i == 0:
                print("     ", end="")
            else:
                if i >= 10:
                    print(str(i) + " ", end="  ")
                else:
                    print(str(i) + "  ", end="  ")
        print()
        for i in range(4):
            print(i + 1, end="  ")
            for j in range(len(self.list_of_numbers)):
                if self.deck[i][j].situation:
                    print(self.deck[i][j].show(), end="")
                else:
                    print(self.deck[i][j].hide(), end="")
            print("\n")
        print("\n")

    def check_finish(self):
        for i in range(4):
            for j in range(len(self.list_of_numbers)):
                if not self.deck[i][j].situation:
                    return True
        return False

    def change_situation(self, x, y, bool):
        self.deck[x - 1][y - 1].situation = bool

    def makes_it_hidden(self):
        for i in range(4):
            for j in range(len(self.list_of_numbers)):
                self.deck[i][j].situation = False

    def check_cards(self, i, j, k, m):
        if self.deck[i-1][j-1].number != self.deck[k-1][m-1].number:
            return False
        return True

    def shuffle(self):
        for i in range(4):
            for j in range(len(self.list_of_numbers)):
                x = randint(0, 3)
                y = randint(0, len(self.list_of_numbers)-1)
                pos = self.deck[i][j]
                self.deck[i][j] = self.deck[x][y]
                self.deck[x][y] = pos

    def check_symbols(self, i, j, k, m):
        if self.deck[i - 1][j - 1].symbol == self.deck[k - 1][m - 1].symbol:
            return True
        return False

    def check_if_there_are_combinatios(self):
        list1 = []
        list2 = []
        for i in range(4):
            for j in range(len(self.list_of_numbers)):
                if not self.deck[i][j].situation:
                    list1.append(self.deck[i][j].number)
                    list2.append(self.deck[i][j].symbol)
        plithos1 = [0 for i in list1]
        plithos2 = [0 for i in list2]
        for i in range(len(list1)):
            for j in range(len(list1)):
                if list1[i] == list1[j]:
                    plithos1[i] += 1
        for i in range(len(list2)):
            for j in range(len(list2)):
                if list2[i] == list2[j]:
                    plithos2[i] += 1
        for i in plithos1:
            if i > 1:
                return True
        for i in plithos2:
            if i > 1:
                return True
        return False
