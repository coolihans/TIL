def run(n):
    if n == 5:
        return

    print(n)
    run(n-1)
    print(n)
    return

run(10)