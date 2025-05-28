import pubchempy as pcp
import re

compound_names = [
    "(HFBA)", "2-ethylhexyl acrylate (EA)", "dodecyl acrylate (DA)", "Lauryl Acrylate (LA)", "VHB matrix",
    "Butyl acrylate (BA)", "isobornyl acrylate (IBOA)", "n-Butyl Acrylate (nBA)", "Polyurethane acrylate (PUA)",
    "PHEA@MDI elastomer", "Sylgard 184 (PDMS)", "PDMS", "Silicone dielectric elastomer (BJB TC5005 A-B/C)",
    "Polymethylvinylsiloxane (PMVS)", "Poly(methylvinylsiloxane) PV", "HTBN + HDI", "Thermoplastic polyurethane (TPU)",
    "Polyether-based polyurethane", "PU (Estane TPU58887)", "PU", "P(VDF-TrFE-CFE)", "P(VDF-HFP)", "Natural rubber",
    "SEBS-g-MA", "(SEHAS)2 (S: polystyrene, EHA: poly(2-ethylhexyl acrylate))",
    "Symmetric poly(styrene-b-butyl acrylate-b-styrene)", "SEBS 161", "SEBS 217", "PO and COS (PPMTC)",
    "Polybutadiene (PB)", "107 rubber", "PVCg", "N/A"
]

# Clean up chemical names for PubChem search
def clean_name(name):
    # Remove commercial codes and abbreviations in parentheses
    cleaned = re.sub(r"\s*\(.*?\)", "", name).strip()
    # Remove mixture descriptors
    for keyword in ["matrix", "elastomer", "rubber", "PU", "PDMS", "SEBS", "Sylgard", "BJB", "Estane", "PO", "COS"]:
        if cleaned.lower().startswith(keyword.lower()):
            return None
    if cleaned in ["N/A", ""]:
        return None
    return cleaned

for name in compound_names:
    search_term = clean_name(name)
    if not search_term:
        print("Not found")
        continue
    compounds = pcp.get_compounds(search_term, 'name')
    if compounds and compounds[0].canonical_smiles:
        smiles = compounds[0].canonical_smiles
        print({smiles})
    else:
        print("Not found")
