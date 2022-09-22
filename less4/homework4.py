import logging


def decorator(log_path='log.log'):
    logging.basicConfig(level=logging.DEBUG, filename=log_path, filemode='a',
                        format='%(asctime)s %(message)s')

    def hw_decorator(old_func):
        def wrapper(*args, **kwargs):
            result = old_func(*args, **kwargs)
            logging.debug(f"\nНазвание функции: {old_func.__name__}\n"
                          f"Аргументы функции: {args, kwargs}\n"
                          f"Результат функции: {result}\n")
            return result

        return wrapper

    return hw_decorator
