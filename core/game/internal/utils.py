from random import randint


def array_shuffle(array: list):
    new_array = array.copy()
    for times in range(20):
        max_index = len(array) - 1
        index1 = randint(0, max_index)
        index2 = randint(0, max_index)
        new_array[index1], new_array[index2] = new_array[index2], new_array[index1]

    return new_array


def text_file_lines(path: str) -> list[str]:
    with open(path) as text_file:
        return text_file.readlines()
