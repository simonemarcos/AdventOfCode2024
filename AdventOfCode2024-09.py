import time

def resolve(nums):
    n=0
    mem=list(nums)
    mem=firstStep(mem)
    mem=secondStep(mem)
    for i in range(len(mem)):
        if mem[i]!='.':
            n+=int(mem[i])*i
    print(n)

def firstStep(list):
    i=0
    mem=[]
    print
    for x in list:
        if not i%2:
            mem+=([str(i//2)]*int(x))
        else:
            mem+=(['.']*int(x))
        i+=1
    return mem

def secondStep(mem):
    i=0
    j=len(mem)-1
    print()
    while i<j:
        while mem[i]!='.':
            i+=1
        while mem[j]=='.':
            j-=1
        if i>=j:
            break
        mem[i]=mem[j]
        mem[j]='.'
    return mem

def load_input():
    with open("message_09.txt", "r") as f:
        return f.read()

nums=load_input()
resolve(nums)