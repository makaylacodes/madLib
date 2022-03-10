# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to ___"



adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famousPerson = input("Famous Person: ")

madlib = f"Hello {adj} I hope that you can {verb1} today. \n Take Joane to {verb2} so she can be like {famousPerson}"

print(madlib)