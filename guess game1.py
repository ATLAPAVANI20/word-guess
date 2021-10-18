#imported sqlite3 for database purpose
import sqlite3
#connection sqlite3 for database
conn =sqlite3.connect("my_first_db1")
cursor =conn.cursor()
#library that we use in odder to choose
#on random words from the list
from random import randrange
#to print the about the game
print('weclome to the game\n',
      'ABOUT THE GAME \n'
      'In word guess the blank space letter\n',
         'we need to guess the word\n' 
            'If user guess correct word.we will the game and move to next level\n',
                'we have 2 attempt.if user loose the game .better luck next time\n',
                'here the difficulty level increased by word to word basic on that score will be added ')
#here the user is asked to enter the name first
user_name = (input("enter the  name:"))
print('welcome',user_name,'to the game, lets the play')
#interpreter will choose random  words form the list
words = ['dog','cat' , 'word','play','run']
#this is the output user must fill the blank space
guess_words = ["d _ g", "_ a t", "w _ _ d","pl _ _","r _ n"]
guess_letter = ["dxg", "xat", "wxd","plx","rxn"]
final_result=0
#Defining a class 
def find_guess():
    # By using global before the variable declared globaly
    global final_result
    # it will show the total score from the user
    point=0
    while len(guess_words)!=0:
        # use to get the guesswords
        random_choice = randrange(len(guess_words))
        # Variable (count) is taken for attempts purpose
        count = 2
        while count>0:
            # all words from the input.word taking one at a time.
            print(guess_words[random_choice])
            #comparing that character with word the character in guesses and it will display
            y = str(input()).lower()
            g = guess_letter[random_choice].replace('x', y)
            # if user guessword win and the print the correct word
            if words[random_choice] == g:
                # user will win the game
                # and 'You Win' will be given as output
                print(g)
                print('good job!!!',' WIN')
                point = 1
                #print(f'Score is : {point}')
                final_result=final_result+point
                # user will get total score
                print(f'Score:: {final_result}')
                #deleting the random form the list
                del guess_words[random_choice]
                del guess_letter[random_choice]
                del words[random_choice]
                break
            else:
                var1 = user_name
                var2 = str(point)
                var3 = 'loose'
                # it will execute the query
                query = "insert into game(name,total,gametry) values ('"  + var1 + " ','" + var2 + "','" + var3 + "')"
                # it save the change
                cursor.execute(query)
                # it close the connection
                conn.commit()
                count -= 1
                # if the character doesn’t match the word
                # then “Wrong” will be given as output with 2 attempts
                if count==0:
                    # finally when we loose the game it will give 2 attempt to the correct word if not it will show like you loose the game
                    print(f'Score is : {point}')
                    print('loose','Better luck next time')
                    exit()
find_guess()
var1=user_name
var2=str(final_result)
var3='win'
#it will execute the query
query = "insert into game(name,total,gametry) values ('"  + var1 + " ','" + var2 + "','" + var3 + "')"
#it save the change
cursor.execute(query)
#it close the connection
conn.commit()
conn.close()
