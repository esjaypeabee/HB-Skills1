# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    newlist = []
    for item in number_list:
        if item %2 == 1:
            newlist.append(item)
    return newlist

#print all_odd(number_list)

# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    newlist = []
    for item in number_list:
        if item %2 == 0:
            newlist = newlist + [item]
    return newlist

#print all_even(number_list)

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    newlist = []
    for word in word_list:
        if len(word) >= 4:
            newlist = newlist + [word]
    return newlist

#print long_words(word_list)


# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    mini = 0
    for num in number_list:
        if num < mini:
            mini = num
    return mini

# print smallest(number_list)


# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    maxd = 0
    for num in number_list:
        if num > maxd:
            maxd = num
    return maxd

#print largest(number_list)


# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    newlist = []
    for num in number_list:
        newlist = newlist + [float(num)/2]
    return newlist

#print halvesies(number_list)


# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lengths(word_list):
    newlist = []
    for word in word_list:
        newlist = newlist + [len(word)]
    return newlist

#print word_lengths(word_list)


# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    the_sum = 0
    for num in number_list:
        the_sum = the_sum + num
    return the_sum

#print sum_numbers(number_list)

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    the_product = 1
    for num in number_list:
        the_product = the_product * num
    return the_product

#print mult_numbers(number_list)

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(word_list):
    new_string = ''
    for word in word_list:
        new_string = new_string + word + ' '
    return new_string

# print join_strings(word_list)


# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    the_sum = 0
    for num in number_list:
        the_sum = the_sum + num
    return float(the_sum) / len(number_list)

print average(number_list)
