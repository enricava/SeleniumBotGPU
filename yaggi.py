import yagmail

def avisame(cual, enlace, precio):
    contenido = "Este es un mensaje automático. La tarjeta " + cual + " está disponible en " + enlace + " por " + precio + "€"
    titulo = "EN STOCK: " + cual
    try:
        #initializing the server connection
        my_user, my_password, notify_user = '', '', ''
        yag = yagmail.SMTP(user=my_user, password=my_password)
        #sending the email
        yag.send(to=notify_user, subject=titulo, contents=contenido)
        print("Email sent successfully")
    except:
        print("Error, email was not sent")
