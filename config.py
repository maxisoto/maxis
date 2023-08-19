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
    #MSJ error Ejercicio 5
    ERROR5 = {'Error_fecha': 'Ud ha ingresado una fecha posterior a la fecha actual...'}
    #ejercicio 6 y 7
    ERROR6 = {'Error_operacion': 'No existe ruta definida para ese enpoint'}
    POSSIBLE_OPERATIONS = {'Error_operacion': 'No existe ruta definida para ese enpoint',
                        'Operaciones Posbiles':'A continuacion se detallan el listado de operciones habilitadas',
                        'sum':'Para sumar de dos numeros A+B=C',
                        'sub': 'Para restar dos numeros A-B=C',
                        'mult': 'Para multiplicar dos numeros AxB=C',
                        'div': 'Para restar dos numeros A/B=C, tener en cuenta que no esta permitida la division por cero',}