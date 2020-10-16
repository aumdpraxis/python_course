class snake:
    def __init__(self,x,y,world_scale,world_limit,color):
        self.x=x
        self.y=y
        self.world_scale = world_scale
        self.world_limit = world_limit
        self.dx= 1
        self.dy= 0
        self.cells=[]
        self.maxCells=4
        self.color=color

    def update_pos(self,pos):
        self.x = pos[0]
        self.y = pos[1]
        self.cells.insert(0,{'x':self.x,'y':self.y})
        if(len(self.cells)>self.maxCells):
            self.cells.pop()
        for cell in self.cells[1:]:
            if(self.cells[0]['x']==cell['x'] and self.cells[0]['y']==cell['y']):
                return 0
        return 1

    def get_current_pos(self):
        return self.cells

    def get_next_state(self):
        temp_x = self.dx*self.world_scale+self.x
        temp_y = self.dy*self.world_scale+self.y
        if(temp_x<0):
            temp_x= self.world_limit[0]-self.world_scale
        elif(temp_x>=self.world_limit[0]):
            temp_x=0

        if(temp_y<0):
            temp_y= self.world_limit[1]-self.world_scale
        elif(temp_y>=self.world_limit[1]):
            temp_y=0
        return [temp_x,temp_y]


    def ate_apple(self):
        self.maxCells+=1

    def on_left_key(self):
        if(self.dx==0):
            self.dx= -1
            self.dy= 0

    def on_right_key(self):
        if(self.dx==0):
            self.dx= 1
            self.dy= 0

    def on_up_key(self):
        if(self.dy==0):
            self.dy= -1
            self.dx= 0

    def on_down_key(self):
        if(self.dy==0):
            self.dy= 1
            self.dx= 0

    def get_metadata(self):
        return {'cells':self.cells,'color':self.color}


class apple:
    def __init__(self,_id,x,y):
        self.x=x
        self.y=y
        self.id=_id
    
    def get_metadata(self):
        return {'id':self.id,'x':self.x,'y':self.y}