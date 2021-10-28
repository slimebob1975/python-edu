class Node:
    """Nodklass för att skapa noder till envägs-länkade listor"""

    def __init__(self, v = None):
        self.value = v   # Nodens värde
        self.next = None # Nästa nod

    def __str__(self):
        """Skapa sträng-representation av nodens värde"""
        return str(self.value)

class Stack:
    """Klass för att skapa och hantera stackar"""

    def __init__(self, f = None):
        # data-attributet first pekar på första noden 
        self.first = f

    def __repr__(self):
        node = self.first
        s = ""
        while node:
            s += ("["+str(node.value) + "]\n |\n v\n")
            node = node.next
        return s

    def __bool__(self):
        if self.first:
            return True
        else:
            return False

    def push(self, val):
        new = Node(val)
        new.next = self.first
        self.first = new

    def pop(self):
        if self.first == None:
            return None
        else:
            node = self.first
            self.first = node.next
            return node.value


def main():
    stack = Stack()
    value = 1
    while value:
        value = input("Give something to push (quit with Enter): ")
        if value:
            stack.push((value))
    print(stack)
    while stack.pop():
        print("\n")
        print(stack)

main()
