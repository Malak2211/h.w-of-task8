
# #task1
ans = "True"

def is_sorted(list1: list[int]) -> bool:
    pass
    if not list1:
      return True
    for i in range(len(list1)-1):
          if list1[i]>list1[i+1]:
                print('list has to be sorted')
                return False
                break
    for i in list1:
        
        if i<0:
              ans=False
              print('list has to contain positive integers')
              return ans
              break
        elif len(list1)==1:
              ans=True
              return ans 
        else:
              ans=True
              return ans
    
              
        
print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([5, 4, 3, 2, 1]))
print(is_sorted([2, 2, 2, 2])) 
print(is_sorted([1])) 
print(is_sorted([]))

#task2
price_of_eachbread=3.49
num_of_bread=int(input('enter number of day old loaves: '))
def calc_bread_price(num_of_bread):
    regular=price_of_eachbread*num_of_bread
    discount=regular*0.06
    total_price=regular-discount
    return regular,discount,total_price
 
regular,discount,total_price=calc_bread_price(num_of_bread)
print('your regular price is: ',regular)
print('your discount is: ',discount)
print('your total price is: ',total_price)








    




    

