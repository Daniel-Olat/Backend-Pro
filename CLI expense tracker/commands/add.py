from .utils import read_expenses , write_expenses 
from datetime import datetime 


def add_expenses(amount , description ):
  if amount <= 0:
    print("Amount must be greater than zero!")
    return 
  
  try:
    amount = float(amount)
    
    
  except ValueError:
    print("Please Enter valid amount!")
    return 
  
  expenses = read_expenses()
  if expenses is None:
    expenses = []
  if not expenses:
    expense_id = 0
  else:
    expense_id = expenses[-1]['id'] + 1
  expenses.append({
    'id': expense_id,
    'amount': amount,
    'description': description,
    'date': datetime.now().isoformat()
  })
  write_expenses(expenses)
  print(f"Expense of {amount} added successfully!")
  return