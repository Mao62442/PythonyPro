def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper_function
@decorator_function
def add(a, b, c):
    return a + b + c

print(add(5, 3, 5))