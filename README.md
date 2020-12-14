# Type-Inference-Cool

La inferencia de tipos en nuestro proyecto se desarrolla a la par del chequeo de tipos. A cada declaracion de clase se le asocia un scope, y dicho scope tendra referencia al scope de la clase padre en caso de que exista herencia. Por ello es necesario que la definicion de la clase de la que se hereda esté anterior a la definicion de la clase actual. 

Para inferir los tipos tenemos dos estructuras de datos, una lista y un diccionario:
1. auto_types : lista de las variables, metodos y argumentos cuyo tipo fue detectado como AutoType y no han sido inferidas aún.
2. infered_types : diccionario de variables, metodos y argumentos cuyo tipo fue inferido.
           
Para identificar un tipo lo podemos hacer de las siguientes maneras:  
* (variable_name, scope_id) => se refiere a la variable de nombre variable_name definida en el scope con id scope_id. Cada scope se le asigna un número de id único al crearse.
* (function_name, type_name) => se refiere al tipo de retorno del metodo con nombre function_name definido en el tipo con nombre type_name.
* (function_name, type_name, arg_pos) => se refiere al tipo del argumento en la posicion arg_pos del metodo function_name definido en type_name.

Las llaves del diccionario y elementos de la lista tendran una de estas tres formas

Nota: Observe el siguiente fragmento:
```
*** Ejemplo 1 ***
class A {
    f ( a : AUTO_TYPE ) : AUTO_TYPE {
        a + 4
    } ;
} ;
```
En este ejemplo cuando entremos a visitar el cuerpo del metodo en la lista auto_types existiran los elementos **(f, A, 0)** y **(a, 2)** el primero refiriéndose al parámetro **a** de la función y el segundo a la variable declarada en el scope. En dicha visita se infiere **(a, 2)** y luego cuando se siga analizando el FuncDeclarationNode inferiremos **(f, A, 0)**

Para inferir, cada nodo realiza acciones específicas. El proceso pasa por acciones sencillas como es el caso del AttributeNode, que infiere si la expresión de inicialización tiene un tipo definido, hasta algunas mas complejas como pueden ser inferir el tipo de una variable que aparezca envuelta en una suma. Veamos ejemplos del proceso de inferencia en la declaración de una función:
```
*** Ejemplo 2 ***
class A {
    f ( a : AUTO_TYPE ) : Int {
        a
    } ;
} ;
```
En este caso se puede inferir que **a** es entero porque es ese el tipo de retorno de la función. Para este tipo de casos el visit tiene un argumento más, llamado set_type, con el tipo de retorno del método. Dicho set_type se pasa al visit de la expresión del cuerpo para, en caso de tener tipo AUTO_TYPE, inferir la variable o llamada a método utilizada
```
*** Ejemplo 3 ***
class A { 
    f ( a : Int ) : AUTO_TYPE {
        a + 7 
    } ;
} ;
```
Cuando se compruebe la expresión del cuerpo de la función, esta dirá que es de tipo **Int** y será asignado entonces en el diccionario de los tipos inferidos a la funcion **f** definida en **A** el tipo **Int**

Una idea similar a la vista en el ejemplo 2 es aplicada en los ArithBinaryNode y BooleanBinaryNode (las operaciones que no sean **=**). En las que se manda a visitiar las expresiones derecha e izquierda con **set_type = Int**. Es valido entonces el siguiente ejemplo:
```
*** Ejemplo 4 ***
class A {
    succ ( n : AUTO_TYPE ) : AUTO_TYPE {
        n + 1
    } ;
} ;
```
La variable **n** es inferida a **Int** pq fue visitada desde el nodo binario y luego **succ** es inferido a **Int** porque es el tipo de retorno de la expresión.

Analizemos ahora el siguiente ejemplo:
```
*** Ejemplo 5 ***
class A {
    f ( n : AUTO_TYPE ) : AUTO_TYPE {
        if 4 < 0 then 1 else 7 * f ( 1 ) fi
    } ;
} ;
```
Ahora empieza a utilizarse el llamado a funciones. Note que el tipo de retorno de **f** se puede inferir por estar en una multiplicación y el tipo de **n** es inferido dado que la llamada a la **f** se realiza con un argumento de tipo **Int**

Pero recorrer una sola vez el AST en el TypeChecker no es suficiente en algunos casos. Veamos:
```
*** Ejemplo 6 ***
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
```
En una primera pasada inferiríamos el tipo de **c** y el retorno de **f**, pero no mas que eso. Es por ello que realizamos varios recorridos por el AST, pero... ¿cuántos?. Se seguirán realizando recorridos por el AST mientras se modifique la cantidad de elementos que hay en la lista **auto_types**. Es de iterés mantener el registro de todos los tipos inferidos durante un recorrido, para utilizar esa información en el próximo. Es por eso que el diccionario de tipos inferidos se pasa de un recorrido al siguiente.

