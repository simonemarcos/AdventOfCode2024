def resolve(nums):
    n=0
    mem=list(nums)
    mem=firstStep(mem)
    mem=secondStep(mem)
    for i in range(len(mem)):
        if mem[i][0]!='.':
            n+=int(mem[i])*i
    print(n)

def firstStep(list):
    i=0
    mem=[]
    print
    for x in list:
        if not i%2:
            mem.append([str(i//2)]*int(x))
        else:
            if int(x):
                mem.append(['.']*int(x))
        i+=1
    return mem

def secondStep(mem):
    current=int(mem[len(mem)-1][0])+1
    j=len(mem)-1
    while current>0:
        i=0
        current-=1
        flag=False
        while mem[j][0]!=str(current):
            j-=1
        while mem[i][0]!='.' or len(mem[i])<len(mem[j]):
            i+=1
            if (i>=j):
                flag=True
                break
        if flag:
            continue
        diff=len(mem[i])-len(mem[j])
        if diff>0:
            remaining=['.']*diff
            moved=['.']*len(mem[j])
            mem[i]=list(mem[j])
            mem.insert(i+1,remaining)
            mem[j+1]=moved
        else:
            t=list(mem[i])
            mem[i]=list(mem[j])
            mem[j]=list(t)

    x=[]
    for a in mem:
        for b in a:
            x.append(b)
    return x

def load_input():
    with open("message_09.txt", "r") as f:
        return f.read()

nums=load_input()
resolve(nums)