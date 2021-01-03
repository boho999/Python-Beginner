i = ""

while( i != "q"):
    i = input("Pls add an integer number: ")

    if i == "q":
        print("Received 'q'. Will exit.")
        raise SystemExit(0)

    try:
        a = int(i)
    except ValueError:
        print (f"The value {i} is not an integer")
        # raise SystemExit(0)
        continue

    if int(i)%2 == 0:
        print(f"The number entered {i} is even")
    else:
        print(f"The number {i} is odd")
