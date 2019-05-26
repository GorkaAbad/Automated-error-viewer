import urllib.request

import sys

import subprocess

import urllib.parse

import requests 

import webbrowser

#Ejecuta el archivo que pasan como parametro

def execute(path):

    print("Ejecutando el archivo: " , path)
    #execfile(path)

    #or

    #theproc = subprocess.Popen([sys.executable, path])

    #theproc.communicate()

    globals=None
    locals=None
    description=''
    try:
        exec(open(path).read())
    except SyntaxError as err:
        print("Error de sintaxis")
        error_class = err.__class__.__name__
        detail = err.args[0]
        line_number = err.lineno
    except Exception as err:
        print("Otra excepcion")
        error_class = err.__class__.__name__
        detail = err.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = traceback.extract_tb(tb)[-1][1]
    else:
        return
    print("Tienes un error")
    print("%s at line %d of %s: %s" % (error_class, line_number, description, detail))
    return detail
 

def run_command(command):

    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

    while True:

        output = process.stdout.readline()

        if output == '' and process.poll() is not None:

            break

        if output:

            #print output.strip('0')

         rc = process.poll()

    return rc

 

#Hace la peticion a la url creada y devuelve el objeto

def make_request(url):

    print("Haciendo la peticion")

    response = requests.get(url)

    return response.json(), response.status_code

 

#Gestiona la respuesta

def manage_response(response, status):

    print("Gestionando la respuesta")

    content = ""

    title = ""

    link = ""

    answer_count = 0

    cont = 0

    answers = {}

    
    print("Status: " , status)

    if status == 200:

        print("    ANSWERS FOUND   ")

        for items in response["items"]:

            title = items["title"]

            link = items["link"]

            score = items["score"]

            answer_count = items["answer_count"]

            answered = items["is_answered"]

            answers.update({cont : link})

            print("  #" , cont , "  " , title , "Score: " , score ,  " Answers: " , answer_count, "Answered?: " , answered)

            print("")

            cont = cont + 1
 

        print("Or type 'n' to close.")
        print("So... which one you choose?")

        selection = input("Please enter a number: ")

        if selection == 'n':
            sys.exit()
        while int(selection) < 0 or int(selection) > cont:

            selection = input("Please enter a number: ")

        manage_answers(answers[int(selection)])

 

#Hace una peticion a la url con la respuesta de la pregunta

def manage_answers(url):
    webbrowser.open_new(url)
 

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



filePath = sys.argv[1].lower()

print("Detectando lenguaje ...")
language = get_language(filePath)
print("lenguaje: " , language)
 

#Conseguir el error y el lenguaje de programacion

error = execute(filePath)

if error != None:
    baseUrl ="https://api.stackexchange.com/2.2/"

    search = "search?order=desc&sort=relevance"

    tag="&tagged=" + language

    error = urllib.parse.quote(error)
    title= "&intitle=" + error

    site ="&site=stackoverflow"

    url = baseUrl + search + tag + title + site

    print("Url generada: " , url)

    response, status = make_request(url)

    manage_response(response, status)
