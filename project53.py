# Iterator

nums = [1,2,3,4,5,6,7,8,9,10]

it = iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))
print(it.__next__())
print(next(it))
print()
for i in nums:
    print(i)

print()
print()
print()
class TopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration

values = TopTen()

print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print()
for i in values:     #for loop calls the next function(in-built)
    print(i)


















