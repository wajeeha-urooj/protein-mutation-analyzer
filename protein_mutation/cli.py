import argparse
import pandas as pd

from .analyzer import (
    compare_proteins,
    check_length_change,
    validate_protein_sequence,
    mutation_summary,
)

from .properties import (
    compare_residue_properties,
    calculate_protein_properties,
)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Protein Mutation Analyzer: "
            "compare wild-type and mutant protein sequences."
        )
    )

    parser.add_argument(
        "wildtype",
        help="Wild-type protein sequence"
    )

    parser.add_argument(
        "mutant",
        help="Mutant protein sequence"
    )

    args = parser.parse_args()

    wildtype = args.wildtype.upper()
    mutant = args.mutant.upper()

    # Validate sequences
    wt_invalid = validate_protein_sequence(wildtype)
    mut_invalid = validate_protein_sequence(mutant)

    if wt_invalid:
        raise ValueError(
            f"Unexpected wild-type characters: {wt_invalid}"
        )

    if mut_invalid:
        raise ValueError(
            f"Unexpected mutant characters: {mut_invalid}"
        )

    # Compare sequences
    substitutions = compare_proteins(
        wildtype,
        mutant
    )

    length_change = check_length_change(
        wildtype,
        mutant
    )

    # Display sequence summary
    print("\nProtein Mutation Analyzer")
    print("=" * 45)

    print(f"Wild-type length: {len(wildtype)} aa")
    print(f"Mutant length: {len(mutant)} aa")
    print(f"Length change: {length_change} aa")
    print(
        f"Number of substitutions: "
        f"{len(substitutions)}"
    )

    # Display substitutions
    if substitutions:
        print("\nDetected substitutions")
        print("-" * 45)

        for mutation in substitutions:
            print(
                f"Position {mutation['position']}: "
                f"{mutation['wild_type']} → "
                f"{mutation['mutant']}"
            )
    else:
        print("\nNo substitutions detected.")

    # Display protein-level properties
    print("\nProtein-level properties")
    print("-" * 45)

    wt_properties = calculate_protein_properties(
        wildtype
    )

    mut_properties = calculate_protein_properties(
        mutant
    )

    property_table = pd.DataFrame({
        "Property": wt_properties.keys(),
        "Wild_Type": wt_properties.values(),
        "Mutant": mut_properties.values(),
    })

    property_table["Change"] = (
        property_table["Mutant"]
        - property_table["Wild_Type"]
    )

    print(property_table.to_string(index=False))

    # Display residue-level properties
    if len(substitutions) == 1:
        mutation = substitutions[0]

        residue_change = compare_residue_properties(
            mutation["wild_type"],
            mutation["mutant"]
        )

        print("\nResidue-level property comparison")
        print("-" * 45)

        print(
            f"{residue_change['wild_type']} "
            f"({residue_change['wild_type_name']})"
            f" → "
            f"{residue_change['mutant']} "
            f"({residue_change['mutant_name']})"
        )

        print(
            "Hydropathy change:",
            f"{residue_change['hydropathy_change']:.2f}"
        )

        print(
            "Wild-type charge:",
            residue_change["wild_type_charge"]
        )

        print(
            "Mutant charge:",
            residue_change["mutant_charge"]
        )

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
