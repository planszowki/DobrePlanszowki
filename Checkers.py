#Zadanie 1. Sebastian Muraszewski (C) 2021

def taskPIT():
    income_sources = int(input("Podaj liczbę źródeł dochodu: ")) #czekanie na określenie przez użytkownika liczby źródeł dochodu

    income = 0 #zainicjowanie zmiennej odpowiadającej za przychód
    income_cost = 0 #zainicjowanie zmiennej odpowiadającej za koszty uzyskania przychodu
    base_amount = 0 #zainicjowanie zmiennej odpowiadającej za kwotę podstawy 
    

    for x in range(income_sources):
        input("Podaj źródło: ") 
        new_income = float(input("Podaj kwotę przychodu w zł (kropka separatorem dziesiętnym): ")) #czekanie na określenie przez użytkownika kwoty przychodu z danego źródła
        new_income_cost = float(input("Podaj kwotę uzyskania przychodu w zł (kropka separatorem dziesiętnym): ")) #czekanie na określenie przez użytkownika kwoty uzyskania przychodu z danego źródła
        
        if new_income < new_income_cost: #sprawdzanie, czy dochód ze źródła jest ujemny
            base_amount += 0    #jeśli tak, zamieniamy go na zero
        if new_income >= new_income_cost:
            base_amount += (new_income - new_income_cost)

    tax = 0 #zainicjowanie zmiennej odpowiadającej za kwotę należnego podatku
    lowering_tax_amount = 0 #zainicjowanie zmiennej odpowiadającej za kwotę zmniejszającą podatek

    #sprawdzanie podstawy obliczenia podatku w złotych pod względem danych progów podatkowych
    if base_amount <= 8000:
        lowering_tax_amount = 1360
        tax = 0.17 * base_amount - lowering_tax_amount
         
    if base_amount > 8000 and base_amount <= 13000:
        lowering_tax_amount = 1360  - (834.88 * (base_amount - 8000) / 5000)
        tax = 0.17 * base_amount - lowering_tax_amount

    if base_amount > 13000 and base_amount <= 85528:
        lowering_tax_amount = 525.12
        tax = 0.17 * base_amount - lowering_tax_amount 

    if base_amount > 85528 and base_amount <= 127000:
        lowering_tax_amount = 525.12 - (525.12 * (base_amount - 85528) / 41472) 
        tax = 14539.76 + (0.32 * (base_amount - 85528) - lowering_tax_amount)

    if base_amount > 127000 and base_amount < 1000000:
        tax = 14539.76 + 0.32 * (base_amount - 85528)

    if base_amount > 1000000:
        tax = 14539.76 + 0.32 * (base_amount - 85528) + (0.04 * (base_amount - 1000000))

    if tax < 0:
        tax = 0

    print(f"Dochód: {base_amount:.2f} zł  wyliczony podatek: {tax:.2f} zł") #skracamy wartości do dwóch cyfr po przecinku         


taskPIT()