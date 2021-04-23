# 1. Join items of given list using "and" and print the string
weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
strg = ""


def convertToString(weekdays):
    global strg
    # Write your code here
    # Output:  'sun and mon and tue and ....'
    for day in weekdays:
        strg = strg + day + " and "
    strg=strg.strip(" and")
    print(strg)


# 2. count the occurrences of a particular element in the list and
#   output highest occuring element
days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']


def findMaxOccuringString(days):
    count = [1,1,1,1,1,1]
    max = 0

    # Your code here
    # Output: Mon (Since monday occurred 3 times)
    for i in range(6):
        aaa = 1
        for j in range(len(days)):
            if days[i] == days[j] and i != j:
                # print(len(days),count[i])
                aaa = aaa + 1
                count[i] = aaa
                if max < aaa:
                    day = days[i]
                    max = aaa
    print(count)
    print(day,"has occured",max,"times")


# 3. Merging dictionaries - The resultant dict must contain all items of
# both dicts. If key is common then the value of key in resultant dict
# must be the sum of value in a and b.
a = {'x': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'b': 6}


def dictMerge(a, b):
    # Your code here
    for key in a.keys():
        if key == b.keys():
            pass



# 4. Item with highest value count
items = [{'apple': 5}, {'banana': 8}, {'orange': 7}, {'grapes': 4}]


def itemWithHighestValue(items):
    max = 0
    # Your code here
    # print the fruit name whose value is maximum
    for item in items:
        for fruit,number in item.items():
            if int(number) > max:
                max = number
                ans = fruit
    print("Fruit with Maximum value is",ans)


# convertToString(weekdays)
# findMaxOccuringString(days)
itemWithHighestValue(items)
# dictMerge(a, b)



