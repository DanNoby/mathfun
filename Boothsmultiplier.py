
def add(a,b):
    s = []
    c=0
    for i in range(-1,-len(a)-1,-1):
        soom = a[i] + b[i] + c
        if soom==0 or soom==1:
            s.append(soom)
            c = 0
        elif soom==2:
            s.append(0)
            c = 1
        elif soom==3:
            s.append(1)
            c = 1
    s.reverse()
    return s
    

def compliment(a):
    c = []
    for i in a:
        if i==0:
            c.append(1)
        else:
            c.append(0)
    one = [0 for i in a]
    one[-1] = 1
    r = add(c,one)
    return r

def display(a):
    s=''
    for i in a:
        s+= str(i)+ " "
    return s

def ASR(AQQ):
    for i in range(-1,-len(AQQ),-1):
        AQQ[i] = AQQ[i-1]
    return AQQ

def Q_B(Q,B):
    Q1, B1 = abs(Q) , abs(B) 
    q = [0,] + [int(i) for i in bin(Q1)[2:]]
    b = [0,] + [int(i) for i in bin(B1)[2:]]

    diff = len(q) - len(b)
    if diff<0:
        q = [0 for i in range(abs(diff))] + q 
    elif diff>0:
        b = [0 for i in range(abs(diff))] + b
    if Q<0:
        q = compliment(q) 
    if B<0:
        b = compliment(b) 
    return q,b
    
        
def operations(Q,B):
    bin = Q_B(Q,B) 
    Q = bin[0]
    B = bin[1] 

    NegB = compliment(B)
    count = len(Q)
    CI = count
    AQQ = [0 for i in range(count)] + Q + [0,]
    print(f"c={count}   {display(AQQ[:CI])} {display(AQQ[CI:-1])} {AQQ[-1]}")
    while count!=0:
        if AQQ[-2] < AQQ[-1]:
            A = AQQ[:CI]
            s = add(A,B) 
            for i in range(CI):
                AQQ[i] = s[i]
            print(f"      {display(AQQ[:CI])} {display(AQQ[CI:-1])} {AQQ[-1]}   -> from {A} + {B}\n")
        elif AQQ[-2] > AQQ[-1]:
            A = AQQ[:CI]
            s = add(A,NegB)
            for i in range(CI):
                AQQ[i] = s[i]
            print(f"      {display(AQQ[:CI])} {display(AQQ[CI:-1])} {AQQ[-1]}   -> from {A} - {B}\n")
        AQQ = ASR(AQQ)
        count -= 1
        print(f"c={count}   {display(AQQ[:CI])} {display(AQQ[CI:-1])} {AQQ[-1]}   -> from ASR")
    if(AQQ[0]==1):
        AQQ = compliment(AQQ)
    print(f"Final:[{display(AQQ[:-1])}]")
    
    s=0
    p=0
    for i in range(-2,-len(AQQ)-1,-1):
        s+= pow(2,p) * AQQ[i]
        p+=1
    print(s)

def main():
    Q = int(input("Q:"))
    B = int(input("B:"))
    operations(Q,B) 
main()
