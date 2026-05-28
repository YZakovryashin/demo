#!/usr/bin/env python3
"""Демонстрация структуры простой программы."""

import sys
from datetime import datetime

MAX_ATTEMPTS = 3

def validate_input(value):
    """Проверяет корректность ввода."""
    return isinstance(value, int) and value > 0

class Calculator:
    """Простой калькулятор."""
    def add(self, a, b):
        return a + b

if __name__ == "__main__":
    calc = Calculator()
    result = calc.add(5, 3)
    print(f"Результат: {result}")
