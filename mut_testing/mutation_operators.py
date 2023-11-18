import pytest
from Polynomial import Polynomial
import random

def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2

    # Strengthen the assertion by checking each coefficient
    assert poly_sum.coefficients == [4, -1, 2], f"Unexpected result: {poly_sum.coefficients}"

def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2

    # Strengthen the assertion by checking each coefficient
    assert poly_diff.coefficients == [2, 1, 4], f"Unexpected result: {poly_diff.coefficients}"

def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2

    # Strengthen the assertion by checking each coefficient
    assert poly_product.coefficients == [3, -3, 2, -2], f"Unexpected result: {poly_product.coefficients}"

def test_random_polynomial():
    # Test the behavior of the Polynomial class with a randomly generated polynomial
    coefficients = [random.randint(-10, 10) for _ in range(5)]
    poly = Polynomial(coefficients)

    # Test the string representation
    assert str(poly) == "a4x^4 + a3x^3 + a2x^2 + a1x + a0"

    # Test a basic property (e.g., the degree is less than or equal to the number of coefficients - 1)
    assert poly.degree() <= len(coefficients) - 1

def test_negative_degree():
    # Test the behavior when creating a polynomial with a negative degree
    with pytest.raises(ValueError, match="Degree cannot be negative"):
        poly = Polynomial([1, 2, 3], -1)