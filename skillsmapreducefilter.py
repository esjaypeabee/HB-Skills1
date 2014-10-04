# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def check_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False

def all_odd(number_list):
    return filter(check_odd, number_list)


def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    return filter(check_even, number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def check_word_length(word):
    if len(word) >= 4:
        return True
    else:
        return False

def long_words(word_list):
    return filter(check_word_length, word_list)

# Write a function that finds the smallest element in a list of integers and returns it.
def is_smaller(num1, num2):
    if num1 <= num2:
        return num1
    else:
        return num2

def smallest(number_list):
    return reduce(is_smaller, number_list)

# Write a function that finds the largest element in a list of integers and returns it.
def is_larger(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2

def largest(number_list):
    return reduce(is_larger, number_list)

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halfer(num):
    return float(num)/2

def halvesies(number_list):
    return map(halfer, number_list)

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def find_word_length(word):
    return len(word)

def word_lengths(word_list):
    return map(find_word_length, word_list)

# Write a function (using iteration) that sums all the numbers in a list.
def sum2(num1, num2):
    return num1 + num2

def sum_numbers(number_list):
    return reduce(sum2, number_list)

# Write a function that multiplies all the numbers in a list together.
def mult2(num1, num2):
    return num1 * num2

def mult_numbers(number_list):
    return reduce(mult2, number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def joined(str1, str2):
    return str1 + ' ' + str2

def join_strings(word_list):
    return reduce(joined, word_list)

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    return reduce(sum2, number_list)/float(len(number_list))

