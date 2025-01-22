import sys


def solution():
    sys_input = sys.stdin.readline

    tc = int(sys_input())
    for _ in range(tc):
        _ = int(sys_input())

        white, black = 0, 0
        for a, b in zip(sys_input().rstrip(), sys_input().rstrip()):
            if a == b:
                continue

            if a == 'W':
                white += 1
            else:
                black += 1

        print(max(white,black))


solution()