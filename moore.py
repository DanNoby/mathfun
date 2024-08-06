def c(n):
    if n==0:
        return 1
    else:
        return 0

def overlap(seq):
    c=0
    for i in range(len(seq)-1):
        if seq[-1-i::]== seq[:i+1]:
            c=i+1
    return c

def sequence_check(seq,ovlap=0,model=0):
    d={}
    chnum = 65
    if model==1:
        seq = seq + seq[0]
    for i in range(len(seq)):
        num = int(seq[i])
        numc = c(num) 
        if numc== int(seq[0]):
            d[chr(chnum)] = {num:chr(chnum+1),numc:'B'}
        else:
            d[chr(chnum)] = {num:chr(chnum+1),numc:'A'}

        if i==len(seq)-1:
            d[chr(chnum)][num] = d['A'][num]
            if ovlap == 1:
                ol = overlap(seq)
                if model==1:
                    seq = seq[:-1]
                    num = int(seq[-2]) 
                    d[chr(chnum)][num] = chr(ord('B') + ol)
                else:
                    d[chr(chnum)][num] = chr(ord('A') + ol)    
                numc = c(num) 
                d[chr(chnum)][numc] = d['A'][numc]    
        chnum+=1
    return d

def main():
    s = input("sequence:")
    o = int(input("non-overlapping (0) / overlapping (1):"))
    m = int(input("Mealy model(0) / Moore model (1):")) 
    D = sequence_check(s,o,m)
    for x,y in D.items():
        print(f"{x} : {y}")
main()
    






