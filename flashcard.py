import ast
import re
from random import shuffle
choice = raw_input("Enter if you would like to add a question(aq) or get asked a question(q): ")
if choice == "aq":
"""Enters the question and the answer for the question"""

    question = raw_input("Enter the question: ")
    answer = raw_input("Enter the answer: ")
    questionType = raw_input("Chemistry(C), Biology/Ecology(BE), Space(S), Electricity(E): ")
    questionFile = open("scienceQuestions", "a")
    scienceQuestion = "\n" + question + ":" + questionType
    questionFile.write(scienceQuestion)
    dictionar = {}
    answerFile = open("scienceAnswers", "r")
    dictionar = ast.literal_eval(answerFile.readline())
    dictionar[scienceQuestion] = answer
    answerFile = open("scienceAnswers", "w")
    answerFile.write(str(dictionar))

elif choice == "q":
    questionType = raw_input("Chemistry(C), Biology/Ecology(BE), Space(S), Electricity(E): ")
    questionType = ":" + questionType
    with open("scienceQuestions.py",'r') as f:
        lineList = f.readlines()
    res = [re.sub("\:[A-Z]+", '', i) for i in lineList if questionType in i]
    shuffle(res)
    answerFile = open("scienceAnswers", "r")
    dictionar = ast.literal_eval(answerFile.readline())
    for j in res:
        askQuestion = raw_input(j)
        print(j)
        answer = dictionar['\n' + j.strip() + questionType]
        print(answer)
