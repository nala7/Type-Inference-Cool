program01 = '''
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
        g ( a : A , c : A ) : A {
            if not 7 + 9 < 2 then a = 5 else c = 3 fi
        } ;
        h ( l : int ) : void {
            let let_name : int <- 5 + 2 , k : int <- 95 in k + 9
        } ; 
    } ;

'''
program0 = '''
    class A { 
        a : AUTO_TYPE <- 5 ;
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
