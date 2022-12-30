def hash_dict(data):
    res = []

    for i in data:
        res.append(f"{i}-{data[i]}")

    return ",".join(res)



def delete_duplicates(data):
    pre_result = dict()

    for i in data:
        if pre_result.get(hash_dict(i)) is None:
            pre_result[hash_dict(i)] = i

    result = []

    for i in pre_result:
        result.append(pre_result[i])

    return result


def main():
    print(
        delete_duplicates(
            [
                {"1": "2"},
                {"1": "2"},
                {"1": "2"},
                {"1": "3"},
            ]
        )
    )


if __name__ == '__main__':
    main()