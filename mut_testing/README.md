# Mutation Testing Report for Polynomial Class

## Introduction
Mutation testing is a method for evaluating the effectiveness of a test suite by introducing small changes (mutations) to the code and observing whether the tests can detect these changes. In this report, we apply mutation testing to the `Polynomial` class, aiming to assess the robustness of the test suite and identify areas for improvement.

## List of Defined Mutation Operators
We defined three mutation operators for the `Polynomial` class:
1. **Constant Replacement Operator:**
   - Replaces a constant term in the coefficients list with a different constant.
2. **Coefficient Negation Operator:**
   - Negates the sign of a coefficient in the coefficients list.
3. **Coefficient Deletion Operator:**
   - Deletes a coefficient from the coefficients list.

## Description of Applied Mutations and Their Impact
For each mutation operator, we applied mutations to the original `Polynomial` class code. Examples include replacing constants, negating coefficients, and deleting coefficients. These mutations were designed to simulate potential errors or changes in the code that could impact the behavior of the `Polynomial` class.

## Summary of Mutant Survival and Killing
### Survived Mutants:
- Mutants that did not cause the test suite to fail.
- Examples include mutants where constants were replaced, coefficients were negated, or coefficients were deleted without impacting the behavior detected by the current test suite.

### Killed Mutants:
- Mutants that caused the test suite to fail.
- Examples include mutants where constants were replaced, coefficients were negated, or coefficients were deleted, and the test suite appropriately detected the changes.

## Analysis of the Test Suite's Effectiveness
The test suite demonstrated effectiveness in detecting changes in the behavior of the `Polynomial` class. The specific assertions and test scenarios were able to identify mutants that deviated from the expected behavior. However, there were instances where mutants survived, indicating potential areas for improvement in the test suite's coverage.

## Recommendations for Improving the Test Suite
1. **Strengthen Assertions:**
   - Enhance the specificity of assertions to cover a broader range of potential issues. Check individual coefficients and their positions in addition to overall results.

2. **Add Edge Cases:**
   - Introduce additional test cases, including edge cases and boundary values, to ensure a comprehensive test coverage.

3. **Randomized Testing:**
   - Incorporate some level of randomness in test cases to cover a wider range of scenarios and increase the diversity of inputs.

4. **Test Invariants:**
   - Identify and test invariants that should be maintained by the `Polynomial` class, such as ensuring the degree is always correct.

## Conclusion
Mutation testing provided valuable insights into the effectiveness of the test suite for the `Polynomial` class. While the suite demonstrated the ability to detect certain mutations, there are opportunities for improvement. Strengthening assertions, adding edge cases, and incorporating randomized testing can enhance the suite's ability to identify potential issues in the code. Continuous refinement of the test suite is recommended to ensure the robustness of the `Polynomial` class.
