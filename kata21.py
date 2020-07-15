

def namelist(names):
    if len(names)==0:
        return ""
    if len(names)==1:
        return names[len(names)-1]['name']

    a = [", ".join([names[i]['name'] for i in range(len(names)-1)]),names[len(names)-1]['name']]
    return " & ".join(a)





print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist([]))

def namelist1(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join([names[i]['name'] for i in range(len(names)-1)]),names[len(names)-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
print(namelist1([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist1([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist1([]))



