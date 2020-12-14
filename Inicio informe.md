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