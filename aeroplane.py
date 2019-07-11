def solution(N: int, S: str) -> int:
    """
    return option count
    """
    n= 3
    taken = [[] for _ in range(N)]
    for s in S.split(" "):
        row = int(s[:-1]) - 1
        if row > N:
            raise Exception("illegal reservation")

        taken[row].append(ord(s[-1]) - ord('A'))

    total_cnt = 0
    for row in taken:
        row.sort()
        row.append(ord('K') - ord('A') + 1)
        last = -1

        cnt = 0
        for idx in range(len(row)):
            free_seats = row[idx] - last - 1
            cnt += max(0, free_seats - (n - 1))
            last = row[idx]

        total_cnt += cnt

    return int(total_cnt/3)


print(solution(1,' '))