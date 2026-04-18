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
def in_order(node):
    return []

# Post-order traversal
def post_order(node):
    return []

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

    pre_order_tests()

    # @test.it('In-order Tests')
    # def in_order_tests():
    #     test.assert_equals(in_order(a), [b.data, a.data, d.data, c.data])
    #     test.assert_equals(in_order(b), [b.data])
    #     test.assert_equals(in_order(c), [d.data, c.data])

    # @test.it('Post-order Tests')
    # def post_order_tests():
    #     test.assert_equals(post_order(a), [b.data, d.data, c.data, a.data])
    #     test.assert_equals(post_order(b), [b.data])
    #     test.assert_equals(post_order(c), [d.data, c.data])

    # @test.it('Empty Node Tests')
    # def None_tests():
    #     test.assert_equals(pre_order(None), [])
    #     test.assert_equals(in_order(None), [])
    #     test.assert_equals(post_order(None), [])

if __name__ == '__main__':
    example_tests()
