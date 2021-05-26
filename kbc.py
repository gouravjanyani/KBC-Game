from ctypes import pointer
from questions import QUESTIONS
import random


def isAnswerCorrect(question, answer):

    '''
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if answer == question["answer"] else False      #remove this


def lifeLine(ques):

    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''
    answer = ques["answer"]
    #option_ans = f"option{answer}"

    if answer ==  1 :
        List1 = [f'Option 2: {ques["option2"]}' ,
                    f'Option 3: {ques["option3"]}' ,
                        f'Option 4: {ques["option4"]}' ]
        print('\t\t\t'+"".join(random.choices(List1)))
        print(f'\t\t\tOption 1: {ques["option1"]}')
        ans = input('Your choice  :')
        
        
    if answer ==  2 :
        List2 = [f'Option 1: {ques["option1"]}' ,
                    f'Option 3: {ques["option3"]}' ,
                        f'Option 4: {ques["option4"]}' ]
        print(f'\t\t\tOption 2: {ques["option2"]}')
        print('\t\t\t'+"".join(random.choices(List2)))
        ans = input('Your choice  :')
        
        
    if answer ==  3 :
        List3 = [f'Option 2: {ques["option2"]}' ,
                    f'Option 1: {ques["option1"]}',
                        f'Option 4: {ques["option4"]}' ]
        print(f'\t\t\tOption 3: {ques["option3"]}')
        print('\t\t\t'+"".join(random.choices(List3)))
        ans = input('Your choice  :')
        
        
    if answer ==  4 :
        List4 = [f'Option 2: {ques["option2"]}' ,
                    f'Option 3: {ques["option3"]}' ,
                        f'Option 1: {ques["option1"]}' ]
        print(f'\t\t\tOption 4: {ques["option4"]}')
        print('\t\t\t'+"".join(random.choices(List4)))
        ans = input('Your choice  :')
        

    if isAnswerCorrect(ques, int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print(f'Total Money Won : Rs.{ques["money"]}')
            if ques["money"] == 10000 :
                print("Congratulations you crossed : The First Level") 
            if ques["money"] == 320000 :
                print("Congratulations you crossed : The Second Level") 
            print('\nCorrect !')
            return True

    else:
            # end the game now.
            # also print the correct answer
            Option_number = ques["answer"]
            print('Oops!! This is an INCORRECT OPTION')
            print(f'CORRECT OPTION is {ques[f"option{Option_number}"]}')
            #print('\nIncorrect !')
            if ques["money"] <= 10000:
                print(f'Total Money Won : Rs.0')
            elif ques["money"] > 10000 and ques["money"]<= 320000:
                print(f'Total Money Won : Rs.10000')
            elif ques["money"] > 320000 and ques["money"] <= 10000000:
                print(f'Total Money Won : Rs.320000')
            return False
            
        
        
    





def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
    print("--------------------Welcome to Kaun Banega Crorepati--------------------")
    lifeline = 0
    pointer = 0
    while pointer < 15:
        print(f'\tQuestion 1: {QUESTIONS[pointer]["name"]}' )
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[pointer]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[pointer]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[pointer]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[pointer]["option4"]}')
        
        if lifeline == 0 :
            print(f'To Avail 50-50 LifeLine , Insert : "LifeLine"')

        ans = input('Your choice ( 1-4 ) :')
        
        if  ans.lower() == "quit" :
            if pointer == 0 :
                print(f'YOU QUIT THE GAME - MONEY YOU WON : Rs.0') 
            else:
                print(f'YOU QUIT THE GAME - MONEY YOU WON : Rs.{QUESTIONS[pointer-1]["money"]}')            
            break

        if  ans.lower() == "lifeline" and lifeline == 0   :
            flag = lifeLine(QUESTIONS[pointer])
            lifeline += 1
            if flag == True:
                pointer += 1
                continue
            else: 
                break
            
            
        elif  ans.lower() == "lifeline" and lifeline != 0   :
            print("Your Lifeline is exhausted")
            print("Penalty : YOU LOST")
            print("Play again")
            break



        # check for the input validations

        if isAnswerCorrect(QUESTIONS[pointer], int(ans) ):
            # print the total money won.
            # See if the user has crossed a level, print that if yes
            print(f'Total Money Won : Rs.{QUESTIONS[pointer]["money"]}')
            if QUESTIONS[pointer]["money"] == 10000 :
                print("Congratulations you crossed : The First Level") 
            if QUESTIONS[pointer]["money"] == 320000 :
                print("Congratulations you crossed : The Second Level") 
            print('\nCorrect !')

        else:
            # end the game now.
            # also print the correct answer
            Option_number = QUESTIONS[pointer]["answer"]
            print('Oops!! This is an INCORRECT OPTION')
            print(f'CORRECT OPTION is {QUESTIONS[pointer][f"option{Option_number}"]}')
            #print('\nIncorrect !')
            if QUESTIONS[pointer]["money"] <= 10000:
                print(f'Total Money Won : Rs.0')
            elif QUESTIONS[pointer]["money"] > 10000 and QUESTIONS[pointer]["money"]<= 320000:
                print(f'Total Money Won : Rs.10000')
            elif QUESTIONS[pointer]["money"] > 320000 and QUESTIONS[pointer]["money"] <= 10000000:
                print(f'Total Money Won : Rs.320000')
            break

        pointer += 1

    # print the total money won in the end.


kbc()
