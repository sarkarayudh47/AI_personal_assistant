def ask_question(question, answer):
    user_answer = input(question + "\nYour answer: ").strip().lower()
    return user_answer == answer.lower()

def generate_score(questions):
    score = 0
    for question, answer in questions.items():
        if ask_question(question, answer):
            score += 1
    return score

def main():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote 'Hamlet'?": "Shakespeare",
        "What is the largest planet in our solar system?": "Jupiter",
        "What is the chemical symbol for water?": "H2O"
    }

    total_score = generate_score(questions)
    print("Total Score:", total_score)

if __name__ == "__main__":
    main()
