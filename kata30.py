

def solution(string,markers):
    lines = string.split('\n')
    lines1=[]
    for i in lines:
        words=i.split()
        for j in markers:
            if j in words:
                del words[words.index(j):]
        for k in words:
            l=len(words)
            for j in markers:
                if j in k:
                    if len(words)==l:
                        del words[words.index(k):]
        lines1.append(" ".join(words))
    return "\n".join(lines1)



print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
print(solution("a #b\nc\nd $e f g", ["#", "$"]))
print(solution('§',['#', '§']))
print(solution("apples, pears # and bananas\ngrapes\nbananas !#apples",["#", "!"]))
























