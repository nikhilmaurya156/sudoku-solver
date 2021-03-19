def checkcell(display,x,y,r):
    for i in range(9):
        y+=1
        if y>8:
            x+=1
            y=0
        if x>8:
            break
        if display[x][y]==-1:
            return x,y
        continue
    return True
def numberCheck(display,number,x,y,counter):
    row = x-x%3
    col = y-y%3
    xy_check = []
    x_y = [[display[row+k][col+j] for j in range(3)] for k in range(3)]
    for k in x_y:
        for j in k:
            xy_check.append(j)
    y_check=[display[j][y] for j in range(6)]
    if  display[x][y]==-1 and number[counter] not in y_check and number[counter] not in display[x] and number[counter] not in xy_check:
        return True
    return False

class Disp:
    def design(display):
        for i in range(9):
            for j in range(9):
                if display[i][j]=='':
                    display[i][j]=-1
        number=[1,2,3,4,5,6,7,8,9]
        n=0
        if solve(display,0,-1,number,n):
            return display
        else:
            print('Solution not exist')

def solve(display,start_x,start_y,option, n):
    z=checkcell(display,start_x,start_y,n)
    if z!=True:
        start_x=z[0]
        start_y=z[1]
    else:
        return True
    for i in range(9):
        if numberCheck(display,option,start_x,start_y,i):
            display[start_x][start_y]=option[i]
            if  solve(display,start_x,start_y, option, n+1):
                return True
            display[start_x][start_y]=-1
    return False

