from flask import Flask
from config import Config
import datetime

def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)

    app.config.from_object(Config)
    # Ejercicio 1
    # Crear una aplicación Flask donde se defina un endpoint para la ruta /, la cual debe mostrar
    #un mensaje de bienvenida a quien envíe una petición a dicho endpoint. Por ejemplo,
    #podemos mostrar el mensaje Bienvenidx!.

    @app.route('/')
    def hola_mundo():
        return 'Bienvenidx!'


    """Ejercicio 2
    Crear una aplicación Flask que tenga una ruta para el endpoint /info que muestre un
    mensaje de bienvenida en el que se indique el nombre de la aplicación. Para esto deberá
    usarse la clase Config, donde uno de sus atributos de clase (al cual podemos nombrar
    APP_NAME) será justamente el nombre de la app. Como resultado tendríamos que devolver
    algo como Bienvenidx a Routing App."""


    @app.route('/info')
    def Ejercico2():
        return Config.APP_NAME

    """Ejercicio 3
        Definir un endpoint para la ruta /about que muestre información sobre la aplicación en
        formato JSON:"""


    @app.route('/about')
    def Ejercicio3():
        return Config.INFO_DEVELOPERS

    """Ejercicio 4
       Definir un endpoint para la ruta /sum/<int:num1>/<int:num2> que sume dos números
       enteros y muestre el resultado. Por ejemplo, para la petición /sum/20/10 devolveríamos
       30."""

    @app.route('/sum/<int:num1>/<int:num2>')
    def Ejercicio4(num1, num2):
        suma = num1 + num2
        return  f'la suma es : {suma} '

    """Ejercicio 5
    Se solicita definir un endpoint que calcule la edad de una persona en base a su fecha de 
    nacimiento. Para ello se establece la ruta /age/<dob>, donde dob se refiere a day of birth
    y se encuentra en formato ISO 8601 (YYYY-MM-DD).
    Por ejemplo, para la petición HTTP /age/2001-10-20 y suponiendo que es enviada en la 
    fecha 2023-05-16 debería devolver 21.
    En caso de que la fecha de nacimiento sea posterior a la fecha actual, se debe devolver un 
    mensaje de error en formato JSON"""

    @app.route('/age/<fecha_nacimiento>')
    def calculo_edad(fecha_nacimiento):

        hoy = datetime.datetime.now().year
        anio = datetime.datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        if anio.year > hoy:
            return Config.EJERCICIO5
        else:
            edad = hoy - anio.year
            return f'su edad es : {edad} '

    """Ejercicio 6
    Se desea realizar operaciones matemáticas simples mediante nuestra API. Para ello se 
    olicita definir un endpoint para
    /operate/<string:operation>/<int:num1>/<int:num2> que opere dos números 
    enteros y devuelva el resultado de la operación como respuesta a la petición. El parámetro 
    de ruta operation indica la operación que se desea realizar, y puede tomar los siguientes 
    valores:  """
    #/operate/<string:operation>/<int:num1>/<int:num2>
    @app.route('/operate?operation=sum&num1=10&num2=20')
    def operaciones(operation, num1, num2):
        opcion_equivo = True
        if operation == 'sum':
            result = num1 + num2
            opcion_equivo = False
            return f'El resultado de la {operation} es : {result}'
        elif operation == 'sub':
            result = num1 - num2
            opcion_equivo = False
            return f'El resultado de la {operation} es : {result}'
        elif operation == 'mult':
            result = num1 * num2
            opcion_equivo = False
            return f'El resultado de la {operation} es : {result}'
        elif operation == 'div':
            if num2 == 0:
                return Config.error_divi
            else:
                result = num1/num2
                opcion_equivo = False
                return f'El resultado de la {operation} es : {result}'
        if opcion_equivo:
            error_exist = Config.error_existencia
            return error_exist

    """Ejercicio 7
    Reformular el ejercicio anterior para el endpoint /operate, con la diferencia que esta ruta
    deberá recibir parámetros de consulta (query params) operation, num1 y num2 en lugar
    de parámetros de ruta como veíamos en el ejercicio 6."""
    
    

    return app

