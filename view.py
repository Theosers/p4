class View:
    def prompt_for_new_tournament_infos(self):
        print("A new tournament has begun\n")

        while True:
            print(
                '-----------------------------------------------------------------------------------------------------')
            name = input("Name of this tournament : ")

            if not self.test_first_as_letter(name):
                continue
            name = name.capitalize()
            place = input("Place of this tournament : ")

            if not self.test_first_as_letter(place):
                continue
            place = place.capitalize()
            date = input("Date : ")

            number_of_rounds = input("Number of rounds : ")

            if not self.test_is_number(number_of_rounds):
                continue

            number_of_players = input("Number of players : ")
            if not self.test_is_number(number_of_players):
                continue

            time_control = input("Bullet, blitz or rapid tournament ? : ")
            time_control = time_control.capitalize()

            if not self.test_time_control_integrity(time_control):
                continue

            description = input("Enter a quick description of this tournament : ")
            print(
                '-----------------------------------------------------------------------------------------------------')
            break

        return [name, place, date, int(number_of_rounds), int(number_of_players), time_control, description]

    def prompt_for_asking_player_name(self):
        while True:
            full_name = input("\nWhat is the full name of the player ? : ")
            if not self.test_only_letter(full_name):
                continue
            if not self.test_is_full_name(full_name):
                continue
            full_name.split()

            full_name[0].capitalize()
            full_name[1].capitalize()
            break
        return full_name

    def prompt_for_new_player(self):
        while True:
            print(
                '***********************************************')
            last_name = input("Last name :")

            if not self.test_only_letter(last_name):
                continue
            last_name.capitalize()
            first_name = input("First name :")


            if not self.test_only_letter(first_name):
                continue
            first_name.capitalize()
            birthday_date = input("Birthday date :")
            gender = input("Gender :")
            if not self.test_first_as_letter(gender):
                continue
            gender = gender.capitalize()
            if not self.test_gender_format(gender):
                continue

            rank = input("Rank :")
            if not self.test_rank_integrity(rank):
                continue
            print("New player added successfully\n")

            print(
                '***********************************************')
            break

        new_player_infos = {'last_name': last_name, 'first_name': first_name, 'birthday_date': birthday_date,
                            'gender': gender, 'rank': rank}

        return new_player_infos

    def prompt_for_end_of_tournament(self, joueur, resultats):
        print(f'The score of {joueur} is {resultats}')

    def prompt_for_winner(self, pairing):
        while True:
            full_name = input(f"Who wins between {pairing[0]} and {pairing[1]} : ")
            if not self.test_is_full_name(full_name):
                continue
            full_name.split()
            if not self.test_only_letter(full_name[0]) and self.test_only_letter(full_name[1]):
                continue
            break
        full_name[0].capitalize()
        full_name[1].capitalize()

        return full_name

    def prompt_menu(self):
        while True:
            print("----------------------------------------------------------------------------")
            print("1. New tournament")
            print("2. Add a player")
            print("3. Player's database")
            print("4. List all tournaments")
            print("5. List of all rounds in a tournament")
            print("6. Exit")
            print("----------------------------------------------------------------------------")
            choice = input("Your choice ? :")
            if not self.test_choice_menu(choice):
                continue
            break
        return int(choice)

    def prompt_menu_player_db(self):
        while True:

            print("1. Show all players")
            print("2. Research a player\n")
            choice = input("Choice : ")
            if not self.test_choice_player_db(choice):
                continue
            break
        return int(choice)

    def prompt_new_profile(self):
        print("\nThis player does not exist")
        print("Adding a new profile...\n")

    def prompt_profile_exist(self):
        print("Player found")

    def prompt_all_db_players(self, player, n=0):
        print(
            '-----------------------------------------------------------------------------------------------------\n')
        print(
            f"N° : {n} || Full name : {player['last_name']} {player['first_name']} ||"
            f" Birthday_date : {player['birthday_date']} || Gender {player['gender']} || rank : {player['rank']}")

    def prompt_all_tournaments(self, n, tournament):
        print(
            '-----------------------------------------------------------------------------------------------------')

        print(
            f"N° {n} || Name : {tournament['name']} || Place : {tournament['place']} || Date : {tournament['date']} ||"
            f" Number of rounds : {tournament['number_of_rounds']} || Time : {tournament['time_control']} ||"
            f" Description : {tournament['description']}\n")

    def prompt_all_rounds(self, index):
        print("-------------------------------------------------------------")
        print(f"Round {str(index + 1)} : ")

    def prompt_all_matchs(self, index, jindex, round):
        print(f"Match {str(jindex + 1)} || Name : "
              f"{round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][0][0]['last_name']} "
              f"{round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][0][0]['first_name']} "
              f"( {round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][1][0]} ) "
              f"|| Name : ",
              f"{round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][0][1]['last_name']} "
              f"{round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][0][1]['first_name']} "
              f"( {round['Round ' + str(index + 1)][jindex]['match ' + str(jindex + 1)][1][1]} )")

    def prompt_asking_tournament_name(self):
        while True:
            name = input("Name of the tournament : ")
            if not self.test_first_as_letter(name):
                continue
            break
        return name

    def prompt_start_round(self, round, current_time):
        input(f"\nPress enter to start the round {round + 1}\n")

        print(f"Round {round + 1} has started at {current_time}\n")

    def prompt_end_round(self, round, current_time):
        print(f"\nEnd of round {round + 1} at {current_time}\n")

    def prompt_press_enter(self):
        input("\nPress enter to continue")

    def prompt_begin_pairing(self):
        input("Press enter to begin pairing")

    def prompt_for_opponent(self, pair):
        print(f"\nplayer [{pair[0]}] plays against [{pair[1]}]")

    def test_first_as_letter(self, text):
        if 65 <= ord(text[0]) <= 90 or 97 <= ord(text[0]) <= 122:
            return True
        print("You need to begin with a letter")
        return False

    def test_time_control_integrity(self, time):
        if time == 'Blitz' or time == 'Bullet' or time == 'Rapid':
            return True
        else:
            print("You should choose between blitz, bullet or rapid")
            return False

    def test_is_number(self, number):
        try:
            int(number)
            return True
        except ValueError:
            print("This is not a number !")
            return False

    def test_is_full_name(self, full_name):
        try:
            if len(full_name.split()) == 2:
                return True
            else:
                print("Please enter a last_name and a first_name")
                return False

        except IndexError:
            print("You have forgotten to write the last_name or first_name")


    def test_gender_format(self, gender):
        if gender == 'M' or gender == 'F':
            return True
        else:
            print("You should enter M or F")
            return False

    def test_only_letter(self, text):
        for char in text:
            if not (65 <= ord(char) <= 90) and not (97 <= ord(char) <= 122) and not ord(char) == 32:
                print("This text does not contain only letters")
                return False
        return True

    def test_rank_integrity(self, rank):
        try:
            rank = int(rank)
            if rank < 0:
                print("A rank should be a positive number")
                return False
            return True

        except ValueError:
            print("This is not a number !")

    def test_choice_menu(self, choice):
        try:
            choice = int(choice)
            if not 1 <= choice <= 6:
                print("Your number is not between [1-6]")
                return False
            return True

        except ValueError:
            print("This is not a number !")

    def test_choice_player_db(self, choice):
        try:
            choice = int(choice)
            if not 1 <= choice <= 2:
                print("Your number is not between [1-2]")
                return False
            return True

        except ValueError:
            print("This is not a number !")

        ''' 
        def test_is_number(self,my_function):
        try:
            my_function
        except ValueError:
            print("This is not a number !")
            

        Bonne ou mauvaise idée ?

        '''
    def prompt_all_round_in_tournament_choice(self):
        while True:
            print("This name matches with no tournament, do you want to try again ?")
            print("1. Yes")
            print("2. No")
            choice = input("Choice ? : ")
            if not self.test_choice_player_db(choice):
                continue
            break
        return int(choice)