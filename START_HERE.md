# Start the simplified project

## Which content belongs in which file?

The ZIP already places each file in its correct folder. Extract the entire ZIP and open that folder in VS Code.

| File | Content |
| --- | --- |
| `app.py` | Python code for the Streamlit website |
| `requirements.txt` | Package names and version limits only |
| `requirements-notebooks.txt` | Extra notebook package requirements |
| `notebooks/01_data_cleaning.ipynb` | Data-cleaning code in notebook cells |
| `notebooks/02_exploratory_analysis.ipynb` | Calculations and charts in notebook cells |
| `notebooks/03_suggestion_analysis.ipynb` | Suggestion keyword analysis in notebook cells |
| `FULL_CODE.md` | A reading reference containing copies of the separate source files |

`requirements.txt` contains only these three lines:

```text
streamlit>=1.50,<2
pandas>=2.2,<4
matplotlib>=3.9,<4
```

For example, `pandas>=2.2,<4` tells the installer to use a Pandas version at least 2.2 and below 4. The symbols specify package versions.

Commands beginning with `python -m` go in the VS Code **Terminal**. Website code beginning with `import pandas` or `import streamlit` belongs in **app.py**. Open `.ipynb` files with the notebook editor and run their cells.

## 1. Extract and open the folder

Extract the ZIP using **Extract All**. In VS Code, choose **File > Open Folder** and select `tilak-nagar-civic-pulse`. You should see `app.py`, `data`, and `notebooks`.

Do not run the project from inside the ZIP. Use this complete updated folder because the app and notebooks now use a simpler workflow.

## 2. Install the packages

Open **Terminal > New Terminal** in that project folder. Run:

```bash
python -m pip install -r requirements.txt
```

This installs Streamlit, Pandas, and Matplotlib. The code was checked with Python 3.12.

Optional: use a separate environment if you already know how. On Windows Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## 3. Start the website

In the same project folder, run:

```bash
python -m streamlit run app.py
```

Open the Local URL shown in the terminal. Keep the terminal open. Press **Ctrl+C** to stop.

The processed CSV files are included, so you can start the website without running the notebooks first. The website runs on your computer; it has not been published online.

## 4. Explore the pages

- **Overview:** purpose and sample counts.
- **Satisfaction dashboard:** service averages, overall ratings, online-service non-use, and reporting experience.
- **Suggestions and priorities:** dissatisfied percentages and comment keyword counts.
- **Community action plan:** proposed follow-up and downloadable activity log and questionnaire.

The website focuses on Tilak Nagar. The extra locality and age filters have been removed to keep the code simple.

## 5. Learn the notebooks

Install notebook support:

```bash
python -m pip install -r requirements-notebooks.txt
```

In VS Code, enable the Python and Jupyter extensions. Open notebook 01, click **Select Kernel**, and choose the Python environment where you installed the packages.

Run each cell from top to bottom, using the play button or **Shift+Enter**. Then run notebook 02 and notebook 03 in order.

| Notebook | What it does |
| --- | --- |
| 01 | Reads and cleans the raw CSV, then saves clean files |
| 02 | Calculates satisfaction summaries and saves charts |
| 03 | Counts suggestion keywords and saves the theme table |

Each notebook includes explanations, comments, blank lines, and saved outputs. Calculations are directly in the cells. There is no `analysis.py` helper to study.

## 6. Make simple edits

- Change headings inside quotation marks in `app.py`.
- Keep the four-space indentation after `if`, `elif`, `for`, and `with`.
- Blank lines are for readability; you may add more.
- Read `TEACHER_EXPLANATION.md` before your demonstration.
- `FULL_CODE.md` contains all app and notebook code in one place, separated by filename. Do not paste the whole document into one Python file.

## 7. If you update the survey

1. Back up the raw CSV.
2. Use an updated export of the same questionnaire.
3. Run notebook 01, then 02, then 03, from top to bottom.
4. Refresh the Streamlit app.
5. Review the written findings and update the Word report and PDF manually.

The app reads the processed files, so replacing only the raw CSV does not update its results.

## Common problems

| Problem | Fix |
| --- | --- |
| Package not found | Run the install command with the same Python selected in VS Code |
| `streamlit` is not recognised | Use `python -m streamlit run app.py` |
| Processed file missing | Check that you opened the full project folder; run notebooks 01, 02, and 03 |
| Notebook cannot find data | Open the project folder in VS Code and keep its folder structure |
| Notebook says a variable is not defined | Run the earlier cells first, or choose Restart Kernel and Run All |
| Unexpected rating error | Check the answer in the raw survey; do not replace it with zero |
| App shows old results | Rerun all three notebooks and refresh the app |
| PowerShell blocks activation | Use Command Prompt, or run `.venv\Scripts\python.exe` directly |

The current report describes the supplied data. Meetings, submissions, and improvements are proposed activities unless you add real evidence of completion.
