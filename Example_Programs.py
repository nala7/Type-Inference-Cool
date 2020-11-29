program1 = '''
    class A {
        a : int ;
        def suma ( a : int , b : int ) : int {
            if { 4 ; 7 + 3 ; } then a + b else a + b + b fi
        } ;
        b : int ;
    } ;

    class B inherits A {
        c : int <- ( 56 + 6 ) ;
        def f ( d : int , a : A ) : void {
            while 4 + 4
            loop let a : F , b : A <- 4 + 6 in 5
            pool
        } ;
        def k ( a : int ) : int {
            case new A
            of a : r => 5 + 8 ;
            esac
        } ;
    } ;
    '''

program10 = '''
    class A {
        a : int ;
        def suma ( a : int , b : int ) : int {
            let a : F , b : A <- 4 + 6 in 5
        } ;
    } ;
    '''


program2 = '''
class Point {
    x : AUTO_TYPE ;
    y : AUTO_TYPE ;
    init ( n : Int , m : Int ) : SELF_TYPE {
    {
        x <- n ;
        y <- m ;
    } } ;
} ;
'''

program3 = '''
f ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
    if ( a == 1 ) then b else
        g ( a + 1 , b / 2 )
    fi
}
g ( a : AUTO_TYPE , b : AUTO_TYPE ) : AUTO_TYPE {
    if ( b == 1 ) then a else
        f ( a / 2 , b + 1 )
    fi
}
'''