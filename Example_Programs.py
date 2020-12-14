program01 = '''
    class A {
        a : Int ;
        suma ( a : Int , b : Int ) : Int {
            if { 4 ; 7 + 3 ; } then a . func ( 8 + 7 , a ) else a + b + b fi
        } ;
        b : AUTO_TYPE <- 6 ;
    } ;
    class B inherits A {
        c : Int <- ( 56 + 6 ) ;
        f ( d : Int , a : A ) : Void {
            while 4 + 4
            loop let a : F , b : A <- 4 + 6 in 5
            pool
        } ;
        prop : SELF_TYPE ;
        k ( a : Int ) : Int {
            case new A
            of a : r => 5 + 8 ;
            esac
        } ;
        g ( a : A , c : A ) : A {
            if not 7 + 9 < 2 then a = 5 else c = 3 fi
        } ;
        h ( l : Int ) : Void {
            let let_name : Int <- 5 + 2 , k : Int <- 95 , m : AUTO_TYPE <- 5 in m + 9
        } ; 
    } ;
    '''
program02 = '''
    class A {
        f ( a : Int ) : Int {
            a
        } ;
    } ;
    class B inherits A {
        f ( a : Int ) : Int {
            a + 1
        } ;
    } ;
    class C inherits B {
        f ( a : Int ) : Int {
            a + 2
        } ;
    } ;
    class Z {
        attr : Int ;
    } ;
    class Main {
        main1 ( ) : Int {
            let c : C <- new C in ( c @ A . f ( 8 ) )
        } ;
        main2 ( ) : Int {
            let d : B <- new B in d @ Z . f ( 7 )
        } ;
    } ;
    '''
program03 = '''
    class A {
        a : SELF_TYPE ;
    } ;
    class B {
        b : AUTO_TYPE ;
    } ;
    class C inherits A {
        func ( a : Int , b : Object ) : Object {
            b . abort ( )
        } ;
    } ;
    class Main {
        main1 ( ) : Void {
            new A = new B
        } ;
        main2 ( ) : Void {
            5 = new A
        } ;
        main3 ( ) : Void {
            8 = 1
        } ;
    } ;
    '''
program04 = '''
    class A {
        a : A ;
    } ;
    class Main {
        main1 ( ) : Void {
            case new A of 
                a : Int => 5 ;
                b : str => 8 ;
                c : Int => 7 ;
            esac
        } ;
    } ;
    '''
program05 = '''
    class Main {
        f ( a : Int ) : Int {
            7 + 8
        } ;
        main1 ( ) : Void {
            new SELF_TYPE
        } ;
        main2 ( ) : Void {
            self . f ( 7 )
        } ;
    } ;
    '''

JanPoul = '''
    class Main inherits IO {
        main ( ) : AUTO_TYPE {
            let x : AUTO_TYPE <- 3 in
                case x of
                    y : Int => out_int ( 2 ) ;
                esac
        } ;
    } ;
    '''

program0 = '''
    class A { 
        a : AUTO_TYPE <- 76 ;
        g : AUTO_TYPE ;
        f ( x : Int ) : AUTO_TYPE {
            let x : AUTO_TYPE in 3
        } ;

    } ;
'''
program1 = '''
    class A {
        a : B ;
        suma ( a : Int , b : Int ) : Int {
            if { 4 ; 7 + 3 ; } then a . func ( 8 + 7 , a ) else a + b + b fi
        } ;
        b : auto ;
    } ;

    class B inherits A {
        c : Int <- ( 56 + 6 ) ;
        f ( d : Int , a : A ) : self {
            while 4 + 4
            loop let a : F , b : A <- 4 + 6 in 5
            pool
        } ;
        k ( a : Int ) : Int {
            case new A
            of a : r => 5 + 8 ;
            esac
        } ;
    } ;
    '''

class_with_attr = '''
    class A {
        a : Int ;
        a : K ;
    } ;
    class B {
        a : Int ;
    } ;
    '''
class_with_herency = '''
    class A inherits K {
        a : Int ;
        a : K ;
    } ;
    class B {
        a : Int ;
    } ;
    class W inherits B {
        s : Int ;
    } ;
    '''
class_attr_assignation = '''
    class A inherits K {
        a : Int <- 6 ;
        a : K <- 8 + 9 ;
    } ;
    class B {
        a : Int ;
    } ;
    '''
method_definition = '''
    class A inherits K {
        a : Int <- 6 ;
        a : K <- 8 + 9 ;
        def f ( ) : A {
            8
        } ;
        def k ( i : Int , j : Z ) : Int {
            4
        } ;
    } ;
    class B {
        a : Int ;
        def j ( m : I ) : A {
            1
        } ;
    } ;
    '''
using_boolean_op = '''
    class A inherits K {
        a : Int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        def f ( ) : A {
            8
        } ;
        def k ( i : Int , j : Z ) : Int {
            8 = 34
        } ;
    } ;
    class B {
        a : Int ;
        def j ( m : I ) : A {
            1
        } ;
    } ;
    '''
large_compare_expr = '''
    class A inherits K {
        a : Int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        def f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        def k ( i : Int , j : Z ) : Int {
            8 = 34
        } ;
    } ;
    class B {
        a : Int ;
        def j ( m : I ) : A {
            true = false
        } ;
    } ;
    '''
let_program = '''
    class A inherits K {
        a : Int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        def f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        def k ( i : Int , j : Z ) : Int {
            let x : H , y : Int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : Int ;
        def j ( m : I ) : A {
            ( let m : K in 7 + 7 ) < 8 = false
        } ;
    } ;
    '''
while_program = '''
    class A inherits K {
        a : Int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        def f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        def k ( i : Int , j : Z ) : Int {
            let x : H , y : Int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : Int ;
        def j ( m : I ) : A {
            ( let m : K in 7 + 7 ) < 8 = false
        } ;
    } ;
    class C {
        def f ( ) : Void {
            while true loop 3 pool
        } ;
    } ;
    '''
func_call_program = '''
    class A inherits K {
        a : K <- 8 + 9 = 9 ;
        def f ( ) : A {
            a . f ( )
        } ;
        def k ( i : Int , j : Z ) : Int {
            let x : H , y : Int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : Int ;
        def j ( m : I ) : A {
            ( let m : K in 7 + 7 ) = 8 = false
        } ;
    } ;
    class C {
        def f ( ) : Void {
            ( a . k ( 1 , 6 ) ) . f ( 7 )
        } ;
    } ;
    '''
program2 = '''
    class A {
        a : Z ;
        def suma ( a : Int , b : B ) : Int {
            a + b ;
        }
        b : Int ;
        c : C ;
    }

    class B : A {
        c : A ;
        def f ( d : Int , a : A ) : Void {
            let f : Int = 8 ;
            let c = new A ( ) . suma ( 5 , f ) ;
            c ;
        }
        z : Int ;
        z : A ;
    }

    class C : Z {
    }

    class D : A {
        def suma ( a : Int , d : B ) : Int {
            d ;
        }
    }

    class E : A {
        def suma ( a : A , b : B ) : Int {
            a ;
        }
    }

    class F : B {
        def f ( d : Int , a : A ) : Void {
            a ;
        }
    }
    '''

program3 = '''
    class A {
        a : Int ;
        def suma ( a : Int , b : Int ) : Int {
            " Cuba es una musica vital. "
        } ;
        b : Int ;
    }

    class B : A {
        c : A ;
        def f ( d : Int , a : A ) : Void {
            let f : Int = 8 ;
            let c = new A ( ) . suma ( 5 , f ) ;
            d ;        
        }
    }
    '''


text = '''
    class A {
        a : Z ;
        suma ( a : Int , b : B ) : Int {
            a + b
        } ;
        b : Int <- 9 ;
        c : C ;
    } ;

    class B inherits A {
        c : A ;
        f ( d : Int , a : A ) : Void {
            {
                let f : Int <- 8 in f + 3 * d ;
                c <- suma ( 5 , f ) ;
            }
        } ;
        z : Int ;
    } ;

    class C inherits Z {
        b : A ;
    } ;
'''
program1 = '''
    class A {
        a : int ;
        suma ( a : int , b : int ) : int {
            if { 4 ; 7 + 3 ; } then a . func ( 8 + 7 , a ) else a + b + b fi
        } ;
        b : auto ;
    } ;

    class B inherits A {
        c : int <- ( 56 + 6 ) ;
        f ( d : int , a : A ) : void {
            while 4 + 4
            loop let a : F , b : A <- 4 + 6 in 5
            pool
        } ;
        k ( a : int ) : int {
            case new A
            of a : r => 5 + 8 ;
            esac
        } ;
    } ;
    '''

class_with_attr = '''
    class A {
        a : int ;
        a : K ;
    } ;
    class B {
        a : int ;
    } ;
    '''
class_with_herency = '''
    class A inherits K {
        a : int ;
        a : K ;
    } ;
    class B {
        a : int ;
    } ;
    class W inherits B {
        s : int ;
    } ;
    '''
class_attr_assignation = '''
    class A inherits K {
        a : int <- 6 ;
        a : K <- 8 + 9 ;
    } ;
    class B {
        a : int ;
    } ;
    '''
method_definition = '''
    class A inherits K {
        a : int <- 6 ;
        a : K <- 8 + 9 ;
        def f ( ) : A {
            8
        } ;
        def k ( i : int , j : Z ) : int {
            4
        } ;
    } ;
    class B {
        a : int ;
        def j ( m : I ) : A {
            1
        } ;
    } ;
    '''
using_boolean_op = '''
    class A inherits K {
        a : int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        def f ( ) : A {
            8
        } ;
        def k ( i : int , j : Z ) : int {
            8 = 34
        } ;
    } ;
    class B {
        a : int ;
        def j ( m : I ) : A {
            1
        } ;
    } ;
    '''
large_compare_expr = '''
    class A inherits K {
        a : int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        def f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        def k ( i : int , j : Z ) : int {
            8 = 34
        } ;
    } ;
    class B {
        a : int ;
        def j ( m : I ) : A {
            true = false
        } ;
    } ;
    '''
let_program = '''
    class A inherits K {
        a : int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        def f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        def k ( i : int , j : Z ) : int {
            let x : H , y : int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : int ;
        def j ( m : I ) : A {
            ( let m : K in 7 + 7 ) < 8 = false
        } ;
    } ;
    '''
while_program = '''
    class A inherits K {
        a : int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        def f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        def k ( i : int , j : Z ) : int {
            let x : H , y : int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : int ;
        def j ( m : I ) : A {
            ( let m : K in 7 + 7 ) < 8 = false
        } ;
    } ;
    class C {
        def f ( ) : void {
            while true loop 3 pool
        } ;
    } ;
    '''
func_call_program = '''
    class A inherits K {
        a : K <- 8 + 9 = 9 ;
        def f ( ) : A {
            a . f ( )
        } ;
        def k ( i : int , j : Z ) : int {
            let x : H , y : int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : int ;
        def j ( m : I ) : A {
            ( let m : K in 7 + 7 ) = 8 = false
        } ;
    } ;
    class C {
        def f ( ) : void {
            ( a . k ( 1 , 6 ) ) . f ( 7 )
        } ;
    } ;
    '''
program2 = '''
    class A {
        a : Z ;
        def suma ( a : int , b : B ) : int {
            a + b ;
        }
        b : int ;
        c : C ;
    }

    class B : A {
        c : A ;
        def f ( d : int , a : A ) : void {
            let f : int = 8 ;
            let c = new A ( ) . suma ( 5 , f ) ;
            c ;
        }
        z : int ;
        z : A ;
    }

    class C : Z {
    }

    class D : A {
        def suma ( a : int , d : B ) : int {
            d ;
        }
    }

    class E : A {
        def suma ( a : A , b : B ) : int {
            a ;
        }
    }

    class F : B {
        def f ( d : int , a : A ) : void {
            a ;
        }
    }
    '''

program3 = '''
    class A {
        a : int ;
        def suma ( a : int , b : int ) : int {
            " Cuba es una musica vital. "
        } ;
        b : int ;
    }

    class B : A {
        c : A ;
        def f ( d : int , a : A ) : void {
            let f : int = 8 ;
            let c = new A ( ) . suma ( 5 , f ) ;
            d ;        
        }
    }
    '''

text1 = '''
    class A {
        a : String <- " Halleluya pa todas aqu " ;
    } ;
'''

text2 = '''
class A inherits IO {
	f ( x : Int , y : Int ) : Int {
        x + y
    } ;
	g ( x : Int ) : Int {
        x + x
    } ;
} ;
class B inherits A {
	f ( a : Int , b : Int ) : Int {
        a - b
    } ;
} ;
class C inherits B {
	ident ( m : Int ) : Int {
        m
    } ;
	f ( m : Int , n : Int ) : Int {
        m * n
    } ;
} ;
class D inherits B { 
	ident ( v : String ) : IO {
        ( new IO ) . out_string ( v )
    } ;
	f ( v : Int , w : Int ) : Int {
        v / w
    } ;
	g ( v : Int ) : Int {
        v + v + v
    } ;

	back ( s : String ) : B { 
        {
		    out_string ( s ) ;
		    self ;          
	    } 
    } ;
} ;

'''

text6 = '''
class A { } ;
class B inherits A { } ;
class C inherits B { } ;

class Main inherits IO {
	main ( ) : IO {
        out_string ( " Hello World! " )
    } ;
	test : Int <- let x : Int <- 1 / 2 - 3 + 4 * ( new A ) . type_name ( ) . concat ( ( new B ) . type_name ( ) . concat ( ( new C ) . type_name ( ) ) ) . length ( )
				in x <- x * ( new A ) . type_name ( ) . concat ( ( new B ) . type_name ( ) . concat ( ( new C ) . type_name ( ) ) ) ;
} ;
'''

text7 = '''
    class A {
        f ( ) : Void {
            ( ( new A ) . type_name ( ) ) . length ( ) + 8
        } ;
    } ;
    '''

text8 = '''
class A inherits IO {
	f ( x : Int , y : Int ) : Int { x + y } ;
	g ( x : Int ) : Int { x + x } ;
} ;
class B inherits A {
	f ( a : Int , b : Int ) : Int { a - b } ;
} ;
class C inherits B {
	ident ( m : Int ) : Int { m } ;
	f ( m : Int , n : Int ) : Int { m * n } ;
} ;
class D inherits B { 
	ident ( v : String ) : IO { ( new IO ) . out_string ( v ) } ;
	f ( v : Int , w : Int ) : Int { v / w } ;
	g ( v : Int ) : Int { v + v + v } ;

	back ( s : String ) : B { {
		out_string ( s ) ;
		self ; 
	} } ;
} ;

class Main inherits IO {
	main ( ) : IO { out_string ( " Hello World! " ) } ;

	test : B <- ( ( new D ) . back ( " Hello " ) ) . back ( " World! " ) ;
} ;

'''

text9 = '''
class Main inherits IO {
	main ( ) : IO { out_string ( " Hello World! " ) } ;

	test : B <- ( ( new D ) . back ( " Hello " ) ) . back ( " World! " ) ;
} ;
'''

text10 = '''
    class A {
        a : AUTO_TYPE ;
        b : AUTO_TYPE <- { a ; } + 7 ;
    } ;
    '''

text11 = '''
class Ackermann {
    ackermann ( m : AUTO_TYPE , n : AUTO_TYPE ) : AUTO_TYPE {
        if m = 0 then n + 1 else
            if n = 0 then ackermann ( m - 1 , 1 ) else
                ackermann ( m - 1 , ackermann ( m , n - 1 ) )
            fi
        fi
    } ;
} ;
'''
text12 = '''
class A {
    f ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
        a
    } ;
} ;
'''

text13 = '''
class A {
    a : AUTO_TYPE ;
    b : AUTO_TYPE ;
    f ( ) : Int {
        a + b 
    } ;
} ;
'''

text14 = '''
class Main {
    main ( ) : Object {
        0
    } ;

    f ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
        if a = 1 then b else
            g ( a + 1 , b / 1 )
        fi
    } ;

    g ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
        if b = 1 then a else
            f ( a / 2 , b + 1 )
        fi
    } ;
} ;
'''

text15 = '''
class Main inherits IO {
    main ( ) : IO {
        let vector : AUTO_TYPE <- ( new Vector2 ) . init ( 0 , 0 ) in
            vector . print_vector ( )
    } ;
} ;

class Vector2 {
    x : AUTO_TYPE ;
    y : AUTO_TYPE ;

    init ( x_ : AUTO_TYPE , y_ : AUTO_TYPE ) : AUTO_TYPE {
        {
            x <- x_ ;
            y <- y_ ;
            self ;
        }
    } ;


    get_x ( ) : AUTO_TYPE {
        x
    } ;

    get_y ( ) : AUTO_TYPE {
        y
    } ;

    add ( v : Vector2 ) : AUTO_TYPE {
        ( new Vector2 ) . init ( x + v . get_x ( ) , y + v . get_y ( ) )
    } ;

    print_vector ( ) : AUTO_TYPE {
        let io : IO <- new IO in {
            io . out_string ( " ( " ) ;
            io . out_int ( get_x ( ) ) ;
            io . out_string ( " ;  " ) ;
            io . out_int ( get_y ( ) ) ;
            io . out_string ( " ) \n " ) ;
        }
    } ;

    clone_vector ( ) : AUTO_TYPE {
        ( new Vector2 ) . init ( x , y )
    } ;
} ;
'''

text16 = '''
class Main {
    main ( ) : Object {
        0
    } ;

    f ( a : AUTO_TYPE , b : AUTO_TYPE , c : AUTO_TYPE , d : AUTO_TYPE ) : AUTO_TYPE {
        {
            a <- b ;
            b <- c ;
            c <- d ;
            d <- a ;
            d + 1 ;
            a ;
        }
    } ;
} ;
'''

text17 = '''
class A {
    f ( ) : AUTO_TYPE {
        9 
    } ;
} ;

class B : A {
    f ( ) : AUTO_TYPE {
        5 < 6
    } ;
} ;
'''
text18 = '''
class A {
    f ( a : AUTO_TYPE ) Int {
        if ( a = 7 ) then "str" else ( 0 = 0 ) fi
    } ;
} ;
'''

prog08 = """
class Main inherits IO {

    main ( ) : Object {
        let id : AUTO_TYPE , name : AUTO_TYPE , email : AUTO_TYPE in {
            out_string ( " Introduzca su id : " ) ;
            id <- self . in_int ( ) ;
            out_string ( " Introduzca su nombre: " ) ;
            name <- self . in_string ( ) ;
            out_string ( " Introduzca su email: " ) ;
            email <- self . in_string ( ) ;
            let user : AUTO_TYPE <- ( new User ) . init ( id , name , email ) in
                out_string ( " Created user: " . concat ( user . get_name ( ) ) . concat ( " \n " ) ) ;
        }
    } ;
} ;

class User {
    id : AUTO_TYPE ;
    name : AUTO_TYPE ;
    email : AUTO_TYPE ;

    init ( id_ : AUTO_TYPE , name_ : AUTO_TYPE , email_ : AUTO_TYPE ) : AUTO_TYPE { {
        id <- id_ ;
        name <- name_ ;
        email <- email_ ;
        self ;
    } } ;

    get_name ( ) : AUTO_TYPE {
        name
    } ;
} ;
"""

proy_example = '''
class Main inherits IO {
    main ( ) : AUTO_TYPE {
        let z : AUTO_TYPE <- 3 + 2 in {
            case z of
                w : Int => out_string ( " Ok " ) ;
            esac ;
        }
    } ;
} ;

class Point {
    x : AUTO_TYPE ;
    y : AUTO_TYPE ;
    init ( n : Int , m : Int ) : SELF_TYPE { {
        x <- n ;
        y <- m ; 
    } } ;
} ;


class Point {
    x : AUTO_TYPE ;
    y : AUTO_TYPE ;
    succ ( n : Int ) : AUTO_TYPE { n + 1 } ;
} ;


class Point {
    x : AUTO_TYPE ;
    y : AUTO_TYPE ;
    succ ( n : AUTO_TYPE ) : AUTO_TYPE { n + 1 } ;
} ;

'''

proy_example2 = '''
class Point {
    succ ( n : AUTO_TYPE ) : AUTO_TYPE { n + 1 } ;
    translate ( n : AUTO_TYPE , m : AUTO_TYPE ) : SELF_TYPE { self } ;
} ;

class Main {
    step ( p : AUTO_TYPE ) : AUTO_TYPE { p . translate ( 1 , 1 ) } ;

    main ( ) : Object {
        let p : AUTO_TYPE <- new Point in {
            step ( p ) ; 
        }
    } ;
} ;
'''