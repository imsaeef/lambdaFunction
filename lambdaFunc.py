# its a one liner function that called lambda function.

#exmple one
# a = [[6, 14], [5, 6], [2, 23]]
# # a.sort(key=lambda x:x[0])
# a.sort(key=lambda x:x[1])
# print(a)
###############################
# #normal function
# def sum(x, y):
#     return x + y

# # convert to lamda function
# sum = lambda x, y: x + y

# print(sum(5, 5))
##############################
#mutiple input in lamda
# fullName = lambda firstName, lastName: firstName.strip().title() + " " + lastName.strip().title()
# print(fullName(" Hey", "SAEEF"))

#quadratic function
def build_quadratic_function(a, b, c):
    """Return the lambda function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))