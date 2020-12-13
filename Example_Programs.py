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
        b : AUTO_TYPE <- { a ; } + 7
    }
    '''