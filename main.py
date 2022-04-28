import  time, os
from ShoppingList import ShoppingList
clear = lambda: os.system('cls')
import print as p

def main():
    sList = ShoppingList("default")   
    lists = [sList]  
    while True:
        clear()
        p.printLists(lists)
        p.printMainMenu()
        ans = input('What next?: ').lower()
        if ans in ['q', 'quit']:
            break
        if ans in '123456789' and int(ans) in range(len(lists)+1):
            listMenu(lists[int(ans)-1])
        elif ans == 'c':
            if len(lists) == 9:
                print('Sorry, you must pay a huge monthly subscription fee for access to more than 9 lists.')
                time.sleep(2)
            else:
                lists.append(ShoppingList(createList()))
        elif ans == 'd':
            lists = deleteList(lists)
        else:
            print('\nInput not recognized')
            time.sleep(2)
          
          
def listMenu(sList):
    while True:
        clear()
        p.printListHeader(sList)
        p.printFullList(sList.items)
        p.printListMenu(sList)
        ans = input('What Next? ').lower()
        if ans in ['b','back']:
            break
        if ans == 'a':
            addItem(sList)
        if ans == 'e':
            editItem(sList)
        if ans == 'd':
            deleteItem(sList)
        if ans == 's':
            shop(sList)
      
def editItem(sList):
    clear()
    p.printListHeader(sList)
    p.printNumberedListItems(sList.items)
    item_num = int(input('Edit which item? '))
    if item_num in range(len(sList.items)+1):
        name = str(input(f"Item name [{sList.items[item_num-1]['name']}]: ") or sList.items[item_num-1]['name'])
        try: 
            qty = int(input(f"Quantity [{sList.items[item_num-1]['qty']}]: ") or sList.items[item_num-1]['qty'])
        except:
            print('Invalid Input. Setting quantity to 1. [E]dit if this is incorrect.')
            time.sleep(2)            
            qty = 1
        sList.items[item_num-1]['name'] = name
        sList.items[item_num-1]['qty'] = qty
        print(f"{sList.items[item_num-1]['name']} updated")
        time.sleep(2)
    else:
        print("{item_num} isn't a valid selection")
        time.sleep(2)
def deleteItem(sList):
    clear()
    p.printListHeader(sList)
    p.printNumberedListItems(sList.items)
    del_item = int(input('DELETE which item? '))
    if del_item in range(len(sList.items)+1):
        del_item_name = sList.items[del_item-1]['name']
        confirm = input(f"Are you sure you want to DELETE {del_item_name}? (y/n): ")
        if confirm in ['y', 'yes']:
            sList.items.pop(del_item-1)
            print(f"{del_item_name} deleted")
            time.sleep(2)
        else:
            print('No deleting, then')
            time.sleep(1)
    else:
        print("{del_item} isn't a valid selection")
        time.sleep(2)    
    
def addItem(sList):
    clear()
    print(f'--- Add New Item to: {sList.name}')
    item = { "collected": False }
    item['name'] = str(input(f"Item name: "))
    try:
        item['qty'] = int(input(f"Quantity: "))
    except:
        print('Invalid Input. Setting quantity to 1. [E]dit if this is incorrect.')
        time.sleep(2)
        item['qty'] = 1
    if item['qty'] < 0:
        print(f"Assuming you meant {-item['qty']}... silly.")
        item['qty'] = -item['qty']
        time.sleep(2)
    sList.items.append(item)
def shop(sList):
    while True:
        clear()
        print(f'l of items = {len(sList.items)}')
        p.printShoppingList(sList)
        p.printShoppingMenu()
        ans = input('[Item #] or [B]: ')
        if ans in ['b', 'B']:
            break
        else:
            try:
                if int(ans) in range(len(sList.items)+1):
                    sList.items[int(ans)-1]['collected'] = not sList.items[int(ans)-1]['collected']
                else:
                    print(f"{ans} isn't one I recognize.")
                    time.sleep(2)
            except:
                print(f"Didn't recognize {ans} as valid input. Try again.")
                time.sleep(2)
    


def createList():
    return input('What is the name of your new list? ')
def deleteList(lists):
    
    deleteList = int(input('Which list did you want to delete? '))
    
    try:
        confirm = input(f"You're sure you want to delete {lists[deleteList-1].name}? Type the name of the list to confirm [{lists[deleteList-1].name}] ")
    except:        
        print("That wasn't one of the choices")
        time.sleep(2)
        return lists
    if confirm == lists[deleteList-1].name: 
        lists.pop(deleteList-1)
        return lists
    else:
        return lists
    
            
main()