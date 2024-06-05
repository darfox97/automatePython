# It says: "I assert that the condition holds true, and if not, there is a bug somewhere, so immediately stop the program.”
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
assert ages[0] <= ages[-1]  # Assert that the first age is <= the last age.
# Si assert devuelve False, mostrará error:
ages.reverse()
assert ages[0] <= ages[-1]

# Unlike exceptions, your code should not handle assert statements with try and except;
# if an assert fails, your program should crash.
