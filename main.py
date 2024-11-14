import random
import time

NUM_LINES= 4 
NUM_COLUMNS= 3
SYMBOLS= ['A', 'B']
WON__K = 2 # Ratio of a winning bet


class Game:
    
    def make_bet(self, amount:int):
        while True:
            temp_bet_amount= input('Make your bet $')    
            if temp_bet_amount.isdigit():
                self.bet_amount=int(temp_bet_amount)
                if self.bet_amount*self.lines_amount > amount:
                    print(f'Sorry! your bet(${self.bet_amount} * {self.lines_amount}) more than your amount(${amount})')
                else:
                    break
            else:
                print('Money! Bet the money!')
        print(f"Congratulations! You made a wager for ${self.bet_amount} amount, let's begin")
        
        return self.bet_amount
    
    def choose_lines(self):         
         while True:
            temp_n= input(f'(to QUIT - press "q")) OR Choose how many lines will be the winner (1-{NUM_LINES}): ')
            if temp_n == 'q':
                return False
                
            if temp_n.isdigit():
                if 0 < int(temp_n) <= NUM_LINES:
                    self.lines_amount= int(temp_n)
                    break
            else:
                print(f'Put the right digit - 1 .. {NUM_LINES}')
        
         print(f"GREATE! You chose {self.lines_amount} lines to win")
         return self.lines_amount
         

class Slot: 
    """
    Game wheel is the main spinned device    
    """
 
    lines= []
    # column= []
    result_lines= []
    
    def spin(self):
        
        """
            spin slot machine
        """         
        #fill the rows of drum
        self.columns=[[random.choice(SYMBOLS) for j in range(NUM_LINES)] for i in range(NUM_COLUMNS)]         
        
        # print(self.columns)          
        self.lines.clear()        
        for row in range(NUM_LINES):            
            self.lines.append([])
            
            for c in self.columns:            
                self.lines[row].append(c[row])              
          

      
    def show_result(self):
        print('\n')
        print('='*13)
        self.result_lines=[]
        
        for row in self.lines:
            s= "| "
            s+= ''.join([c + ' | ' for c in row])                
            s+= ' - \033[31m!WIN!\033[0m' if all([row[0] ==_ for _ in row]) else ' -  LOSE'
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

    def calc_profit(self, res_lines:list, bet_lines:int, bet:int) -> int:
        sum_lines  = sum(res_lines)
                
        if sum_lines > 0:
            if bet_lines <= sum_lines:
                print(f'Congratilations! You won ${(min(bet_lines, sum_lines) * bet *  WON__K * 2) - (min(bet_lines, sum_lines) * bet)} !')
                self.amount+= min(bet_lines, sum_lines)*bet*WON__K - (min(bet_lines, sum_lines) * bet)         
            
            else: # won less than bet lines
                print(f'Congratilations! You just won ${(sum_lines * bet * WON__K) - (bet_lines * bet)} !')
                self.amount+= (sum_lines * bet * WON__K) - (bet_lines * bet)
                
            
        else:            
            print(f'Sorry! You loose ${bet * bet_lines}!')             
            self.amount-= bet * bet_lines
        
        print(f'Your balance is: ${self.amount}')
        return self.amount

        

def main_cycle():
    cashier = Cashier()
    cashier.fill_amount()
    slot= Slot()
    game= Game()
    
    exit_flag= False    
    while not exit_flag:            
        if not game.choose_lines():
            print(f'Your balance is ${cashier.amount}, BYE!')
            break
        
        game.make_bet(cashier.amount)     
        slot.spin()
        slot.show_result()
        cashier.calc_profit(slot.result_lines, game.lines_amount, game.bet_amount)
        
        if cashier.amount==0:
            print('Sorry! you have 0 at balance, back with money  and start again')
            exit_flag = True
            
        time.sleep(1)  
        
    
    
    
if __name__ == '__main__':    
    main_cycle()