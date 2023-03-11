#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, mul, sub, div

    argv = sys.argv[1:]
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    arg1 = int(argv[0])
    arg2 = int(argv[2])
    op = argv[1]
    ans = None
    if op == '+':
        ans = add(arg1, arg2)
    elif op == '-':
        ans = sub(arg1, arg2)
    elif op == '*':
        ans = mul(arg1, arg2)
    elif op == '/':
        ans = div(arg1, arg2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {:s} {:d} = {:d}".format(arg1, op, arg2, ans))
