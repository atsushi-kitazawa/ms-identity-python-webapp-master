def add(a, b):
    return a + b

def ortest(lists):
    print(', '.join(map(str, lists)))

if __name__ == "__main__":
    ortest([1, 2, 3])
    ortest([])