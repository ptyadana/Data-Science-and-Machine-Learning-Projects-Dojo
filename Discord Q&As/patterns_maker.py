""""
    1
   232
  34543
 4567654
567898765
"""
def get_odd_numbers(n):
    odd_numbers = []
    num = 1
    while len(odd_numbers) < n:
        if num%2 != 0:
            odd_numbers.append(num)
        num += 1
            
    return odd_numbers

def make_pattern_fixed():
    # starting number # 5-(1)   => 5-(2)  => 5-3  => 5-4  => 5-5
    # space           # 4       => 3      => 2    => 1    => 0
    # for innner loop # odd number (1,3,5,7,9) , number itself and maximum limit
    MY_CONSTANT = 5
    odd_numbers_list = get_odd_numbers(MY_CONSTANT)
    for x in range(1, 6):
        # space loop
        for space_loop in range(MY_CONSTANT - x):
            print(' ', end='')
            
        # number loop
        number = x
        reach_max = False
        
        for number_loop in range(odd_numbers_list[x-1]):
            print(number, end='')
            
            if number < odd_numbers_list[x-1] and reach_max == False:
                number += 1
            else:
                # restart the number
                reach_max = True
                number -= 1
        print()

def make_pattern_dynamic(n):
    """Make a patttern of tree using n numbers with Maximum n of 5.
    Example: if n = 5
        1
       232
      34543
     4567654
    567898765
    """
    # starting number # 5-(1)   => 5-(2)  => 5-3  => 5-4  => 5-5
    # space           # 4       => 3      => 2    => 1    => 0
    # for innner loop # odd number (1,3,5,7,9) , number itself and maximum limit
    
    # max check
    if n > 5:
        print('n should be less than 5.')
        return
    
    odd_numbers_list = get_odd_numbers(n)
    for x in range(1, n+1):
        # space loop
        for space_loop in range(n - x):
            print(' ', end='')
            
        # number loop
        number = x
        reach_max = False
        
        for number_loop in range(odd_numbers_list[x-1]):
            print(number, end='')
            
            if number < odd_numbers_list[x-1] and reach_max == False:
                number += 1
            else:
                # restart the number
                reach_max = True
                number -= 1
        print()
        
                
def main():
    # print(get_odd_numbers(10))
    # make_pattern_fixed()
    make_pattern_dynamic(5)
    


if __name__ == "__main__":
    main()
