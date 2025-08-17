def get_word_count(file_contents):
    wordcount = 0
    parsestring = file_contents.split()
    for w in parsestring:
        wordcount += 1
    return wordcount

def get_char_count(file_contents):
    chardict = {}
    parsestring = file_contents
    for c in parsestring:
        char = c.lower()
        if char not in chardict:
           chardict[char] = 1
        else:
           value = chardict[char]
           chardict[char] = value + 1
    return chardict

def sort_on(items):
    return items["num"]

def sort_char_dict(chardict):
    sorted_dict = {}
    sorted = []
    for s in chardict:
        print(chardict[s])
        sorted_dict["char"] = s
        sorted_dict["num"] = chardict[s]
        sorted.append(sorted_dict)
        sorted_dict = {}

    sorted.sort(reverse = True, key = sort_on)
    return sorted