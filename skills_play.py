# Things you should be able to do.

number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]

# Write a function that takes a list of numbers and returns a new list with only the odd numbers.
def all_odd(number_list):
    odd_list = []
    for i in range(len(number_list)):
        if number_list[i] % 2 != 0:
            odd_list.append(number_list[i])

    return odd_list

def odd_list(number_list):
    print [item for item in number_list if item % 2 == 1]
    print ("*********************************")
odd_list(number_list)

def odd_filt(number_list):
    print(filter(lambda (x): x%2 ==1, number_list))
odd_filt(number_list)

def odd_map(number_list):
    print(map(lambda (x): x%2 == 1, number_list))

def odd_reduce(number_list):
    pass

print("right answer:")
print(all_odd(number_list))



# Write a function that takes a list of numbers and returns a new list with only the even numbers.
def all_even(number_list):
    even_list = []
    for i in range(len(number_list)):
        if number_list[i] % 2 == 0:
            print(number_list[i])
            even_list.append(number_list[i])

    return even_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    strings_longer_4 = []
    for i in range(len(word_list)):
        if len(word_list[i]) >= 4:
            strings_longer_4.append(word_list[i])

    return strings_longer_4

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(number_list):
    smallest_current = number_list[0]
    for i in range(1,len(number_list)):
        if number_list[i] < smallest_current:
            smallest_current = number_list[i]
    return smallest_current

# Write a function that finds the largest element in a list of integers and returns it.
def largest(number_list):
    largest_current = number_list[0]
    for i in range(1,len(number_list)):
        if number_list[i] > largest_current:
            largest_current = number_list[i]
    return largest_current


# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(number_list):
    halved_list = []
    for i in range(len(number_list)):
        halved_list.append(number_list[i]/2.0)
    return halved_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
# def word_lengths(word_list):
#     len_words = []
#     for i in range(len(word_list)):
#         len_words.append(len(word_list[i]))

#     return len_words

def word_lengths(word_list):
    len_words = []
    lengthwordlist = 0
    for aword in word_list:
        lengthwordlist+=1
    for i in range(lengthwordlist):
        stringcount = 0
        word = word_list[i]
        for j in word:
            stringcount += 1
        len_words.append(stringcount)
    return len_words

print(word_lengths(word_list))
assert(word_lengths(word_list) == [4, 5, 3, 4, 7, 4, 4, 5, 4, 6, 3, 4])


# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(number_list):
    summation = number_list[0]
    for i in range(1,len(number_list)):
        summation = summation + number_list[i]
    return summation
print(sum_numbers(number_list))

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(number_list):
    prod = number_list[0]
    for i in range(1,len(number_list)):
        prod = prod*number_list[i]
    return prod
print(mult_numbers(number_list))
# Write a function that joins all the strings in a 
#list together (without using the join method) and returns a single string.
def join_strings(word_list):
    joinedstring = ""
    for i in range(len(word_list)):
        joinedstring = joinedstring+word_list[i]
    return joinedstring
print(join_strings(word_list))

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(number_list):
    summation = number_list[0]
    for i in range(1,len(number_list)):
        summation = summation + number_list[i]
    mean = float(summation)/float(i+1)
    return mean
print(average(number_list))