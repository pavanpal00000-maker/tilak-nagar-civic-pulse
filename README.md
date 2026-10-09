# Resident Satisfaction with Local Services in Tilak Nagar, Mumbai

A community engagement project using Python, Pandas, Matplotlib, and Streamlit. This edition uses basic variables, loops, conditions, and small notebook cells. Comments appear above the code, with blank lines between steps. Start with `START_HERE.md`.

## What has been simplified

- Removed the shared `analysis.py` file. Cleaning and calculations are directly in the notebooks.
- Replaced regular expressions, lambda functions, comprehensions, and compact calculations with ordinary steps.
- Made suggestion counting use separate `if` statements and named counters.
- Made the app read the CSV results saved by the notebooks.
- Removed locality and age filters from the website. Main results consistently use Tilak Nagar.
- Removed optional DAX code from the Power BI instructions.
- Added a teaching guide with small examples and a suggested learning order.

The raw survey and calculated findings are unchanged. Missing ratings stay missing. Each service's percentage uses its own valid rating count.

## Run the website

Extract the ZIP, open the project folder in VS Code, and run these commands in that folder:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The processed CSV files are included, so the app is ready to run. It displays local results on your computer; it has not been published online.

## Understand the workflow

| Step | File | Input | Output |
| --- | --- | --- | --- |
| 1 | `notebooks/01_data_cleaning.ipynb` | Original survey CSV | All-locality and Tilak Nagar clean CSVs |
| 2 | `notebooks/02_exploratory_analysis.ipynb` | Tilak Nagar clean CSV | Service and priority tables, five charts |
| 3 | `notebooks/03_suggestion_analysis.ipynb` | Tilak Nagar clean CSV | Theme table and suggestion chart |
| 4 | `app.py` | Clean and summary CSVs | Four-page Streamlit website |

Each notebook runs from top to bottom. Run them in the order 01, 02, 03. The app has an Overview, Satisfaction dashboard, Suggestions and priorities page, and Community action plan. Summary downloads, reporting counts, the questionnaire, and the blank activity log remain available.

## Files included

| File or folder | Purpose |
| --- | --- |
| `app.py` | Website with comments above every executable statement |
| `requirements.txt` | Packages for the app and charts |
| `requirements-notebooks.txt` | Additional notebook support |
| `data/raw/survey_responses_raw.csv` | Original survey, unchanged |
| `data/processed/responses_clean.csv` | All 32 consenting responses |
| `data/processed/tilak_nagar_clean.csv` | The 26 Tilak Nagar responses |
| `data/processed/service_summary.csv` | Service means, valid counts, and percentages |
| `data/processed/issue_priority.csv` | Services sorted by dissatisfied percentage |
| `data/processed/suggestion_theme_counts.csv` | Keyword theme counts |
| `notebooks/` | Three explained notebooks with executed outputs |
| `images/` | Six saved charts |
| `dashboard/power_bi_guide.md` | Optional Power BI steps without DAX |
| `report/` | Word and PDF report of the supplied survey |
| `survey/` | Original questions, form-link placeholder, and blank activity log |
| `START_HERE.md` | Setup steps |
| `TEACHER_EXPLANATION.md` | Code examples and viva preparation |
| `FULL_CODE.md` | Complete source code, separated by file and notebook cell |
| `VERIFICATION.md` | Checks performed and limitations |

## Survey scope and findings

The supplied CSV has 32 responses: 26 Tilak Nagar, three Chembur, and three Other. The main report, charts, and website analysis use Tilak Nagar. Other responses remain in the all-locality clean file.

- Average overall satisfaction: **3.81/5**, from 26 valid ratings.
- Overall satisfied: **14/26 = 53.85%**.
- Public toilets: mean **3.04/5** and **8/26 = 30.77%** dissatisfied, the highest dissatisfied share in the measured services.
- Public cleanliness: mean **4.35/5**, the highest service average.
- Online municipal services: **14** non-use answers and **12** numeric ratings, with mean **3.42/5**.
- Suggestions: **15** recorded comments and **11** blanks.

These findings describe the respondents. The sample is small, recruitment details are unknown, and 18 of the 26 Tilak Nagar respondents are aged 18–30. Two report an age below 18; guardian-permission details were unavailable and should be discussed with the supervisor.

## Cleaning and calculations

Notebook 01 preserves the raw CSV, removes only exact full-row duplicates, renames columns by question text, strips extra spaces, checks consent, and standardises labels. It uses an explicit answer dictionary and `pd.to_numeric` to convert ratings. Unknown rating text or numbers outside 1–5 cause an error. Non-use, not-applicable, and blank ratings remain missing. The original online-service answer is retained so non-use can be counted separately.

Notebook 02 uses these formulas:

```text
Average = sum of valid ratings / number of valid ratings

Satisfied % = number of ratings 4 or 5 / valid rating count * 100

Dissatisfied % = number of ratings 1 or 2 / valid rating count * 100
```

Most services have 26 valid ratings. Drainage has 25. Online services has 12. The service summary shows these denominators. Priority means ordering the dissatisfied percentages for discussion; it does not establish severity or an official urgency ranking.

Notebook 03 uses keyword checks. Each theme is counted at most once per comment, but a comment can match multiple themes. Keywords can miss context, spelling, and negation. Read the original comments before interpreting the counts. A blank comment does not mean no concerns.

## Community engagement

The analysis is complete. Sharing findings, holding discussions, preparing a summary for the appropriate office, and reviewing progress are proposed activities. Record only actual fieldwork in `survey/community_activity_log.csv`. Add the real collection method, dates, and evidence from your records before submission. The website does not collect new responses or submit complaints.

The CSV contains no form URL. Add your actual URL to `survey/google_form_link.txt` if available.

## Update the project

1. Back up the original CSV.
2. Replace it with an updated export of the same questionnaire.
3. Run notebooks 01, 02, and 03 from top to bottom.
4. Refresh the app, which reads the processed files.
5. Review the written interpretations, community recommendations, Word report, and PDF. These are snapshots and do not rewrite themselves.

Changing only the raw CSV does not update the website. The simple file paths assume you start Streamlit from the project folder. The notebooks support starting in that folder or its `notebooks` subfolder.

## Optional Power BI and sharing

A genuine `.pbix` is not included. Use the optional guide if Power BI is required. The Streamlit website works without it.

Individual responses and original comments are included for private project study. The `.gitignore` excludes raw/clean response CSVs and the activity log by default. Clear notebook 03's comment outputs before public sharing or keep the project private. The app requires the clean files, so a code-only public upload would be incomplete.

## Technical references

- [Streamlit API reference](https://docs.streamlit.io/develop/api-reference)
- [Streamlit downloads](https://docs.streamlit.io/develop/api-reference/widgets/st.download_button)
- [Streamlit AppTest](https://docs.streamlit.io/develop/api-reference/app-testing/st.testing.v1.apptest)

Data source: the user-supplied `survey_responses_raw(2).csv`. No synthetic responses or external population estimates were added.
