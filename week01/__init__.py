import check50

@check50.check()
def w01_hw01_basic_check():
    """w01-hw01 basic check"""
    check50.run("python hw01.py").stdout("Hello Python World!", regex=False).exit(0)

@check50.check()
def w01_hw02_1_test_case():
    """w01-hw02 1 test case"""
    check50.run("python hw02.py").stdin("1 2", prompt=False).stdout("1 2 3", regex=False).exit(0)

@check50.check()
def w01_hw02_3_test_cases():
    """w01-hw02 3 test cases"""
    check50.run("python hw02.py").stdin("1 2 3 4", prompt=False).stdout("1 2 3 4 10", regex=False).exit(0)