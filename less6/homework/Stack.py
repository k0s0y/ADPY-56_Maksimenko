class Stack:
    def __init__(self):
        self.stack = []

    # isEmpty - проверка стека на пустоту. Метод возвращает True или False.
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    # push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, value):
        self.stack.append(value)

    # pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    # peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    # size - возвращает количество элементов в стеке.
    def size(self):
        return len(self.stack)
