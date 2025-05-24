def get_num_words(text):
    return len(text.split())

def get_ascii_distribution(text):
    result = {}
    for c in text.lower():
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result
