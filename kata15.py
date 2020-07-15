
#Counting Duplicates

def duplicate_count(text):
    n=0
    text = text.lower()
    for i in set(text):
        if text.count(i)>1:
            n=n+1
    return n

print(duplicate_count("abcde"))
print(duplicate_count("Abcdea"))
print(duplicate_count("indivisibility"))



































