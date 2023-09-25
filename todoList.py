mytodolist=[]
donelist=[]
while(True):
    print("Enter command. Type 'h' for help:")
    c=input()
    if c.isdigit():
        c=int(c)
        if c in range(1,len(mytodolist)+1):
            donelist.append(mytodolist.pop(c-1))
            for i in range(len(mytodolist)):
                print(f"{i+1}) {mytodolist[i]}" )
    elif c=='q':
        if len(donelist)==0:
            print(f"Today you completed {len(donelist)} topics:")
        else:
            print(f"Today you completed {len(donelist)} topics:") 
            for i in donelist:
                print("*",i)

        print("*"*15)        
        break        
    elif c=='h':
        print("TODO LIST HELP")        
        print("Type 'q' to quit")
        print("To add a todo to the list, type it and hit enter")
        print("To complete a todo enter its number")
    else:
        mytodolist.append(c)
        for i in range(len(mytodolist)):
                print(f"{i+1}) {mytodolist[i]}" ) 

    