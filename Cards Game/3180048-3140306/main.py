import time
from myfunctions import *
from classes import *


def main():
    print("Καλωσήλθατε στο Matching Game")
    flag = give_kind_of_game()  # συναρτηση.επιλεγει το ειδος παιχνιδιου
    level = get_level()                                   # καλειται συναρτηση για ελεγχο εγκυροτητας
    c = Deck_of_cards(level)                              # δημιουργια αντικειμενου τραπουλας
    c.shuffle()                                           # αναμειξη των φυλλων
    c.show_deck()                                         # εεκτυπωση της τραπουλας
    input("Press Enter to continue...")
    c.makes_it_hidden()                                   # τη μετατρεπω σε κρυφη για να αρχισει το παιχνιδι
    time.sleep(0.5)
    c.show_deck()
    number_of_players = get_number_of_players()           # καλειται συναρτηση για ελεγχο εγκυροτητας
    # δημιουργια λιστας με αντικειμενα τους παιχτες
    player = []
    for i in range(number_of_players):
        name = input("πληκτρλογηστε το ονομα του παιχτη νο" + str(i+1) + " : ")
        player.append(Player(name))
    print("\n")
    # αν επιλεχθει ενας παιχτης τοτε παιζει εναντιον του υπολογιστη.χρησιμοποιειται κληρονομικοτητα!!
    if number_of_players == 1:
        print("Παιζετε εναντιον του υπολογιστη.")
        number_of_players = 2
        player.append(Computer("windows10", level))
    # ταξινομηση της λιστας αντικειμενων βαση το ονομα καθε παιχτη
    for i in range(1, number_of_players):
        for j in range(number_of_players-1, i-1, -1):
            if player[j].name < player[j-1].name:
                temp = player[j]
                player[j] = player[j-1]
                player[j-1] = temp
    """
    player.sort(key=lambda x:x.name)
    θα μπορουσα και με μια σειρα!!
    """
    key = True
    while key:
        i = 0
        while i < number_of_players:
            print(player[i].name + " παιζει")                   # τυπωνει το ονομα του παιχτη που παιζει
            x, y = player[i].play(c)                            # ο παιχτης παιζει και επιστρεφεται η θεση που επιλεγει
            k, m = player[i].play(c)                            # ο παιχτης επιλεγει τη δευτερη θεση
            # αν τα φυλλα δεν ειναι ιδια τοτε αλλαζει η κατασταση τους ξανα σε κρυφη αλλιως προστιθενται οι ποντοι
            if c.check_cards(x, y, k, m):
                player[i].points += c.deck[x-1][y-1].value
                print("Επιτυχές ταίριασμα +" + str(c.deck[x - 1][y - 1].value) + " πόντοι! " + player[i].name + " έχεις συνολικά " + str(player[i].points) + " πόντους.")
            # ελεγχοσ σε περιπτωση που μετρανε και τα συμβολα.προσθετει το αθροισμα τηα αξιας των 2 συμβολων
            elif flag and c.check_symbols(x, y, k, m):
                player[i].points += c.deck[x - 1][y - 1].value + c.deck[k - 1][m - 1].value
                print("Επιτυχές ταίριασμα +" + str(c.deck[x - 1][y - 1].value + c.deck[k - 1][m - 1].value)+ " πόντοι! " + player[i].name + "  έχεις συνολικά "+ str(player[i].points)+ " πόντους.")
            #  ελεγχος 3ης περιπτωσης για ειδικες καρτες
            elif (c.deck[x-1][y-1].number == "Q" and c.deck[k-1][m-1].number == "K") or (c.deck[x-1][y-1].number == "K" and c.deck[k-1][m-1].number == "Q") :
                z, e = player[i].play(c)
                if c.check_cards(x, y, z, e):
                    player[i].points += c.deck[x - 1][y - 1].value
                    print("Επιτυχές ταίριασμα +" + str(c.deck[x - 1][y - 1].value) + " πόντοι!  " + player[i].name + "  έχεις συνολικά " + str(player[i].points) + " πόντους.")
                    input("Press Enter to continue...")
                    c.change_situation(k, m, False)
                    c.show_deck()
                elif c.check_cards(k, m, z, e):
                    player[i].points += c.deck[k - 1][m - 1].value
                    print("Επιτυχές ταίριασμα +" + str(c.deck[x - 1][y - 1].value) + " πόντοι!  " + player[i].name + "  έχεις συνολικά " + str(player[i].points) + " πόντους.")
                    input("Press Enter to continue...")
                    c.change_situation(x, y, False)
                    c.show_deck()
                elif flag and c.check_symbols(x, y, z, e):
                    player[i].points += c.deck[x - 1][y - 1].value + c.deck[z - 1][e - 1].value
                    print("Επιτυχές ταίριασμα +" + str(c.deck[x - 1][y - 1].value + c.deck[z - 1][e - 1].value) + " πόντοι! " + player[i].name + "  έχεις συνολικά " + str(player[i].points) + " πόντους.")
                    input("Press Enter to continue...")
                    c.change_situation(k, m, False)
                    c.show_deck()
                elif flag and c.check_symbols(k, m, z, e):
                    player[i].points += c.deck[k - 1][m - 1].value + c.deck[z - 1][e - 1].value
                    print("Επιτυχές ταίριασμα +" + str(c.deck[k - 1][m - 1].value + c.deck[z - 1][e - 1].value) + " πόντοι! " + player[i].name + "  έχεις συνολικά " + str(player[i].points) + " πόντους.")
                    input("Press Enter to continue...")
                    c.change_situation(x, y, False)
                    c.show_deck()
                else:
                    input("Press Enter to continue...")
                    c.change_situation(x, y, False)
                    c.change_situation(k, m, False)
                    c.change_situation(z, e, False)
                    c.show_deck()
            else:
                input("Press Enter to continue...")
                c.change_situation(x, y, False)
                c.change_situation(k, m, False)
                c.show_deck()
            time.sleep(1)
            #  τσεκαρει αν υπαρχει νοημα να συνεχιστει το παιχνιδι.αν μπορουν ακομη να προκυψουν εγκυροι συνδυασμοι.
            if flag and not c.check_if_there_are_combinatios():
                key = False
                break
            # ειδικες καρτες και σειρα επομενου παιχτη
            if c.deck[x-1][y-1].number == "J" and c.deck[k-1][m-1].number == "J":
                i = i
            elif c.deck[x-1][y-1].number == "K" and c.deck[k-1][m-1].number == "K":
                i += 2
            else:
                i += 1  # αλλαζει ο δεικτης δηλαδη παιρνει σειρα ο επομενος παικτης
            print("="*50)
            # ελεγχος αν εχει εμφανιστει ολη η τραπουλα
            if c.check_finish():
                continue
            else:
                key = False
                break
    # βρισκει και εμφανιζει τον νικητη
    maximum = player[0].points
    list_of_winners = []
    for i in range(number_of_players):
        if maximum < player[i].points:
            maximum = player[i].points
    for i in range(number_of_players):
        if player[i].points == maximum:
            list_of_winners.append(player[i].name)
    if len(list_of_winners) == 1:
        print("ο νικητης με  " + str(maximum) + " ποντουσ ειναι ο παιχτης : " + list_of_winners[0])
    else:
        print("το παιχνιδι εληξε ισοπαλια αναμεσα στους παιχτες :", end="")
        for i in list_of_winners:
            print(i, end=" ")


if __name__ == '__main__':
    main()
