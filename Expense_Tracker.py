
def add_expense(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

expenses = []

def print_expenses(expenses):
    for expense in expenses:
        pass

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    





def main():
    expenses = []
    while True: 
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            amount = input('Enter amount: ')
            category = input('Enter category: ')
            add_expense(expenses, amount, category)
        elif choice == '2':
            print('\nAll Expenses: ')
            print_expenses(expenses)
            print('\nTotal Expenses: ', total_expenses(expenses))
            elif choice == '4':
            category = input('Enter category to filter: ')
            print(f"\nExpenses for {catergory}:")
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
            print('Exiting the program.')
            break

main()





