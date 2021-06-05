import check50
import check50.c

@check50.check()
def exists():
    """hello.c exists"""
    check50.exists("hello.c")

@check50.check(exists)
def compiles():
    """hello.c compiles"""
    check50.c.compile("hello.c", cc="gcc")

@check50.check(compiles)
def hello():
    """Test case 1"""
    check50.run("./hello").stdout("Hello, world!\n").exit()
