# Type-Inference-Cool

La inferencia de tipos en nuestro proyecto se desarrolla a la par del chequeo de tipos.

Sobre la Inferencia:
    auto_types : lista de las variables, metodos y argumentos cuyo tipo fue detectado como AutoType y no han sido inferidas
    infered_types : diccionario de variables, metodos y argumentois cuyo tipo logro ser inferido.
        La llave del diccionario puede tener una de las siguientes 3 formas:
            - (variable_name, scope_id) => se refiere a la variable de nombre variable_name definida en el scope con id scope_id. Scope_id es un entero
            - (function_name, type_name) => se refiere al tipo de retorno del metodo con nombre function_name definido en el tipo con nombre type_name
            - (function_name, type_name, arg_pos) => se refiere al tipo del argumento en la posicion arg_pos del metodo function_name definido en type_name

la clase tiene que ser definida antes de heredar de ella