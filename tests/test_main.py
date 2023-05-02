import sys
from pprint import pprint

from hoge import main


def test_add_one():
    assert main.add_one(1) == 2

def test_add_one2():
    assert main.add_one(7) == 8

def test_add_one3():
    assert main.add_one(7) == 8

def test_add_one4():
    assert main.add_one(7) == 8

def test_hoge():
    pprint(sys.path)
    assert True


