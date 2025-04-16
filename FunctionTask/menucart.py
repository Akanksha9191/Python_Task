# menu card application

def MenuList(lst):
    
    print(f"Options: \n 1. Display \n 2. Update \n 3. Delete \n 4. Add")
    option = int(input("Please Enter a option: "))
    
    while True:
        if(option==1):
            print("List =",lst)
        elif(option==2):
            lst[2] = input('Enter update element: ')
            print('Updated list = ', lst)
        elif(option==3):
            lst.remove(input('Enter delete element: '))
            print('Deleted element List=', lst)
        elif(option==4):
            lst.append(input('Enter added element = '))
            print("Added element list = ", lst)
        else:
            print("Invalid option")
        
    
def main():
    menulst = ['Dosa', 'Pizza', 'Sandwich', 'PavBhaji']
    print("Menu List = ", menulst)
    
    MenuList(menulst)
    
if __name__ == '__main__':
    main()