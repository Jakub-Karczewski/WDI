import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_many(numbers): 
    if len(numbers) == 1:
        return numbers[0]
    
    res = gcd(numbers[0], numbers[1]) # gcd operation is associative, in contrary to lcm
    for i in range(2, len(numbers)):
        res = gcd(res, numbers[i])
    return res


def gcd_naive(numbers):
    min_number = float('inf')
    for x in numbers:
        min_number = min(min_number, x) # we need to find teh smallest number, because gcd cannot be larger than that
    
    for k in range(min_number, 0 , -1): # we try every possible option from our smallest number down to 1
        flag = True
        for x in numbers:
            if x % k != 0:
                flag = False
                break
        if flag:
            return k
        
for nums in [[12, 15, 9], [100, 75, 50], [17, 19, 23], [20, 30, 40, 50], [random.randint(20, 100) * 2 * 7 for _ in range(10)]]:
    print(gcd_many(nums))
    print(gcd_naive(nums) == gcd_many(nums))