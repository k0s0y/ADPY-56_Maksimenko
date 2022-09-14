nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

iterator_list = [item for item in nested_list]
print(iterator_list)