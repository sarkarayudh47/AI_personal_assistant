import sqlite3

def fetch_questions_from_database():
    # Connect to your database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Fetch questions and answers from the database
    cursor.execute("SELECT question, answer FROM questions")
    questions = cursor.fetchall()

    # Close the database connection
    conn.close()

    return questions

def ask_question(question, answer):
    user_answer = input(question + "\nYour answer: ").strip().lower()
    return user_answer == answer.lower()

def generate_score(questions):
    score = 0
    for question, answer in questions:
        if ask_question(question, answer):
            score += 1
    return score

def main():
    questions = fetch_questions_from_database()

    total_score = generate_score(questions)
    print("Total Score:", total_score)

if __name__ == "__main__":
    main()
