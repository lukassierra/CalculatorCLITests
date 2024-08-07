import subprocess

def run_calculator(operation, *args):
    command = ["docker", "run", "--rm", "public.ecr.aws/l4q9w4c5/loanpro-calculator-cli", operation] + list(map(str, args))
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

# Test Case Runner
def run_test_case(test_func, description):
    try:
        test_func()
        print(f"[PASS] {description}")
    except AssertionError:
        print(f"[FAIL] {description}")

# Test Cases
def test_addition():
    assert run_calculator("add", 10, 11) == "Result: 21"

def test_subtraction():
    assert run_calculator("subtract", 10, 4) == "Result: 6"

def test_multiplication():
    assert run_calculator("multiply", 3, 7) == "Result: 21"

def test_division():
    assert run_calculator("divide", 9, 3) == "Result: 3"

def test_division_by_zero():
    assert "Error: Cannot divide by zero" in run_calculator("divide", 1, 0)

def test_invalid_operand_count():
    assert "Error: Only one operator was passed" in run_calculator("add", 85)

def test_handling_more_than_two_operands():
    assert "Error: More than two operators were passed" in run_calculator("add", 8, 5, 3)

def test_handling_non_numeric_input():
    assert "Invalid argument. Must be a numeric value." in run_calculator("add", "A", 3)

def test_large_number_addition():
    assert run_calculator("add", 99999999, 1) == "Result: 100000000"

def test_precision_handling():
    assert run_calculator("add", 1.00000001, 1.00000001) == "Result: 2.00000002"

def test_negative_number_subtraction():
    assert run_calculator("subtract", -5, 10) == "Result: -15"

def test_large_number_multiplication():
    assert run_calculator("multiply", 99999999, 99999999) == "Result: 9999999800000000"

def test_float_division():
    assert run_calculator("divide", 10, 4) == "Result: 2.5"

def test_large_number_division_by_zero():
    assert "Error: Cannot divide by zero" in run_calculator("divide", 1000000000, 0)

def test_addition_very_large_numbers():
    assert run_calculator("add", 9999999999, 9999999999) == "Result: 19999999998"

def test_subtraction_resulting_in_zero():
    assert run_calculator("subtract", 100, 100) == "Result: 0"

def test_multiplication_by_zero():
    assert run_calculator("multiply", 0, 9999) == "Result: 0"

def test_division_small_by_large_number():
    assert run_calculator("divide", 1, 99999999) == "Result: 0.00000001"

def test_addition_with_floating_point_numbers():
    assert run_calculator("add", 0.1, 0.2) == "Result: 0.3"

def test_multiplication_with_negative_number():
    assert run_calculator("multiply", -5, 6) == "Result: -30"

def test_invalid_operation_handling():
    assert ("Error: Unknown operation: invalid_operation" in
            run_calculator("invalid_operation", 2, 1))

def test_subtraction_of_two_negative_numbers():
    assert run_calculator("subtract", -10, -5) == "Result: -5"

def test_result_formatting_for_large_floats():
    assert run_calculator("add", 1.23456789, 0.00000001) == "Result: 1.2345679"

def test_multiplication_of_very_large_numbers():
    assert run_calculator("multiply", 1000000000, 1000000000) == "Result: 1000000000000000000"

# Execute Test Cases
if __name__ == "__main__":
    run_test_case(test_addition, "TC001: Verify addition operation with positive integers")
    run_test_case(test_subtraction, "TC002: Verify subtraction operation with positive integers")
    run_test_case(test_multiplication, "TC003: Verify multiplication operation with positive integers")
    run_test_case(test_division, "TC004: Verify division operation with positive integers")
    run_test_case(test_division_by_zero, "TC005: Verify division by zero handling")
    run_test_case(test_invalid_operand_count, "TC006: Verify handling of less than two operands")
    run_test_case(test_handling_more_than_two_operands, "TC007: Verify handling of more than two operands")
    run_test_case(test_handling_non_numeric_input, "TC008: Verify handling of non-numeric input")
    run_test_case(test_large_number_addition, "TC009: Verify large number addition operation")
    run_test_case(test_precision_handling, "TC010: Verify precision of result up to 8 decimal places")
    run_test_case(test_negative_number_subtraction, "TC011: Verify handling of negative numbers in subtraction")
    run_test_case(test_large_number_multiplication, "TC012: Verify multiplication resulting in large numbers")
    run_test_case(test_float_division, "TC013: Verify division resulting in a float value")
    run_test_case(test_large_number_division_by_zero, "TC014: Verify error handling when dividing by zero in large numbers")
    run_test_case(test_addition_very_large_numbers, "TC015: Verify addition of two very large numbers")
    run_test_case(test_subtraction_resulting_in_zero, "TC016: Verify subtraction resulting in zero")
    run_test_case(test_multiplication_by_zero, "TC017: Verify multiplication by zero")
    run_test_case(test_division_small_by_large_number, "TC018: Verify division of a small number by a large number")
    run_test_case(test_addition_with_floating_point_numbers, "TC019: Verify addition with floating-point numbers")
    run_test_case(test_multiplication_with_negative_number, "TC020: Verify multiplication with a negative number")
    run_test_case(test_invalid_operation_handling, "TC021: Verify invalid operation handling")
    run_test_case(test_subtraction_of_two_negative_numbers, "TC022: Verify subtraction of two negative numbers")
    run_test_case(test_result_formatting_for_large_floats, "TC023: Verify result formatting for large floating-point numbers")
    run_test_case(test_multiplication_of_very_large_numbers, "TC024: Verify multiplication with very large numbers")

    print("Test execution completed.")
