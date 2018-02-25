#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in random order, along with the answer key

import random

#The quiz data. Keys are states and values are their capitals
teams = {'Orlando': 'Magic','Miami': 'Heat','Atlanta': 'Hawks','Charlotte': 'Hornets','New York': 'Knicks','Brooklyn': 'Nets','Boston': 'Celtics','Minnesota': 'Timberwolves','Dallas': 'Mavericks','Houston': 'Rockets','San Antonio': 'Spurs','Oklahoma City': 'Thunder','Denver': 'Nuggets','Utah': 'Jazz','Portland': 'Trailblazers','New Orleans': 'Pelicans','Los Angeles': 'Lakers','Cleveland': 'Cavs'}

#Generate 35 quiz files
for quizNum in range(35):
    #Create the quiz and answer key files
    quizFile = open('nbaquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('nbaquiz_answer%s.txt' % (quizNum + 1 ), 'w')

    #Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(('' * 20) + 'NBA Team Name Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')    
    
    #Shuffle the order of the team
    cities = list(teams.keys())
    random.shuffle(cities)
    
    #Loop through all teams, making a question for each
    for questionNum in range(15):
        #Get right and wrong answers
        correctAnswer = teams[cities[questionNum]]
        wrongAnswers = list(teams.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        #Write the question and answer options to the quiz file
        quizFile.write('%s. What team plays at %s?\n' % (questionNum + 1, cities[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        #Write the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()