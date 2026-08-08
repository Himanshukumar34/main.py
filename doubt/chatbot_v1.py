print("Hii ,Iam a chatbot ask me question  , Type thanks for end \n")

responses={
    "hello": "Hi ,I'm Studybot . Ask me anything about your exama! ",
    "exams" :"Exams are tough !Try : 1 topic per hour , short breaks , mock tests ",
    "stress" : "Take a deep breath . sleep matters more than last minute creamming ",
    "maths" : "Pratice 10 problems daily . Focus on steps , not just answers " ,
    "pyhiscs ": "Draw diagrams for every problem . Visulaise before  calculating " ,
    "help" : "I can help with : exams , stress , maths , pyhiscs or chemistry " ,
    "thanks" : "Good luck ! you've got this! "

}
while True:
    user_input=str(input("hello iam chatbot how can i help you : "))
    for i in responses:
        if user_input==i:
            print(responses[i])
