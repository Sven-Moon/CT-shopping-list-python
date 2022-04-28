listwidth = 36
def printMainMenu():
    print(f'-- Main Menu --')
    print('[1 - 9] Select a List  [C]reate New List  [D]elete List')
    print('[Q]uit')
    print('') 
                
def printListMenu(l):
    print(f'-- List Menu --')
    print('[A]dd Item  [E]dit Item  [D]elete Item')
    print('[S]hop                       Go [B]ack')
    print('') 
                

def printHeader():
    print(' My LIST '.center(listwidth, 'X'))
    print("Qty".rjust(9),"Item".rjust(20))    
    print("")
                
def printFullList(items):
    """list format: [(name, qty), ...]"""
    for item in items:
        print(f"({item['qty']})".rjust(6), f"{item['name']}".rjust(29) )
    print("")
        
def printNumberedListItems(items):
    """list format: [(name, qty), ...]"""
    for i, item in enumerate(items):
        print(f"({item['qty']})".rjust(6), f"{item['name']}".rjust(29),f"[{i+1}]" )
    print("")

def printLists(lists):
    print('~'*5, 'My Lists ', '~'*5)
    for i in range(len(lists)):
        print(f"[{i+1}] {lists[i].name} ")
    print('')
    
def printListHeader(l):
    print(f' {l.name} '.center(listwidth,'-'))
    print('Qty'.rjust(6),'Item'.rjust(23))
    
def printShoppingList(l):
    print(f' {l.name} '.center(listwidth,'-'))
    # uncollected list
    print(f" List ".center(listwidth, '-'))
    print('Qty'.rjust(6),'Item'.rjust(23))
    for i, item in enumerate(l.items):
        if not item['collected']:
            print(f"({item['qty']})".rjust(6), f"{item['name']}".rjust(29),f"[{i+1}]" )
            print('')
    # collected list
    print(f" Cart ".center(listwidth, '='))
    for i, item in enumerate(l.items):
        if item['collected']:
            print(f"({item['qty']})".rjust(6), f"{item['name']}".rjust(29),f"[{i+1}]" )
        print('')
    
def printShoppingMenu():
    print(f'-- Shopping Menu --')
    print('Enter Item Number to Mark (Un)Collected')
    print('Go [B]ack')
    print('') 
    