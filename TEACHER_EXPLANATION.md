# Explain your project in simple language

## Start with this introduction

“My project studies residents' satisfaction with local services in Tilak Nagar, Mumbai. I used a survey with 32 responses. My main analysis uses the 26 responses from Tilak Nagar. I cleaned the data, calculated averages and percentages, counted suggestion keywords, and displayed the findings on a Streamlit website.”

## Learn the project in this order

1. Notebook 01: read, clean, and save the survey.
2. Notebook 02: calculate satisfaction results and draw charts.
3. Notebook 03: count keywords in suggestions.
4. `app.py`: display the saved results on a website.

You do not need to learn a separate `analysis.py` file. All calculations are visible in the notebooks. The website uses their saved CSV files.

## The simple flow

The raw CSV goes into notebook 01. Notebook 01 saves clean CSV files. Notebooks 02 and 03 read the Tilak Nagar clean file and save summary CSV files and chart images. The website reads the clean and summary CSV files.

The processed files are already included, so you can start the website immediately. After changing the raw survey, rerun notebooks 01, 02, and 03 before refreshing the website. The written report must be updated separately.

## Notebook 01 — cleaning

Say: “I remove exact duplicate rows, rename long questions, remove extra spaces, check consent, convert ratings into numbers, and select Tilak Nagar.”

Example:

```python
# Select only responses from the study area.
tilak_data = data[data["locality"] == "Tilak Nagar"].copy()
```

Read it as: “Check the locality column and keep each row where the answer is Tilak Nagar.”

The rating dictionary changes `4 - Satisfied` to `4`. Non-use and not-applicable answers become missing values. They do not become zero.

## Notebook 02 — calculations

First understand one calculation, then understand the loop that repeats it.

```python
# Keep valid public toilet ratings.
ratings = data["public_toilets"].dropna()

# Count those ratings.
valid_count = len(ratings)

# Select ratings of 1 or 2.
dissatisfied = ratings[ratings <= 2]

# Count the dissatisfied ratings.
dissatisfied_count = len(dissatisfied)

# Calculate their percentage.
dissatisfied_percent = dissatisfied_count / valid_count * 100
```

For your supplied data, the toilet calculation is `8 / 26 * 100 = 30.77%`.

The notebook uses a `for` loop to repeat these steps for all eight services. An `if valid_count > 0` check avoids dividing by zero. A service with no ratings keeps a blank result.

Other examples:

- Overall average: `99 / 26 = 3.81` out of 5.
- Overall satisfied: `14 / 26 * 100 = 53.85%`.
- Online-service average: `41 / 12 = 3.42` out of 5. Fourteen non-use answers are excluded from that average.

## Notebook 03 — suggestions

Say: “I read the comments and count words using simple if statements.”

```python
# Start the toilet counter at zero.
toilet_count = 0

# Visit each recorded comment.
for comment in comments:

    # Ignore differences in capital letters.
    comment = comment.lower()

    # Check for a toilet mention.
    if "toilet" in comment:

        # Increase the counter by one.
        toilet_count = toilet_count + 1
```

One comment can match several themes. Each theme is counted at most once per comment. This is simple keyword counting; read the comments to check context and spelling. There are 15 recorded comments from Tilak Nagar.

## app.py — the website

The file has six numbered steps:

1. Import Pandas and Streamlit.
2. Set the page title and heading.
3. Read the saved CSV tables.
4. Ask the visitor to choose one of four pages.
5. Use `if` and `elif` to display the chosen page.
6. Add a footer.

The website now shows the main Tilak Nagar results without locality or age filters. This keeps the code easier to follow.

```python
# Display this page only when the visitor selects Overview.
if page == "Overview":

    # Show a heading on the website.
    st.subheader("Project aim")
```

`st` is simply a short name for Streamlit. `st.write()` displays text, `st.metric()` displays a main number, `st.bar_chart()` draws bars, and `st.dataframe()` displays a table.

## Small Python reference

| Code | Meaning |
| --- | --- |
| `=` | Store a value in a variable |
| `==` | Check whether two values are equal |
| `>=` or `<=` | Greater than or equal to; less than or equal to |
| `data["locality"]` | Read one column from the table |
| `len(data)` | Count rows |
| `.dropna()` | Leave out missing answers |
| `.mean()` | Calculate the average |
| `round(value, 2)` | Round to two decimal places |
| `.value_counts()` | Count each answer |
| `.sort_values()` | Put values in order |
| `.set_index("service")` | Use service names as row or chart labels |
| `.to_csv(..., index=False)` | Save a CSV without extra row numbers |
| `for` | Repeat steps for each item |
| `if` / `elif` / `else` | Choose which steps to run |
| `try` / `except` | Handle a specific error with a useful message |
| `#` | Begin a comment; Python does not run it |
| Four spaces | Place a statement inside a loop or condition |

Blank lines separate steps. They help people read the program and do not change its result. Spaces at the beginning of a line are different: keep those unchanged because they define the blocks.

## A short demonstration

1. Show notebook 01 and explain one cleaning step.
2. Show the service table from notebook 02 and explain `8 / 26 * 100`.
3. Show the toilet keyword check in notebook 03.
4. Start Streamlit and visit the four pages.
5. Explain that the community activities are proposals unless you have actually carried them out.

## Likely questions

**Why does the main analysis use 26, not 32?** Six responses are from other localities. They remain in the all-locality clean file, while the project focuses on Tilak Nagar.

**Why not score missing answers as zero?** The scale runs from 1 to 5. Missing or non-use answers do not express dissatisfaction. Zero would give a misleading average.

**Why have different valid counts?** Drainage has one not-applicable answer, and online services has 14 non-use answers. Each calculation uses the number of valid ratings for that question.

**Why save CSV files between notebooks and the website?** The steps are easy to check separately. The app displays the saved results, so it does not repeat the whole analysis.

**Does changing the raw CSV immediately update the website?** No. Run notebooks 01, 02, and 03 again, then refresh the app. Update written interpretations and the report yourself.

**What is the community engagement part?** Gathering resident feedback, sharing findings, discussing specific concerns, and recording real follow-up. Do not claim that proposed activities have already happened.

**Can these results describe every resident?** No. The sample is small, recruitment details are unknown, and most respondents are younger adults.

**Did you receive help with the code?** Explain your real process honestly. For example: “I used AI assistance to prepare the code, studied each step, and checked the calculations.” Follow your college's rules for acknowledging assistance.
