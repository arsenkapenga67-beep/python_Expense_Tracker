expenses=[]
def add_expense():
    description=input("Description : ")
    amount=float(input("Montant : "))
    expenses.append({
        "description": description,
        "amount": amount
    })
    print("Depense ajoutee !")
    pass
def show_expenses():
    # travail de l'etudiant B
    pass
def show_total():
    # Travail de l'etudiant B
    pass
def main():
    while True:
        print("\n==== SUIVI DES DEPENSES ====")
        print("1. Ajouter une dépense")
        print("2. Afficher les dépenses")
        print("3.Afficher le total")
        print("4. Quitter")
        choice=input("1")
        if choice=="1":
            add_expense()
        elif choice=="2":
            show_expenses()
        elif choice=="3":
            show_total()
        elif choice=="4":
            print("Au revoir!")
            break
        else:
            print("choix invalide.")
if __name__ == "__main__":
    main()

            