import json
import os 

EXPENSES = 'expenses.json' 
 #read expenses from the json file
def read_expenses():
  if not os.path.exists(EXPENSES):
    print("File does not exist! ")
    return[]
  try:
    with open(EXPENSES , "r") as file:
      json.load(file)
  except json.JSONDecodeError:
    print("Error: file has been corrupted")
    user_input = input("Do you want to delete the corrupted file?(yes/no)").lower()
    if user_input == 'yes':
      os.remove(EXPENSES)
      print("corrupted file deleted")
    else: 
      print('Delete the corrupted file manually to continue!')
    #write expenses to the json file  
def write_expenses(expenses):
  with open(EXPENSES , "w") as file:
    json.dump(expenses , file , indent=4)
    
def get_month_text(month):
  return ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"][month - 1] if month else ""