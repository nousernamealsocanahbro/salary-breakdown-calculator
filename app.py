def validator(prompt:str, prompt_type:type):
    while True:
        try:
            message = prompt_type(input(prompt))
            
            return message
        except ValueError:
            print("Invalid input, please try again.")

def calculate_cpf(salary:float):
    CPF_RATE_UNDER_500 = 0.6
    CPF_RATE_STANDARD = 0.2
    
    if salary < 500:
        cpf_contributions = 0
    elif salary < 750:
        cpf_contributions = CPF_RATE_UNDER_500 * (salary - 500)
    else:
        cpf_contributions = min(CPF_RATE_STANDARD * salary, 1600)
        
    return cpf_contributions

def calculate_savings(percentage, take_home_pay):
    percentage /= 100
    savings = take_home_pay * percentage
    
    return savings
    
def main():
    while True:
        salary = validator("Input salary: ", float)
        savings_percentage = validator("Input percent to save: ", float)
        
        cpf_contributions = calculate_cpf(salary)
        savings = calculate_savings(savings_percentage, salary - cpf_contributions)
        
        print(f"Salary: ${salary}")
        print(f"CPF contributions: ${round(cpf_contributions, 2)}")
        print(f"Amount to save: ${round(savings, 2)}")
        print(f"Amount left: ${round(salary - cpf_contributions - savings, 2)}")
        
        choice = validator("Press any key to continue, or type 'n' to exit program: ", str)
        
        if choice == 'n':
            break
    
main()