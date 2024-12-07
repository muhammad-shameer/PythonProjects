# list of questions and their answers
questions = [
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1],
    ["Question\na.something\nb.something\nc.something\nd.something", 1]
]

# money ladder
money_ladder = [
    100, 200, 300, 500, 1_000,                       # levels 1-5: safe level at 5
    2_000, 4_000, 8_000, 16_000, 32_000,             # levels 6-10: safe level at 10
    64_000, 125_000, 250_000, 500_000, 1_000_000     # levels 11-15
]

safe_levels = {
    5 : 1_000,
    10 : 32_000
}

def main():
    money_earned = 0
    for level, question in enumerate(questions):
        print(f"{level + 1}. {question[0]}")
        print("")
        usr_input = int(input("Enter the correct choice: "))
        if usr_input == question[1]:
            money_earned = money_ladder[level]
            print("That is correct!")
            if (level + 1) == len(questions):
                print("You are a Millionaire!")
            else:
                print(f"You have reached level {level + 2}")
            print(f"You have earned: ${money_earned}")
            print("")
        else:
            print("The answer is incorrect!")
            last_safe_level = max([l for l in safe_levels if l <= (level + 1)], default=0)
            money_earned = safe_levels.get(last_safe_level, 0)
            break
    print(f"You earned ${money_earned}")

if __name__ == "__main__":
    main()