from Bio.SeqUtils.ProtParam import ProteinAnalysis


RESIDUE_PROPERTIES = {
    "R": {
        "name": "Arginine",
        "hydropathy": -4.5,
        "pka": 12.48,
        "charge_at_ph_7_4": "+1",
        "classification": "Basic / strongly polar"
    },
    "H": {
        "name": "Histidine",
        "hydropathy": -3.2,
        "pka": 6.00,
        "charge_at_ph_7_4": "Predominantly 0; partially +1",
        "classification": "Basic / polar / aromatic"
    },
    "A": {
        "name": "Alanine",
        "hydropathy": 1.8,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar"
    },
    "C": {
        "name": "Cysteine",
        "hydropathy": 2.5,
        "pka": 8.18,
        "charge_at_ph_7_4": "Predominantly 0",
        "classification": "Polar"
    },
    "D": {
        "name": "Aspartic acid",
        "hydropathy": -3.5,
        "pka": 3.65,
        "charge_at_ph_7_4": "-1",
        "classification": "Acidic / polar"
    },
    "E": {
        "name": "Glutamic acid",
        "hydropathy": -3.5,
        "pka": 4.25,
        "charge_at_ph_7_4": "-1",
        "classification": "Acidic / polar"
    },
    "F": {
        "name": "Phenylalanine",
        "hydropathy": 2.8,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar / aromatic"
    },
    "G": {
        "name": "Glycine",
        "hydropathy": -0.4,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar"
    },
    "I": {
        "name": "Isoleucine",
        "hydropathy": 4.5,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar"
    },
    "K": {
        "name": "Lysine",
        "hydropathy": -3.9,
        "pka": 10.53,
        "charge_at_ph_7_4": "+1",
        "classification": "Basic / polar"
    },
    "L": {
        "name": "Leucine",
        "hydropathy": 3.8,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar"
    },
    "M": {
        "name": "Methionine",
        "hydropathy": 1.9,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar"
    },
    "N": {
        "name": "Asparagine",
        "hydropathy": -3.5,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Polar"
    },
    "P": {
        "name": "Proline",
        "hydropathy": -1.6,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar"
    },
    "Q": {
        "name": "Glutamine",
        "hydropathy": -3.5,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Polar"
    },
    "S": {
        "name": "Serine",
        "hydropathy": -0.8,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Polar"
    },
    "T": {
        "name": "Threonine",
        "hydropathy": -0.7,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Polar"
    },
    "V": {
        "name": "Valine",
        "hydropathy": 4.2,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar"
    },
    "W": {
        "name": "Tryptophan",
        "hydropathy": -0.9,
        "pka": None,
        "charge_at_ph_7_4": "0",
        "classification": "Nonpolar / aromatic"
    },
    "Y": {
        "name": "Tyrosine",
        "hydropathy": -1.3,
        "pka": 10.07,
        "charge_at_ph_7_4": "0",
        "classification": "Polar / aromatic"
    }
}


def get_residue_properties(residue):
    """
    Return physicochemical properties for an amino acid.
    """

    residue = residue.upper()

    if residue not in RESIDUE_PROPERTIES:
        raise ValueError(
            f"Unsupported amino-acid residue: {residue}"
        )

    return RESIDUE_PROPERTIES[residue]


def compare_residue_properties(wild_type, mutant):
    """
    Compare physicochemical properties of two amino acids.
    """

    wt = get_residue_properties(wild_type)
    mut = get_residue_properties(mutant)

    return {
        "wild_type": wild_type.upper(),
        "mutant": mutant.upper(),
        "wild_type_name": wt["name"],
        "mutant_name": mut["name"],
        "wild_type_hydropathy": wt["hydropathy"],
        "mutant_hydropathy": mut["hydropathy"],
        "hydropathy_change": (
            mut["hydropathy"] - wt["hydropathy"]
        ),
        "wild_type_pka": wt["pka"],
        "mutant_pka": mut["pka"],
        "wild_type_charge": wt["charge_at_ph_7_4"],
        "mutant_charge": mut["charge_at_ph_7_4"]
    }


def calculate_protein_properties(sequence):
    """
    Calculate sequence-derived physicochemical properties
    for a complete protein.
    """

    analysis = ProteinAnalysis(sequence)

    return {
        "molecular_weight": analysis.molecular_weight(),
        "isoelectric_point": analysis.isoelectric_point(),
        "gravy": analysis.gravy(),
        "aromaticity": analysis.aromaticity(),
        "instability_index": analysis.instability_index()
    }
