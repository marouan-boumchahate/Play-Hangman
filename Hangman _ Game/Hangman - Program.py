import MyFunctions
import os
from random import randint
from collections import defaultdict

#file = "C:/Users/marou/OneDrive/Desktop/Courses/Python/Python Learning/PROJECTS/Codes/Hangman _ Game/Hangman - Data/####.txt"
file = "Hangman - Data/####.txt"

class Hangman:
    def __init__(self, word):
        self.Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.Alphabets_Dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

        self.wrong_counter = 0

        self.XP = 0

        self.word = word

        self.word_to_dict()

        self.filling_word()

    # Convert letters to dictionary to help me access the index directly for a letter
    def word_to_dict(self):
        self.dict_word = defaultdict(list)

        idx = 0

        for letter in self.word:
            if letter != ' ':
                self.dict_word[letter].append(idx)
                idx += 1

        del idx

    # Create another list of that word without letters to assign each letter whenever he is right
    def filling_word(self):
        self.filling_word = []

        for letter in self.word:
            if letter != ' ':
                self.filling_word.append(" ")

    # Draw THe hangman part everytime the user enter a letter wrong
    def draw_hangman(self):
        match(self.wrong_counter):
            case 0:
                self.hangman_0()
            case 1:
                self.hangman_1()
            case 2:
                self.hangman_2()
            case 3:
                self.hangman_3()
            case 4:
                self.hangman_4()
            case 5:
                self.hangman_5()
            case 6:
                self.hangman_6()
            case 7:
                self.hangman_7()
            case 8:
                self.hangman_8()
            case 9:
                self.hangman_9()
            case 10:
                self.hangman_10()

        
        print()

    # Empty Hangman
    def hangman_0(self):
        print("\n"*23)

    # Buttom Part
    def hangman_1(self):
        print("\n"*19)

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # The vertical line
    def hangman_2(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        print(des*17, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # The horizontal line
    def hangman_3(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        print(" "*40 + "* "*10)
        print(des*16, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # The head
    def hangman_4(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        print(" "*40 + "* "*10)
        print(des*3, end = "")

        print(" "*40 + "*" + " "*20 + "  * *  ")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "  * *  ")

        print(des*13, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # The body
    def hangman_5(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        des_1 = " "*40 + "*" + " "*23 + "*" + "\n"
        print(" "*40 + "* "*10)
        print(des*3, end = "")

        print(" "*40 + "*" + " "*20 + "  * *  ")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "  * *  ")

        print(des_1*6, end = "")
        print(des*7, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # Left hand
    def hangman_6(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        des_1 = " "*40 + "*" + " "*23 + "*" + "\n"
        print(" "*40 + "* "*10)
        print(des*3, end = "")

        print(" "*40 + "*" + " "*20 + "  * *  ")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "  * *  ")

        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "  * *")
        print(" "*40 + "*" + " "*19 + "*   *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")

        print(des*7, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # Right hand
    def hangman_7(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        des_1 = " "*40 + "*" + " "*23 + "*" + "\n"
        print(" "*40 + "* "*10)
        print(des*3, end = "")

        print(" "*40 + "*" + " "*20 + "  * *  ")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "  * *  ")

        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "  * * *")
        print(" "*40 + "*" + " "*19 + "*   *   *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")

        print(des*7, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # Left leg
    def hangman_8(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        des_1 = " "*40 + "*" + " "*23 + "*" + "\n"
        print(" "*40 + "* "*10)
        print(des*3, end = "")

        print(" "*40 + "*" + " "*20 + "  * *  ")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "  * *  ")

        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "  * * *")
        print(" "*40 + "*" + " "*19 + "*   *   *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "  *")
        print(" "*40 + "*" + " "*19 + "*")

        print(des*5, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # Right leg
    def hangman_9(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        des_1 = " "*40 + "*" + " "*23 + "*" + "\n"
        print(" "*40 + "* "*10)
        print(des*3, end = "")

        print(" "*40 + "*" + " "*20 + "  * *  ")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "*     *")
        print(" "*40 + "*" + " "*20 + "  * *  ")

        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "  * * *")
        print(" "*40 + "*" + " "*19 + "*   *   *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "  *   *")
        print(" "*40 + "*" + " "*19 + "*       *")

        print(des*5, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # The cord
    def hangman_10(self):
        print("\n")
        des = " "*40 + "*" + "\n"
        des_1 = " "*40 + "*" + " "*23 + "*" + "\n"
        print(" "*40 + "* "*10)
        print(" "*40 + "*" + " "*17 + "*")
        print(" "*40 + "*" + " "*17 + "*")
        print(" "*40 + "*" + " "*17 + "*")

        print(" "*40 + "*" + " "*17 + "*" + " "*2 + "  * *  ")
        print(" "*40 + "*" + " "*17 + "*" + " "*2 + "*     *")
        print(" "*40 + "*" + " "*17 + "*" + " "*2 + "*     *")
        print(" "*40 + "*" + " "*17 + "*" + " "*2 + "  * *  ")

        print(" "*40 + "*" + " "*17 + "**" + "*****")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "  * * *")
        print(" "*40 + "*" + " "*19 + "*   *   *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "    *")
        print(" "*40 + "*" + " "*19 + "  *   *")
        print(" "*40 + "*" + " "*19 + "*       *")

        print(des*5, end = "")

        print(" "*30 + "      * * * * *      " )     
        print(" "*30 + "    *           *    ")
        print(" "*30 + "  *               *  ")
        print(" "*30 + "*                   *")

    # print all the letters user still can choose from them
    def Print_Available_Letters(self):
        print(" "*20, end = "")
        for i in range(13):
            print(" --- " + "  ", end = "")
        print()

        print(" "*20, end = "")
        for i in range(13):
            print("| " + self.Alphabets[i] + " |" + "  ", end = "")
        print()

        print(" "*20, end = "")
        for i in range(13):
            print(" --- " + "  ", end = "")
        print()

        print()

        print(" "*20, end = "")
        for i in range(13, 26):
            print(" --- " + "  ", end = "")
        print()

        print(" "*20, end = "")
        for i in range(13, 26):
            print("| " + self.Alphabets[i] + " |" + "  ", end = "")
        print()

        print(" "*20, end = "")
        for i in range(13, 26):
            print(" --- " + "  ", end = "")
        print()

    # add 1 to the number of wrongs
    def increment_counter(self):
        self.wrong_counter += 1

    # update the score by the value has gotten from the parameter
    def update_score(self, value):
        self.XP = self.XP + value

    # check if the user won by checking if he find all the letters
    def user_win(self):
        return self.dict_word == {}

    # remove the letter from dict_word and assign them to the filling_word
    def apply_changes(self, char):
        indices = self.dict_word.pop(char)

        for idx in indices:
            self.filling_word[idx] = char
            self.update_score(25)

    # Remove Alphabet from the Alphabets
    def remove_alphabet(self, char):
        self.Alphabets[self.Alphabets_Dict.pop(char)] = " "

    # does user letter exist in dict_word
    def isletterinword(self, char):
        return char in self.dict_word

    # check if the hangman dead
    def user_lost(self):
        return self.wrong_counter == 10

    # print the letters that has been entered with the ones that not
    def print_filling_words(self):
        print("\n" + " "*45, end = "")

        for char in self.filling_word:
            print(char + "    ", end = "")
        
        print("\n" + " "*45, end = "")
        for char in self.filling_word:
            print("-    ", end = "")

class Play:
    def __init__(self):
        self.words = {1:"animals", 2:"foods", 3:"clothes", 4:"countries", 5:"subjects", 6:"sports"}

        while True:
            self.perform_hangman_menu()

    def perform_hangman_menu(self):
        self.hangman_menu()

        choice = MyFunctions.read_choice("\n" + " "*35 + "Enter a choice from above (1-2): ", end = 2)

        match(choice):
            case 1:
                self.play()
            case 2:
                self.game_explination()
                input("\n\n" + " "*45 + "Press enter to go back...")

    def hangman_menu(self):
        os.system("cls")

        MyFunctions.Draw_Header_Screen("WELCOME TO HANGMAN GAME", 35)

        print(" "*42 + "1- Play")
        print(" "*42 + "2- Learn How To Play")

    def play(self):
        while True:
            self.categories_menu()

            self.Hangman_Start = Hangman(self.find_word())

            # os.system("cls")
            # print(f"the word is {self.Hangman_Start.word}")
            # input("")
            
            self.start_playing()

            if not MyFunctions.isyes("Do you wanna play more (Y/N): "):
                break

    def game_explination(self):
        os.system("cls")
        MyFunctions.Draw_Header_Screen("How To Play?? SCREEN", 45)

        print(" "*20 + "1- Choose the category group (the word will be from the category you chose)\n")
        print(" "*20 + "2- There are letters available in the game. You have to choose from them\n")
        print(" "*20 + "3- You will guess a letter for the target word\n")
        print(" "*20 + "4- If the letter is correct, it will be placed in its corresponding position and you will gain 25 XP\n")
        print(" "*20 + "5- If the letter is wrong, it will be removed from available letters and build the HANGMAN part\n")
        print(" "*20 + "6- You can type 'hint' to let the game helps you\n")
        print(" "*20 + "8- After typing 'hint' you will have two choices:\n")
        print(" "*25 + "a- Undo a letter from available alphabets. (NOTICE: 50 XP will be charged from you)\n")
        print(" "*25 + "b- Get a letter from the target word. (NOTICE: 100 XP will be charged from you)\n")
        print(" "*20 + "9- You will LOSE if the game is done drawing the whole parts for the HANGMAN\n")
        print(" "*20 + "10- You will WIN if you complete the whole word before the HANGMAN is done drawing\n")
        print(" "*25 + "--> WARNING!! if you take a hint you will NOT get the full score <--".upper())
            
    def categories_menu(self):
    
        os.system("cls")
        MyFunctions.Draw_Header_Screen("Categories", 35)

        print(" "*32 + "1- Animals       2- Foods")
        print(" "*32 + "3- Clothes       4- Countries")
        print(" "*32 + "5- Subjects      6- Sports")

        print()

    def find_word(self):
        choice = MyFunctions.read_choice(" "*30 + "Enter a number of which category (1-6): ", end = 6)

        all_words = MyFunctions.LoadtxtData(file.replace("####", self.words[choice]))
        word = all_words[randint(0, len(all_words) - 1)]

        del all_words

        return word.upper()

    def start_playing(self):
        while True:
            os.system("cls")
            MyFunctions.Draw_Header_Screen("Hangman", 55)

            self.Hangman_Start.draw_hangman()
            self.Hangman_Start.Print_Available_Letters()

            self.Hangman_Start.print_filling_words()

            print()

            letter = self.Read_Letter()

            if self.Hangman_Start.isletterinword(letter):
                self.Hangman_Start.apply_changes(letter)
                self.Hangman_Start.remove_alphabet(letter)

                if self.Hangman_Start.user_win():
                    os.system("cls")
                    score = self.Hangman_Start.XP / (len(self.Hangman_Start.filling_word)  * 25) * 100
                    MyFunctions.Draw_Header_Screen("Congratulation!! The word is {a}, and your score is {b:.2f}%".format(a = self.Hangman_Start.word, b = score), 40)
                    break

                else:
                    continue
            else:
                self.Hangman_Start.remove_alphabet(letter)

                self.Hangman_Start.increment_counter()

                if self.Hangman_Start.user_lost():
                    os.system("cls")
                    MyFunctions.Draw_Header_Screen(f"LOST!!! the word was {self.Hangman_Start.word}", 33)
                    self.Hangman_Start.draw_hangman()

                    break

    def Read_Letter(self):
        print()

        print(" "*55 + f"XP points = {self.Hangman_Start.XP}")

        print()

        while True:
            letter = input(" "*40 + "Enter a letter (or type 'hint' - to get some help): ")

            if letter.lower() == "hint":
                self.hint_menu()
                return self.perform_hint_choice()

            if letter.isalpha():
                if letter.upper() in self.Hangman_Start.Alphabets:
                    return letter.upper()
                else:
                    print("Error!! letter NOT found\nTry Again")
            else:
                print("Error!! letter is expected\nTry Again")

    def hint_menu(self):
        os.system("cls")

        MyFunctions.Draw_Header_Screen("Hint Menu", 40)

        print(" "*33 + "1- Undo a letter from available letters (-50 XP)")
        print(" "*33 + "2- Provide a letter for you (-100 XP)")

    def perform_hint_choice(self):
        choice = MyFunctions.read_choice("\n" + " "*33 + "Enter the number of your hint choice (1-2): ", end = 2)

        match(choice):
            case 1:
                return self.undo_letter()
            case 2:
                return self.guissed_letter()

    def undo_letter(self):
        if self.Hangman_Start.XP >= 50:
            for letter in self.Hangman_Start.Alphabets:
                if (letter not in self.Hangman_Start.word) and (letter != " "):

                    os.system("cls")
                    print(" "*40 + f"The letter '{letter}' has been undo for you\n")
                    input(" "*40 + "Press enter to continue playing...")

                    self.Hangman_Start.update_score(-50)
                    self.Hangman_Start.wrong_counter -= 1
                    return letter
        else:
            os.system("cls")
            print(" "*40 + "SORRY!! you don't have enough XP points\n")
            input(" "*40 + "press enter to continue playing...")
            self.start_playing()

    def guissed_letter(self):
        if self.Hangman_Start.XP >= 100:
            for letter in self.Hangman_Start.dict_word:
                if letter not in self.Hangman_Start.filling_word:
                    os.system("cls")
                    print(" "*40 + f"The letter '{letter}' is placed for you\n")
                    input(" "*40 + "Press enter to continue playing...")

                    self.Hangman_Start.update_score(-125)
                    return letter
        else:
            os.system("cls")
            print(" "*40 + "SORRY!! you don't have enough XP points\n")
            input(" "*40 + "press enter to continue playing...")
            self.start_playing()    

play_1 = Play()