import pytest
import hexorcist

def test_to_decimal():
    assert hexorcist.to_decimal('8',8) == 8
    assert hexorcist.to_decimal('ZA', 36) == 1270

def test_from_decimal():
    assert hexorcist.from_decimal(918395923509,16) == 'D5D4A9AC35'
    assert hexorcist.from_decimal(0,36) == '0'
    assert hexorcist.from_decimal(654, 32) == 'KE'