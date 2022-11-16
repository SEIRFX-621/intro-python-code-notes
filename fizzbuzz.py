def fizzbuzz(num):
    '''number divisble by 3 return fizz, divisble by 5, return buzz
    and divisible by 3 and 5 return fizzbuzz, if no condition is met,
    return the number'''
    print('this is a fizzbuzz problem')
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num

print('answer for 3', fizzbuzz(3))
print('answer for 15', fizzbuzz(15))
print('answer for 10', fizzbuzz(10))
print('answer for 7', fizzbuzz(7))