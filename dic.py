directory = {"sasha":"10/10","Cayman":"6/10","alana":"10/10"}
def search(name):
    print(directory[name])
def add(name, rate):
    directory[name] = rate
    print(directory)
def delete(name):
    del directory[name]
    print(directory)


answer = input("add or kill or search? ")
if answer == "kill":
    answer = input("who needs to die? ")
    delete(answer)
elif answer == "add":
    answer1 = input("who do you wanna add? ")
    answer2 = input("rate em")
    add(answer1, answer2)
elif answer == "search":
    answer= input("who do you wanna see rated? ")
    search(answer)

    
                  
