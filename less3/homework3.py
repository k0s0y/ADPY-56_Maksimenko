nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class Iterator:
    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.iter_cursor = -1
        self.iter_list_len = len(self.iter_list)

    def __iter__(self):
        self.iter_cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.iter_list[self.iter_cursor]):
            iter(self)
        if self.iter_cursor == self.iter_list_len:
            raise StopIteration
        self.nest_cursor += 1
        return self.iter_list[self.iter_cursor][self.nest_cursor - 1]


def flat_generator(iter_list, ignore_types=(str)):
    for i in iter_list:
        if hasattr(i, '__iter__') and not isinstance(i, ignore_types):
            yield from flat_generator(i)
        else:
            yield i


if __name__ == '__main__':

    iterator_list = [item for item in Iterator(nested_list)]
    print(iterator_list)
    print('-' * 80)

    for item in Iterator(nested_list):
        print(item)
    print('-' * 80)

    generator_list = [item for item in flat_generator(nested_list)]
    print(generator_list)
    print('-' * 80)

    for item in flat_generator(nested_list):
        print(item)
