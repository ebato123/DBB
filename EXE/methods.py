from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def check_fields_post_comment(request, text):
    if request == None:
        raise AttributeError("El campo 'request' no puede ser None.")
    
    #Campos de la pagina Comments
    if not text:
        messages.error(request,"ERROR: El campo 'Comentario' no puede estar vacío.")
        return False
    else:
        return True

def check_fields_register(request, email, username, password, confirmPassword) :
    if request == None:
        raise AttributeError("El campo 'request' no puede ser None.")
    
    #Validador de contraseñas de DJango
    try:
        validate_password(password)
    except ValidationError as e:
        messages.error(request,e.messages)
        return False
    
    #Campos de la pagina Register
    if User.objects.filter(email=email):
        messages.error(request,"ERROR: Ya existe un usuario creado con el mismo email.")
        return False
    if User.objects.filter(username=username):
        messages.error(request,"ERROR: Ya existe un usuario creado con el mismo username.")
        return False
    if not email:
        messages.error(request,"ERROR: El campo 'Dirección Email' no puede estar vacío.")
        return False
    if not username:
        messages.error(request,"ERROR: El campo 'Usuario' no puede estar vacío.")
        return False
    if User.objects.filter(username=username):
        messages.error(request,"ERROR: Ya existe un usuario con ese nombre. Porfavor, utiliza otro.")
        return False
    if len(username) < 5:
        messages.error(request,"ERROR: El nombre de usuario no puede contener menos de 5 caracteres.")
        return False
    if not password:
        messages.error(request,"ERROR: El campo 'Contraseña' no puede estar vacío.")
        return False
    if password != confirmPassword:
        messages.error(request,"ERROR: Las contraseñas no coinciden.")
        return False
    else:
        return True


