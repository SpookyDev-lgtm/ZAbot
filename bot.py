def responder(mensaje):
    mensaje = mensaje.lower()

    if mensaje == "hola":
        return "Que onda bro 🗿 soy ZAbot"

    if mensaje == "ping":
        return "Pong 🗿"

    return "No entiendo todavía 💀"


print(responder("hola"))
