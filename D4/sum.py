def calsum(n1,n2):
    print(n1+n2)
calsum(10,20) 

def sum (a=10,b=23):
    print(a+b)

sum(10,20)
sum() 

def sum(*n1):
    sum=0
    for i in n1:
        sum=sum+i 
    print("Ans is ",sum)
sum(10,20)
sum(10,20,30)
