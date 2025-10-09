from commands.add import add_expenses
from commands.delete import delete_expenses
from commands.list import list_expenses
def main():
  while True:
    print("CUSTOM EXPENSE TRACKER!")
    print("1. Add Expense")
    print("2. Delete Expense")
    print("3 . List Expenses")
    try:
      user_input = int(input("What is your choice? "))
      if user_input == 1:
        amount = int(input("Enter expense amount(Naira): "))
        description = input("Enter expense description: ")
        add_expenses(amount , description)
      elif user_input == 2:
        expense_id = int(input("Enter the ID of the expense you want to delete: "))
        delete_expenses(expense_id)
      elif user_input == 3:
        list_expenses
      else:
        print("Error occured: Operation not found")
    except ValueError:
      print("Error occured!")
      
    
if __name__ == "__main__":
  main()