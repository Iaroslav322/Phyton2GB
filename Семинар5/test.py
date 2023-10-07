def fibona44i(limit: int):
    f = fibona44i()
    for i in range(10):
        yield f[-1]
        f.append(f[-1] + f[-2])
        limit -= 1


for number in fibona44i(10):
    print(number)








