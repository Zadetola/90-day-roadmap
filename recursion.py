def countdown(n):
    if n == 0:
        print('Done')
    else:
        print(n)
        countdown(n - 1)
countdown(3)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print (fib(3))

def binary_search(items, target, low, high):
    if low > high:
        return -1
    middle = (low + high) // 2
    if items[middle] == target:
        return middle
    elif items[middle] < target:
        return binary_search(items, target, middle+1, high)
    else:
        return binary_search(items, target, low, middle-1)
print(binary_search([4, 8, 15, 16, 23, 42], 23, 0, 5))
print(binary_search([4, 8, 15, 16, 23, 42], 99, 0, 5))


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.value)
    in_order(node.right)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

a.left = b
a.right = c
b.left = d
b.right = e

in_order(a)