# KBC Quiz Game

def kbc_game():
    # Questions list
    questions = [
        ["What is the capital of Bangladesh?", "A. Dhaka", "B. Chittagong", "C. Khulna", "D. Sylhet", "A"],
        ["Which language is used for Python?", "A. English", "B. Programming Language", "C. Machine Code", "D. Binary", "B"],
        ["2 + 2 = ?", "A. 3", "B. 4", "C. 5", "D. 6", "B"],
        ["Which planet is known as Red Planet?", "A. Earth", "B. Mars", "C. Jupiter", "D. Venus", "B"],
        ["Who developed Python?", "A. Elon Musk", "B. Bill Gates", "C. Guido van Rossum", "D. Mark Zuckerberg", "C"]
    ]

    # Prize money for each question
    prizes = [1000, 2000, 5000, 10000, 20000]

    total_money = 0

    print("🎉 Welcome to KBC Game 🎉\n")

    for i in range(len(questions)):
        q = questions[i]
        print(f"\nQuestion {i+1} for Tk {prizes[i]}:")
        print(q[0])

        # Print options
        for option in q[1:5]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q[5]:
            print("✅ Correct Answer!")
            total_money = prizes[i]
        else:
            print("❌ Wrong Answer!")
            print(f"Correct answer was: {q[5]}")
            break

    print("\n🏁 Game Over!")
    print(f"💰 You are taking home: Tk {total_money}")


# Run the game
kbc_game()
