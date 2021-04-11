
import sys


def main():
    if (len(sys.argv) < 1):
        return

    if (sys.argv[1].lower() == "b"):
        print(find_body(int(sys.argv[2])))
    elif (sys.argv[1].lower() == "l"):
        print(find_list(int(sys.argv[2])))
    elif (sys.argv[1].lower() == "d"):
        print(get_double_arrow(int(sys.argv[2])))
    elif (sys.argv[1].lower() == "s"):
        print(get_single_arrow(int(sys.argv[2])))


# Given an integer, returns its << >> encoding
# eg get_double_arrow(8) = 3, 0
def get_double_arrow(a):
    if (a == 0):
        return 0, 0
    temp = a
    x = 0
    while (temp % 2 == 0):
        temp /= 2
        x += 1
    y = a / (2 ** x)
    return int(x), int((y-1)/2)

# Given an integer, returns its < > encoding
# eg get_single_arrow(27) = 2, 3
def get_single_arrow(a):
    if (a == 0):
        return 0, 0
    return get_double_arrow(a+1)

# Given an integer, returns its representation as a list
def find_list(a):
    result = []
    while True:
        x, l = get_double_arrow(a)
        result.append(x)
        if (l == 0):
            break
        a = l
    return result

    # Given an integer, returns its representatin as an instruction body
def find_body(a):
    if a == 0:
        return "HALT"
    x, y = get_double_arrow(a)
    if (x % 2 != 0):
        j, k = get_single_arrow(y)
        return "R{}-  ->  L{}, L{}".format(int((x-1)/2), j, k)
    return "R{}+  ->  L{}".format(int(x/2), y)

if __name__ == '__main__':
    main()
