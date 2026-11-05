import pytest
from .greeting import make_greeting


def test_greeting():
    assert make_greeting("Angelito") == "Hello, Angelito!"