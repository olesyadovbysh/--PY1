def get_count_char(str_):

    str_ = str_.lower()
    symbol_dict = {}
    DEFAULT = 0
    for symbol in str_:
        if symbol.isalpha() == True:
            symbol_dict[symbol] = symbol_dict.get(symbol, DEFAULT) + 1
    return symbol_dict

def percent_char(dict_):
    symbol_percent = {}
    total_value = sum(dict_.values())
    for symbol in dict_:
        symbol_percent[symbol] = 100 * dict_[symbol] / total_value
        symbol_percent[symbol] = round(symbol_percent[symbol], 2)
    return symbol_percent

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_dict = get_count_char(main_str)

print(get_count_char(main_str))
#print(percent_char(main_dict))
