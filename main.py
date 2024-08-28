import os
import subprocess
import sys
import json
from Player import Player

def main():
    loadQuizzes()

# TODO: get the data from the JSON file
def loadQuizzes():
    with open('./quizzes.json', encoding="utf-8") as read_json:
        decoded = json.load(read_json)
    print(decoded)
    # get the entire json object
    # json.JSONDecoder()
    # split it into individual objects
    # populate each of these objects into a quiz class



# TODO: Populate a quiz class

# TODO: Be able to display titles of each quiz in a list

# TODO: Display a single question in a quiz

# TODO: Display all answers of a question in a quiz

# TODO: Choose an answer and display if the answer was correct

main()
