def divide_by_zero():
    try:
        result = 5 / 0
        return result
    except ZeroDivisionError as e:
        return f"Error: {e}"


result = divide_by_zero()
print(result)


def generate_all_sentences():
    subjects = ["Americans", "Indians"]
    verbs = ["play", "watch"]
    objects = ["Baseball", "Cricket"]

    for subject in subjects:
        for verb in verbs:
            for obj in objects:
                sentence = f"{subject} {verb} {obj}."
                print(sentence)
                
generate_all_sentences()
