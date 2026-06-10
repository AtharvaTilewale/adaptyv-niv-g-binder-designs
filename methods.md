# Methods

## Target and design objective

We targeted the Nipah virus attachment glycoprotein G (NiV-G) to identify compact protein binders suitable for competition submission and downstream experimental screening.

## Epitope selection

Epitope residues were selected by combining literature-supported receptor-contact information with molecular-dynamics-informed accessibility and stability considerations. The public-facing BoltzGen campaign targeted residues S241, R402, E501, W504, E505, V507, Q530, E533, and N557.

## BoltzGen targeted de novo binder design

BoltzGen was used as the primary targeted de novo route to generate candidate binders constrained to the selected NiV-G epitope patch.

## RFDiffusion + SolMPNN exploratory binder design

RFDiffusion was used to generate exploratory backbones and SolMPNN was used for sequence design to diversify scaffold classes and interface hypotheses.

## ProteinMPNN receptor-mimetic design

ProteinMPNN was used in a receptor-mimetic exploratory mode to generate binders inspired by local receptor-like interaction motifs.

## Structural prediction and complex modelling

For each design route, binder-only folding and binder-target complex predictions were evaluated with Boltz2 and AlphaFold-based tools.

## RMSD filtering

Designs were filtered by structural self-consistency using RMSD between independent structure predictions and/or model variants.

## pLDDT, pTM, and ipTM confidence filtering

Model confidence thresholds were applied using pLDDT (local confidence), pTM (global fold confidence), and ipTM (interface confidence).

## ipSAE interface ranking

Surviving candidates were ranked by ipSAE to prioritize likely high-quality binding interfaces.

## Final candidate selection

Final candidates were selected using a combined decision rule over RMSD, pLDDT, pTM, ipTM, and ipSAE, with method diversity considered during shortlisting.

## Limitations

These results are computational predictions and may not directly translate to biophysical affinity, expression, stability, specificity, or neutralization activity without experimental validation.
