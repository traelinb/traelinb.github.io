---
layout: page
title: Research
permalink: /research/
description: Tabular data synthesis and reproducible experiments.
nav: true
nav_order: 2
---

## Tabular data synthesis

**Ongoing undergraduate research · 2026.07–present**

I work on the experimental side of a tabular data synthesis project. The goal is to evaluate generative models on datasets containing both numerical and categorical features.

### What I work on

- **Baseline reproduction.** Setting up and running models including CTGAN, TVAE, VAE, TabDDPM, TabDiff, and GaussianCopula.
- **Data preparation.** Recording explicit column types and preparing metadata so that datasets can be used consistently across experiments.
- **Reproducibility.** Separating training from sampling, saving model checkpoints, and recording random seeds and experiment settings.
- **Evaluation.** Comparing the statistical fidelity of generated data across repeated samples.

### Current focus: a reusable SDV pipeline

I am building dataset-independent tools for metadata preparation, GaussianCopula training, and repeated sampling. The pipeline uses configurable data paths and records training and sampling settings with the outputs.

### Tools

Python · PyTorch · pandas · NumPy · SDV · Conda · Git · Linux

[Back to my introduction]({{ '/' | relative_url }})
