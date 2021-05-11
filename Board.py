class Board:
    def __init__(self):
        self.block = [["Empty" for x in range(3)] for y in range(3)]
        self.won = False

    def set_block(self, location, xo):

        self.block[location[0]][location[1]] = xo
        
        self.won = self.horizontal_check(location, xo)


    def available_block(self, location):
        if self.block[location[0]][location[1]] == "Empty":
            return True
        else:
            return False

        
    def horizontal_check(self, location, xo):
        empty1 = False
        empty2 = False
        consecutive = 1
        for i in range(2):
            if -1 < location[0] + 1 + i < 3 and not empty1:
                if self.block[location[0] + 1 + i][location[1]] == xo:
                    consecutive += 1
                else:
                    empty1 = True
            if -1 < location[0] - 1 - i < 3 and not empty2:
                if self.block[location[0] - 1 - i][location[1]] == xo:
                    consecutive += 1
                else:
                    empty2 = True 
        if consecutive >= 3:
            return True
        else:
            return self.vertical_check(location, xo)  



    def vertical_check(self, location, xo):
        empty1 = False
        empty2 = False        
        consecutive = 1
        for i in range(2):
            if -1 < location[1] + 1 + i < 3 and not empty1:
                if self.block[location[0]][location[1] + 1 + i] == xo:
                    consecutive += 1
                else:
                    empty1 = True
            if -1 < location[1] - 1 - i < 3 and not empty2:
                if self.block[location[0]][location[1] - 1 - i] == xo:
                    consecutive += 1
                else:
                    empty2 = True                
        if consecutive >= 3:
            return True
        else:
            return self.forward_diagonal_check(location, xo)
            
    
    def forward_diagonal_check(self, location, xo):
        empty1 = False
        empty2 = False   
        consecutive = 1
        for i in range(2):
            if -1 < location[0] + 1 + i < 3 and -1 < location[1] + 1 + i < 3 and not empty1:
                if self.block[location[0] + 1 + i][location[1] + 1 + i] == xo:
                    consecutive += 1
                else:
                    empty1 = True
            if -1 < location[0] - 1 - i < 3 and -1 < location[1] - 1 - i < 3 and not empty2:
                if self.block[location[0] - 1 - i][location[1] - 1 - i] == xo:
                    consecutive += 1
                else:
                    empty2 = True                
        if consecutive >= 3:
            return True
        else: 
            return self.backward_diagonal_check(location, xo)
            
        
    def backward_diagonal_check(self, location, xo):
        empty1 = False
        empty2 = False 
        consecutive = 1
        for i in range(2):
            if -1 < location[0] - 1 - i < 3 and -1 < location[1] + 1 + i < 3 and not empty1:
                if self.block[location[0] - 1 - i][location[1] + 1 + i] == xo:
                    consecutive += 1
                else:
                    empty1 = True
            if -1 < location[0] + 1 + i < 3 and -1 < location[1] - 1 - i < 3 and not empty2:
                if self.block[location[0] + 1 + i][location[1] - 1 - i] == xo:
                    consecutive += 1
                else:
                    empty2 = True                    
        if consecutive >= 3:
            return True
        else:
            return False
    