#1. PROGRAM TO PRINT TABLE OF A NUMBER: 
n = int(input("Enter a number : "))
for i in range(n,n*10+1,n):
    print(i)

#2. PROGRAM TO PRINT THE REVERSE TABLE OF A NUMBER:
n = int(input("Enter a number = "))
for i in range(n*10,n-1,-n):
    print(i)

#3. PROGRAM TO PRINT THE OUTCOMES OF 2 ROLLING DICES WITH DIFFERENT SEPARATIONS
#-->(a) SEPARATION 
for i in range(1,7):
    print('*'*5)
    for j in range(1,7):
        print(i,j)
#-->(b) SEPARATION 
for i in range(1,7):
    for j in range(1,7):
        print(i,j)
        print('*'*5)
#-->(c) SEPARATION 
for i in range(1,7):
    for j in range(1,7):
        print(i,j)
    print('*'*5)
#-->(d) SEPARATION 
for i in range(1,7):
    for j in range(1,7):
        print(i,j)
print('*'*5)

#4. PROGRAM TO PRINT ALL THE DICE OUTCOMES WHERE SUM > 10
for i in range(1,7):
    for j in range(1,7):
        if (i+j>10):
            print(i,j)

#5. PROGRAM TO PRINT THE PROBABILITY OF OUTCOMES WHERE SUM OF THE DICES IS = 10
count = 0 
for i in range(1,7):
    for j in range(1,7):
        if(i+j == 10):
            print(i,j)
            count=count+1 
print("Probability =",round((count*100/36),2),"%")

#6. PROGRAM FOR PROBABILITY OF ALL THE SUMS WHEN ROLLING TWO DICES USING FOR LOOP
for k in range(2,13):
    count = 0
    for i in range(1,7):
        for j in range(1,7):
            if(i+j == k):
                count=count+1 
    print("Probability of getting sum as",k,"is",round((count*100/36),2),"%")

        
          