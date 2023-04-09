import random
import math
from art import logo
from replit import clear
def calculate_score(cards):
    if(sum(cards)==21 and len(cards)==2):
        return 0
    if(sum(cards)>21 and 11 in cards):
        cards.remove(11)
        cards.append(1)
    return sum(cards)
############### Our Blackjack House Rules #####################
def deal_card():
    cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    chosen_card=random.choice(cards)
    return chosen_card
user_card=[]
dealer_card=[]

for _ in range(2):
    user_card.append(deal_card())
    dealer_card.append(deal_card())
def compare(user_mark,computer_mark):
    #Correcting a bug
    if(user_mark>21 and computer_mark>21):
        print("You Lose")
    elif(user_mark==computer_mark):
        print("Draw")
    elif(computer_mark==0):
        print("You Lose, Opponent has Blackjack")
    elif(user_mark==0):
        print("You Win with blackjack")
    elif(user_mark>21):
        print("You went over, You Lose")
    elif(computer_mark>21):
        print("Opponent went over, You Win")
    elif (user_mark>computer_mark):
        print("You Win")
    else:
        print("You Lose")
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calc_score(list_cards):
    return sum(list_cards)
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

def play_game():
    print(logo)
    is_game_over=False
    while not is_game_over:
        user_score=calculate_score(user_card)
        computer_score=calculate_score(dealer_card)
        print(f"User Cards : {user_card}, current score : {user_score}")
        print(f"Computer's first card : {dealer_card[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if(user_should_deal=='y'):
        
                user_card.append(deal_card())
            else:
                is_game_over=True
 
    # sum_my_deck=0
    # sum_dealers_deck=0
    
    # for ch in range(0,2):
    #     my_deck.append(random.choice(cards))
    #     dealers_deck.append(random.choice(cards))
    #     sum_my_deck+=my_deck[ch]
    #     sum_dealers_deck+=dealers_deck[ch]
    # to_continue=True
    # while to_continue==True :
        
    #     whether_continue=input("Type 'y' to get another card, type 'n' to pass : ")
    #     if(whether_continue=='y'):
    #         to_continue=True
    #     elif(whether_continue=='n'):
    #         to_continue=False
    #     print(f"Your Cards : {my_deck} , Current score is : {sum_my_deck}")
    #     print(f"Computer's first card : {dealers_deck[0]}")
    #     if(sum_my_deck==21 and sum_dealers_deck<21):
    #         print("You Win 😃")
    #         break
    #     elif(sum_my_deck<21 and sum_dealers_deck==21):
    #         print("You Lose 😤")
    #         break
    #     elif(sum_my_deck==21 and sum_dealers_deck==21):
    #         print("Draw 🙃")
    #         break
        
    #     if to_continue == True :
        
    #         card_chosen=random.choice(cards)
    #         my_deck.append(card_chosen)
    #         sum_my_deck+=card_chosen
            
            
            
        
        
    #     elif to_continue == False:   
    #         card_chosen=random.choice(cards)
    #         dealers_deck.append(card_chosen)
    #         sum_dealers_deck+=card_chosen
    #         if(sum_dealers_deck<=21): 
    #             if(sum_dealers_deck==sum_my_deck):
    #                 print("Draw 🙃")
    #                 to_continue=False
    #             elif(sum_dealers_deck<sum_my_deck):
    #                 print("You win 😃")
    #                 to_continue=False
    #             else:
    #                 print("You lose 😤")
    #                 to_continue=False
    #         else:
    #             print(f"Your final hand : {my_deck} , Final score is : {sum_my_deck}")       
    #             print(f"Computer's final hand : {my_deck} , Final score is : {sum_my_deck}")     
    #             print("Opponent Went Over . You win 😃")
    #             to_continue=False
                
    # print("Thank You !!!")   
    while(computer_score<17 and computer_score!=0):
        dealer_card.append(deal_card())
        computer_score=calculate_score(dealer_card)
    print(f"Your final hand is : {user_card} and final score is : {user_score}")
    print(f"Computer's final hand is : {dealer_card} and final score is : {computer_score}")  
    compare(user_score,computer_score)  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n' :")=='y':
    clear()
    play_game()
    
    
