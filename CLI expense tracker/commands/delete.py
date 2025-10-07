from .utils import read_expenses , write_expenses

def delete_expenses(expense_id):
  expenses = read_expenses
  if not expenses:
    print("No expenses found!")
    
  if not any (expense['id'] == expense_id for expense in expenses):
    print(f"Expense ID:{expense_id} not found")
    return 
  
  expenses = [expense for expense in expenses if expense['id'] != expense_id]
  
  write_expenses(expenses)
  print(f"Expense with ID {expense_id} has been deleted succesfully")
  