s=int(input())
temp=s
r=0
if s<=1000:
    while temp!=0:
        r=(r*10)+(temp%10)
        temp=temp//10
if s==r:
            print("yes")
else:
            print("not")
