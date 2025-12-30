def words_counter(book_string):
    number_of_words = 0

    list_of_words = book_string.split()
    number_of_words = len(list_of_words)

    return number_of_words

def characters_counter(book_string):
    lower_book_string = book_string.lower()

    tablica_znakow = []

    for character in lower_book_string:
        if (character in tablica_znakow) == False:
            tablica_znakow.append(character)

    cnt = 0
    slownik={}

    for znak in tablica_znakow:
        for letter in lower_book_string:
            if letter == znak:
                cnt += 1

        slownik[znak]=cnt
        cnt = 0

    return slownik

def sort_on(items):
    return items["num"]

def sortownica(dict):

    list_of_dict = []

    for unit in dict:
        temp_dict={}
        temp_dict["char"]=unit
        temp_dict["num"]=dict[unit]
        list_of_dict.append(temp_dict)

    list_of_dict.sort(reverse=True, key=sort_on)

    return list_of_dict