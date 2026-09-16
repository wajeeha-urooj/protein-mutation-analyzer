def compare_proteins(wildtype, mutant):
    """
    Compare two protein sequences and identify substitutions.

    Parameters
    ----------
    wildtype : str
        Reference protein sequence.
    mutant : str
        Mutant protein sequence.

    Returns
    -------
    list
        List of detected amino-acid substitutions.
    """

    differences = []

    min_length = min(len(wildtype), len(mutant))

    for i in range(min_length):
        if wildtype[i] != mutant[i]:
            differences.append({
                "position": i + 1,
                "wild_type": wildtype[i],
                "mutant": mutant[i],
                "mutation_type": "substitution"
            })

    return differences


def check_length_change(wildtype, mutant):
    """
    Calculate the length difference between two protein sequences.

    A positive value indicates that the mutant is longer.
    A negative value indicates that the mutant is shorter.
    Zero indicates no length change.
    """

    return len(mutant) - len(wildtype)


def validate_protein_sequence(sequence):
    """
    Validate that a protein sequence contains standard amino acids.

    Returns
    -------
    list
        Unexpected characters found in the sequence.
    """

    standard_amino_acids = set(
        "ACDEFGHIKLMNPQRSTVWY"
    )

    sequence = sequence.upper()

    return sorted(
        set(sequence) - standard_amino_acids
    )


def mutation_summary(wildtype, mutant):
    """
    Generate a summary of differences between two protein sequences.
    """

    substitutions = compare_proteins(
        wildtype,
        mutant
    )

    length_change = check_length_change(
        wildtype,
        mutant
    )

    return {
        "wild_type_length": len(wildtype),
        "mutant_length": len(mutant),
        "length_change": length_change,
        "number_of_substitutions": len(substitutions),
        "substitutions": substitutions
    }
