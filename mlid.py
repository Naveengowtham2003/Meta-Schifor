class dec1:
    def dec1(self, func):
        def wrapper(*args, **kwargs):
            print("Decorator  1")
            return func(*args, **kwargs)

        return wrapper


class dec2:
    def dec2(self, func):
        def wrapper(*args, **kwargs):
            print("Decorator  2")
            return func(*args, **kwargs)

        return wrapper


class lam:
    lambda_func = lambda self, x: x * 2



class Myclass(dec1, dec2, lam):
    pass


obj = Myclass()


@obj.dec1
def add(a, b):
    return a + b


@obj.dec2
def mul(a, b):
    return a * b


a, b = map(int, input().split())
print("Addition of :", a, "and", b, "is", add(a, b))
print("Multiplication of :", a, "and", b, "is", mul(a, b))
print("lambda function:", obj.lambda_func(5))
