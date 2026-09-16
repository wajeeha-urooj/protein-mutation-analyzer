from protein_mutation.properties import (
    get_residue_properties,
    compare_residue_properties,
    calculate_protein_properties,
)


def test_get_residue_properties():
    properties = get_residue_properties("R")

    assert properties["name"] == "Arginine"
    assert properties["hydropathy"] == -4.5


def test_get_residue_properties_case_insensitive():
    properties = get_residue_properties("r")

    assert properties["name"] == "Arginine"


def test_compare_residue_properties():
    result = compare_residue_properties("R", "H")

    assert result["wild_type"] == "R"
    assert result["mutant"] == "H"
    assert result["wild_type_name"] == "Arginine"
    assert result["mutant_name"] == "Histidine"


def test_hydropathy_change():
    result = compare_residue_properties("R", "H")

   assert abs(result["hydropathy_change"] - 1.3) < 1e-9

def test_protein_properties():
    sequence = "ACDEFGHIKLMNPQRSTVWY"

    properties = calculate_protein_properties(sequence)

    assert "molecular_weight" in properties
    assert "isoelectric_point" in properties
    assert "gravy" in properties
    assert "aromaticity" in properties
    assert "instability_index" in properties
