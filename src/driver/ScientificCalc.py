"""Performing Arithmetic Operation"""

import logging
logging.basicConfig(filename="configure.log", level=logging.ERROR,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='w')


class ScientificCalc:
    """class Scientific"""

    def __init__(self):
        """constructor"""

        self.a_input = 0
        self.b_input = 0

    @classmethod
    def addition(cls, add_input1, add_input2):
        """calculating addition function"""

        try:
            a_input = float(add_input1)
            b_input = float(add_input2)
            return a_input + b_input
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"

    @classmethod
    def subtraction(cls, sub_input1, sub_input2):
        """calculating subtraction function"""
        try:
            a_input = float(sub_input1)
            b_input = float(sub_input2)
            return a_input - b_input
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"

    @classmethod
    def multiply(cls, mul_input1, mul_input2):
        """calculating multiply function"""
        try:
            a_input = float(mul_input1)
            b_input = float(mul_input2)
            return a_input * b_input
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"

    @classmethod
    def divide(cls, div_input1, div_input2):
        """calculating divide function"""
        try:
            a_input = float(div_input1)
            b_input = float(div_input2)
            return a_input / b_input
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"
        except ZeroDivisionError as ex:
            print("ZeroDivisionError")
            logging.error(ex)
            return "Enter a number greater than zero"
