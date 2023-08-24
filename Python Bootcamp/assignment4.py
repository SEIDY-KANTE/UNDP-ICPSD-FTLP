"""
                        🚀 Frontier Tech Leaders Programme
||||||||||||||||||||||||||||||||| ASSIGNMENT 4 ||||||||||||||||||||||||||||||||||

"""

def get_guest_info(guest_name:str):

    if guest_name in guests.keys():
        return f"{guest_name} (Age:{guests[guest_name][0]}) is comming to the party! Email:{guests[guest_name][1]}"
    else:
       return f"{guest_name} is not on the guest list"

def display_guest_in_order(guests):
    print("\n=======Guests===========\n")
    sorted_by_age=sorted(guests.items(),key=lambda item: item[1])

    for key,val in sorted_by_age:
        print(f"{key}: {val}")

#1 Empty dictionary
guests={}

#2 Adding guests
guests["Alice"]=(28,"alice@email.com")
guests["Bob"]=(35,"bobmail.com")
guests["Charlie"]=(30,"charlie@email.com")

#print(guests)

#3 Updating the guests
## adding
guests["David"]=(22,"david@email.com")
## removing
del guests["Bob"]

#print(guests)

#4 Guest Information Retriever
print(get_guest_info("Bob"))
print(get_guest_info("Alice"))

#5 Guest Counter
print("Count: ",len(guests))

### Extensions: 

# Allow users to input their own guests, with the required details.
# Display guests in order of age.
# Handle the scenario where someone tries to add an existing guest. Prompt to update details or skip.

display_guest_in_order(guests) 

print("\n")

result=input("Do you want to add your own guests (Y/N) ? : ")

if result.lower()=="y":
    name=input("Enter name: ")

    if name in guests.keys():
        print("This name already exist")
        update=input("Do you want to update details (Y/N) ? :")
        if update.lower()=="y":
            print(f"Updating : {name} (Age: {guests[name][0]} Email: {guests[name][1]})")
        else:
            print("Please enter another name (key) that does not already exist!")
            exit()

    age=int(input("Age: "))
    email=input("Email: ")

    guests[name]=(age,email)

display_guest_in_order(guests) 