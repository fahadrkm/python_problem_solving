#pythoncodingstandard
def check_scope():
    def dolocal():
        test="local tst"
    def do_non_local():
        nonlocal test
        test="chnge  non local test"
    def do_global():
        global test
        test="global test"

    test="default"
    dolocal()
    print("test value after do local: "+test)
    do_non_local()
    print("test value after non_do local: "+test)
    do_global()
    print('test value after do global '+test)
    
check_scope( )
print(test)