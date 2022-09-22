# nested_list = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None],
# ]
#
# iterator_list = [item for item in nested_list]
# print(iterator_list)

mylistsimple = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]


mylisthard = [
[],
[1, [2], 3, 4, [5, 6, 7]],
[8, 9, 10, 11],
[12, 13, 14, [[[[15]]]]], []
]


class FlatIterator:

    def __init__(self, multi_list):

        self.multi_list = multi_list  # список с воложенными списками

    def __iter__(self):
        self.multi_list_iter = iter(self.multi_list)
        self.nested_list = []  # вложенный список с элементами
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1
        if len(self.nested_list) == self.nested_list_cursor:
            self.nested_list = None
            self.nested_list_cursor = 0
            while not self.nested_list:
                self.nested_list = next(self.multi_list_iter)
                #  если  список пустой, то получаем следующий
                #  если списки закончаться, получим stop iteration

        return self.nested_list[self.nested_list_cursor]