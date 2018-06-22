def convert_int(c):
    if c == 'I':
        return 1
    elif c == 'V':
        return 5
    elif c == 'X':
        return 10
    elif c == 'L':
        return 50
    elif c == 'C':
        return 100
    elif c == 'D':
        return 500
    elif c == 'M':
        return 1000
    else:
        return None


def roman_to_int(s):
    data = 0
    tmp = 0
    for c in reversed(s):
        if convert_int(c) >= tmp:
            tmp = convert_int(c)
            data += tmp
        else:
            tmp = convert_int(c)
            data -= tmp
    return data


dic = {}


def convert_str(line):
    s = ''
    res = ''
    lis = line.split(' ')
    if convert_int(lis[-1]) is not None:
        dic[lis[0]] = lis[-1]
        # print(line)
    elif lis[-1] == 'Credits':
        dic[lis[2]] = int(lis[-2]) / int(roman_to_int(dic[lis[0]] + dic[lis[1]]))
        # print(line)
    elif lis[1] == 'much':
        for r in lis[3:-1]:
            s += dic[r]
            res += r + ' '
        res += 'is ' + str(roman_to_int(s))
        print(res)
    elif lis[1] == 'many':
        for r in lis[4:-2]:
            s += dic[r]
            res += r + ' '
        res += lis[-2] + ' is '
        res += str(int((roman_to_int(s) * dic[lis[-2]])))
        res += ' Credits'
        print(res)
    pass


if __name__ == '__main__':
    f = open('input.txt', 'r')
    line = f.readline()
    while line:
        # print(line)
        try:
            convert_str(line.strip())
        except KeyError as e:
            print('I have no idea what you are talking about')
        line = f.readline()
    pass
