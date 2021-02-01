class step:
    type = ""
    x = 0
    y = 0
    def __init__(v,a,b,c):
        v.type=a
        v.x=b
        v.y=c
def MED(source,target,del_cost,ins_cost,s_cost):
    x = len(source)
    y = len(target)
    print(x)
    print(y)
    b=y+1
    a=x+1
    M = [[0 for j in range(b)] for i in range(a)]
    M[0][0]=0
    for i in range(1,a):
        M[i][0]=M[i-1][0]+del_cost
        
    for j in range(1,b):
        M[0][j]=M[0][j-1]+ins_cost
        
    for i in range(1,a):
        for j in range(1,b):
            if source[i-1]==target[j-1]:
                cost = 0
            else:
                cost=s_cost
            M[i][j]=min(M[i-1][j]+1,M[i][j-1]+1,M[i-1][j-1]+cost)
    i=x
    j=y
    backtrace=[]
    while i!=0 or j!=0:
          if M[i][j]==M[i-1][j]:
                i=i-1
                s=step("Del",i,j)
                backtrace.append(s)
          elif M[i][j]==M[i][j-1]:
                j=j-1
                s=step("Del",i,j)
                backtrace.append(s)
          elif M[i][j]==M[i-1][j-1]:
                j=j-1
                i=i-1
                s=step("Sub",i,j)
                backtrace.append(s)
          print(i)
          print(j)
    for i in range(0,len(backtrace)):
        print(backtrace[i])
        print(i)
    return M[x][y]
        
MED("intention","execution",1,1,2)