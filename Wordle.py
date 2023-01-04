import random

def word_list():
    f = open("5_letter_words.txt", "r")
    list_of_words = []
    for i in f:
        word = i.strip()
        list_of_words.append(word)
    return(list_of_words)
    
def random_word(list_of_words):
    word_random = random.choice(list_of_words)
    return(word_random)
    
def is_real_word(guess, list_of_words):
    if guess in list_of_words:
        return(True)
    else:
        return(False)
    
def check_guess(guess, word_random):
    result = ""
    guess_word = []
    for i in guess:
        guess_word.append(i)

    r_word = []
    for j in word_random:
        r_word.append(j)
        

    for x in range(5):
        if r_word[x] == guess_word[x]:
            result += "X"
        elif guess_word[x] in r_word:
            result += "O"
        else:
            result += "_"
            
    print(result)
    
def next_guess(list_of_words):
    guess = input("Please enter a guess: ")
    guess = guess.lower
    if is_real_word() == True:
        check_guess()
        return(guess)
    else:
        print("That is not a real word!")
    
def play():
    word_list()
    random_word()
    print(next_guess())
    
    

