import argparse


def myparser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-f", "--filename", help="Enter the file name to be used to write the data")
    parser.add_argument(
        "-m", "--maxnum", help="Enter the file name to be used to write the data", type=int)
    args = parser.parse_args()
    # print(args.filename)
    return args


def filewriter(text, fname="out.txt"):
    with open(fname, "wt") as f:
        f.writelines(text)


def isprime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    args = myparser()
    print(f"The number u wanted to find the max prime is {args.maxnum}")
    print(f"The file u wanted to save the max prime is {args.filename}")
    largestPrime = -1
    print(f"*******************Processing*******************")
    for i in reversed(range(args.maxnum)):
        if isprime(i):
            largestPrime = i
            break
    print(f"*******************Processing Completed*******************")
    print(f"The largest prime is {largestPrime}")

    print(f"*******************Writing to a file*******************")

    filewriter(f"The largest prime is {largestPrime}", args.filename)

    print(f"*******************File writing successful*******************")

# python .\Main_argparser.py -f test.txt -m 100
# python .\Main_argparser.py -h
