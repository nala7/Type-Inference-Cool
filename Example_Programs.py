program01 = """
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
            if not ( 7 + 9 < 2 ) then a = 5 else c = 3 fi
        } ;
        h ( l : Int ) : Void {
            let let_name : Int <- 5 + 2 , k : Int <- 95 , m : AUTO_TYPE <- 5 in m + 9
        } ; 
    } ;
    """
program02 = """
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
    """
program03 = """
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
    """
program04 = """
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
    """
program05 = """
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
    """

JanPoul = """
    class Main inherits IO {
        main ( ) : AUTO_TYPE {
            let x : AUTO_TYPE <- 3 in
                case x of
                    y : Int => out_int ( 2 ) ;
                esac
        } ;
    } ;
    """

class_with_attr = """
    class A {
        a : Int ;
        a : K ;
    } ;
    class B {
        a : Int ;
    } ;
    """
class_with_inheritance = """
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
    """
class_attr_assignation = """
    class A inherits K {
        a : Int <- 6 ;
        a : K <- 8 + 9 ;
    } ;
    class B {
        a : Int ;
    } ;
    """
method_definition = """
    class A inherits K {
        a : Int <- 6 ;
        a : K <- 8 + 9 ;
        f ( ) : A {
            8
        } ;
        k ( i : Int , j : Z ) : Int {
            4
        } ;
    } ;
    class B {
        a : Int ;
        j ( m : I ) : A {
            1
        } ;
    } ;
    """
using_boolean_op = """
    class A inherits K {
        a : Int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        f ( ) : A {
            8
        } ;
        k ( i : Int , j : Z ) : Int {
            8 = 34
        } ;
    } ;
    class B {
        a : Int ;
        j ( m : I ) : A {
            1
        } ;
    } ;
    """
large_compare_expr = """
    class A inherits K {
        a : Int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        k ( i : Int , j : Z ) : Int {
            8 = 34
        } ;
    } ;
    class B {
        a : Int ;
        j ( m : I ) : A {
            true = false
        } ;
    } ;
    """
let_program = """
    class A inherits K {
        a : Int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        k ( i : Int , j : Z ) : Int {
            let x : H , y : Int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : Int ;
        j ( m : I ) : A {
            ( let m : K in 7 + 7 ) < 8 = false
        } ;
    } ;
    """
while_program = """
    class A inherits K {
        a : Int <- 6 = 0 ;
        a : K <- 8 + 9 < 9 ;
        f ( ) : A {
            ( 3 + 56 ) + 84 < 200 = true
        } ;
        k ( i : Int , j : Z ) : Int {
            let x : H , y : Int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : Int ;
        j ( m : I ) : A {
            ( let m : K in 7 + 7 ) < 8 = false
        } ;
    } ;
    class C {
        f ( ) : Void {
            while true loop 3 pool
        } ;
    } ;
    """
func_call_program = """
    class A inherits K {
        a : K <- 8 + 9 = 9 ;
        f ( ) : A {
            a . f ( )
        } ;
        k ( i : Int , j : Z ) : Int {
            let x : H , y : Int <- 34 + 87 * ( 7 ) in x + 4 * ( y + y )
        } ;
    } ;
    class B {
        a : Int ;
        j ( m : I ) : A {
            ( let m : K in 7 + 7 ) = 8 = false
        } ;
    } ;
    class C {
        f ( ) : Void {
            ( a . k ( 1 , 6 ) ) . f ( 7 )
        } ;
    } ;
    """
text ="""
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
"""

text1 = """
    class A {
        a : String <- " Halleluya pa todas aqu " ;
    } ;
"""

text2 = """
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

"""

text6 = """
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
"""

text7 = """
    class A {
        f ( ) : Void {
            ( ( new A ) . type_name ( ) ) . length ( ) + 8
        } ;
    } ;
    """

text8 = """
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

"""

text9 = """
class Main inherits IO {
	main ( ) : IO { out_string ( " Hello World! " ) } ;

	test : B <- ( ( new D ) . back ( " Hello " ) ) . back ( " World! " ) ;
} ;
"""

text10 = """
    class A {
        a : AUTO_TYPE ;
        b : AUTO_TYPE <- { a ; } + 7 ;
    } ;
    """

text11 = """
class Ackermann {
    ackermann ( m : AUTO_TYPE , n : AUTO_TYPE ) : AUTO_TYPE {
        if m = 0 then n + 1 else
            if n = 0 then ackermann ( m - 1 , 1 ) else
                ackermann ( m - 1 , ackermann ( m , n - 1 ) )
            fi
        fi
    } ;
} ;
"""
text12 = """
class A {
    f ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
        a
    } ;
} ;
"""

text13 = """
class A {
    a : AUTO_TYPE ;
    b : AUTO_TYPE ;
    f ( ) : Int {
        a + b 
    } ;
} ;
"""

text14 = """
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
"""

text15 = """
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
"""

text16 = """
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
"""

text17 = """
class A {
    f ( ) : AUTO_TYPE {
        9 
    } ;
} ;

class B inherits A {
    f ( ) : AUTO_TYPE {
        5 < 6
    } ;
} ;
"""
text18 = """
class A {
    f ( a : AUTO_TYPE ) : Int {
        if ( a = 7 ) then " str " else ( 0 = 0 ) fi
    } ;
} ;
"""

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
                out_string ( ( " Created user: " . concat ( user . get_name ( ) ) ) . concat ( " \n " ) ) ;
        }
    } ;
} ;

class User {
    id : AUTO_TYPE ;
    name : AUTO_TYPE ;
    email : AUTO_TYPE ;

    init ( id_ : AUTO_TYPE , name_ : AUTO_TYPE , email_ : AUTO_TYPE ) : AUTO_TYPE {
        {
            id <- id_ ;
            name <- name_ ;
            email <- email_ ;
            self ;
        }
     } ;

    get_name ( ) : AUTO_TYPE {
        name
    } ;
} ;
"""

proy_example = """
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

"""

proy_example2 = """
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
"""

proy_example3 = """
class A {
    fact ( n : AUTO_TYPE ) : AUTO_TYPE {
        if ( n < 0 ) then 1 else n * fact ( n - 1 ) fi
    } ;
} ;

"""

proy_example4 = """
class A {
    ackermann ( m : AUTO_TYPE , n : AUTO_TYPE ) : AUTO_TYPE {
        if ( m = 0 ) then n + 1 else
            if ( n = 0 ) then ackermann ( m - 1 , 1 ) else
                ackermann ( m - 1 , ackermann ( m , n - 1 ) )
            fi
        fi
    } ;
} ;
"""

proy_example5 = """
class A {
    f ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
        if ( a = 1 ) then b else
            g ( a + 1 , b / 2 )
        fi
    } ;
    g ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
        if ( b = 1 ) then a else
            f ( a / 2 , b + 1 )
        fi
    } ;
} ;
"""

proy_example6 = """
class A {
    b : AUTO_TYPE ;
    a : AUTO_TYPE ;

    f ( ) : Int { {
        let x : String , x : AUTO_TYPE <- a + b in x ;
    } } ;
} ;

"""

proy_example7 = """
class A {
    b : AUTO_TYPE ;
    a : AUTO_TYPE ;

    f ( ) : Int { {
        let x : AUTO_TYPE <- " str " , x : AUTO_TYPE <- a + b , self : AUTO_TYPE , x : AUTO_TYPE <- let c : AUTO_TYPE in a in x ;
    } } ;
} ;
"""

proy_example8 = """
class A {
    b : AUTO_TYPE ;
    a : AUTO_TYPE ;

    f ( ) : AUTO_TYPE { {
        let x : String , x : AUTO_TYPE <- a + b , self : AUTO_TYPE , x : AUTO_TYPE <- let c : AUTO_TYPE in a in x ;
    } } ;
} ;
"""

cyclic_inheretance = """
class B inherits B { } ;
class A inherits B { } ;
"""

cyclic_inheretance1 = """
class C inherits B { } ;
class A inherits B { } ;
class B inherits A { } ;
class C { } ;
class D inherits E { } ;
class E inherits F { } ;
class F inherits D { } ;
class G inherits F { } ;
"""

inference = """
class A inherits B {
    b : AUTO_TYPE ;
    a : AUTO_TYPE ;
    c : String ;
    f ( ) : Int { 
        {
            b + a ;
            k <- b ;
        } 
    } ;
} ;
class B {
    k : AUTO_TYPE ;
    foo ( k : AUTO_TYPE ) : AUTO_TYPE { k <- " d " } ;
} ;
"""

inference2 = """
class B {
    k : AUTO_TYPE ;
} ;

class A inherits B {
    b : AUTO_TYPE ;
    a : AUTO_TYPE ;
    c : String ;
    f ( ) : Int { {
        b + k + a ;
        1 ;
        k <- " m " ;
    } } ;

    foo ( k : AUTO_TYPE ) : AUTO_TYPE { k <- a } ;
} ;
"""

inference3 = """
class A {
    b : AUTO_TYPE ;
    a : AUTO_TYPE ;
    c : String ;
    f ( ) : Int { {
        b <- c . substr ( 0 , a ) ;
    } } ;
} ;
"""

no_errors = """
class A {
    a : C ;
    suma ( a : Int , b : B ) : Int {
        a + b
    } ;
    b : Int <- 9 ;
    c : C ;
} ;

class B inherits A {
f ( d : Int , a : A ) : B {
    {
        let f : Int <- 8 in f + 3 * d ;
        c <- suma ( 5 , f ) ;
    }
} ;
z : Int ;
} ;

class C inherits A {
} ;

class Main inherits A { 
main ( ) : SELF_TYPE { 
    a . copy ( )
} ;
} ;
"""

g08 = """
class Main inherits IO {
    main ( ) : Object {
        let id : AUTO_TYPE , name : AUTO_TYPE , email : AUTO_TYPE in {
            out_string ( " Introduzca su id:  " ) ;
            id <- self . in_int ( ) ;
            out_string ( " Introduzca su nombre:  " ) ;
            name <- self . in_string ( ) ;
            out_string ( " Introduzca su email:  " ) ;
            email <- self . in_string ( ) ;
            let user : AUTO_TYPE <- ( new User ) . init ( id , name , email ) in
                out_string ( ( " Created user: " ) . concat ( user . get_name ( ) ) . concat ( " \n " ) ) ;
        }
    } ;
} ;

class User {
    id : AUTO_TYPE ;
    name : AUTO_TYPE ;
    email : AUTO_TYPE ;

    init ( id_ : AUTO_TYPE , name_ : AUTO_TYPE , email_ : AUTO_TYPE ) : AUTO_TYPE {
        {
            id <- id_ ;
            name <- name_ ;
            email <- email_ ;
            self ;
        }
    } ;

    get_name ( ) : AUTO_TYPE {
        name
    } ;
} ;
"""

form = """
class A {
    f ( a : AUTO_TYPE ) : Int {
        a
    } ;
} ;
"""

g07 = """
class Main {
    main ( ) : Object {
        let total : AUTO_TYPE <- 10 ,
            i : AUTO_TYPE <- 1 ,
            io : AUTO_TYPE <- new IO in
                while i <= total loop {
                    io . out_int ( fibonacci ( i ) ) ;
                    io . out_string ( " \n " ) ;
                    i <- i + 1 ;
                }
                pool
    } ;

    fibonacci ( n : AUTO_TYPE ) : AUTO_TYPE {
        if n <= 2 then 1 else fibonacci ( n - 1 ) + fibonacci ( n - 2 ) fi
    } ;
} ;
"""

g06 = """
class Main inherits IO {
    main ( ) : IO {
        let vector : AUTO_TYPE <- ( new Vector2 ) . init ( 0 , 0 ) in
            vector . print_vector ( )
    } ;
} ;

class Vector2 {
    x : AUTO_TYPE ;
    y : AUTO_TYPE ;

    init ( x_ : AUTO_TYPE , y_ : AUTO_TYPE ) : Int { 
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

    add ( v : Vector2 ) : AUTO_TYPE 
    {
        ( new Vector2 ) . init ( x + v . get_x ( ) , y + v . get_y ( ) )
    } ;

    print_vector ( ) : AUTO_TYPE 
    {
        let io : IO <- new IO in 
        {
            io . out_string ( " ( " ) ;
            io . out_int ( get_x ( ) ) ;
            io . out_string ( " ;  " ) ;
            io . out_int ( get_y ( ) ) ;
            io . out_string ( " ) n " ) ;
        }
    } ;

    clone_vector ( ) : AUTO_TYPE 
    {
        new Vector2 . init ( x , y )
    } ;
} ;
"""

form2 = """
class A {
    fact ( n : AUTO_TYPE ) : AUTO_TYPE {
        if n < 0 then 1 else fact ( n - 1 ) fi
    } ;
} ;
"""

g05 = """
class Main {
    main ( ) : Object {
        0
    } ;

    f  ( a : AUTO_TYPE , b : AUTO_TYPE , c : AUTO_TYPE , d : AUTO_TYPE ) : AUTO_TYPE {
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
"""

recursividad = """
class A {
    f ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
        if ( a = 1 ) then b else
            g ( a + 1 , b / 2 )
        fi
    } ;
    g ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
        if ( b = 1 ) then a else
            f ( a / 2 , b + 1 )
        fi
    } ;
} ;

"""

g04 = """
class Main {
    main ( ) : Object {
        0
    } ;
} ;

class Point {
    x : Int ;
    y : Int ;

    init ( x0 : AUTO_TYPE , y0 : AUTO_TYPE ) : AUTO_TYPE {
	    {
	        x <- x0 ;
	        y <- y0 ;
	        self ;
	    }
    } ;
} ;
"""

gsem = """
class Main inherits IO {
	main ( ) : IO { out_string ( " hi! " ) } ;

	main : IO <- out_string ( " bye! " ) ;
} ;

class A {
	x : Int <- 3 ;

	x ( ) : String { " :) " } ;
} ;

class B inherits A {
	x : Int ;

	div ( a : Int , b : Int ) : Int { a / b } ;
} ;
"""

gdispatch = """

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
	sum ( m : Int , n : Int , p : Int ) : Int { m + n + p } ;
} ;
class D inherits B { 
	ident ( v : String ) : IO { new IO . out_string ( v ) } ;
	f ( v : Int , w : Int ) : Int { v / w } ;

	back ( s : String ) : B {
		{
			out_string ( s ) ;
			g ( 2 ) ;
			sum ( 1 , 2 , 3 ) ;
			self ; 
		} 
	} ;
} ; 

class Main inherits IO {
	main ( ) : IO { out_string ( " Hello World! " ) } ;
} ;
"""

ejemplo1 = """
class A {
    f ( a : AUTO_TYPE ) : AUTO_TYPE {
        a + 4
    } ;
} ;
"""

ejemplo2 = """
class A {
    f ( a : AUTO_TYPE ) : Int {
        a
    } ;
} ;
"""

ejemplo3 = """
class A { 
    f ( a : Int ) : AUTO_TYPE {
        a + 7 
    } ;
} ;
"""
ejemplo4 = """
class A {
    succ ( n : AUTO_TYPE ) : AUTO_TYPE {
        n + 1
    } ;
} ;
"""

ejemplo5 = """
class A {
    f ( n : AUTO_TYPE ) : AUTO_TYPE {
        if 4 < 0 then 1 else 7 * f ( 1 ) fi
    } ;
} ;
"""

ejemplo6 = """
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
"""

ejemplo7 = """
class A {
    ackermann ( m : AUTO_TYPE , n : AUTO_TYPE ) : AUTO_TYPE {
        if m = 0 then n + 1 else
            if n = 0 then ackermann ( m - 1 , 1 ) else
                ackermann ( m - 1 , ackermann ( m , n - 1 ) )
            fi
        fi
    } ;
} ;
"""

ejemplo8 = """
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
"""

ejemplo9 = """
class A {
    f ( a : AUTO_TYPE ) : AUTO_TYPE {
        {
            a + 6 ;
            self ;
        }
    } ;
} ;
class B inherits A {
    f ( b : AUTO_TYPE ) : Object {
        b <- " Esto es un String "
    } ;
} ;
"""

examples = [
    (example_name, example_text)
    for (example_name, example_text) in locals().items()
    if not example_name.startswith("__")
]