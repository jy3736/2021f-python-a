import check50

@check50.check()
def w02_hw01():
    """w02-hw01"""
    check50.run("python hw01.py").stdin("4", prompt=True).stdout("*\n**\n***\n****\n", regex=False).exit(0)
    check50.run("python hw01.py").stdin("1", prompt=True).stdout("*\n", regex=False).exit(0)
    check50.run("python hw01.py").stdin("3", prompt=True).stdout("*\n**\n***\n", regex=False).exit(0)
    
