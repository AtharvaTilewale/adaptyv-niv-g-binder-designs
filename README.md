# adaptyv-niv-g-binder-designs

Open, reproducible computational repository for AI-guided design of binders against the Nipah virus attachment glycoprotein G (NiV-G) in the Adaptyv / ProteinBase Nipah Binder Competition.

## Project scope

This repository documents computational binder design workflows, design rationale, filtering strategy, metadata templates, and final candidate tracking for public reuse.

## Workflow overview

1. NiV-G target selection
2. Literature- and MD-guided epitope residue identification
3. De novo binder generation using BoltzGen
4. Exploratory routes using RFDiffusion + SolMPNN and ProteinMPNN receptor-mimetic design
5. Binder folding and binder-target complex prediction using Boltz2 and AlphaFold-based tools
6. RMSD-based structural self-consistency filtering
7. Confidence filtering using pLDDT, pTM, and ipTM
8. Interface-quality ranking using ipSAE
9. Final binder selection for ProteinBase submission

## Public-facing BoltzGen target epitope

Targeted residues: **S241, R402, E501, W504, E505, V507, Q530, E533, N557**.

## Campaign summary

Across the broader exploratory campaign, we generated and scored **more than 5,000 candidate binders** using multiple computational strategies. Final candidates were selected using **RMSD, pLDDT, pTM, ipTM, and ipSAE**. The strongest BoltzGen-derived design achieved an **ipSAE of 0.76**.

## Repository structure

- `methods.md` - detailed computational methods
- `results.md` - placeholder result tables and reporting format
- `responsible_use.md` - biosafety and responsible-use statement
- `DATA_LICENSE.md` - CC BY 4.0 license for datasets/figures/metadata/docs
- `datasets/niv_g_binder_designs/` - data templates, scripts, and figures

## Quick start

```bash
pip install -r requirements.txt
python datasets/niv_g_binder_designs/scripts/01_prepare_metadata.py
python datasets/niv_g_binder_designs/scripts/02_filter_designs.py
python datasets/niv_g_binder_designs/scripts/03_rank_by_ipsae.py
python datasets/niv_g_binder_designs/scripts/04_plot_filtering_funnel.py
python datasets/niv_g_binder_designs/scripts/05_plot_ipsae_scores.py
```

## Licensing

- **Code:** MIT License (`LICENSE`)
- **Datasets, figures, metadata, and documentation:** CC BY 4.0 (`DATA_LICENSE.md`)

## Citation

See `CITATION.cff`.
