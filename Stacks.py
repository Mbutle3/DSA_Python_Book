class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty stack"""
        self._data = []  # private list instance

    def __len__(self):
        """Returns the number of elements in the stack"""
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()


print("Stack ADT Example")
S = ArrayStack()
S.push(5)
S.push(3)
print(len(S))
print(S.pop())
print(S.is_empty())
print(S.pop())
print(S.is_empty())
S.push(7)
S.push(9)
print(S.top())
S.push(4)
print(len(S))
print(S.pop())
S.push(6)
print()

print("Array Based Stack Implementation Time Complexities")
print("Push -> O(1)\n"
      "Pop -> O(1)\n"
      "Top -> O(1) \n"
      "Is_Empty -> O(1)\n"
      "Len -> O(1)")
print()


def reverse_file(filename):
    s2 = ArrayStack()
    original = open(filename)
    for line in original:
        s2.push(line.rstrip('\n'))
    original.close()
    output = open(filename, 'w')
    while not s2.is_empty():
        output.write(str(s2.pop()) + '\n')
    output.close()


print("Reversing 'reverse_text.txt' file")
# reverse_file("reverse_text.txt")
print()

print("Matching Parenthesis")


def is_Matching(expression):
    """Returns True if all delimiters are properly matched
               False otherwise"""
    left = '{[('  # opening delimiters
    right = '}])'  # closing delimiters
    s3 = ArrayStack()

    for c in expression:
        if c in left:
            s3.push(c)  # push left delimiter on stack
        elif c in right:
            if s3.is_empty():
                return False  # noting to match with
            if right.index(c) != left.index(s3.pop()):
                return False  # mismatched
    return s3.is_empty()  # Were all symbols matched if so returns True otherwise returns False


print(is_Matching("( )(( )){([( )])}"))
print(is_Matching("( )"))
print(is_Matching("((()(()){([()])}))"))
print(is_Matching("({[])}"))
print(is_Matching('{'))
print()
