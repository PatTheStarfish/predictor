import random

minimal_length = 100
capital = 1000

prediction_dict = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
                   "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}


def update_prediction(s):
    for i in range(len(s) - 3):
        key = s[i] + s[i + 1] + s[i + 2]
        if s[i + 3] == "0":
            prediction_dict[key][0] += 1
        else:
            prediction_dict[key][1] += 1


def create_profile(min_length):
    data = []
    print("Please give AI some data to learn...")
    print(f"The current data length is 0, {min_length} symbols left")
    while True:
        new_data = input("Print a random string containing 0 or 1:")
        new_data = [x for x in new_data if x == "0" or x == "1"]
        data.extend(new_data)
        data_length = len(data)
        if data_length < min_length:
            print(f"Current data length is {data_length}, {min_length - data_length} symbols left")
        else:
            data = "".join(data)
            update_prediction(data)
            print()
            print("Final data string:")
            print(data)
            print()
            print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
            print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")
            print()
            break


def get_string():
    while True:
        s = input("Print a random string containing 0 or 1:")
        if s == "enough":
            return s
        else:
            s = [x for x in s if x == "0" or x == "1"]
            if len(s) > 0:
                return s


def predict_string(s):
    p = []
    for i in range(3):
        p.append(str(random.randint(0, 1)))

    for i in range(len(s) - 3):
        key = s[i] + s[i + 1] + s[i + 2]
        if prediction_dict[key][0] > prediction_dict[key][1]:
            p.append("0")
        else:
            p.append("1")
    return p


def print_string(s, p, c):
    print("".join(s))
    print("prediction:")
    print("".join(p))
    print()
    count = 0
    for i in range(3, len(s)):
        if s[i] == prediction[i]:
            count += 1
    print(f"Computer guessed right {count} out of {len(s) - 3} symbols ({(count / (len(s) - 3)) * 100:.2f} %)")
    print()
    print(f"Your capital is now ${c}")
    print()


def update_game(s, p, c):
    count = 0
    for i in range(3, len(s)):
        if s[i] == p[i]:
            count += 1
    c = c - count + (len(s) - 3 - count)
    return c


create_profile(minimal_length)

while True:
    input_string = get_string()
    if input_string == "enough":
        print()
        print("Game over!")
        break
    else:
        prediction = predict_string(input_string)
        capital = update_game(input_string, prediction, capital)
        print_string(input_string, prediction, capital)
        update_prediction(input_string)
