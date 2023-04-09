def hundredNumber():
    i=0
    while i<100:
        yield i
        i+=1


g=hundredNumber()
print(next(g))
print(next(g))
print(list(g))

class hundredNumberClass:
    def __init__(self):
        self.number=0
    def __next__(self):
        if self.number <100:
            current=self.number
            self.number+=1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return hundredNumberClass()


newGenerator=hundredNumberClass()
print(next(newGenerator))
print(next(newGenerator))
print(next(newGenerator))
print(next(newGenerator))

class firstFiveGenerator:
    def __init__(self):
        self.numbers=[1,2,3,4,5]
        self.i=0
    def __next__(self):
        if self.i<len(self.numbers):
            current= self.numbers[self.i]
            self.i+=1
            return current
        else:
            raise StopIteration()


newIterator=firstFiveGenerator()
print(next(newIterator))
print(next(newIterator))
print(next(newIterator))
print(next(newIterator))
print(next(newIterator))

print(sum(hundredNumberClass()))

class cars:
    def __init__(self):
        self.cars=['Ford','BMW']
    def __len__(self):
        return len(self.cars)
    def __getitem__(self, i):
        return self.cars[i]

for car in cars():
    print(car)


#len() and getitem() = __iter__


#copy list elements
myList=[x for x in [1,2,3,4,5]]
#copy list element 1 by 1
myListGenerator=(x for x in [1,2,3,4,5])

print(myList)
print(next(myListGenerator))
print(next(myListGenerator))