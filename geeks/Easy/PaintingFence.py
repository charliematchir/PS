

def fense(n, k):
    mod = 1000000007
    same, diff, total = 0, 0, k
    prev_total, prev_diff = k, k

    total = k
    

    for i in range(1, n):
        diff = prev_total * (k-1)
        same = prev_diff

        total =  diff + same
        prev_total = total

    print(total)


def main():
    fense(2, 4)


if __name__== '__main__':
	main()

