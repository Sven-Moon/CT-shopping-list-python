import os, random

class ShoppingList:    
    def __init__(self, name) -> None:
        self.list_index = 0
        self.basket_index = 0
        self.li_max = 0
        self.items = [{
                "name": 'pickled pigs feet',
                "collected": False,
                "qty": 1
            },{
                "name": 'potted meat',
                "collected": False,
                "qty": 1
            }, {
                "name": 'toe jam',
                "collected": False,
                "qty": 1
            }
        ]
        self.list_index = 0
        # basket_index = 0
        self.name = name
            
    def addItem(self):
        while True:
            self.clear()
            name = input('Item Name: ')
            try:
                qty = int(input('How many? ') or 1) 
            except:
                print('Whole numbers only for quantities')
                time.sleep(2)
                continue
            try:
                price_ea = float(input("What's it cost? $") or 0)
            except:
                print("Try a number since that's how we measure money")
                time.sleep(2)
                continue
            item_id = random.randint(100000,999999)
            self.items[item_id] = { "name": name, "price": price_ea, "qty": qty, "collected": False }
            
            print('\n----------------------------\n')
            print('Added: {} ({} @ ${:1.2f} = ${:1.2f})'.format(name, self.items[item_id]['qty'], self.items[item_id]['price'], self.items[item_id]['qty']* self.items[item_id]['price']))        
            if input('\nEnter another item? (y/n): ').lower() not in ['y', 'yes']:
                break

            
    # def printFullList(self):
    #     for i, item in enumerate(self.items):
    #         if self.list_index == i:
    #             print(f"->> ({self.items[item]['qty']})".rjust(9), self.items[item]['name'].rjust(20), "<<-" )
    #         else:
    #             print(f"({self.items[item]['qty']})".rjust(9), self.items[item]['name'].rjust(20) )
    def getItems(self):
        return [(item['name'], item['qty']) for item in self.items]
    def printItems(self):
        print('X'+" "*3, end="")
        print("X" + " "*56+"X")
        print("X" + " "*56+"X")
    def printSeparator(self):
        print("")
        # print('X'*56)
        print("MY BASKET".center(56,"~"))
        print('')

    def editItem(self, item):
        pass
    def deleteItem(self):
        pass
