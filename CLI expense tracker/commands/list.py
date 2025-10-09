from .utils import read_expenses, write_expenses 
from datetime import datetime

def list_expenses():
  expenses = read_expenses
  if not expenses:
    print("No Expenses found!")
  else:
    for expense in expenses:
      print(f"{expense['description']} : {expense['amount']} : {expense['date']}")
  return