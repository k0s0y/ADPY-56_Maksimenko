def cached_decor(cache_size):
    def _cached_decor(old_function):
        CACHE = {}

        def new_function(*args, **kwargs):
            key = f'{args}{kwargs}'
            if key in CACHE:
                return CACHE[key]
            result = old_function(*args, **kwargs)
            if len(CACHE) > cache_size:
                CACHE.popitem()
            CACHE[key] = result
            return result

        return new_function

    return _cached_decor


def decor(foo):
    def new_foo(*args, **kwars):
        print('Код до вызова функции')
        result = foo(*args, **kwars)
        print('Код после вызова функции')
        return result

    return new_foo


def parametrized_decor(parameter):
    def decor(foo):
        def new_foo(*args, **kwars):
            print('Код до вызова функции')
            result = foo(*args, **kwars)
            print('Код после вызова функции')
            return result

        return new_foo

    return decor


def make_trace(old_function):
    def new_function(*args, **kwargs):
        print(f'вызвана функция {old_function.__name__}')
        print(f'с аргументами {args} и {kwargs}')
        result = old_function(*args, **kwargs)
        print(f'Получили {result}')
        print('-' * 120)
        print('\n')
        return result

    return new_function


@parametrized_decor(parameter=None)
def foo():
    pass
