# Confounder & Randomization Challenge

## Recovering Lost Figures: Visualizing Confounders and Causal Inference

This challenge demonstrates the critical importance of understanding confounding variables in causal inference. Through three key visualizations, we explore how confounding can mislead us, and how randomization and stratification can reveal the truth.

## The Challenge

A critical report on confounding and causal inference was being prepared when disaster struck—the figures were lost! The data files survived (`patients_data.csv` and `patients_data_randomized.csv`), and the narrative text is intact, but all three key visualizations have disappeared.

**Mission:** Recover the lost figures by reading the narrative carefully and creating compelling visualizations that match the story being told.

## The Three Figures

1. **Figure 1**: Post-surgical outcomes by patient (observational data)
2. **Figure 2**: Post-surgical outcomes for randomized patients
3. **Figure 3**: Post-surgical outcomes by patient severity (stratification)

## Key Insights

- **Confounding**: Patient severity acts as a common cause, making Doc Dreamy appear better than Doc Duck in observational data
- **Randomization**: When patients are randomly assigned, the true causal effect is revealed—Doc Duck is actually the better surgeon
- **Stratification**: When randomization isn't possible, stratifying by severity reveals the truth

## Files

- `index.qmd`: Main Quarto document with narrative and code
- `patients_data.csv`: Observational data with confounding
- `patients_data_randomized.csv`: Randomized data without confounding
- `generate_data_precise.py`: Script to generate the data files

## Rendering

To render the document:

```bash
quarto render index.qmd
```

Or use the Render button in RStudio/VS Code.

## GitHub Pages

After rendering, push the HTML output to GitHub and enable GitHub Pages to share your site.

