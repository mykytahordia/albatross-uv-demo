import numpy as np
from .core import core_fun


def assert_no_httpie() -> None:
    np_present = False
    try:
        import httpie

        np_present = True
    except ImportError:
        np_present = False
        print("httpie from bird-feeder is not present")
    assert not np_present


def test() -> None:
    assert_no_httpie()
    core_fun()
    print("OK", "numpy", np.__version__)
