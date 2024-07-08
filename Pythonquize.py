class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, options, correct_answer):
        print(question)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        
        while True:
            try:
                user_answer = int(input("Enter your answer: "))
                if 1 <= user_answer <= len(options):
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and", len(options))
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        if options[user_answer - 1] == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print("Incorrect")
    
    def start(self):
        for question in self.questions:
            self.ask_question(question['question'], question['options'], question['correct_answer'])
            
        
        print(f"Your final score is {self.score} out of {len(self.questions)}.")

if __name__ == "__main__":
    # Customize your quiz questions here
    quiz_questions = [
        {
            "question":" Which bird lays the largest egg?",
            "options": ["Owl", "Ostrich", "Kingfisher", "Woodpecker"],
            "correct_answer": "Ostrich"
        },

        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_answer": "Mars"
        },

        {
            "question": "What is a group of lions called?",
            "options": ["Drift", "Flock", "Drove" ,"Pride"],
            "correct_answer": "Pride"
        },

        {
           "question": "What is the longest river in the world?",
           "options" : ["Ganga River" , "Narmada River" , "Penna River" , "The Nile"],
           "correct_answer": "The Nile"

        },

        {
           "question": "What is the term for the ability of an AI system to learn from data and improve its performance over time?",
           "options": ["cloud computing" , "Machine Learing" , "Artificial intelligence" , "None the above"],
           "correct_answer": "Machine Learing"
        },
    ]

    quiz = Quiz(quiz_questions)
    quiz.start()
