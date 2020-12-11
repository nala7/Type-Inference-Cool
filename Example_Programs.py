program01 = '''
    class A {
        a : int ;
        suma ( a : int , b : int ) : int {
            if { 4 ; 7 + 3 ; } then a . func ( 8 + 7 , a ) else a + b + b fi
        } ;
        b : AUTO_TYPE <- 6 ;
    } ;
    class B inherits A {
        c : int <- ( 56 + 6 ) ;
        f ( d : int , a : A ) : void {
            while 4 + 4
            loop let a : F , b : A <- 4 + 6 in 5
            pool
        } ;
        prop : SELF_TYPE ;
        k ( a : int ) : int {
            case new A
            of a : r => 5 + 8 ;
            esac
        } ;
        g ( a : A , c : A ) : A {
            if not 7 + 9 < 2 then a = 5 else c = 3 fi
        } ;
        h ( l : int ) : void {
            let let_name : int <- 5 + 2 , k : int <- 95 , m : AUTO_TYPE <- 5 in m + 9
        } ; 
    } ;
    '''
program02 = '''
    class A {
        f ( a : int ) : int {
            a
        } ;
    } ;
    class B inherits A {
        f ( a : int ) : int {
            a + 1
        } ;
    } ;
    class C inherits B {
        f ( a : int ) : int {
            a + 2
        } ;
    } ;
    class Z {
        attr : int ;
    } ;
    class Main {
        main1 ( ) : int {
            let c : C <- new C in ( c @ A . f ( 8 ) )
        } ;
        main2 ( ) : int {
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
        func ( a : int , b : Object ) : Object {
            b . abort ( )
        } ;
    } ;
    class Main {
        main1 ( ) : Void {
            new A = new B
        } ;
        main2 ( ) : void {
            5 = new A
        } ;
        main3 ( ) : void {
            8 = 1
        } ;
    } ;
    '''
program04 = '''
    class A {
        a : A ;
    } ;
    class Main {
        main1 ( ) : void {
            case new A of 
                a : int => 5 ;
                b : str => 8 ;
                c : int => 7 ;
            esac
        } ;
    } ;
    '''
program05 = '''
    class Main {
        f ( a : int ) : int {
            7 + 8
        } ;
        main1 ( ) : void {
            new SELF_TYPE
        } ;
        main2 ( ) : void {
            self . f ( 7 )
        } ;
    } ;
    '''

program0 = '''
    class A { 
        a : AUTO_TYPE <- 76 ;
        g : AUTO_TYPE ;
        f ( x : int ) : AUTO_TYPE {
            let x : AUTO_TYPE in 3
        } ;

    } ;
'''
program1 = '''
    class A {
        a : B ;
        suma ( a : int , b : int ) : int {
            if { 4 ; 7 + 3 ; } then a . func ( 8 + 7 , a ) else a + b + b fi
        } ;
        b : auto ;
    } ;

    class B inherits A {
        c : int <- ( 56 + 6 ) ;
        f ( d : int , a : A ) : self {
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
