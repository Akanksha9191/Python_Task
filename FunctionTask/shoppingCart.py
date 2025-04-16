# shopping cart application
# add, remove, total item

shopping_list =[]

def addItem():
    size = int(input('How many items do you want to add?'))
    print('Enter Items: ')
    for i in range(size):
        item = input()
        
        if item:
            shopping_list.append(item)
            print(f'Added Item: {item}')
        else:
            print('Empty')

def removeItem(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'Remove item list: {shopping_list}')
    else:
        print('Item in not list')
        
def total_item():
    print(f'Total item in cart {len(shopping_list)}')
    
def show_menu():
    print("______________Shopping cart____________")
    print('1. Add Item')
    print('2. Remove Item')
    print('3. Total Item') 
    
def main():
    while True:    
        show_menu()
        
        option = int(input('Enter your choice: '))
        
        if(option == 1):
            addItem()
        elif(option ==2):
            item = input('Enter remove item: ')
            removeItem(item)
        elif(option==3):
            total_item()
            break
        else:
            print('Invalid option.')
    

   
if __name__ == '__main__':
    main()