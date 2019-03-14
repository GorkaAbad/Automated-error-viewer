import urllib.request
import json

langugage =""
error = ""
baseUrl ="https://api.stackexchange.com/2.2/"
search = "search?order=desc&sort=relevance"
tag="&tagged=" + language
title= "&intitle=" + error
site ="&site=stackoverflow"

#Conseguir el error y el lenguaje de programacion

url = baseUrl + search + tag + title + site


response = urllib.request.urlopen(url).read()
status = response.status
content = ""
title = ""
link ""
answer_count = 0
cont = 0
answers = {}

if status == 200:
    print("    ANSWERS FOUND   ")
    content = response.content
    contentJson = content.loads(content)
    for items in contentJson["items"]:
        title = items["title"]
        link = items["link"]
        answer_count = items["answer_count"]
        aceptedAnswer = items["accepted_answer_id"]
        answers.update({cont : link})
        print("  #" + cont + "  " + title " Answers: " + answer_count)
        print("")

    print("So... which one you choose?")
    selection = input("Please enter a number: ")

    while input < 0 and input > cont:
        selection = input("Please enter a number: ")
