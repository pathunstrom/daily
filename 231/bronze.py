

def generate_row(r):
    rv = []
    length = len(r)
    for i in xrange(length):
        if i == 0:
            rv.append(r[i+1])
        elif i == length - 1:
            rv.append(r[i-1])
        else:
            rv.append(r[i+1] ^ r[i-1])
    return rv


def generate_output(output, rows):
    for _ in xrange(rows):
        yield output
        output = generate_row(output)


def main(initial, length):
    row = map(int, list(initial))
    for row in generate_output(row, length):
        print ''.join(["X" if i else " " for i in row])


def test_generate_row():
    test_row = [1, 1, 1]
    assert generate_row(test_row) == [1, 0, 1]
    test_row = [1, 0, 1]
    assert generate_row(test_row) == [0, 0, 0]
    test_row = [0, 0, 1]
    assert generate_row(test_row) == [0, 1, 0]


def test_generate_output():
    test_input = [1, 1, 1]
    test_val = 5
    test_result = [[1, 1, 1],
                   [1, 0, 1],
                   [0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
    assert [x for x in generate_output(test_input, test_val)] == test_result
    test_input = [1, 1, 0]
    test_result = [[1, 1, 0],
                   [1, 1, 1],
                   [1, 0, 1],
                   [0, 0, 0],
                   [0, 0, 0]]
    assert [x for x in generate_output(test_input, test_val)] == test_result

if __name__ == "__main__":
    test_generate_row()
    test_generate_output()
    main('00000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000', 25)
