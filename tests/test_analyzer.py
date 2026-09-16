from protein_mutation.analyzer import (
    compare_proteins,
    check_length_change,
    validate_protein_sequence,
    mutation_summary,
)


def test_compare_proteins():
    wildtype = "ACDEFG"
    mutant = "ACDFFG"

    result = compare_proteins(
        wildtype,
        mutant
    )

    assert len(result) == 1
    assert result[0]["position"] == 4
    assert result[0]["wild_type"] == "E"
    assert result[0]["mutant"] == "F"
    assert result[0]["mutation_type"] == "substitution"


def test_no_mutation():
    sequence = "ACDEFG"

    result = compare_proteins(
        sequence,
        sequence
    )

    assert result == []


def test_length_change():
    wildtype = "ACDEFG"
    mutant = "ACDEFGH"

    assert check_length_change(
        wildtype,
        mutant
    ) == 1


def test_negative_length_change():
    wildtype = "ACDEFGH"
    mutant = "ACDEFG"

    assert check_length_change(
        wildtype,
        mutant
    ) == -1


def test_sequence_validation():
    sequence = "ACDEFGHIK"

    assert validate_protein_sequence(
        sequence
    ) == []


def test_invalid_sequence():
    sequence = "ACDEFG1"

    result = validate_protein_sequence(
        sequence
    )

    assert result == ["1"]


def test_mutation_summary():
    wildtype = "ACDEFG"
    mutant = "ACDFFG"

    summary = mutation_summary(
        wildtype,
        mutant
    )

    assert summary["wild_type_length"] == 6
    assert summary["mutant_length"] == 6
    assert summary["length_change"] == 0
    assert summary["number_of_substitutions"] == 1
