from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = [] 

for x in question_data: 
    question_text = x["text"]                               #izvlaci text u obliku pitanja iz question_data
    question_answer = x["answer"]                           #izvlaci odgovore iz questions_data
    new_question = Question(question_text, question_answer) #koristimo klasu da za svaki x iz question_date napravi objekat sa svojim pitanjem i odgovorom
    question_bank.append(new_question)                      #ta izvucena pitanja stavljamo u nasu novu listu question_bank[]


quizz = QuizBrain(question_bank)                            
while quizz.still_has_questions():
    quizz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quizz.score}/{quizz.question_number}")