# Scenario
# Let's play a game. We will give you two strings: one being a word (e.g., "dog") and the second being a combination of any characters.

# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside
# the second string?

# For example:

# if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)
# Hints:

# you should use the two-argument variants of the pos() functions inside your code;
# don't worry about case sensitivity.

####################################################################################################

# Test your code using the data we've provided.

# Test data
# Sample input:

# donor
# Nabucodonosor
# Sample output:

# Yes


# Sample input:

# donut
# Nabucodonosor
# Sample output:

# No

####################################################################################################


def letrcounter(st):
    st = st.lower()
    dic = {}
    for i in st:
        dic[i] = 1 + dic.get(i, 0)
    return dic


def wordFinder(st1, st2):
    dic1 = letrcounter(st1)
    dic2 = letrcounter(st2)
    for k in dic1:
        if dic2.get(k, 0) < dic1[k]:
            return "No"

    return "Yes"


val1 = input("Enter the first word : \n")
val2 = input("Enter the second word : \n")
result = wordFinder(val1, val2)
print(result)
