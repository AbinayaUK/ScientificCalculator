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


    def addition(self, input1, input2):
        """calculating addition function"""

        try:
            a_input = float(input1)
            b_input = float(input2)
            return a_input + b_input
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"


    def subtraction(self, input1, input2):
        """calculating subtraction function"""
        try:
            a_input = float(input1)
            b_input = float(input2)
            return a_input - b_input
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"


    def multiply(self, input1, input2):
        """calculating multiply function"""
        try:
            a_input = float(input1)
            b_input = float(input2)
            return a_input * b_input
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"


    def divide(self, input1, input2):
        """calculating divide function"""
        try:
            a_input = float(input1)
            b_input = float(input2)
            return a_input / b_input
        except ValueError as ex:
            print("ValueError")
            logging.error(ex)
            return "Enter only numbers"
        except ZeroDivisionError as ex:
            print("ZeroDivisionError")
            logging.error(ex)
            return "Enter a number greater than zero"
