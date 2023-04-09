def startWithM(friend):
    return friend.startswith('M')

friends=['Mahmoud','Mostafa','Yasset','Taha','Mohamed']

myFilter=filter(startWithM,friends)
print(next(myFilter))
print(list(myFilter))
myFilter=filter(lambda friend:friend.startswith('M'),friends)
print(list(myFilter))
myFilter=(friend for friend in friends if friend.startswith('M'))
print(list(myFilter))

def customFilter(func,iterable):
    for i in iterable:
        if(func(i)):
            yield i

print(next(customFilter(startWithM,friends)))