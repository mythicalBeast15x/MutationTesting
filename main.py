# create_mutants.py
'''
from Polynomial import Polynomial
from mutation_operators import MutationOperators

def create_mutant(original_poly, mutation_sequence):
    mutant = Polynomial(original_poly.coefficients.copy())

    for mutation in mutation_sequence:
        mutation_type, *params = mutation
        if mutation_type == 'replace':
            MutationOperators.constant_replace(mutant, *params)
        elif mutation_type == 'negate':
            MutationOperators.negate_coefficient(mutant, *params)
        elif mutation_type == 'delete':
            MutationOperators.delete_coefficient(mutant, *params)

    return mutant

def main():
    original_poly = Polynomial([3, 0, 2])
    mutation_sequences = [
        [('replace', 1, 5)],
        [('negate', 2)],
        [('delete', 0), ('replace', 1, 4)],
    ]

    for i, mutation_sequence in enumerate(mutation_sequences):
        mutant = create_mutant(original_poly, mutation_sequence)
        print(f"Mutant {i + 1}: {mutant.coefficients}")

if __name__ == "__main__":
    main()
'''
# create_mutants.py
from Polynomial import Polynomial
from mutation_operators import MutationOperators

def create_mutant(original_poly, mutation_sequence):
    mutant = Polynomial(original_poly.coefficients.copy())

    for mutation in mutation_sequence:
        mutation_type, *params = mutation
        if mutation_type == 'replace':
            MutationOperators.constant_replace(mutant, *params)
        elif mutation_type == 'negate':
            MutationOperators.negate_coefficient(mutant, *params)
        elif mutation_type == 'delete':
            MutationOperators.delete_coefficient(mutant, *params)

    return mutant

def classify_mutants(original_poly, mutants, test_function):
    results = {'Survived': [], 'Killed': [], 'Equivalent': [], 'Harmless': []}

    for i, mutant in enumerate(mutants):
        try:
            test_function(mutant)
            # If the test passes, the mutant survived
            results['Survived'].append(i + 1)
        except AssertionError:
            # If the test fails, the mutant was killed
            results['Killed'].append(i + 1)

    return results

def main():
    original_poly = Polynomial([3, 0, 2])
    mutation_sequences = [
        [('replace', 1, 5)],
        [('negate', 2)],
        [('delete', 0), ('replace', 1, 4)],
    ]

    mutants = [create_mutant(original_poly, sequence) for sequence in mutation_sequences]

    def test_function(poly):
        # Use the test function from your test suite
        # e.g., assert str(poly) == "expected_result"
        pass

    results = classify_mutants(original_poly, mutants, test_function)

    print("Survived Mutants:", results['Survived'])
    print("Killed Mutants:", results['Killed'])
    # You can further analyze and classify mutants into 'Equivalent' and 'Harmless' categories

if __name__ == "__main__":
    main()
