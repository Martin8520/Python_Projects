n = int(input())

result = ""
counter = None


for i in range(n):
    int_str = input()

    if (int_str.lstrip('-')).isdigit():
        if counter is not None and (counter.lstrip('-')).isdigit():
            counter = str(int(counter) + int(int_str))
        else:
            if counter is not None:
                result += counter + "\n"
            counter = int_str
    else:
        if counter is not None and (counter.lstrip('-')).isdigit():
            result += counter + "\n"
            counter = None
        if counter is not None:
            result += counter + "-"
        counter = int_str

if counter is not None:
    result += counter

print(result)
