def get_level():
    while True:
        try:
            level = int(input("Δώστε επίπεδο δυσκολίας Εύκολο (1), Μέτριο (2), Δύσκολο (3) :"))
            if level == 1 or level == 2 or level == 3:
                break
            else:
                print("ο αριθμος που δωσατε δεν αντιστοιχει σε καποιο επιπεδο")
                continue
        except:
            print("δεν πληκτρολογησατε αριθμο ")
            continue
        break
    return level


def get_number_of_players():
    while True:
        try:
            number_of_players = int(input("Δώστε αριθμό παικτών :"))
            if 0 < number_of_players < 10:
                break
            else:
                print("δωστε αριθμο απο το 1 εως το 10 ")
                continue
        except:
            print("δεν πληκτρολογησατε αριθμο ")
            continue
        break
    return number_of_players


def give_kind_of_game():
    while True:
        try:
            flag = int(input("πληκτρολογηστε 0 αν θελετε απλο παιχνιδι η 1 αν θελετε θελετε το συνθετο :"))
            if flag == 0:
                return False
            elif flag == 1:
                return True
            else:
                print("παρακαλουμε πληκτρολογηστε 0 η 1 ")
                continue
        except:
            print("δεν δωσατε αριθμο ")
            continue