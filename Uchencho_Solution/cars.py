print("Welcome to Uchencho's solution\n\nLoading")
import pandas as pd

#Read in saved list of cars from whatsapp (the question)
question = pd.read_table('question.txt', header=None)

#Read in list of all cars saved as a txt file from wikipedia
cars = pd.read_table('list_of_cars.txt')

#Clean and convert the question to a list
question_list = question[0].tolist()
question_list = [line.strip() for line in question_list]

#Clean and convert our 'database' to a list
cars_world = cars.Adelmo.tolist()
clean = [line.split(" ")[0] for line in cars_world]
clean = list(set(clean))
clean = [line.lower() for line in clean]

#Create a dictionary that will store the question and answer(key, value pair)
test_dict = {}
potentials = []

#Loop through the question list searching for the answer
for test in question_list:
    for j in clean:
        if len(test) == len(j) and len(set(test)) == len(set(j)):
            potentials.append(j)
    letters = [line.lower() for line in test]
    for line in sorted(potentials):
        for letter in letters:
            if letter not in line:
                potentials.remove(line)
                break
            else:
                pass
        continue
    try:
        test_dict[test] = potentials[0]
    except Exception as e:
        test_dict[test] = 'Not found'

solution = pd.DataFrame(test_dict, index=['Answer']).T
solution = solution.reset_index()
solution.columns = ['Question', 'Solution']
solution.to_csv("cars_pyfesh_challenge_uchencho.csv", index = False)

print("File has been saved to where the script file was also saved")