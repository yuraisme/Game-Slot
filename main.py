import random
import time

NUM_LINES = 3 
NUM_COLUMNS = 3
SYMBOLS = ['A', 'B', 'C', 'D']

class Game:
    
    def make_bet(self):
        while true:
            temp_bet_amount= input('Make your bet $')    
            if temp_bet_amount.isdigit():
                self.bet_amount=temp_bet_amount
                    

class Slot: 
    """
    Game wheel is the main spinned device    
    """
    SYMBOLS= ['A', 'B', 'C']
    lines= []
    # column= []
    result_lines= []
    
    def spin(self):
        
        """spin drum
        """         
        #fill the rows of drum
        self.columns=[[random.choice(self.SYMBOLS) for j in range(NUM_LINES)] for i in range(NUM_COLUMNS)]         
        
        # print(self.columns)          
        self.lines.clear()        
        for row in range(NUM_LINES):            
            self.lines.append([])
            
            for c in self.columns:            
                self.lines[row].append(c[row])              
          

      
    def show_result(self):
        print('\n','='*13)
        self.result_lines=[]
        
        for row in self.lines:
            s= "| "
            s+= ''.join([c + ' | ' for c in row])                
            s+= ' - !WIN!' if all([row[0] ==_ for _ in row]) else ' -  LOSE'
            self.result_lines.append(1 if all([row[0] ==_ for _ in row]) else  - 0)
            print(s) 
        print('='*13)      
        # print(self.result_lines)
        # print(type(self.result_lines))
        print(f'\n Won {sum(self.result_lines)} lines! ')     
        
    
class Cashier:
    def fill_amount(self):
        
        temp_amount = input('Put you money to the slot $')
        if temp_amount.isdigit():
            self.amount = float(temp_amount)
            print(f"You have ${self.amount} amount!")        
    

def main_cycle():
    cashier = Cashier()
    cashier.fill_amount()
    slot = Slot()
    while True:        
        slot.spin()
        slot.show_result()
        time.sleep(1)
    
    
    
    
main_cycle()