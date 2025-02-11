

def alphabet_to_int(a):
    if a=='A':
        return 1
    if a=='B':
        return 2
    if a=='C':
        return 3
    if a=='D':
        return 4
    if a=='E':
        return 5
    if a=='F':
        return 6
    if a=='G':
        return 7
    if a=='H':
        return 8
def int_to_alpha(a):
    if a==1:
        return 'A'
    if a==2:
        return 'B'
    if a==3:
        return 'C'
    if a==4:
        return 'D'
    if a==5:
        return 'E'
    if a==6:
        return 'F'
    if a==7:
        return 'G'
    if a==8:
        return 'H'

def move(op,pos):
    if op=='L':
        return(pos[0]-1,pos[1])
    elif op=='T':
        return(pos[0],pos[1]+1)
    elif op=='R':
        return(pos[0]+1,pos[1])
    elif op=='B':
        return(pos[0],pos[1]-1)
    
KP,SP,N=input().split()
N=int(N)
KP= (alphabet_to_int(KP[0]),int(KP[1]))
SP= (alphabet_to_int(SP[0]),int(SP[1]))

for _ in range(N):
    op=input()
    tempKP=KP
    tempSP=SP
    for i in op:
        tempKP=move(i,tempKP)
    if tempKP==SP:
        for i in op:
            tempSP=move(i,tempSP)
    if 0<tempKP[0]<9 and 0<tempKP[1]<9 and 0<tempSP[0]<9 and 0<tempSP[1]<9:
        KP=tempKP
        SP=tempSP
print(int_to_alpha(KP[0]),end='')
print(KP[1])
print(int_to_alpha(SP[0]),end='')
print(SP[1])
                