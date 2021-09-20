# Escribir un programa que pregunte el correo electrónico del usuario 
# en la consola y muestre por pantalla otro correo electrónico con el mismo nombre 
# (la parte delante de la arroba @) pero con dominio ceu.es.

def run():
    mail = input("Introduzca su dirección de email: ")
    list_mail = mail.split(sep="@")
    name_mail = list_mail[0]
    final_mail = "@ceu.es"  
    new_mail = name_mail + final_mail
    print("Su nuevo mail es: "+new_mail)


if __name__ == "__main__":
    run()