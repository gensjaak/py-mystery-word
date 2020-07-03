import random

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_TRIES_COUNT = 5


class MartinMystere:
    def __init__(self,
                 support_max_tries=False,
                 min_number=MIN_NUMBER,
                 max_number=MAX_NUMBER,
                 max_tries_count=MAX_TRIES_COUNT
                 ):
        self._support_max_tries = support_max_tries
        self._min_number = min_number
        self._max_number = max_number
        self._max_tries_count = max_tries_count

        self._user_tries_count = 0
        self._mystery_number = random.randint(self._min_number, self._max_number)
        self._candidate_number = None

        self._failed = False

    def ask_for_name(self):
        self._user_name = input("Hey ! What's your name ? ")

    def greet_user(self):
        print("Welcome " + str(self._user_name) + " !")

    def present_game(self):
        print("The mystery number is between " +
              str(self._min_number) + " and " +
              str(self._max_number) + ".")

    def inform_if_support_max_tries(self):
        if self._support_max_tries:
            print("You have " + str(self._max_tries_count) + " maximum tries.")

    def have_failed(self):
        self._failed = True
        print("Wrong number after " + str(self._max_tries_count) + " tries. You failed !" +
              "\nThe mystery number to guess was: " + str(self._mystery_number))

    def have_won(self):
        print("You found the mystery number after " + str(self._user_tries_count) + " trie(s).")

    def ask_for_user_number(self):
        if self._candidate_number != None:
            precision_str = "lower"
            if self._candidate_number < self._mystery_number:
                precision_str = "greater"

            print("The mystery number is " + precision_str + " than " + str(self._candidate_number) + ".")

            if self._user_tries_count >= int(self._max_tries_count / 2):
                print("Be more smart " + str(self._user_name) + ".")
                print("Following tries are critical." + str(
                    self._max_tries_count - self._user_tries_count) + " remaining tries...")

            self._candidate_number = int(input("Your choice: "))

    def run(self):
        self.ask_for_name()
        self.greet_user()
        self.present_game()
        self.inform_if_support_max_tries()

        while self._candidate_number != self._mystery_number or not self._failed:
            print(self._user_tries_count)
            if self._support_max_tries and self._user_tries_count >= self._max_tries_count:
                self.have_failed()
                return

            self.ask_for_user_number()
            self._user_tries_count += 1

        self.have_won()


mystery = MartinMystere(support_max_tries=True)
mystery.run()
