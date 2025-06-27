def mydecorator(func):
    def wrapper(*args):
        print(f"We are learning about python decorators")
        result = func(*args)
        return result.lower()
    return wrapper

@mydecorator
def inputString(person):
    return f"{person} is very intelligent."

print(inputString("Varun Athithiya"))