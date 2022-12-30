
def delete_duplicates(data):
    pre_result = dict()

    for i in data:
        if pre_result.get(tuple(i)) is None:
            pre_result[tuple(i)] = i

    result = []

    for i in pre_result:
        result.append(pre_result[i])

    return result


def main():
    print(
        delete_duplicates(
            [
                {"key1": "value1"},
                {"k1": "v1", "k2": "v2", "k3": "v3"},
                {},
                {},
                {"key1": "value1"},
                {"key1": "value1"},
                {"key2": "value2"}
            ]
        )
    )


if __name__ == '__main__':
    main()