        ### Python 101 manual

    ## Variables and data types

#character_name = "John"#
#character_age = "50"#
#is_male = False#
#print("There once was a man named " + character_name + ", ")#
#print("he was " + character_age + " years old ")#


    ## Working with strings

    #print("The umbrella\nAcademy")

#phrase = "The umbrella Academy"
#print(phrase + " is cool")
#print(phrase.upper())


    ## Working with numbers

#print(-2.524)
#print(3*(4+5))
#print(10%3)

#my_num = 5
#print(str(my_num) + " is my favourite number")
#print(pow(my_num, 2))
#print(max(4, 6))
#print(round(3.66))

#from math import *
#print(sqrt(36))


    ## Getting Input from users

#name = input("Enter your name: ")
#age = input("Enter your age: ")

#print("Hello " + name + "! You are " + age)


    ## Building a basic calculator

#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)

#print(result)


    ## Mad Libs Game

#color = input("Enter a color ")
#plural_noun = input("Enter a plural noun ")
#celebrity = input("Enter a celebrity ")

#print("Roses are " + color)
#print(plural_noun + " are blue")
#print("and I love " + celebrity)


    ## Lists

#friends = ["Kevin", "Karen", "Jim"]
                        
#print(friends[0:1])
#print(friends[1:])


    ## Lists Functions

#lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Kevin", "Karen", "Jim", "Oscar", "Toby"]
#friends.extend(lucky_numbers)
#friends.append("Creed")
#friends.insert(1, "Kelly")
#friends.remove("Jim")
#friends.pop()
#friends.index("Kevin")
#friends.sort()
#lucky_numbers.sort()
#lucky_numbers.reverse()

#friends2 = friends.copy()

#print(friends)
#print(lucky_numbers)
#print(friends.count("Kevin"))

#print(friends2)


    ## Tuples

#coordinates = [(4, 5), (6, 7), (80, 34)]
#print(coordinates[0])


    ## Functions = def

#def say_hi(name, age):
    #print("Hello " + name + ", you are " + age)

#say_hi("Tom", "20")
#say_hi("Steve", "35")


    ## Return statement

#def cube(num):
    #return num*num*num

#result = cube (4)
#print(result)


    ## If statements

#is_male = False
#is_tall = True

#if is_male or is_tall:
    #print("You are a male or tall or both")
#else:
    #print("You are neither male or tall")

#if is_male and is_tall:
    #print("You are a tall male")
#elif is_male and not(is_tall):
    #print("You are a short male")
#elif not(is_male) and is_tall:
    #print("You are not a male but you are tall")
#else:
    #print("You are not male or not tall")


    ## If statements & comparisons (<=, >=, ==, !=, <, >, =<, =>)

#def max_num(num1, num2, num3):
    #if num1 >= num2 and num1 >= num3:
        #return num1
    #elif num2 >= num1 and num2 >= num3:
        #return num2
    #else:
        #return num3

#print(max_num(3, 4, 5))


    ## Building a better calculator

#num1 = float(input("Enter first number: "))
#op = input("Enter operator: ")
#num2 = float(input("Enter second number: "))

#if op == "+":
    #print(num1 + num2)
#elif op == "-":
    #print(num1 - num2)
#elif op == "/":
    #print(num1 / num2)
#elif op == "*":
    #print(num1 * num2)
#else:
    #print("Invalid operator")


    ## Dictionaries

#monthConversions = {
    #"Jan": "January",
    #"Feb": "February",
    #"Mar": "March",
    #"Apr": "April",
    #"Jun": "June",
    #"Jul": "July",
    #"Aug": "August",
    #"Sep": "September",
    #"Oct": "October",
    #"Nov": "November",
    #"Dec": "December",
#}

#print(monthConversions["Nov"])
#print(monthConversions.get("Dec"))
#print(monthConversions.get("Luv", "Not a valid key"))


    ## While loops

#i = 1
#while i <= 10:
    #print(i)
    #i += 1

#print("Done with loop")


    ## Building a game

#secret_word = "Giraffe"
#guess = ""
#guess_count = 0
#guess_limit = 3
#out_of_guesses = False

#while guess != secret_word and not(out_of_guesses):
    #if guess_count < guess_limit:
        #guess = input("Enter guess: ")
        #guess_count += 1
    #else:
        #out_of_guesses = True

#if out_of_guesses:
    #print("Game over")
#else:
    #print("You win")


    ##