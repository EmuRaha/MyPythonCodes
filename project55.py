# Exception Handling

a = 5
b = 2

try:
    print("Open")
    print(a/b)
    inp = int(input("Enter a number="))
    print(inp)
except ZeroDivisionError as e:
    print("Can not divide by Zero",e)
except ValueError as e:
    print("Invalid input",e)
except Exception as e:
    print(e)
finally:
    print("Close")

try:
    print("Open")
    print(a/b)
    inp = int(input("Enter a number="))
except ZeroDivisionError as e:
    print("Can not divide by Zero",e)
except ValueError as e:
    print("Invalid input",e)
except Exception as e:
    print(e)
else:
    print(inp)
finally:
    print("Close")




































