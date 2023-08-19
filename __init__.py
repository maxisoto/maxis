from flask import Flask
from flask import request
from config import Config
import datetime
import json

def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

    app.config.from_object(Config)

    # Ejercicio 1
    # Crear una aplicación Flask donde se defina un endpoint para la ruta /, la cual debe mostrar
    # un mensaje de bienvenida a quien envíe una petición a dicho endpoint. Por ejemplo,
    # podemos mostrar el mensaje Bienvenidx!.

    @app.route('/')
    def hola_mundo():
        return 'Bienvenidx!'

    # Ejercicio 2
    # Crear una aplicación Flask que tenga una ruta para el endpoint /info que muestre un
    # mensaje de bienvenida en el que se indique el nombre de la aplicación. Para esto deberá
    # usarse la clase Config, donde uno de sus atributos de clase (al cual podemos nombrar
    # APP_NAME) será justamente el nombre de la app. Como resultado tendríamos que devolver
    # algo como Bienvenidx a Routing App.


    @app.route('/info')
    def Ejercico2():
        return Config.APP_NAME

    # Ejercicio 3
    # Definir un endpoint para la ruta /about que muestre información sobre la aplicación en
    # formato JSON:


    @app.route('/about')
    def Ejercicio3():
        return Config.INFO_DEVELOPERS

    # Ejercicio 4
    # Definir un endpoint para la ruta /sum/<int:num1>/<int:num2> que sume dos números
    # enteros y muestre el resultado. Por ejemplo, para la petición /sum/20/10 devolveríamos 30.

    @app.route('/sum/<int:num1>/<int:num2>')
    def Ejercicio4(num1, num2):
        if int(num1) and int(num2):

            suma = num1 + num2
            return  f' La suma de {num1} + {num2} es: {suma} '
        else:
            return {'error': 'Ha ocurrido un error'}, 400

    # Ejercicio 5
    # Se solicita definir un endpoint que calcule la edad de una persona en base a su fecha de 
    # nacimiento. Para ello se establece la ruta /age/<dob>, donde dob se refiere a day of birth
    # y se encuentra en formato ISO 8601 (YYYY-MM-DD).
    # Por ejemplo, para la petición HTTP /age/2001-10-20 y suponiendo que es enviada en la 
    # fecha 2023-05-16 debería devolver 21.
    # En caso de que la fecha de nacimiento sea posterior a la fecha actual, se debe devolver un 
    # mensaje de error en formato JSON.

    @app.route('/age/<fecha_nacimiento>')
    def calculo_edad(fecha_nacimiento):

        hoy = datetime.datetime.now()
        anio = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        if anio > hoy:
            return Config.ERROR5
            #return {'error': 'Ha ocurrido un error'}, 400
        else:
            edad = hoy.year - anio.year
            return f'su edad es : {edad} '

    # Ejercicio 6
    # Se desea realizar operaciones matemáticas simples mediante nuestra API. Para ello se 
    # solicita definir un endpoint para
    # /operate/<string:operation>/<int:num1>/<int:num2> que opere dos números 
    # enteros y devuelva el resultado de la operación como respuesta a la petición. El parámetro 
    # de ruta operation indica la operación que se desea realizar, y puede tomar los siguientes 
    # valores:
    

    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def operaciones(operation, num1, num2):
        
        
        if operation == 'sum':
            try:
                result = num1 + num2
                return f'El resultado de la SUMA {num1} + {num2}  es : {result}'
            except TypeError:
                return {'Error de ingreso': 'Solo esta permitido ingresar datos numericos'}, 400  
            
        elif operation == 'sub':
            try:   
                result = num1 - num2
                return f'El resultado de la RESTA {num1} - {num2} es : {result}'
            except TypeError:
                return {'Error de ingreso': 'Solo esta permitido ingresar datos numericos'}, 400  
            
        elif operation == 'mult':
            try:
                result = num1 * num2
                return f'El resultado de la MULTIPLICACION {num1} x {num2} es : {result}'
            except TypeError:
                return {'Error de ingreso': 'Solo esta permitido ingresar datos numericos'}, 400
        
        elif operation == 'div':
            try:
                result = num1/num2
                return f'El resultado de la DIVISION {num1} / {num2} es : {result}'
            except ZeroDivisionError:
                return {'Error Division por Cero': 'No esta permitido la division por cero'}, 400 
            except TypeError:
                return {'error de ingreso': 'Solo esta permitido ingresar un dato numerico'}, 400  
        else:
            return Config.ERROR6, Config.POSSIBLE_OPERATIONS
           
    

    # Ejercicio 7
    # Reformular el ejercicio anterior para el endpoint /operate, con la diferencia que esta ruta
    # deberá recibir parámetros de consulta (query params) operation, num1 y num2 en lugar
    # de parámetros de ruta como veíamos en el ejercicio 6.
    
    @app.route('/operate')
    def operaciones1():
        operation = request.args.get('operation')
        numero1 = request.args.get('num1')
        numero2 = request.args.get('num2')
        print(operation)
        print(numero1)
        print(numero2)
        num1 = int(numero1)
        num2 = int(numero2)
        print(operation, num1, num2)
        if operation == 'sum':
            try:
                result = num1 + num2
                return f'El resultado de la SUMA {num1} + {num2}  es : {result}'
            except TypeError:
                return {'Error de ingreso': 'Solo esta permitido ingresar datos numericos'}, 400  
            
        elif operation == 'sub':
            try:   
                result = num1 - num2
                return f'El resultado de la RESTA {num1} - {num2} es : {result}'
            except TypeError:
                return {'Error de ingreso': 'Solo esta permitido ingresar datos numericos'}, 400  
            
        elif operation == 'mult':
            try:
                result = num1 * num2
                return f'El resultado de la MULTIPLICACION {num1} x {num2} es : {result}'
            except TypeError:
                return {'Error de ingreso': 'Solo esta permitido ingresar datos numericos'}, 400
        
        elif operation == 'div':
            try:
                result = num1/num2
                return f'El resultado de la DIVISION {num1} / {num2} es : {result}'
            except ZeroDivisionError:
                return {'Error Division por Cero': 'No esta permitido la division por cero'}, 400 
            except TypeError:
                return {'error de ingreso': 'Solo esta permitido ingresar un dato numerico'}, 400  
        else:
            return Config.POSSIBLE_OPERATIONS
        
    # Ejercicio 8 
    # Se solicita crear una ruta para en el endpoint /title/<string:word>, el cual aplica 
    # el formato título al parámetro de ruta word (la primera letra de la palabra es mayúscula
    #  y el resto minúscula), y devolverá una respuesta en formato JSON donde la palabra 
    # formateada estará asociada a la clave formatted_word. 
    # Por ejemplo, para la petición /title/SARmienTo devolverá: 

    # { "formatted_word": "Sarmiento" 
    # }

    @app.route('/title/<string:word>')
    def formato_titulo(word):
        try:
            titulo = word.title()
            return {'formatted_word': titulo}, 400
        except TypeError:
            return {'Error_operacion': 'No existe ruta definida para ese enpoint'}, 400
        

    # Ejercicio 9 
    # Para en el endpoint /formatted/<string:dni> se necesita implementar una función que reciba como parámetro de ruta un DNI, y 
    # devuelva el DNI convertido a un entero. El parámetro de ruta recibido puede contar con las siguientes características a 
    # ser tenidas en cuenta para la conversión: 
    # 1. El DNI siempre tendrá 8 caracteres numéricos en la cadena recibida. Por ejemplo, 23456007, 23.456.007, 23-456-007, 00023456, etc. 
    # 2. El DNI puede contener puntos (.) como separador de miles. 
    # 3. El DNI puede contener guiones (-) como separador de miles. 
    # 4. El DNI puede tener ceros a la izquierda. Por ejemplo, 00023456. En este caso el DNI no se considera válido, por lo que 
    # se deberá devolver un mensaje de error en la respuesta. 

    # La respuesta a una petición debe tener formato JSON, donde el DNI formateado estará asociado a la clave formatted_dni.
    # Por ejemplo, para la petición /formatted/23.456.007 devolverá: 
    # { "formatted_dni": 23456007 
    # }
    

    @app.route('/formatted/<string:dni>')
    def formato_dni(dni):
        try:
            cadena = dni
            lista = []
            for i in cadena:
                if i.isnumeric() and len(lista) < 8:
                    lista.append(i)                   
                dni_posta = ''.join(lista)            
            print(dni_posta)
            return {'formatted_dni': dni_posta}, 400
        except TypeError:
            return {'Error_operacion': 'No existe ruta definida para ese enpoint'}, 400
        

    # Ejercicio 10
    @app.route('/format')
    def ejercicio10():
        ErrorDNI = False
        ErrorEdad = False
        nombre = request.args.get('firstname')
        nombre = nombre.title()
        apellido = request.args.get('lastname')
        apellido = apellido.title()
        fecha_nac = request.args.get('dob')
        dni = request.args.get('dni')

        """calculo de edad"""
        hoy = datetime.datetime.now()
        anio = datetime.datetime.strptime(fecha_nac, '%Y-%m-%d')
        if anio > hoy:
            ErrorEdad = True
        else:
            edad = hoy.year - anio.year
    
        """verificar dni"""
        cadena = dni
        lista = []
        for i in cadena:
            if i.isnumeric() and len(lista) < 8:
                lista.append(i)
        if len(lista)==8:
            dni_posta = ''.join(lista)
        else:
            ErrorDNI = True

        """SALIDA A MOSTRAR"""
        if ErrorDNI == False:
            if ErrorEdad == False:
                salida = { 
                    'firstname': f'{nombre}',
                    'lastname': f'{apellido}',
                    'age': f'{edad}',
                    'dni': f'{dni_posta}'
                }
            else:
                salida = {'Error_fecha': 'Ud ha ingresado una fecha posterior a la fecha actual...'}
                
        else:
            salida =  {'Error_DNI': 'El DNI no tiene la extension correcta'}           
       
        return salida   


    return app

