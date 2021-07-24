def power_set(input):
    '''
    :param input: (list) Starting array of numbers
    :return: (list) All subsets of starting array
    '''

    if (len(input) == 0):
        return [[]]
    else:
        main_subset = []
        for small_subset in power_set(input[1:]):
            main_subset += [small_subset]
            main_subset += [[input[0]] + small_subset]
        return main_subset

print(power_set([1,2,3]))