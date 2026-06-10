# Adaptyv NiV-G Binder Designs

This repository documents our AI-guided protein binder design workflow for the Adaptyv Nipah Binder Competition. The target was Nipah virus glycoprotein G. We explored multiple computational design strategies, including BoltzGen-based targeted de novo binder generation, RFDiffusion + SolMPNN blind binder design, and ProteinMPNN-based receptor-mimetic sequence design.

Candidate binders were evaluated using AlphaFold-based and Boltz2-based structural prediction. Final candidates were selected using RMSD, pLDDT, pTM, ipTM, and ipSAE, with the final ProteinBase collection emphasizing targeted BoltzGen designs against a literature- and MD-defined NiV-G epitope.