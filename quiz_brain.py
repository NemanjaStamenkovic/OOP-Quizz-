class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0                       #stavjamo redni broj pitanja
        self.question_list = q_list                    #pravimo atribut koj asajnuje objektu q_list (svi objekti iz question bank-a)
        self.score = 0                                 #rezultat pravimo 

    def still_has_questions(self):                     #metod koj gleda da li idalje ima pitanja
        return len(self.question_list) > self.question_number      #vraca true ako je broj pitanja iz liste veci od rednog broja pitanja
        
    def next_question(self):
        current_question = self.question_list[self.question_number] #uzima prvo pitanje iz liste question bank
        self.question_number += 1 #dodaje jedan na redni broj jer ne moze da bude prvo pitanje pod rednim brojem 0 
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer): #metod koj proverava da li je unet odgovor tacan ili ne
        if user_answer == correct_answer:
            self.score += 1
            print("correct")
            print(f"Your current score is {self.score}/{self.question_number}")
        else: 
            print("wrong")
            print(f"Your current score is {self.score}/{self.question_number}")
        

