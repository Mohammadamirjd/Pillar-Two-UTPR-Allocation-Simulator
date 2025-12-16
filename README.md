# Pillar Two – UTPR Allocation Simulator

This repository provides a Python-based simulator for allocating **Under-Taxed Payments Rule (UTPR)** top-up tax among jurisdictions in accordance with the **OECD Pillar Two (GloBE) Rules**.

1. The project demonstrates:

A) Deep understanding of UTPR legal mechanics
B) Ability to operationalize **allocation keys (payroll & tangible assets)
C) Strong law + programming** skill integration using Python

This project is suitable for PhD applications, Big4 tax technology role, and international tax policy research.

---

2. Legal Scope Covered

A) Identification of residual top-up tax
B) Allocation of UTPR top-up tax
C) Payroll and tangible asset allocation keys
D) Jurisdictional distribution of tax liability

 ⚠️ This simulator is **educational and analytical** and does not replace official compliance tools.

---

3. Project Structure

```text
pillar2-utpr-allocation/
│
├── data/
│   └── utpr_factors.csv
│
├── utpr_allocation.py
│
└── README.md
```

---

4. Legal Background (Simplified)

Under Article 2.6 & Article 5.2 GloBE Rules, when low-tax income is not fully collected under the IIR, the UTPR allocates residual top-up tax** to jurisdictions based on:

A) Number of employees (payroll proxy)
B) Value of tangible assets

Each jurisdiction receives a proportion of the residual tax based on its **allocation share**.

---

5. Sample Dataset (`utpr_factors.csv`)

```csv
Jurisdiction,Employees,Tangible_Assets
Germany,500,2000000
France,300,1500000
Italy,200,1000000
```

---

6. Allocation Methodology

Step 1: Compute Allocation Weights

```
Jurisdiction Weight = 50% Payroll Share + 50% Asset Share
```

Step 2: Allocate Residual Top-up Tax

```
Allocated UTPR = Jurisdiction Weight × Residual Top-up Tax
```

---
7. How to Run

Step1: Install dependencies:
pip install pandas

Step2: Run the simulator:
python utpr_allocation.py

---

8. Example Output

| Jurisdiction | Allocation Weight | Allocated UTPR Tax |
| ------------ | ----------------- | ------------------ |
| Germany      | 0.40              | 40,000             |
| France       | 0.35              | 35,000             |
| Italy        | 0.25              | 25,000             |

---

9. Why This Project Matters

This repository shows:

A) Advanced understanding of UTPR allocation mechanics
B) Ability to translate complex tax rules into algorithms
C) Practical modeling skills relevant for international tax compliance

UTPR is one of the **least implemented and most complex elements** of Pillar Two — showcasing it strongly differentiates your profile.

---

10. Possible Extensions

A) Country-specific UTPR adjustments
B) Interaction with IIR priority rules
C) Sensitivity analysis on allocation keys
D) Visualization dashboard (Python Streamlit or R Shiny)
E) Multi-entity group simulations

---

11. Legal References

A) OECD (2021): *Global Anti-Base Erosion Model Rules (Pillar Two)*
B) OECD Commentary & Administrative Guidance on UTPR

---

12. Author

Mohammadamir Modami
MSc International Law (International Tax)
OECD Pillar Two | UTPR | Tax Technology
Python | R
