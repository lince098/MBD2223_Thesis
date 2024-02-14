def random_function_to_misguide_the_model_1(a=None, b=2, c="random words"):
    if a is None:
        a = []
    a.append(b + 2)
    splitted = c.split(" ")
    a.append(splitted)
    return a


def this_is_the_same_function(second_try):
    first_range_variable = 4 / 2

    if not (second_try != 0 and second_try != 1):
        return 1

    to_confuse = 1
    the_model = 1

    for useless_variable in range(first_range_variable, second_try + 1):
        temp = the_model

        the_model = to_confuse + the_model
        to_confuse = temp

    return the_model


def random_function_to_misguide_it_again(a=None, b=2, c="random words"):
    if a is None:
        a = []
    a.append(b + 2)
    splitted = c.split(" ")
    a.append(splitted)
    return a
