# Imports module
import random

# Main function, shuffles names
def main():
# Counter
  count = 0
# Number of shuffle required, determines the number of shuffle to be conducted and the number of list
  num_of_shuffle = 5
  max_shuffle = False
  while count != num_of_shuffle:
      if count < num_of_shuffle:
    # Calls prompt_user function
        prompt_user()
    # adds counter
        count += 1
      else:
          max_shuffle = True
  if max_shuffle:
      print("End Cycle")
      exit()
  else:
       print("Yo want to start again? Type yes, if no, type nah")
    # gets the user response
       yow = input("Enter response: ").lower()
    # if the user want to continue using the program
       if yow == "yes":
          main()
    # if the user wants to stop
       elif yow == "nah":
           print("Have a nice day!")
     # activates  when none of the response is the following "yes" and "nah"
       else:
           print("Error")
           quit()


# The function for randomizing names and inserting into a list
def prompt_user():
# Opens text file containing names
  mane = open("Names", "r+")
# Reads text file
  sesame = mane.readlines()
# shuffles name in text file
  random.shuffle(sesame)
# Initializes a list
  items = []
# Appends List with randomized selection of names
  [items.append(x) for x in sesame if x not in items]
# for loops in initializing the list with names
  for i in sesame:
    items.append(i)
  new_items = [x[:-1] for x in items]
# Determines the amount of items in the list
  new_items = new_items[:5]
# prints list with names
  print(new_items)

# defines the main function
if __name__ == '__main__': main()

