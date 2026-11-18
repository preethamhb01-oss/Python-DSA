#day 2 of dsa 

#Q1. Sum of List Elements

l = [10 , 20, 30, 40 , 50 ]
sum = 0

for i in l :
    sum+=i
    
print(f"Sum of the List is : {sum}")


#Q2. find the second-largest unique number without using sort() or max().

numbers = [12, 45, 23, 67, 45, 89, 67]
numbers.sort()


high = numbers[0]
second = 0

for i in numbers:
    if i>high :
        second = high
        high = i
        
print(second)

#Q3. Count how many even and odd numbers are present in a list.
numbers = [11, 20, 33, 42, 55, 60, 71, 88]

odd=[]
even=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
        
        
print(f"odd list : {odd}")
print(f"even list : {even}")
        
print(f"odd numbers count is : {len(odd)}")
print(f"even numbers count is : {len(even)}")

#Q4. Reverse a List Without Using reverse()
numbers = [1, 2, 3, 4, 5]

reverselist=[]

i =4
while i >=0:
    reverselist.append(numbers[i])
    i-=1
    
print(f"reverse sorted list : {reverselist}")
    
    
        
    