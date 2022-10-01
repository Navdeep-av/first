li=["Hello","Hi","How","Name"]
mi=[4,5,6,7]

def func(test):
    if len(test)%2==0:
        return "Even"
    else:
        return test[0]

# print(func(li))         

print(list(map(func,li)))