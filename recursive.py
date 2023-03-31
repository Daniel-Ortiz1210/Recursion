def pyramind_sum(lower, upper, margin=0):
    blanks = ' ' * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, '0')
        return 0
    else:
        result = lower + pyramind_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result


if __name__ == '__main__':
    pyramind_sum(1, 5)
