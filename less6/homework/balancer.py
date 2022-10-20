from Stack import Stack


def balancer(line: str):
    list_of_brackets = list(line)
    brackets_dict = {')': '(', '}': '{', ']': '['}
    m_stack = Stack()
    for bracket in list_of_brackets:
        if bracket in ['(', '{', '[']:
            m_stack.push(bracket)
        if bracket in [')', '}', ']']:
            if m_stack.peek() == brackets_dict[bracket]:
                m_stack.pop()
            else:
                return False
    return True


if __name__ == '__main__':
    task_list = ('(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]')

    for task in task_list:
        if balancer(task):
            print('Сбалансированно')
        else:
            print('Несбалансированно')
