input = [91, 2, 2, 1, 2002, 0.1]
# output = []
# i = 0

def sort(input, output, i):
    global index_min

    if not (len(input) == 0) and (len(input) != 1):
        len_index = len(input) - 1
        min = input[0]

        for elem in input:
            if (min >= input[len_index - i]):  # Was finded the number, that is smaller than currently number
                min = input[len_index - i]
                index_min = len_index - i
                i += 1
            else:
                i += 1

        # Minimum was founded on i-th iteration

        input.pop(index_min)
        output.append(min)
        i=0;
        sort(input, output,i)
        return output

    else:
        output.append(input[0])


res = sort(input, output=[], i=0)
