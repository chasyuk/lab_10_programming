def tree_by_levels(node, tree_sorted=[]):
    if node is None:
        return []

    levels_list = []

    def traverse_node(node, level):
        if node is None:
            return

        if len(levels_list) == level:
            levels_list.append([])

        levels_list[level].append(node.value)

        traverse_node(node.left, level + 1)
        traverse_node(node.right, level + 1)

    traverse_node(node, 0)

    tree_sorted = []
    for level in levels_list:
        tree_sorted.extend(level)

    return tree_sorted
