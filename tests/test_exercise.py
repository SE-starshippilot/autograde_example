import pytest
from src.exercise import avg_list

def test_exercise(capsys):
    numbers = [1,3,10,-1,5,0]
    assert avg_list(numbers) == 3
