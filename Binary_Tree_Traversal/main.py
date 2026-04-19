class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left

# Pre-order traversal
def pre_order(node):
    def traverse_node(root):
        if root is None:
            return []

        order = [root.data]

        if root.left is not None:
            order = order + traverse_node(root.left)

        if root.right is not None:
            order = order + traverse_node(root.right)

        return order



    return traverse_node(node)

# In-order traversal
def in_order(node, data=[]):
    def traverse_node(root):
        if root is None:
            return []

        order = []

        if root.left is not None:
            order = traverse_node(root.left)

        order = order + [root.data]

        if root.right is not None:
            order = order + traverse_node(root.right)

        return order



    return traverse_node(node)

# Post-order traversal
def post_order(node):
    def traverse_node(root):
        if root is None:
            return []

        order = []

        if root.left is not None:
            order = traverse_node(root.left)

        if root.right is not None:
            order = order + traverse_node(root.right)

        order = order + [root.data]

        return order



    return traverse_node(node)

def example_tests():

    a = Node(5)
    b = Node(10)
    c = Node(2)
    d = Node("leaf")
    a.left = b
    a.right = c
    c.left = d

    def pre_order_tests():
        assert pre_order(a) == [a.data, b.data, c.data, d.data], pre_order(a)
        assert pre_order(b) == [b.data]
        assert pre_order(c) ==  [c.data, d.data]



    def in_order_tests():
        assert in_order(a) == [b.data, a.data, d.data, c.data], in_order(a)
        assert in_order(b) == [b.data]
        assert in_order(c) == [d.data, c.data]

    def post_order_tests():
        assert post_order(a) == [b.data, d.data, c.data, a.data], post_order(a)
        assert post_order(b) == [b.data], post_order(a)
        assert post_order(c) == [d.data, c.data]

    # @test.it('Empty Node Tests')
    # def None_tests():
    #     test.assert_equals(pre_order(None), [])
    #     test.assert_equals(in_order(None), [])
    #     test.assert_equals(post_order(None), [])

    pre_order_tests()
    in_order_tests()
    post_order_tests()

if __name__ == '__main__':
    example_tests()
