def func(x):
    func_res=0.25*(x**4.1) #here will be your function
    return func_res

def calculate_understandable(a,b,dx):
    ops=int((b-a)/dx) #how many areas we need to add up
    result=0 #starting result
    x=a #our x cursor is now on starting point
    for i in range(ops):
        fx=func(x) #after this we'll know our y, when x cursor is in this point
        dx_area=fx*dx #calculating small area (dx*y)
        result+=dx_area #adding up result of calculating small areas
        x+=dx #moving cursor by value of "dx"
    return result

#optimized method
def calculate(a,b,dx):
    result=0
    for i in range(int((b-a)/dx)):
        result+=func(a)*dx
        a+=dx
    return result


a=3 #lower limit
b=6 #upper limit
dx=0.0001 #defines precision of calculation. less=better (dx>0, dx<(b-a))
print(calculate(a,b,dx))