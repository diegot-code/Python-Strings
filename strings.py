# Python Strings

#________________________________________________________________________________________________________

# Asssigning strings to Variables
# Commonly used: everyhere and anywhere
 
print("Start of the String Intro:")

x = "Hello, World!" # good
# x = 'Hello, World?' # good

# print(x)

y = "6"

# print(y)

u = "18 chickens"

# print(u)

#------------------

k = """Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
Incidunt illo beatae nemo sit ab. Consectetur, eum adipisci. 
Omnis, eos dolorem?""" # multi-line string

# print(k)


g = '''I went to ride my bike.
I saw a beach.
I stopped to rest.
'''

# print(g)



#________________________________________________________________________________________________________

# Concatenation
# Commonly used: to combine strings together or join groups of elements


z = "I want to hunt"
c = "deer"

# print(z + c) # no space error

# print(z + "6" + c) # no space error

# print(z + " " + c) # good

# print(z, c) # better


#________________________________________________________________________________________________________

# Strings are Arrays
# Commonly used: extracting sub strings

transaction_data = "2024-02-08,12345,John Doe,Product A,29.99"

transaction_date = transaction_data[:10] 

transaction_client = transaction_data[17:25] # when slicing strings, the second index is also included compared to list arrays where it isn't

transaction_price = transaction_data[36:41]

# print("Transaction Date:", transaction_date)

# print("Transaction's User:", transaction_client ) 

# print("Transaction's Price:", "$" + transaction_price )


#________________________________________________________________________________________________________

# Modification
# Commonly used: when user credentials (firstname/lastname and password) is given

firstname = "DIEGO"
lastname = "torres"


# print(firstname)
# print(lastname)

# print(firstname.lower) # bad
# print(lastname.upper) # bad

# print(firstname.lower()) # better
# print(firstname.casefold()) # good
# print(lastname.upper()) #better

# print(firstname.capitalize())
# print(lastname.capitalize())

#------------------

circus = "weLcomE to THE CIrcUS"

# print(circus)

# print(circus.title())

circus_title = "Welcome To The Circus"

# print(circus_title.istitle())



#------------------

# True/False

username = "LunarEcho87"

passcode = "993665"

nonAscii = "I'll give you a 🌟"

empty =  "         "

name = "george maloney"




# alphanumerical- if all characters are letters and/or numbers
# print(username.isalnum())


# # alphabet- if all characters are letters
# print(username.isalpha())


# ascii- if all characters can be ascii coded
# print(nonAscii.isascii())


# digit- if all characters are numbers
# print(passcode.isdigit())



# lowercase- if all characters are lowercase, can have  numbers
# print(name.islower())


# identifer- if the entire item can identified as a variable
# print(name.isidentifier())


# whitespace- if the item only contains whitespace
# print(name.isspace())


#________________________________________________________________________________________________________
# Stripping Whitespace off strings
# Commonly used: after appending strings with no values

sentence = "        I went home and realized I forgot everything I learned today...                   "


# print(sentence)

# print(sentence.strip()) #gets rid of all whitespace

sentence2 = "        I went home and realized I forgot everything I learned today...             well, at least I found my notes...      "

# print(sentence2.strip())


#________________________________________________________________________________________________________
# Replacing Specified character groups
# Commonly used: on urls/links

hello = "Hello, Herald"

# print(hello)

# print(hello.replace("H", "J"))

#------------------

google = "www.google.com"

# print(google)

# print(google.replace("www.", ""))

# print(google.replace(".com", ""))

# print(google.replace("www.", "").replace(".com", ""))


#________________________________________________________________________________________________________
# Splitting the string into a list


splitting = "I like Python, the language."

# print(splitting)

# print(splitting.split())

# print(splitting.split(","))

# print(splitting.split("."))


#________________________________________________________________________________________________________

# Formatting

age = 28

txt = "Howdy, I'm Diego and I'm {} and come from {}" #(variable) txt: Literal['Howdy, I\'m Diego and I\'m {}']

# print(txt.format(age, "Jacksonville")) 

#------------------

age2 = 32

# txt2 = "Howdy, I'm Josh and I'm " + age2 # can't

# print(txt2)

#------------------

age3 = 26

# txt3 = ("Howdy, I'm Adam and I'm " + age3) # can't

# print(txt3)

#------------------

age4 = 45

txt4 = "Howdy, I'm George, I am" + str(age4) # can

# print(txt4)

#------------------

# Formatting using index numbers

quantity = 4

item_id = 279

price = 35.96

myorder = "I will pay {2} dollars for {0} packs of item '{1}'."

# print(myorder.format(quantity, item_id, price)) # index[0] == quantity, index[1] == item_id, index[2] == price

#------------------

# Finding the word "transformers" in the string
# Similar to the .index() method but this one does not display an error if it can't find anything

cars = "I liked that new cars movie where they transform into 'Autobots', oh yeah, the movie is called Transformers. They have a few movies but their recent one was my favorite."

# print(cars)

# print(cars.find("transformers")) # casing is important

# print(cars.find("Transformers"))

# print(cars[95])

# print(cars.find("hotdog"))