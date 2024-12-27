
print("How many pencils would you like to use:")
while True:
    try:
        pencils = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
        continue
    if pencils < 1:
        print("The number of pencils should be positive")
        continue
    break
print("Who will be the first (John, Jack):")
while True:
    turn = input()
    if turn == "John" or turn == "Jack":
        break

    print("Choose between 'John' and 'Jack'")

print('|'*pencils)

while True:
    if turn == "John":
        print("John's turn:")
        while True:
            try:
                i = int(input())
            except ValueError:
                print("The number of pencils should be numeric")

            if not (0 < i < 4):
                print("Possible values: '1', '2' or '3'")
                continue
            if pencils - i < 0:
                print("Too many pencils were taken")
                continue
            pencils -= i
            break
    elif turn == "Jack":
        print("Jack's turn:")
        match pencils % 4:
            case 0:
                take = 3
            case 1:
                take = 1  # lose
            case 2:
                take = 1
            case 3:
                take = 2

        print(take)
        pencils -= take

    turn = "Jack" if turn == "John" else "John"

    if pencils == 0:
        if turn == "John":
            print("John won!")
        elif turn == "Jack":
            print("Jack won!")
        break

    print('|' * pencils)

