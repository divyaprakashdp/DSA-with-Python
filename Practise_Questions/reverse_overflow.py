def reverse(x: int) -> int:
    if x > 0:
        ans = int(str(x)[:: -1])
        return ans if ans < 2**31 else 0
    ans = - int(str(- x)[:: -1])

    return ans if ans > - 2**31 else 0

print(reverse(233))