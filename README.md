# Proyecto II: Type Inferer

### Nadia González Fernández
### José Alejandro Labourdette-Lartigue Soto

- - - - - - - - - - - - - - - - - - - - - - - - -

Nuestro proyecto se encuentra en github y se puede acceder con el siguiente
link: https://github.com/nala7/Type-Inference-Cool . La rama en la que se
ecuentra la versión final es ALabBranch2.

Para dar solución al problema nuestro proyecto se ejecuta en cuarto fases:
- Tokenizer
- TypeCollector
- TypeBuilder
- TypeChecker

En el typeCollector se hace un primer recorrido por el AST recolectando todos los tipos. Acá también se añaden los tipos predefinidos por el lenguaje COOL.

En el TypeBuilder se analizan los parámetros, valores de retorno, y otras refencias a tipos. En esta fase se definen todos los atributos y las funciones y se hace el an'alisis sint'actico de la entrada

En el typeChecker se hace el an'alisis sem'antico. En esta fase se recoleccionan y construyen los tipos. Tambi'en se hace la inferencia de tipos.

La inferencia de tipos en nuestro proyecto se hace a la par del chequeo de tipos. A cada declaración de clase se le asocia un scope, y dicho scope tendrá referencia al scope de la clase padre en caso de que exista herencia. Por ello es necesario que la definicion de la clase de la que se hereda esté anterior a la definicion de la clase actual. 

Para inferir los tipos tenemos dos estructuras de datos:
- auto_types : lista de las variables, métodos y argumentos cuyo tipo fue detectado como AutoType y no han sido inferidas aún.
- infered_types : diccionario de variables, métodos y argumentos cuyo tipo fue inferido.
           
<!-- Para identificar un tipo lo podemos hacer de las siguientes maneras:   -->
Las llaves del diccionario y elementos de la lista tendran una de estas tres formas:
* (variable_name, scope_id) => se refiere a la variable de nombre variable_name definida en el scope con id scope_id. Cada scope se le asigna un número de id único al crearse.

* (function_name, type_name) => se refiere al tipo de retorno del método con nombre function_name definido en el tipo con nombre type_name.

* (function_name, type_name, arg_pos) => se refiere al tipo del argumento en la posición arg_pos del método function_name definido en type_name.


Nota: Observe el siguiente fragmento:
 ## Ejemplo 1 

```
class A {
    f ( a : AUTO_TYPE ) : AUTO_TYPE {
        a + 4
    } ;
} ;
```
```
Errors: []
Auto Types: []
Infered Types {
    ('a', 2): type Int : Object {},
    ('f', 'A', 0): type Int : Object {},
    ('f', 'A'): type Int : Object {}
}
```
En este ejemplo cuando entremos a visitar el cuerpo del método en la lista _auto_types_ existirán los elementos **(f, A, 0)** y **(a, 2)** el primero refiriéndose al parámetro **a** de la función y el segundo a la variable declarada en el scope. En dicha visita se infiere **(a, 2)** y luego cuando se siga analizando el FuncDeclarationNode inferiremos **(f, A, 0)**.

Para inferir, cada nodo realiza acciones específicas. El proceso pasa por acciones sencillas como es el caso del AttributeNode, que infiere si la expresión de inicialización tiene un tipo definido, hasta algunas más complejas como pueden ser inferir el tipo de una variable que aparezca envuelta en una suma. Veamos ejemplos del proceso de inferencia en la declaración de una función:

 ## Ejemplo 2

```
class A {
    f ( a : AUTO_TYPE ) : Int {
        a
    } ;
} ;
```
```
Errors: []
Auto Types: []
Infered Types {
    ('a', 2): type Int : Object {},
    ('f', 'A', 0): type Int : Object {}
}
```
En este caso se puede inferir que **a** es entero porque es ese el tipo de retorno de la función. Para este tipo de casos el visit tiene un argumento más, llamado __set_type__, con el tipo de retorno del método. Dicho __set_type__ se pasa al visit de la expresión del cuerpo para, en caso de tener tipo __AUTO_TYPE__, inferirlo.
 ## Ejemplo 3
```
class A { 
    f ( a : Int ) : AUTO_TYPE {
        a + 7 
    } ;
} ;
```
```
Errors: []
Auto Types : []
Infered Types {
    ('a', 2): type Int : Object {},
    ('f', 'A', 0): type Int : Object {}
}
```

Cuando se compruebe la expresión del cuerpo de la función, esta dirá que es de tipo **Int** y será asignado entonces en el diccionario de los tipos inferidos a la funcion **f** definida en **A** el tipo **Int**.

Una idea similar a la vista en el ejemplo 2 es aplicada en los ArithBinaryNode y BooleanBinaryNode (excepto la operación **=**). En las que se manda a visitiar las expresiones derecha e izquierda con **set_type = Int**. Es válido entonces el siguiente ejemplo:
 ## Ejemplo 4
```
class A {
    succ ( n : AUTO_TYPE ) : AUTO_TYPE { AUTO_TYPE
        n + 1
    } ;
} ;
```
```
Errors: []
Auto Types: []
Infered Types {
    ('n', 2): type Int : Object {},
    ('succ', 'A', 0): type Int : Object {},
    ('succ', 'A'): type Int : Object {}
}
```

La variable **n** es inferida a **Int** porque fue visitada desde el nodo binario y luego **succ** es inferido a **Int** porque es el tipo de retorno de la expresión.

Analizemos ahora el siguiente ejemplo:
 ## Ejemplo 5
```
class A {
    f ( n : AUTO_TYPE ) : AUTO_TYPE {
        if 4 < 0 then 1 else 7 * f ( 1 ) fi
    } ;
} ;
```
```
Errors: []
Auto Types: []
Infered Types {
    ('f', 'A', 0): type Int : Object {},
    ('f', 'A'): type Int : Object {}
}
```
Ahora empieza a utilizarse el llamado a funciones. Note que el tipo de retorno de **f** se puede inferir por estar en una multiplicación y el tipo de **n** es inferido dado que la llamada a **f** se realiza con un argumento de tipo **Int**.

Recorrer una sola vez el AST en el TypeChecker no es suficiente para inferir todos los tipos en algunos casos. Veamos:
 ## Ejemplo 6
```
class A {
    a : AUTO_TYPE ;
    b : AUTO_TYPE ;
    c : AUTO_TYPE ;
    f ( ) : AUTO_TYPE {
        {
            a <- b ;
            b <- c ;
            c <- 4 ;
        }
    } ;
} ;
```

```
Errors: []
Auto Types: []
Infered Types {
    ('c', 1): type Int : Object {},
    ('f', 'A'): type Int : Object {},
    ('b', 1): type Int : Object {},
    ('a', 1): type Int : Object {}
}
```
En una primera iteración se infere el tipo de **c** y el retorno de **f**, pero no se infieren __a__ y __b__. Por ello se realizan varios recorridos por el AST, pero... ¿cuántos?. Se seguirán realizando recorridos por el AST mientras disminuya la cantidad de elementos que hay en la lista **auto_types** de una visita a la otra, es decir mientras que en el último recorrido realizado se haya inferido al menos un tipo. Es de interés mantener el registro de todos los tipos inferidos durante un recorrido, para utilizar esa información en el próximo. Es por eso que el diccionario de tipos inferidos se pasa de un recorrido al siguiente.

 ## Ejemplo 7

```
class A {
    ackermann ( m : AUTO_TYPE , n : AUTO_TYPE ) : AUTO_TYPE {
        if m = 0 then n + 1 else
            if n = 0 then ackermann ( m - 1 , 1 ) else
                ackermann ( m - 1 , ackermann ( m , n - 1 ) )
            fi
        fi
    } ;
} ;
```
```
Errors: []
Auto Types: []
Infered Types {
    ('n', 2): type Int : Object {},
    ('m', 2): type Int : Object {},
    ('ackermann', 'A', 0): type Int : Object {},
    ('ackermann', 'A', 1): type Int : Object {},
    ('ackermann', 'A'): type Int : Object {}
}
```

Para este caso se infiere **n** en el cuerpo del **then** luego, dado que la expresión del **else** son llamados a la propia función que termina en _AUTOTYPE_ (note que dentro se infiere __m__ también como _AUTO_TYPE_) se intenta establecer el tipo de la condicional como el tipo del then_expr. Luego se infiere el retorno de __ackerman__ como entero.

Especial atención toma la redefinición de métodos de clases ancestras. Veamos el siguiente ejemplo:
 ## Ejemplo 8
```
class A {
    f ( a0 : AUTO_TYPE , a1 : AUTO_TYPE ) : AUTO_TYPE {
        a0
    } ;
} ;
class B inherits A {
    f ( b0 : AUTO_TYPE , b1 : AUTO_TYPE ) : AUTO_TYPE {
        {
            b0 + 7 ;
            b1 ;
        } 
    } ;
} ;
class C inherits B {
    f ( c0 : AUTO_TYPE , c1 : AUTO_TYPE ) : AUTO_TYPE {
        c1 + 1
    } ;
} ;
```
```
Errors: []
Auto Types: []
Infered Types {
    ('b0', 4): type Int : Object {},
    ('f', 'B', 0): type Int : Object {},
    ('f', 'C', 0): type Int : Object {},
    ('c1', 7): type Int : Object {},
    ('f', 'C', 1): type Int : Object {},
    ('f', 'C'): type Int : Object {},
    ('f', 'A', 0): type Int : Object {},
    ('f', 'B'): type Int : Object {},
    ('f', 'A'): type Int : Object {},
    ('b1', 4): type Int : Object {},
    ('f', 'B', 1): type Int : Object {},
    ('f', 'A', 1): type Int : Object {}
}
```

La regla que se tiene para la redefinición de funciones es mantener los tipos para cada una de ellas, tanto los tipos de los argumentos como el tipo de retorno. Entonces la inferencia de un argumento o del tipo de retorno tiene que verse reflejada en el resto de las definiciones, tanto en clases ancestras como en descendientes. En el proceso de comparación de la redefinición de una funcion con la última función ancestra, hay q encargarse también de inferir los tipos que sean inferibles en el momento. Luego de varios recorridos por el AST veremos que hemos logrado inferir todos los tipos y que no existen errores en la entrada.

Analicemos el siguiente ejemplo entonces:
 ## Ejemplo 9
```
class A {
    f ( a : AUTO_TYPE ) : Object {
        a + 6
    } ;
} ;
class B inherits A {
    f ( b : AUTO_TYPE ) : Object {
        b <- " Esto es un String "
    } ;
} ;
```
```
Errors: 
[
    Cannot convert "String" into "Int".
]
Auto Types: []
Infered Types {
    ('a', 2): type Int : Object {},
    ('f', 'A', 0): type Int : Object {},
    ('f', 'B', 0): type Int : Object {}
}
```
En un recorrido por el __TypeBuilder__ no se debería detectar ningún error, pero una vez inferidos los tipos se detectan errores. Cuando se está visitando la declaración de la función __f__ en __B__ esta tendrá como tipo del argumento **Int**, que fue inferido en **A**. Al intentar realizar la asignación entonces estaremos intentando guardar un string en un entero.
