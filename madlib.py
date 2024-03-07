# STRING CONCATENATION
# string to be created is "Subscribe to ____"
# a string variable: youtuber = "Kunjan Patel"
# 3 Ways to concatenate String:
# 1) print("Subscribe to " + youtuber)
# 2) print("Subscribe to {}".format(youtuber))
# 3) print(f"subscribe to {youtuber}")

adjective = input("Adjective: ")
verb1 = input("Verb : ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adjective}. It makes me so excited all the time because \
    I love to {verb1}. Stay hydrated and {verb2}, you are {famous_person}"

print(madlib)