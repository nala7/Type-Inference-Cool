program1 = '''
class Main inherits IO {
    main ( ) : AUTO_TYPE {
        let x : AUTO_TYPE <- 3 + 2 in {
            case x of
            y : Int => out_string ( " Ok " ) ;
            esac
        }
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