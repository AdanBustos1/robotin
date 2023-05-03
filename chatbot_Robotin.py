from pywebio.platform.flask import webio_view
from pywebio.platform.flask import start_server
from pywebio import STATIC_PATH
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import nltk
from nltk.chat.util import Chat, reflections
"""Un pequeño chatbot, algo mas o menos original, espero."""
pairs = [
    [
        r"mi nombre es (.*)",
        ["Hola %1, ¿cómo estás?", "Hola %1, ¿en qué puedo ayudarte?"]
    ],
    [
        r"hola|buenos dias|buenas tardes|buenas",
        ["Hola, ¿en qué puedo ayudarte?"]
    ],
    [
        r"cual es tu nombre",
        ["Mi nombre es Robotin y soy un chatbot creado con PyWebIO y NLTK.", "Puedes llamarme Robotin"]
    ],
    [
        r"como estas",
        ["Estoy bien, gracias por preguntar", "¡Genial! ¿Y tú?"]
    ],
    [
        r"que puedes hacer",
        ["Puedo ayudarte con cualquier pregunta que tengas", "Puedo ofrecerte información sobre diversos temas", "Puedo darte recomendaciones si necesitas alguna"]
    ],
    [
        r"quien eres",
        ["Soy Robotin, un chatbot creado con PyWebIO y NLTK", "Puedes llamarme Robotin", "Soy tu amigo virtual Robotin, ¿en qué puedo ayudarte?"]
    ],
    [
        r"ayuda",
        ["Las opciones para interactuar conmigo son: 'mi nombre es [nombre]', 'hola|buenos dias|buenas tardes|buenas', 'cual es tu nombre', 'como estas', 'que puedes hacer', 'quien eres', 'ayuda', 'adios'"]
    ],
    [
        r"adios",
        ["Adiós, ¡que tengas un buen día!", "¡Hasta luego!"]
    ]
]

chatbot = Chat(pairs, reflections)

def chat():
    put_markdown("## Bienvenido al chatbot Robotin, escribe con minúsculas y sin tildes. Pra ver las opciones disponibles escribe 'ayuda'.")
    user_input = input("¿Cómo puedo ayudarte?", type=TEXT)
    while True:
        response = chatbot.respond(user_input)
        put_text("Robotin:", response)
        user_input = input("", type=TEXT)
        if user_input == "adios":
            break

if __name__ == '__main__':
    start_server(chat, port=8080)
