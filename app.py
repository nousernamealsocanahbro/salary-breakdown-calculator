def calculate_cpf(salary):
    # trans = transitional
    CPF_RATE = .37
    E_RATE = .2
    E_TRANS_RATE = .6
    
    E_CAP = 1600
    CPF_CAP = 2960
    
    TRANS_FLOOR = 500
    TRANS_CEILING = 750
    
    if salary < TRANS_FLOOR:
        total_cpf = 0
        employees_share = 0
    elif TRANS_FLOOR <= salary <= TRANS_CEILING:
        employees_share = E_TRANS_RATE * (salary - TRANS_FLOOR)
        total_cpf = salary * CPF_RATE
    else:
        employees_share = min(salary * E_RATE, E_CAP)
        total_cpf = min(salary * CPF_RATE, CPF_CAP)
            
    return total_cpf, employees_share

def calculate_savings(salary):
    SAVINGS_RATE = .2
    
    savings = salary * SAVINGS_RATE
    
    return savings

def main():
    salary = float(input("Input salary: $"))
    
    total_cpf, employees_share = calculate_cpf(salary)
    savings = calculate_savings(salary - employees_share)
    
    print("")
    print(f"Total CPF contributions: ${total_cpf:,.2f}")
    print(f"Your CPF share: ${employees_share:,.2f}")
    print(f"Amount to save: ${savings:,.2f}")
    print('-' * 20)
    print(f"Amount left: ${salary - employees_share - savings:,.2f}")
    
if __name__ == "__main__":
    main()