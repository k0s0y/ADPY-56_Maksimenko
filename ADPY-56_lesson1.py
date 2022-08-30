import re

text = 'Что такое регулярные выражения и как их использовать? ' \
       'Говоря простым языком, регулярное выражение — это последовательность символов, ' \
       'используемая для поиска и замены текста в строке или файле. Как уже было упомянуто, ' \
       'их поддерживает множество языков общего назначения: Python, Perl, R. ' \
       'Так что изучение регулярных выражений рано или поздно пригодится!'

# подсчет количества слов
pattern = r"\w+"
words_list = re.findall(pattern, text)
# print(words_list)
# print(len(words_list))

# подсчет количества предложений
pattern2 = r"[.!?]"
sent_list = re.split(pattern2, text)
# удаляем пустое предложение
sent_list.remove('')
# print(sent_list)
# print(len(sent_list))

pattern3 = r"регулярн\w+ выражен\w+"
result = re.search(pattern3, text)
# print(result)
# print(result.group())
# выводим начало и конец в строке (span)
# print(result.start(), result.end())

# Меняем регулярные выражения на "Regex"
result_sub = re.sub(pattern3, "Regex", text)
# print(result_sub)
