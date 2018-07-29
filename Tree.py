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

    def sum_node(self):
        my = self.data
        left_sum = 0
        right_sum = 0
        if self.left:
            left_sum = self.left.sum_node()

        if self.right:
            right_sum = self.right.sum_node()

        if (my + left_sum) == right_sum:
            print('found edge ' + str(my) + "  " + str(self.right.data))
        elif (my + right_sum) == left_sum:
            print('found edge ' + str(my) + "  " + str(self.left.data))
        return my+left_sum+right_sum

root = Node(10)
root.insert(19)
root.insert(9)
root.print_node()

root.sum_node()


