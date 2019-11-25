import sys
from src.driver.ScientificCalc import ScientificCalc


def main():
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    addcalc = ScientificCalc()
    result1 = addcalc.addition(input1, input2)
    print(result1)
    result2 = addcalc.subtraction(input1, input2)
    print(result2)
    result3 = addcalc.multiply(input1, input2)
    print(result3)
    result4 = addcalc.divide(input1, input2)
    print(result4)
