import check50

@check50.check()
def w02_hw01_a():
    """w02-hw01"""
    check50.run("python hw01.py").stdin("4", prompt=False).stdout("*\n**\n***\n****\n", regex=False).exit(0)
    
@check50.check()
def w02_hw01_b():
    """w02-hw01"""
    check50.run("python hw01.py").stdin("2", prompt=False).stdout("*\n**\n", regex=False).exit(0)
