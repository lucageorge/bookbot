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

def prepare_report_data(data):
    result = []
    for char, num in data.items():
        result.append({"char": char, "num": num})
    result.sort(key=lambda x: x["num"], reverse=True)
    return result
