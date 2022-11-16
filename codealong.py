# this is comment

"""_summary_
    This is 
    a multi line comment
"""

# print("some sting:", "another string")

# my_first_variable = 5
# print("our varaible:", my_first_variable)

# this_is_none=None

# if this_is_none:
#     print("will not hit this")
# else:
#     print("will hit this")
    
# # boolean

# is_true=True
# is_false=False

# print("this is a boolean:", is_true)

# # numbers

# an_int = 32
# a_float = 1.8675
# a_complex = 15+4j

# print("int: ", an_int)
# print("float: ", a_float)
# print("complex: ", a_complex)

# print("complex addition complex(15+4j): ", a_complex +5 +6j)

# print("int / float", 15/5.0)
# print("int / int", 15/5)
# print("int // int", 15//2)

# # how we did below in javascript: Math.pow(2, 4) = 16 

# print("raising to exponent:", 2 ** 999)

# # strings

# card1="ace of SPADES"
# card2='king of hearts'

# print("split card 1: ", card1.split(' '))
# print("index test: ", "qqxzzz".index("x"))
# print("uppercase and lowercase:", card1.lower())

# print("is Egg inside of 'green eggs and ham':", "egg" in "green eggs and ham")

# # string.length

# print("length test: ", len(card2))

# print("get last letter: ", 'my code rules'[-1])
# print("get string from location 3-7:", 'my code rules'[3:7])
# print("reverse string:", 'my code rules'[::-1])
# print("take every other character:", 'my code rules'[::-7])

# # /
# # *
# # +
# # -
# # **
# # %
# # +=
# # -=
# # *=
# # /=
# # **=

# # boolean operators

# #  these are not in python === !==, ! || &&

# # ==
# # !=
# # not
# # and
# # or

# b_false=False
# b_true=True

# if not b_false and b_true:
#     print("this shouln't show")
# else: 
#     print(" should show this")

# # list(arrays)

# arr = [1,2,3]

# print(len(arr))

# five_trues=[0] * 5
# print("five trues", five_trues)

# str_arr=['a', 'cb', 'texas']
# print("get last item of list:", str_arr[-1])

# one_to_ten = list(range(10))
# print(one_to_ten)

# a=[1, 23, 12, 99, 82]
# a.sort()
# print("sorted array", a)

# a.append(42)

# print(a)

# result=a.pop()
# print(result)
# print(a)

# a.insert(3, 123)
# print(a)

# a.append(42)

# if 42 in a:
#     print("42 is inside of list a")
    
# # help(list)
# name_field="name"

# person = {
#     "key": "value",
#     name_field: "John",
#     "age": 35 
# }

# print(person[name_field])

# # type casting

# print(int("42"))
# print(str(42))
# print(bool(42))
# print(bool(0))
# print(bool("something"))
# print(float(42))


# # string interpolations

# # `${}`


# something="test"

# print(f"this is my f-string: {something}")

# # if() {} else if() {} else {}

# vip=True
# food_place="busy"

# if food_place == "full" and not vip:
#     print("sorry we have no room")
# elif food_place == "busy" and not vip:
#     print("please wait 10 minutes")
# else:
#     print("welcome, come have a seat")
    
# # tuples

# tuple = ("fireman", "fire department")
# job_title, office = tuple

# print(" our job title: ", job_title)
# print(" our office: ", office)
# # good way with tuples
# def divide_mod(numerator, denominator):
#     division = numerator // denominator
#     mod = numerator % denominator
#     return (division, mod)


# num_groups, left_over = divide_mod(11, 4)

# # bad way without tuples
# def name_fn(num, den):
#     div = num // den
#     mod = num % den
#     return {
#             "div": div,
#             "mod": mod
#             }
# result = name_fn(11, 4)

# result["div"]


# print(" num group: ", num_groups)
# print(" left over: ", left_over)

