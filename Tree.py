class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def print_node(self):
        if self.left:
            self.left.print_node()
        print(self.data)

        if self.right:
            self.right.print_node()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def sum_node(self, sums):
        sum = self.data
        if self.left:
            sum += self.left.sum_node(sums)
        if self.right:
            sum += self.right.sum_node(sums)
        sums[self] = sum
        return sum

root = Node(10)
root.insert(11)
root.insert(9)
root.print_node()

sums = dict()

root.sum_node(sums)
print sums
