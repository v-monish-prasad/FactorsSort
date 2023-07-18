def numberOfFactors(number):
    noOfFactors, iterator = 1, 2

    while iterator * iterator <= number:
        if number % iterator == 0:
            if iterator < number // iterator:
                noOfFactors += 2
            else:
                noOfFactors += 1
        iterator += 1

    return noOfFactors


def factorsSort(array):
    array.sort(key=lambda x: (numberOfFactors(x), x))

    return array


if __name__ == "__main__":
    A = list(map(int, input().strip('[').strip(']').split(',')))

    print(factorsSort(A))
