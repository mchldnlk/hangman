import random
import os 

def pick_capital(capitals):
    '''
    Picks a random European capital
    '''
    password = random.choice(capitals) 
    return password

def get_hashed(password):
    '''
    Generates a password based on the word with dashes instead of letters
    Keeps whitespaces undashed.
    '''
    new_list = []
    for letter in password:
        if letter == " ":
            line = " "
            new_list.append(line)
        else:
            line = "_"
            new_list.append(line)
    print("\n"," ".join(new_list),"\n")
    hashed_password = "".join(new_list)
    
    return hashed_password

def uncover(hashed_password, password, letter):
    '''
    Uncovers all occurences of the given letter in the hashed password based on the password
    '''
    password_list = [char for char in password]
    hashed_password_list = [char for char in hashed_password]
    hashed_password_to_print_list = [char for char in hashed_password]
    for i in range(0,len(password_list)):
        if letter == password_list[i]:
            hashed_password_list[i] = letter
            hashed_password_to_print_list[i] = letter

    hashed_password_to_print = " ".join(hashed_password_to_print_list)
    hashed_password = "".join(hashed_password_list)
    return hashed_password, hashed_password_to_print

def is_win(hashed_password, password):
    '''
    Checks if the hashed password is fully uncovered
    '''
    if hashed_password == password:
        print("You win!")
        print("Correct asnwer is exactly: ", password)
        print("\n")
        return True
    else:
        return False

def is_loose(life_points, password):
    '''
    Checks if life points is equal 0
    '''
    if life_points == 0:
        print("You loose!")
        print("Correct asnwer: ", password)
        print("\n")
        return True
    else:
        return False

def get_input(life_points, password, used_letters, capitals_upper, hashed_password_to_print):
    '''
    Reads a user input until it contains only letter or correct asnwer
    '''
    temp = False
    while temp != True:

        letter = input("Give me a letter or correct answer: ")
        letter = letter.upper()

        if letter in 'ABCDEFGHIJKLMNOPRSQTUVWXYZ' and len(letter) == 1:
            temp = True
        elif letter in capitals_upper:
            temp = True
        elif letter != password and (len(letter) == len(password)) and letter not in used_letters:
            life_points -= 1
            os.system('clear')
            used_letters.append(letter)
            temp = True
        else:
            print("Wrong input.")
            temp = False

    return letter, life_points, used_letters

def drawing(life_points, used_letters, letter, password):

    print("\nLives: ",life_points)
    print("Used answers: ",used_letters)
    if life_points == 7:
        return ('          \n          \n          \n          \n          \n          ')
    elif life_points == 6:
        return ('          \n   |      \n   |      \n   |      \n   |      \n  / \     ')
    elif life_points == 5:
        return ('   _____  \n   |      \n   |      \n   |      \n   |      \n  / \     ')
    elif life_points == 4:
        return ('   _____  \n   |   |  \n   |      \n   |      \n   |      \n  / \     ')
    elif life_points == 3:
        return ('   _____  \n   |   |  \n   |   O  \n   |      \n   |      \n  / \     ')
    elif life_points == 2:
        return ('   _____  \n   |   |  \n   |   O  \n   |   |  \n   |      \n  / \     ')
    elif life_points == 1:
        return ('   _____  \n   |   |  \n   |   O  \n   |  /|\ \n   |      \n  / \     ')
    elif life_points == 0:
        return ('   _____  \n   |   |  \n   |   O  \n   |  /|\ \n   |  / \ \n  / \     ')

def print_result(password):
    hashed_password = password
    hashed_password = hashed_password.upper()
    hashed_password_to_print = [char for char in hashed_password]
    hashed_password_to_print = (" ").join(hashed_password)
    hashed_password = hashed_password.lower()
    print("\n",hashed_password_to_print)

def adding_letter_to_used_answers(letter, life_points, used_letters, hashed_password):
    if letter not in used_letters:
        used_letters.append(letter)
        if letter not in hashed_password:
            life_points = life_points - 1
            return letter, used_letters, life_points
    return letter, used_letters, life_points

def main():
    
    capitals = [line.rstrip('\n') for line in open("./hangman.txt")]
    capitals_upper = [item.upper() for item in capitals]
    os.system('clear')
    print("\nTry to guess what eauropean capital I am thinking about!")
    life_points = 7
    password = pick_capital(capitals).upper()
    # print(password)
    letter = ""
    hashed_password = get_hashed(password)
    hashed_password_to_print = ""
    used_letters = []

    
    while hashed_password != password:   

        letter, life_points, used_letters = get_input(life_points, password, used_letters, capitals_upper, hashed_password_to_print)
        
        os.system('clear')

        hashed_password = uncover(hashed_password, password, letter)[0]
        hashed_password_to_print = uncover(hashed_password, password, letter)[1].upper()
        
        letter, used_letters, life_points = adding_letter_to_used_answers(letter, life_points, used_letters, hashed_password)

        if letter == password:
            life_points = life_points + 1
            print_result(password)
            hashed_password = password
        else:
            print("\n",hashed_password_to_print)
            
        print("\n",drawing(life_points, used_letters, letter, password))
        
        if is_win(hashed_password, password) == True:
            break

        if is_loose(life_points, password) == True:
            break

if __name__ == '__main__':
    main()
