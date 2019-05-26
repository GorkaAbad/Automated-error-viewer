import urllib.request

import json

import sys

import subprocess

filePath = sys.argv[1].lower()

langugage =get_language(filePath)

 

error = ""

baseUrl ="https://api.stackexchange.com/2.2/"

search = "search?order=desc&sort=relevance"

tag="&tagged=" + language

title= "&intitle=" + error

site ="&site=stackoverflow"

 

#Conseguir el error y el lenguaje de programacion

 

url = baseUrl + search + tag + title + site

 

execute(filePath)

response = make_request(url)

manage_response(response)

 

#Ejecuta el archivo que pasan como parametro

def execute(path):

    #execfile(path)

    #or

    exec(open(path).read())

    #or

    #theproc = subprocess.Popen([sys.executable, path])

    #theproc.communicate()

 

def run_command(command):

    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

    while True:

        output = process.stdout.readline()

        if output == '' and process.poll() is not None:

            break

        if output:

            print output.strip('0')

    rc = process.poll()

    return rc

 

#Hace la peticion a la url creada y devuelve el objeto

def make_request(url):

    response = urllib.request.urlopen(url).read()

    return response

 

#Gestiona la respuesta

def manage_response(response):

    status = response.status

    content = ""

    title = ""

    link = ""

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

            print("  #" , cont , "  " , title , " Answers: " , answer_count)

            print("")

 

        print("So... which one you choose?")

        selection = input("Please enter a number: ")

 

        while selection < 0 and selection > cont:

            selection = input("Please enter a number: ")

 

        manage_answers(answers.get(input))

 

#Hace una peticion a la url con la respuesta de la pregunta

def manage_answers(url):

    response = make_request(url)

 

    #Web scraping?

 

 

 

def get_language(file):

    if file.endswith('.py'):

        return "Python"

    elif file.endswith('.java'):

        return "Java"

    elif file.endswith('.go'):

        return "Go"

    elif file.endswith('.rb'):

        return "Ruby"

    elif file.endswith('.js'):

        return "JavaScript"

    elif file.endswith('.java'):

        return "Java"

    elif file.endswith('.c'):

        return "C"

    else:
        raise Exception("Language unknown.") #Error, lenguaje no conocido