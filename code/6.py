nos=int(input())
if nos%4==0:
        if nos%100==0:
            if nos%400==0:
                print("Yes")
            else:
                print("No")
        else:       
            print("Yes")
else:
    print("No")
