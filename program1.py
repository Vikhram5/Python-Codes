# def function(numbers):
#     arr=sorted(numbers,reverse=True)
#     return arr[0]

# numbers=[5,6,1,2,3]
# val=function(numbers)
# print(val)

#-----------#


#factorial of a number

# def fact(n):
#     if(n<=1):
#         return n
#     return n*fact(n-1)

# val=fact(5)

# print(val)




# filter out strings that are palindrome

# def fun(word):
#     n=len(word)
#     word=word.lower()
#     for i in range(n//2):
#         if(word[i]!=word[n-i-1]):
#             return False
#     return True
    

# arr=["malayalam","vikhram","india","mom","water"]
# for i in range(len(arr)):
#     val=fun(arr[i])
#     print(val)

def common_elements(list1,list2):
    arr=[]
    n=len(list2)
    for i in range(n):
        if list2[i] in list1:
            arr.append(list2[i])
    return arr

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(common_elements(list1, list2))  # Output: [4, 5]

