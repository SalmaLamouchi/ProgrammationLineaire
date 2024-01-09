from pulp import *

def resoudre_programme_lineaire(type_objectif, nombre_variables, nombre_contraintes, matrice_A, types_inegalites, positivite_variables):
    # Création du problème
    prob = LpProblem(name="ProblemeLineaire", sense=LpMaximize if type_objectif == "maximization" else LpMinimize)

    # Déclaration des variables
    variables = [LpVariable(f'x{i}', lowBound=0, cat=LpContinuous) for i in range(1, nombre_variables + 1)]

    # Déclaration de la fonction objectif
    prob += lpSum([variables[i - 1] * matrice_A[0][i] for i in range(1, nombre_variables + 1)])

    # Déclaration des contraintes
    for i in range(1, nombre_contraintes + 1):
        contrainte = lpSum([variables[j - 1] * matrice_A[i][j] for j in range(1, nombre_variables + 1)])
        if types_inegalites[i - 1] == "<=":
            prob += contrainte <= matrice_A[i][0]
        elif types_inegalites[i - 1] == ">=":
            prob += contrainte >= matrice_A[i][0]
        elif types_inegalites[i - 1] == "=":
            prob += contrainte == matrice_A[i][0]

    # Résolution du problème
    prob.solve()

    # Affichage des résultats
    print(f"Status: {LpStatus[prob.status]}")
    print("Variables:")
    for variable in variables:
        print(f"{variable.name} = {value(variable)}")
    print(f"Fonction Objectif: {value(prob.objective)}")

# Demander à l'utilisateur d'entrer les informations nécessaires
type_objectif = input("Type du problème (maximization ou minimization): ")
nombre_variables = int(input("Nombre de variables: "))
nombre_contraintes = int(input("Nombre de contraintes: "))

# Matrice A et types d'inegalites
matrice_A = [[0] * (nombre_variables + 1) for _ in range(nombre_contraintes + 1)]
types_inegalites = []

print("Entrez les coefficients de la fonction objectif:")
for i in range(1, nombre_variables + 1):
    matrice_A[0][i] = float(input(f"Coef. x{i}: "))
matrice_A[0][0] = 0

for i in range(1, nombre_contraintes + 1):
    print(f"Contrainte {i}:")
    for j in range(1, nombre_variables + 1):
        matrice_A[i][j] = float(input(f"Coef. x{j}: "))
    matrice_A[i][0] = float(input("RHS: "))
    types_inegalites.append(input("Type d'inegalite (<, >, =): "))

# Positivite des variables
positivite_variables = [True] * nombre_variables

# Résoudre le problème
resoudre_programme_lineaire(type_objectif, nombre_variables, nombre_contraintes, matrice_A, types_inegalites, positivite_variables)
