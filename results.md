# Results

## Filtering funnel from generated candidates to final selected binders

| stage | method | input_count | output_count | pass_rate | notes |
|---|---|---:|---:|---:|---|
| generation | BoltzGen / RFDiffusion+SolMPNN / ProteinMPNN | TBA | TBA | TBA | placeholder |
| RMSD filter | all | TBA | TBA | TBA | placeholder |
| confidence filter | all | TBA | TBA | TBA | pLDDT/pTM/ipTM |
| ipSAE ranking shortlist | all | TBA | TBA | TBA | placeholder |
| final submission | selected | TBA | TBA | TBA | placeholder |

## Final selected binder metadata

| design_id | method | sequence_length | design_class | pLDDT | pTM | ipTM | ipSAE | RMSD | selection_reason |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| TBD_001 | BoltzGen | TBA | de_novo | TBA | TBA | TBA | TBA | TBA | placeholder |

## ipSAE ranking

| rank | design_id | method | ipSAE | passed_filter | final_selected |
|---:|---|---|---:|---|---|
| 1 | TBD_001 | BoltzGen | TBA | TRUE | TRUE |

## RMSD versus ipSAE summary

| design_id | method | RMSD | ipSAE | interpretation |
|---|---|---:|---:|---|
| TBD_001 | BoltzGen | TBA | TBA | placeholder |

## Scaffold/design class summary

| design_class | method | count | selected_count | notes |
|---|---|---:|---:|---|
| de_novo | BoltzGen | TBA | TBA | placeholder |
| diffusion_scaffold | RFDiffusion+SolMPNN | TBA | TBA | placeholder |
| receptor_mimetic | ProteinMPNN | TBA | TBA | placeholder |
