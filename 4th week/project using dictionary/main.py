import bankcore
import accounts

def main():
    print("Welcome to ABC Bank")
    
    while True:
        print("\n1.--- Create Account ---")
        print("2. login")
        print("3. deposit")
        print("4. withdraw")
        print("5. check balance")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter name: ")
            password = input("Enter password: ")
            customer_id = bankcore.create_account(name, password)

        elif choice == '2':
            customer_id = input("Enter Customer ID: ")
            name = input("Enter name: ")
            password = input("Enter Password: ")
            bankcore.login(customer_id, name, password)
            
        elif choice == '3':
            customer_id = input ('Enter customer id ')
            amount = float(input('Enter Amount to deopsit'))
            accounts.deposit(customer_id,amount)
            
        elif choice == '4':
            customer_id = input ('Enter customer id ')
            amount = float(input('Enter Amount to deopsit'))
            accounts.withdraw(customer_id,amount)
            
        elif choice == '5':
            customer_id = input ('Enter customer id ')
            balance= accounts.check_balance(customer_id)
            print('Your balance is :',balance)
        
        elif choice == '6':
            print('thank you for using ABC bank')
            break
         
        else:
            print('Invalid choice')
            
if __name__ == "__main__":
    main()
