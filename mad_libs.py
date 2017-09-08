statement=["__1__ is a bat-and-ball game played between two teams of __2__ players each on a cricket field, at the centre of which is a rectangular 22-yard-long pitch with a target called the __3__ (a set of three wooden stumps topped by two bails) at each end. Each phase of play is called an __4__ during which one team bats, attempting to score as many runs as possible, whilst their opponents field.",
                       "The __1__ massacre, also known as the Amritsar massacre, took place on __2__ 1919 when a crowd of nonviolent protesters, along with Baishakhi pilgrims, who had gathered in Jallianwala Bagh, Amritsar, Punjab, were fired upon by troops of the British Indian Army under the command of Colonel __3__. The civilians, in the majority Sikhs, had assembled to participate in the annual __4__ celebrations, a religious and cultural festival for Punjabi people and also to condemn the arrest and deportment of two national leaders",
                       "The __1__ is an arm of the Pacific Ocean defined by the curve of the southern coast of Alaska, stretching from the __2__ and Kodiak Island in the west to the __3__ Archipelago in the east, where __4__ and the Inside Passage are found.Here two oceans meet but do not Mix"]
answer=[["cricket","eleven","wickets","innings"],["jallianwala bagh","13 april","reginald dyer","baisakhi"],["gulf of alaska","alaska peninsula","alexander","glacier bay"]]
def mad_lib():
            print("welcone to this amazing game")
            level() #call to level function
def level():
    #takes input about the level from the user
        user_input=raw_input("Enter the level you want to select from\n1.Beginner\n2.Intermediate\n3.Expert\n")
        level_select=["1","2","3"]
        index=0
        flag=0
        levels = 3 #number of levels in the game
        while index<levels:
                if(user_input==level_select[index]):
                           print(statement[index])
                           flag=1
                           break
                index+=1
                 
        if(flag==0):
                print("Wrong selection!!! Please try again \n ")
                level()
        #Calls the replace function and passes the argument of the index which is selected.
        replace(index)
#To ask user for the answer and if the user enters correct answer then it replace with the blank else prompt answer once again
def replace(index):
        place=1
        temp=["","",""]
        temp[index]=statement[index]
        #maximum variable saves the number of answers. It tells how many times to reun the loop
        maximum = 4
        while place<=maximum:
                user_answer=raw_input("Enter "+str(place)+" = ")
                #Checks the condition if the answer entered by the user is correct or not
                if(user_answer==answer[index][place-1]):
                        #The below statement replaces the answer with the desired index if the answer is coorect
                        statement[index]=statement[index].replace(("_"+str(place)+"_"),answer[index][place-1])
                        print(statement[index])
                        place=place+1
                else:
                        #If the answer is wrong the 
                        print("Wrong Answer!!! Please try again \n")
        statement[index]=temp[index]
        further()
#Prompts user that if he/she wants to play the game again
def further():
        forward=raw_input("If you wish to continue forward then enter yes else enter no :- ")
        if(forward=="yes"):
                mad_lib()
        elif(forward=="no"):
                print("Thank You!!!")
        else:
                print("Wrong input!!! Please try again \n")
                further()
mad_lib()
