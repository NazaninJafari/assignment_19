import random

user_score = 0
cp1_score = 0
cp2_score = 0

i = 0
while i<=5:
    print('1.✋🏻  or  2.🤚🏻')
    user_choice = int(input('Enter your choice: '))

    cp1_choice = random.randint(1,2)
    cp2_choice = random.randint(1,2)
    i+=1

    if user_choice == cp1_choice and cp1_choice != cp2_choice :
        cp2_score += 1
    elif cp1_choice == cp2_choice and cp1_choice != user_choice:   
        user_score += 1
    elif user_choice == cp2_choice and user_choice != cp1_choice:
        cp1_score += 1   
    elif user_choice == cp1_choice == cp2_choice:
        pass      
    
    print(f'user_score: {user_score} \ncampioter 1 score: {cp1_score} \ncampioter 2 score: {cp2_score}') 
    print('------------------')    

if user_score > cp1_score and user_score > cp2_score:
    print('you won!')
elif user_score == cp1_score and user_score > cp2_score:
    print('you and campoiter 1 are equal!')     
elif user_score == cp2_score and user_score > cp1_score:
    print('you and campoiter 2 are equal!')
elif cp1_score > user_score and cp1_score > cp2_score:
    print('campioter 1 won!')
elif cp2_score > user_score and cp2_score > cp1_score:
    print('campioter 2 won!')    
            