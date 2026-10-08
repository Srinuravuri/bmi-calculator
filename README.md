# BMI Calculator

A lightweight BMI calculator with three ways to try it: a Python command-line app, a browser-based calculator, and a Jupyter notebook.

## Features

- Calculates BMI from weight in pounds and height in inches.
- Reports the BMI category and corresponding screening risk.
- Accepts decimal measurements and checks for invalid or non-positive values.
- Runs locally without third-party Python packages.

## BMI formula

The calculator uses the standard imperial formula:

```text
BMI = (weight in pounds × 703) / (height in inches)²
```

## BMI categories

| BMI | Category | Health risk |
| --- | --- | --- |
| Below 18.5 | Underweight | Minimal |
| 18.5 to below 25 | Normal weight | Minimal |
| 25 to below 30 | Overweight | Increased |
| 30 to below 35 | Obese | High |
| 35 to below 40 | Severely obese | Very high |
| 40 and above | Morbidly obese | Extremely high |

## Getting started

### Python command-line calculator

1. Install [Python 3](https://www.python.org/downloads/).
2. Clone or download this repository.
3. From the project directory, run:

   ```bash
   python bmi_calculator.py
   ```

4. Enter your name, weight in pounds, and height in inches when prompted.

### Browser calculator

Open `index.html` in a modern web browser. No server or installation is required.

### Jupyter notebook

Open `bmi_calculator.ipynb` in Jupyter Notebook or JupyterLab and run its cells.

## Example

For a weight of 150 pounds and a height of 65 inches:

```text
BMI: 24.96
Category: Normal weight
Health risk: Minimal
```

## Disclaimer

BMI is a general screening measure, not a diagnosis or a substitute for medical advice. It does not account for individual factors such as body composition or health history. Consult a qualified healthcare professional for guidance.
