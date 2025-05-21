class Calculate:
    def  add(self,x,y):
        return(x+y)
    
    def  sub(self,x,y):
        return(x-y)
    
    def  mul(self,x,y):
        return(x*y)
    
    def  div(self,x,y):
        if y==0:
            raise ValueError("Division by Zero error")
        return(x/y)
    
    