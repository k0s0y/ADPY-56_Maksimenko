import requests
import datetime
from pympler.asizeof import asizeof
from pprint import pprint

# Измеряем вес объекта

my_list = [1,2,3,4,5,6,7]
my_range = range(1,100000)

def memory_value(obj):
    print(asizeof(obj))

# if __name__ == '__main__':
#     memory_value(my_range)
#     memory_value(list(my_range))

# --------------------------------


# итератор для вывода диапазона по датам

# class DataRange:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         self.cursor = self.start - datetime.timedelta(days=1)
#         return self
#
#     def __next__(self):
#         self.cursor += datetime.timedelta(days=1)
#
#         if self.cursor >= self.end:
#             raise StopIteration
#         return self.cursor
#
#
# for item in DataRange(datetime.date(2022,1,1),datetime.date(2022,1,10)):
#     print(item)
# ----------------------------------
# class SwapiPeople:
#
#     base_url = 'https://swapi.dev/api/people/'
#
#     def __iter__(self):
#         self.page = 0
#         self.results = iter([])
#         return self
#
#     def __next__(self):
#
#         try:
#             item = next(self.results)
#         except StopIteration:
#             self.page += 1
#             response = requests.get(self.base_url, params={'page': self.page}).json()
#             if not response.get('next'):
#                 raise StopIteration
#             results = response['results']
#             self.results = iter(results)
#             item = next(self.results)
#         return item
#
#
#
# for charachter in SwapiPeople():
#     print(charachter)
# ----------------------------------
def swapiPeople():
    page = 1
    base_url = 'https://swapi.dev/api/people/'

    next_page = True
    while next_page:
        response = requests.get(base_url, params={'page': page}).json()
        results = response['results']
        for item in results:
            # yield item # выводим все
            yield item['name'] # выводим только имя
        next_page = response.get('next')
        page += 1


# for charachter in swapiPeople():
#     print(charachter)

#---------------------------------------------------------

numbers = [1, 2, 4, 5]
numbers = [item ** 2 for item in numbers]
print(numbers)