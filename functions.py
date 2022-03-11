def print_employee_data(name: str, year_of_birth: int, actual_year: int):
    print("Name:", name)
    print("Age:", actual_year - year_of_birth)


def calculate_age(year_of_birth: int, actual_year: int):
    return actual_year - year_of_birth

print_employee_data("John Doe", 1970, 2022)
print_employee_data("Jack Doe", 1980, 2022)
print_employee_data("Jane Doe", 1990, 2022)

print(calculate_age(2012, 2022))

result = calculate_age(2012, 2022)
print(f"A gyerek {result} éves.")

year_of_birth = 2012
actual_year = 2022
print(calculate_age(year_of_birth, actual_year))