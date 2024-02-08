# Python Strings

#________________________________________________________________________________________________________
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

z = "I want to hunt"
c = "deer"

# print(z + c) # no space error

# print(z + "6" + c) # no space error

# print(z + " " + c) # good


#________________________________________________________________________________________________________

# Strings are Arrays


#refer to lines 26-29

# print(g[0])

# print(g[1])

# print(g[2])

# print(g[2:6]) # when slicing strings, the second index is also included compared to list arrays

# print(g[0:23])

# print(g[24:])


#________________________________________________________________________________________________________

# Modification

firstname = "DIEGO"
lastname = "torres"


# print(firstname)
# print(lastname)

# print(firstname.lower)
# print(lastname.upper)

# print(firstname.lower())
# print(lastname.upper())

# print(firstname.capitalize())
# print(lastname.capitalize())

#------------------

sentence = "        I went home and realized I forgot everything I learned today...                   "


# print(sentence)

# print(sentence.strip()) #gets rid of all whitespace

sentence2 = "        I went home and realized I forgot everything I learned today...             well, at least I found my notes...      "

# print(sentence2.strip())

#------------------

hello = "Hello, Herald"

# print(hello)

# print(hello.replace("H", "J"))

#------------------

google = "www.google.com"

# print(google)

# print(google.replace("www.", ""))

# print(google.replace(".com", ""))

# print(google.replace("www.", "").replace(".com", ""))

#------------------

splitting = "I like Python, the language."

# print(splitting)

# print(splitting.split())

# print(splitting.split(","))

# print(splitting.split("."))

#------------------

# Formatting