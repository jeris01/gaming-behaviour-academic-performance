# Gaming Behaviour and Academic Performance Analysis

## Project objective
Explore how daily gaming time relates to academic scores while also considering study hours, sleep, attendance, and self-reported stress.

## Important data note
The included CSV is **synthetic demonstration data** generated for learning. It is not collected from real students and should not be presented as real survey results. Any patterns in it are simulated and do not prove that gaming causes academic outcomes.

## Files
- `gaming_academic_synthetic_data.csv` — simulated dataset with 250 student-like records and a few missing values for cleaning practice.
- `gaming_academic_analysis.py` — Python analysis script.
- `Customer...` (not applicable) — use the included notebook for the guided version.
- `visualizations/` — charts created when the script runs.

## Variables
- `daily_gaming_hours`: hours spent gaming per day
- `daily_study_hours`: hours spent studying per day
- `sleep_hours`: hours slept per day
- `attendance_percent`: attendance percentage
- `stress_level_1_to_10`: simulated stress rating from 1 to 10
- `academic_score_percent`: simulated academic score from 0 to 100

## Run in Google Colab
1. Open https://colab.research.google.com/
2. Upload `Gaming_Behaviour_Academic_Performance.ipynb`.
3. Upload `gaming_academic_synthetic_data.csv` using the Files panel, or run the notebook's upload cell.
4. Run cells from top to bottom.

## Run locally
Install dependencies:
```bash
pip install pandas matplotlib seaborn
```
Keep the CSV and Python script in the same folder, then run:
```bash
python gaming_academic_analysis.py
```

## Method
1. Load and inspect the data.
2. Check missing values and duplicate rows.
3. Fill missing numeric values with medians.
4. Summarize scores across gaming-hour groups.
5. Create scatter plots, a bar chart, and a correlation heatmap.

## Limitations
- Data is simulated, not real student data.
- The relationships are designed for demonstration and may not match real-world patterns.
- Correlation does not imply causation.
- Self-reported gaming, study, and sleep data can be inaccurate in a real survey.
- A real study would need consent, privacy safeguards, a documented sampling method, and appropriate approval from the institution.

## Suggested next step
If your faculty requires real-data analysis, ask permission to collect an anonymous survey or use a properly licensed public dataset. Clearly cite any external dataset.
