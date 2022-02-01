import check50

@check50.check()
def test01():
    """test01"""
    check50.run("python3 main.py").stdin("22 33", prompt=False).stdout("55", regex=False).exit(0)

@check50.check()
def test02():
    """test02"""
    check50.run("python3 main.py").stdin("11 22 33", prompt=False).stdout("66", regex=False).exit(0)

@check50.check()
def test03():
    """test03"""
    check50.run("python3 main.py").stdin("1 2 3 4 5 6 7 8 9 10", prompt=False).stdout("55", regex=False).exit(0)