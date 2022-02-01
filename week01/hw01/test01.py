import check50

@check50.check()
def hw01():
    """hw01"""
    check50.run("python3 hw01.py").stdout("Hello, World!", regex=False).exit(0)
    check50.run("python3 hw02.py").stdout("Hello, STUST!", regex=False).exit(0)