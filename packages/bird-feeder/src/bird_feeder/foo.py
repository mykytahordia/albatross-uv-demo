from albatross.core import core_fun
import httpie


def assert_no_numpy() -> None:
    np_present = False
    try:
        import numpy as np

        np_present = True
    except ImportError:
        np_present = False
        print("numpy from core module extra is not present")
    assert not np_present


def test() -> None:
    assert_no_numpy()
    core_fun()
    print("OK", "httpie", httpie.__version__)
