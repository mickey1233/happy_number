def ishappy(n):
    visited = []

    while True:
        total = 0
        while n != 0:
            num = n % 10
            total = total + num**2
            n = n // 10
        n = total
        if total in visited:
            return False
        elif total == 1:
            return True
        visited.append(total)


def main():
    print(ishappy(19))
    print(ishappy(2))
    print(ishappy(70))


if __name__ == "__main__":
    main()
