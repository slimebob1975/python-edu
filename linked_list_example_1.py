class ListNode:
    """Nodklass för att skapa noder till envägs-länkade listor"""

    def __init__(self, v = None):
        self.value = v   # Nodens värde
        self.next = None # Nästa nod

    def __str__(self):
        """Skapa sträng-representation av nodens värde"""
        return str(self.value)

class LinkedList:
    """Klass för att skapa och hantera envägs-länkade listor"""

    def __init__(self, f = None):
        # data-attributet first pekar på första noden 
        self.first = f

    def append(self, val):
        new = ListNode(val)
        if self.first == None:
            self.first = new
        else:
            node = self.first
            while node.next:
                node = node.next
            node.next = new

    def length(self):
        n = 0
        node = self.first
        if node:
            n = 1
            while node.next:
                n +=1
                node = node.next
        return n

    def print_list(self):
        node = self.first
        while node:
            print("["+str(node.value) + "] -> ", end = "")
            node = node.next


def main():
    linkedlist = LinkedList()
    value = 1
    while value:
        value = input("Give next value (quit with Enter): ")
        if value:
            linkedlist.append((value))
    print("The list has length: ",linkedlist.length())
    linkedlist.print_list()

main()
