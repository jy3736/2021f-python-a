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
    """responds to name Emma"""
    check50.run("./hello").stdout("Hello, world!\n").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./hello").stdin("Rodrigo").stdout("Rodrigo").exit()
