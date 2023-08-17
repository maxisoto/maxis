class Config:
    SERVER_NAME = "127.0.0.1:5000"
    DEBUG = True
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static_folder/"
    #Ejercicio 2
    APP_NAME = 'Bienvenidos a Routing App'
    #Ejercicio 3
    INFO_DEVELOPERS = {'app_name':'Routing App',
                        'description': 'Aplicación para practicar routing en Flask',
                        'developers': [
                        {'nombre': 'Carlos',
                         'apellido': 'Santana'
                        },
                        {'nombre': 'James',
                         'apellido': 'Hetfield'
                        }],'version': '1.0.0'}

    EJERCICIO5 = {'erro_fecha': 'ud ingreso una fecha posterior a la fecha actual...'}
    error_divi = {'Error' : 'La divicion no esta preparada para esos valores.'}
    error_existencia = {'Error': 'No existe ruta definida para ese enpoint'}
