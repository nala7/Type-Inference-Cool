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
            a + b + new B ( ) ;
        }
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