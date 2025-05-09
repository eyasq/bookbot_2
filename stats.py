def count_words(text):
    splitted = text.split()
    count_words = 0
    for word in splitted:
        count_words+=1
    return count_words

def counter(text):
    letters_dict = {}
    for char in text.lower():
        if char in letters_dict:
            letters_dict[char]+=1
        else:
            letters_dict[char] = 1

    return letters_dict

def sort_on(letters_dict):
    return letters_dict['count']


def report(letters_dict):
    dict_list =[]
    for key,value in letters_dict.items():
        dict_list.append({'char':key, 'count':value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
