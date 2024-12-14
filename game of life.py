class cells:
    
    def __init__(self,pos,rect,i,j):
        self.x,self.y = pos
        self.rect = rect,
        self.i = i
        self.j = j
        self.color = BLACK
        self.updat = False
        
    def render(self):
        #0 = nada
        #1 = cobra
        #2 = pareda
        #3 = maçã
        if array[self.i][self.j] == 1:
            self.color = (0,255,0)
            
            #print(f'the list is {snakeind} and the item that gonna be in will be ({self.i}, {self.j})')
            if (self.i,self.j) not in snakeind:
                snakeind.append((self.i,self.j))
                
            if len(snakeind) > length:
                #print(f'im deleting item {snakeind[0]} from {snakeind}')
                del snakeind[0]
            
            for i in range(len(snakeind)):
                self.rect = pg.Rect((snakeind[i][0]*WIDTH/gridx,snakeind[i][1]*HEIGHT/gridy,
                                 WIDTH/gridx-1,HEIGHT/gridy-1))
                
                pg.draw.rect(screen,(self.color),self.rect)
        if array[self.i][self.j] == 2:
            self.color = (255,0,0)
            pg.draw.rect(screen,(self.color),self.rect)

        if array[self.i][self.j] == 3:
            self.color = (255,0,255)
            pg.draw.rect(screen,(self.color),self.rect)
        
            
        


#resolver o bug da movimntação em grid, mesmo problema do sandbox,
#esta se movendo instantaneamente
    def update(self):
        ri = rand.randint(1,gridx-2)
        rj = rand.randint(1,gridy-2)
        global length
        global apple_spawn
        if (not apple_spawn):
            if ((ri,rj) not in snakeind):
                
                array[ri][rj] = 3
                apple_spawn = True
                
##        print('im updatinnnnnng')
        #abovegrid = array[self.i][self.j-1]
        #belowgrid = array[self.i][self.j+1]
        #rightgrid = array[self.i+1][self.j]
        #leftgrid  = array[self.i-1][self.j]
        
        if direction == 2:#S
            
            if (array[self.i][self.j+1] == 2) or ((self.i,self.j+1) in snakeind):
                print('game over')
                print(snakeind)
                print(len(snakeind))
                pg.quit()
                quit()
                
            if (array[self.i][self.j+1] == 3):
                print('i ate an apple S')
                print(f'my size now is {length}')
                apple_spawn = False
                length += 1
                array[self.i][self.j+1] = 0
            if (self.j+1 < int(gridx-1)):
                    array[self.i][self.j+1] = 1
                    array[self.i][self.j] = 0
                    print(self.j)
            
                    
        if direction == 4: #A
            
            if (array[self.i-1][self.j] == 2) or ((self.i-1,self.j) in snakeind):
                print('game over')
                print(snakeind)
                print(len(snakeind))
                pg.quit()
                quit()
                
            if (array[self.i-1][self.j] == 3):
                print('i ate an apple A')
                print(f'my size now is {length}')
                apple_spawn = False
                length += 1
                array[self.i-1][self.j] = 0
            if (self.i-1 > 0):
                array[self.i-1][self.j] = 1
                array[self.i][self.j] = 0
                print(self.i)
            
        if direction == 6:#D
            
            if (array[self.i+1][self.j] == 2) or ((self.i+1,self.j) in snakeind):
                print('game over')
                print(snakeind)
                print(len(snakeind))
                pg.quit()
                quit()
                
            if (array[self.i+1][self.j] == 3):
                print('i ate an apple D')
                print(f'my size now is {length}')
                apple_spawn = False
                length += 1
                array[self.i+1][self.j] = 0
            if(self.i+1 < int(gridx-1)):
                array[self.i+1][self.j] = 1
                array[self.i][self.j] = 0
                print(self.i)
            
        if direction == 8:#W
            
            if (array[self.i][self.j-1] == 2) or ((self.i,self.j-1) in snakeind):
                print('game over')
                print(snakeind)
                print(len(snakeind))
                pg.quit()
                quit()
                
            if (array[self.i][self.j-1] == 3):
                print('i ate an apple W')
                print(f'my size now is {length}')
                apple_spawn = False
                length += 1
                array[self.i][self.j-1] = 0
                
            if (self.j-1 > 0):
                array[self.i][self.j-1] = 1
                array[self.i][self.j] = 0
                print(self.j)
