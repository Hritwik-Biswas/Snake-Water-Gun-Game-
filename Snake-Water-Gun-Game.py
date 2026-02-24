import random

computer=random.choice([-1,0,1])

userstr = input("Enter Your Choice(s/w/g): ").lower()

userDict = {'s':-1,'w':0,'g':1}
viewDict = {-1:'Snake',0:'Water',1:'Gun'}

user = userDict.get(userstr)

if user is None:
    print("Invalid input! Please enter s, w, or g.")
    exit()

print(f'User Choose: {viewDict[user]}')
print(f'Computer Choose: {viewDict[computer]}')

if(computer==user):
    print('It is DRAW')

else:
    if(computer==-1 and user==0):
        print('Computer WIN')
    elif(computer==-1 and user==1):
        print('User WIN')
    elif(computer==0 and user==-1):
        print('User WIN')
    elif(computer==0 and user==1):
        print('Computer WIN')
    elif(computer==1 and user==-1):
        print('Computer WIN')
    elif(computer==1 and user==0):
        print('User WIN')
    else:
        print('Something Went Wrong!!! ')