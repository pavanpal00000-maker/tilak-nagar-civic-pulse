# Full simplified project code

Resident Satisfaction with Local Services in Tilak Nagar, Mumbai.

Use the editable files in the ZIP to run the project. This document collects all source code for reading and copying. Each heading tells you the destination filename. Do not paste the whole document into one Python file.

Learning order: notebook 01, notebook 02, notebook 03, then app.py. All notebook calculations are visible in small cells; no analysis.py helper is needed. The app reads the processed CSV files saved by the notebooks.

## File locations

Use the actual files in the ZIP. This Markdown document is only a reading copy.

| Content | Correct location |
| --- | --- |
| Website Python code | `app.py` |
| Package names and version limits | `requirements.txt` |
| Notebook package requirements | `requirements-notebooks.txt` |
| Cleaning code | Code cells in `notebooks/01_data_cleaning.ipynb` |
| Analysis and charts | Code cells in `notebooks/02_exploratory_analysis.ipynb` |
| Suggestion analysis | Code cells in `notebooks/03_suggestion_analysis.ipynb` |
| Installation and start commands | VS Code Terminal opened in the project folder |

## Run the website

Open a terminal in the extracted project folder:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## app.py

```python
# Resident Satisfaction with Local Services in Tilak Nagar, Mumbai.
# Run this file from the project folder:
# python -m streamlit run app.py


# STEP 1: IMPORT THE TWO TOOLS WE NEED

# Pandas reads CSV files as tables.
import pandas as pd

# Streamlit displays headings, tables, charts, and buttons on a website.
import streamlit as st


# STEP 2: SET UP THE WEBSITE

# Set the title shown in the browser tab.
st.set_page_config(page_title="Tilak Nagar Civic Pulse", layout="wide")

# Show the main website heading.
st.title("Tilak Nagar Civic Pulse")

# Show the project topic.
st.write("Resident Satisfaction with Local Services in Tilak Nagar, Mumbai")

# Explain which respondents appear in the results.
st.caption("Community engagement project | Main results use Tilak Nagar responses.")


# STEP 3: READ THE RESULTS SAVED BY THE NOTEBOOKS

# Try to open the files included in the project download.
try:

    # Read all cleaned responses for the total response count.
    all_data = pd.read_csv("data/processed/responses_clean.csv")

    # Read only the Tilak Nagar responses for the main analysis.
    data = pd.read_csv("data/processed/tilak_nagar_clean.csv")

    # Read the service averages and percentages from notebook 02.
    summary = pd.read_csv("data/processed/service_summary.csv")

    # Read the discussion-priority table from notebook 02.
    priority = pd.read_csv("data/processed/issue_priority.csv")

    # Read the suggestion theme counts from notebook 03.
    themes = pd.read_csv("data/processed/suggestion_theme_counts.csv")

# Explain what to do if a required CSV file is missing.
except FileNotFoundError:

    # Show a useful message instead of a long error.
    st.error("Open the project folder and run notebooks 01, 02, and 03 to create the processed CSV files.")

    # Stop until the files are available.
    st.stop()


# STEP 4: LET THE VISITOR CHOOSE A PAGE

# Store the four page names in a list.
pages = [
    "Overview",
    "Satisfaction dashboard",
    "Suggestions and priorities",
    "Community action plan",
]

# Display a page selector in the sidebar.
page = st.sidebar.radio("Choose a page", pages)

# Explain how to refresh the results after changing the raw survey.
st.sidebar.caption("Changed the raw CSV? Run notebooks 01, 02, and 03 again, then refresh this page.")


# STEP 5: DISPLAY THE SELECTED PAGE

# Show this section when Overview is selected.
if page == "Overview":

    # Introduce the project aim.
    st.subheader("Project aim")

    # Explain the purpose in simple language.
    st.write("Understand residents' satisfaction with local services and use their feedback to propose community follow-up.")

    # Display the total cleaned response count.
    st.metric("Total survey responses", len(all_data))

    # Display the main study-area count.
    st.metric("Tilak Nagar responses", len(data))

    # Display responses from the other localities.
    st.metric("Other-locality responses", len(all_data) - len(data))

    # Introduce the services studied.
    st.subheader("Services covered")

    # List the eight services.
    st.write("Water supply, garbage collection, public cleanliness, roads and footpaths, street lighting, drainage, public toilets, and online municipal services.")

    # Introduce the project objectives.
    st.subheader("Objectives")

    # State the first objective.
    st.write("1. Measure satisfaction with local services.")

    # State the second objective.
    st.write("2. Identify concerns in ratings and suggestions.")

    # State the third objective.
    st.write("3. Share findings and propose practical community activities.")

    # Keep the claims within the evidence.
    st.info("This is a small survey sample. The findings describe these respondents and may not represent all Tilak Nagar residents.")


# Show this section when Satisfaction dashboard is selected.
elif page == "Satisfaction dashboard":

    # Add the page heading.
    st.subheader("Satisfaction dashboard")

    # Keep only recorded overall ratings.
    ratings = data["overall_satisfaction"].dropna()

    # Only calculate an average when there are valid ratings.
    if len(ratings) > 0:

        # Calculate the mean rating.
        average = ratings.mean()

        # Select ratings of 4 or 5.
        satisfied = ratings[ratings >= 4]

        # Calculate the satisfied percentage.
        satisfied_percent = len(satisfied) / len(ratings) * 100

        # Show the overall average rounded to two decimal places.
        st.metric("Average overall rating out of 5", round(average, 2))

        # Show the satisfied percentage rounded to two decimal places.
        st.metric("Overall satisfied (%)", round(satisfied_percent, 2))

        # Show the denominator used for both calculations.
        st.write("Valid overall ratings:", len(ratings))

    # Handle a dataset without overall ratings.
    else:

        # Explain why no overall average is shown.
        st.info("There are no valid overall ratings.")

    # Explain the meaning of satisfied.
    st.caption("Satisfied means a rating of 4 or 5. Missing ratings are excluded.")

    # Introduce the service-average chart.
    st.subheader("Average service ratings")

    # Use the service names as chart labels.
    chart_data = summary.set_index("service")

    # Draw a bar chart of the average ratings.
    st.bar_chart(chart_data["mean_rating"], horizontal=True)

    # Explain the scale and missing-answer rule.
    st.caption("Scale: 1 = very dissatisfied, 5 = very satisfied. Non-use and not-applicable answers are not zero ratings.")

    # Show each service's valid count, mean, and percentages.
    st.dataframe(summary, hide_index=True)

    # Introduce the overall rating distribution.
    st.subheader("Overall satisfaction ratings")

    # Count each overall rating.
    rating_counts = ratings.value_counts()

    # Include all five rating categories, including zero counts.
    rating_counts = rating_counts.reindex([1, 2, 3, 4, 5], fill_value=0)

    # Display the rating counts as bars.
    st.bar_chart(rating_counts)

    # Introduce the online municipal service results.
    st.subheader("Online municipal services")

    # Select explicit non-use answers.
    not_used = data[data["online_services_response"] == "I have not used them"]

    # Count valid online-service ratings.
    online_ratings = data["online_services"].dropna()

    # Display the non-use count.
    st.write("Respondents who have not used the service:", len(not_used))

    # Display the numeric rating count.
    st.write("Respondents who provided a rating:", len(online_ratings))

    # Explain the limits of the non-use question.
    st.caption("Non-use does not tell us the reason, dissatisfaction, or digital skill level.")

    # Introduce reporting experience.
    st.subheader("Have residents reported a civic problem?")

    # Count each response to the reporting question.
    reporting_counts = data["reported_problem"].value_counts()

    # Display the response counts.
    st.bar_chart(reporting_counts)

    # Keep the meaning of the original question clear.
    st.caption("The survey did not specify online or offline reporting.")

    # Convert the summary table to CSV text.
    summary_csv = summary.to_csv(index=False)

    # Let the visitor download the summary.
    st.download_button("Download service summary", summary_csv, "service_summary.csv", "text/csv")


# Show this section when Suggestions and priorities is selected.
elif page == "Suggestions and priorities":

    # Introduce the discussion-priority results.
    st.subheader("Services to discuss with residents")

    # Explain how the priority table was calculated.
    st.write("Dissatisfied percentage = ratings 1 or 2 divided by valid ratings, multiplied by 100.")

    # Use service names as labels for the chart.
    priority_chart = priority.set_index("service")

    # Compare the dissatisfied percentages.
    st.bar_chart(priority_chart["dissatisfied_percent"], horizontal=True)

    # Show the valid rating counts alongside the percentages.
    st.dataframe(priority, hide_index=True)

    # Explain how to interpret the ranking.
    st.caption("This is a starting point for discussion, not an official urgency or severity score.")

    # Introduce the suggestion themes.
    st.subheader("Themes in residents' suggestions")

    # Keep recorded comments and exclude blank answers.
    comments = data["suggestion"].dropna()

    # Show how many respondents supplied a comment.
    st.write("Recorded comments:", len(comments), "out of", len(data), "responses")

    # Use theme names as chart labels.
    theme_chart = themes.set_index("theme")

    # Draw the keyword counts.
    st.bar_chart(theme_chart["mentions"], horizontal=True)

    # Display the exact counts.
    st.dataframe(themes, hide_index=True)

    # Explain overlapping themes and the need for manual review.
    st.caption("One comment can match several themes. Keywords can miss context or spelling, so comments also need manual review.")

    # Convert the theme table to CSV text.
    themes_csv = themes.to_csv(index=False)

    # Let the visitor download aggregate theme counts.
    st.download_button("Download suggestion themes", themes_csv, "suggestion_theme_counts.csv", "text/csv")


# Show this section when Community action plan is selected.
elif page == "Community action plan":

    # Make it clear that these are proposed activities.
    st.subheader("Proposed community action plan")

    # Suggest sharing the results with residents.
    st.write("1. Share the survey findings with participating residents.")

    # Suggest discussing the main measured concern.
    st.write("2. Discuss public toilet concerns, which had the highest dissatisfied share in this sample.")

    # Suggest checking other concerns and their locations.
    st.write("3. Ask residents about garbage, lighting, roads, and other issues. Confirm specific locations and problems.")

    # Suggest preparing a useful summary.
    st.write("4. Prepare a summary for the relevant service office after checking the correct contact.")

    # Suggest documenting actual follow-up.
    st.write("5. Record actual activities and residents' feedback in the activity log.")

    # Do not present proposed fieldwork as completed work.
    st.info("Meetings, complaint submissions, and improvements are proposed unless you have evidence that they occurred.")

    # Read the blank activity log included with the project.
    activity_log = pd.read_csv("survey/community_activity_log.csv")

    # Convert the log into CSV text.
    activity_csv = activity_log.to_csv(index=False)

    # Offer the activity log as a download.
    st.download_button("Download blank activity log", activity_csv, "community_activity_log.csv", "text/csv")

    # Open the questionnaire as a text file.
    with open("survey/survey_questions.txt", encoding="utf-8") as question_file:

        # Read the questionnaire text.
        questions = question_file.read()

    # Offer the questionnaire as a download.
    st.download_button("Download survey questions", questions, "survey_questions.txt", "text/plain")


# STEP 6: ADD A FOOTER

# Separate the page content from the footer.
st.divider()

# Explain the website's role.
st.caption("Student survey project | This website displays findings and does not submit municipal complaints.")

```

## requirements.txt

```text
streamlit>=1.50,<2
pandas>=2.2,<4
matplotlib>=3.9,<4

```

## requirements-notebooks.txt

```text
-r requirements.txt
ipykernel>=6,<8

```

## .streamlit/config.toml

```toml
# Use Streamlit's built-in theme.
[theme]

# Use a light background.
base = "light"

# Use green for buttons and selected controls.
primaryColor = "#176B63"

# Use a simple readable font.
font = "sans serif"

```

## .gitignore

```text
# Keep environments and generated Python files out of Git.
.venv/
venv/
__pycache__/
*.pyc
.ipynb_checkpoints/

# Keep credentials and individual response files private by default.
.streamlit/secrets.toml
.env
data/raw/*.csv
data/processed/*clean.csv
survey/community_activity_log.csv

```

## notebooks/01_data_cleaning.ipynb

# 01 Data cleaning

**Topic:** Resident Satisfaction with Local Services in Tilak Nagar, Mumbai.

Run each cell from top to bottom. This notebook reads the raw survey, cleans it, and saves two CSV files. Every important step is visible here; there is no helper file to learn.

A **variable** is a name for a value. A **DataFrame** is a table. A **dictionary** pairs an old name with a new name. A **for loop** repeats the same step for each column.

## 1. Import tools and find the project folder
This setup works when the notebook starts in the project folder or the notebooks folder.

```python
# Pandas helps us work with tables.
import pandas as pd

# os helps us check where the data folder is.
import os

# Start by looking in the project folder.
project_folder = "."

# A notebook may start inside the notebooks folder instead.
if not os.path.exists("data/raw/survey_responses_raw.csv"):

    # Two dots mean the folder one level above this one.
    project_folder = ".."
```

## 2. Read the raw survey
Read everything as text at first. Keep blank answers as empty text. The original CSV will stay unchanged.

```python
# Read the original survey file.
data = pd.read_csv(project_folder + "/data/raw/survey_responses_raw.csv", dtype=str, keep_default_na=False)

# Count the supplied rows.
print("Raw responses:", len(data))

# Show the first five rows.
data.head()
```

## 3. Remove exact duplicate rows
An exact duplicate has the same values in every column, including its timestamp. Matching answers alone do not prove a duplicate person.

```python
# Count completely identical rows.
print("Exact duplicate rows:", data.duplicated().sum())

# Keep one copy of each completely identical row.
data = data.drop_duplicates()

# Remove spaces from the beginning and end of column headings.
data.columns = data.columns.str.strip()
```

## 4. Shorten the column names
Each line in this dictionary means **old question: new column name**. Matching the question text keeps the code correct even if the CSV columns move.

```python
# Give each long survey question a short column name.
column_names = {
    'Timestamp': 'timestamp',
    '1. Do you agree to participate in this survey?': 'consent',
    '2. Which locality do you live in?': 'locality',
    '3. What is your age group?': 'age_group',
    '4. How long have you lived in this area?': 'years_in_area',
    '5. How satisfied are you with the regularity of water supply?': 'water_supply',
    '6. How satisfied are you with garbage collection?': 'garbage_collection',
    '7. How satisfied are you with the cleanliness of public areas?': 'public_cleanliness',
    '8. How satisfied are you with the condition of roads and footpaths?': 'roads_footpaths',
    '9. How satisfied are you with street lighting in your area?': 'street_lighting',
    '10. How satisfied are you with drainage and sewage services?': 'drainage',
    '11. How satisfied are you with the availability and cleanliness of public toilets?': 'public_toilets',
    '12. How satisfied are you with online municipal services or complaint systems?': 'online_services',
    '13. Have you ever reported a local civic problem?': 'reported_problem',
    '14. Overall, how satisfied are you with local government services in your area?': 'overall_satisfaction',
    '15. Which local service needs the most urgent improvement, and what is your suggestion?': 'suggestion',
}

# Rename the columns using the dictionary above.
data = data.rename(columns=column_names)

# Show the short column names.
print(data.columns.tolist())
```

## 5. Clean text and check consent
A for loop lets us remove spaces from every text column without writing the same command sixteen times.

```python
# Repeat the cleaning step for each column.
for column in data.columns:

    # Remove spaces before and after each answer.
    data[column] = data[column].str.strip()

# Keep only people who answered Yes to participation.
data = data[data["consent"].str.lower() == "yes"].copy()

# Use the same capital letters for each locality.
data["locality"] = data["locality"].str.title()

# Use a normal hyphen in age ranges.
data["age_group"] = data["age_group"].str.replace("–", "-", regex=False)

# Keep the original online-service answer before changing it to a number.
data["online_services_response"] = data["online_services"]
```

## 6. Explain the rating scale
The service answers include text such as `4 - Satisfied`. We first keep just the numeric text, such as `"4"`. The next step converts it into a number. `None` means no numeric answer; it is **not zero**.

```python
# Match each full rating answer to its numeric text.
rating_numbers = {
    "1 - Very dissatisfied": "1",
    "2 - Dissatisfied": "2",
    "3 - Neutral": "3",
    "4 - Satisfied": "4",
    "5 - Very satisfied": "5",
    "Not applicable": None,
    "I have not used them": None,
    "": None,
}

# List the columns that contain satisfaction ratings.
rating_columns = [
    "water_supply",
    "garbage_collection",
    "public_cleanliness",
    "roads_footpaths",
    "street_lighting",
    "drainage",
    "public_toilets",
    "online_services",
    "overall_satisfaction",
]
```

## 7. Convert ratings into numbers
`pd.to_numeric` converts numeric text such as `"3"` into a number. An unexpected word causes an error so we can check it. The extra check rejects numbers outside 1 to 5.

```python
# Repeat these steps for each rating column.
for column in rating_columns:

    # Replace the full rating answers using our dictionary.
    data[column] = data[column].replace(rating_numbers)

    # Convert the remaining numeric text into numbers.
    data[column] = pd.to_numeric(data[column])

    # Leave out missing answers when checking the scale.
    valid_answers = data[column].dropna()

    # Check that every recorded rating is 1, 2, 3, 4, or 5.
    if not valid_answers.isin([1, 2, 3, 4, 5]).all():

        # Stop instead of calculating with an incorrect rating.
        raise ValueError("Check the ratings in " + column)
```

## 8. Select the study area
Keep all consenting responses in one file. Save the Tilak Nagar responses separately for the main analysis.

```python
# Keep the rows for the project locality.
tilak_data = data[data["locality"] == "Tilak Nagar"].copy()

# Show the sample sizes.
print("All consenting responses:", len(data))
print("Tilak Nagar responses:", len(tilak_data))
print("Other locality responses:", len(data) - len(tilak_data))

# Count valid ratings for every service.
print(tilak_data[rating_columns].count())
```

## 9. Save the cleaned files
`index=False` means do not add the table row numbers as another CSV column.

```python
# Create the output folder if it does not exist.
os.makedirs(project_folder + "/data/processed", exist_ok=True)

# Save all consenting responses.
data.to_csv(project_folder + "/data/processed/responses_clean.csv", index=False)

# Save the Tilak Nagar responses.
tilak_data.to_csv(project_folder + "/data/processed/tilak_nagar_clean.csv", index=False)

# Confirm that cleaning is complete.
print("Saved the two cleaned CSV files. Open notebook 02 next.")
```

## What to tell your teacher

“I read the survey, removed exact duplicate rows, shortened the column names, kept consenting responses, changed rating text into numbers, selected Tilak Nagar, and saved the results.”

For the supplied file: **32** responses, **26** from Tilak Nagar, and **0** exact duplicate rows. Drainage has **25** valid ratings. Online services have **12** valid ratings and **14** explicit non-use answers. Missing ratings are excluded from averages.

Two Tilak Nagar respondents reported an age below 18. Guardian-permission details were not supplied; discuss use of these records with your supervisor. The sample is small and recruitment details are unknown, so findings describe these respondents.

If the data changes, run this notebook and then notebooks 02 and 03 again. Review the written findings and report separately.

## notebooks/02_exploratory_analysis.ipynb

# 02 Exploratory analysis

Run notebook 01 first. This notebook reads the cleaned Tilak Nagar file, calculates summaries, and saves five charts.

We use ordinary variables and for loops. Each calculation has its own line. All results describe the surveyed residents, not every person in Tilak Nagar.

## 1. Import tools and read the clean file

```python
# Pandas helps us work with tables.
import pandas as pd

# os helps us check where the data folder is.
import os

# Start by looking in the project folder.
project_folder = "."

# A notebook may start inside the notebooks folder instead.
if not os.path.exists("data/raw/survey_responses_raw.csv"):

    # Two dots mean the folder one level above this one.
    project_folder = ".."

# Matplotlib creates chart images.
import matplotlib.pyplot as plt

# Read the Tilak Nagar responses saved by notebook 01.
data = pd.read_csv(project_folder + "/data/processed/tilak_nagar_clean.csv")

# Create the chart folder if needed.
os.makedirs(project_folder + "/images", exist_ok=True)

# Show the number of respondents.
print("Tilak Nagar respondents:", len(data))
```

## 2. Calculate overall satisfaction
`dropna()` removes missing ratings from the calculation. `mean()` calculates an average. `>= 4` selects ratings 4 and 5.

```python
# Keep only valid overall ratings.
overall_ratings = data["overall_satisfaction"].dropna()

# Calculate the average overall rating.
overall_average = overall_ratings.mean()

# Select respondents who gave a rating of 4 or 5.
satisfied_ratings = overall_ratings[overall_ratings >= 4]

# Calculate the satisfied percentage using valid overall ratings.
overall_satisfied_percent = len(satisfied_ratings) / len(overall_ratings) * 100

# Show the results rounded to two decimal places.
print("Overall average:", round(overall_average, 2))
print("Overall satisfied percentage:", round(overall_satisfied_percent, 2))
```

## 3. List the services
The left side is the CSV column. The right side is the name shown to the reader.

```python
# Match each rating column to a readable chart label.
services = {
    'water_supply': 'Water supply',
    'garbage_collection': 'Garbage collection',
    'public_cleanliness': 'Public cleanliness',
    'roads_footpaths': 'Roads and footpaths',
    'street_lighting': 'Street lighting',
    'drainage': 'Drainage',
    'public_toilets': 'Public toilets',
    'online_services': 'Online municipal services',
}
```

## 4. Calculate one row for each service
**Mean = sum of ratings / valid rating count.**

**Satisfied % = ratings 4 or 5 / valid rating count × 100.**

**Dissatisfied % = ratings 1 or 2 / valid rating count × 100.**

The loop repeats these same steps for each service. Missing ratings are excluded. A service with no valid ratings gets a blank result, not zero.

```python
# Start an empty list for the summary rows.
summary_rows = []

# Work on one service column at a time.
for column in services:

    # Find the readable service name.
    service_name = services[column]

    # Keep only valid ratings for this service.
    ratings = data[column].dropna()

    # Count the valid ratings.
    valid_count = len(ratings)

    # Leave results blank until we know there are valid ratings.
    average = None
    satisfied_percent = None
    dissatisfied_percent = None

    # Only divide when there is at least one valid rating.
    if valid_count > 0:

        # Find the mean rating.
        average = round(ratings.mean(), 2)

        # Select the satisfied and dissatisfied ratings.
        satisfied = ratings[ratings >= 4]
        dissatisfied = ratings[ratings <= 2]

        # Work out the percentages one step at a time.
        satisfied_percent = len(satisfied) / valid_count * 100
        dissatisfied_percent = len(dissatisfied) / valid_count * 100

        # Round the percentages for the saved table.
        satisfied_percent = round(satisfied_percent, 2)
        dissatisfied_percent = round(dissatisfied_percent, 2)

    # Put this service's results into one row.
    row = [service_name, valid_count, average, satisfied_percent, dissatisfied_percent]

    # Add the row to the list.
    summary_rows.append(row)
```

## 5. Save the service summary
A list stores the rows. A DataFrame turns those rows into a table with named columns.

```python
# Name the columns in the summary table.
summary_columns = [
    "service",
    "valid_ratings",
    "mean_rating",
    "satisfied_percent",
    "dissatisfied_percent",
]

# Turn our list of rows into a table.
summary = pd.DataFrame(summary_rows, columns=summary_columns)

# Save the table for the website.
summary.to_csv(project_folder + "/data/processed/service_summary.csv", index=False)

# Display the finished table.
summary
```

## 6. Draw average service ratings
The chart compares means out of 5. The previous table shows each service’s valid count: online services has 12 and drainage has 25; other services have 26.

```python
# Put the lower averages first.
chart_data = summary.sort_values("mean_rating")

# Create a figure with enough room for the service names.
plt.figure(figsize=(10, 5))

# Draw horizontal bars using service names and average ratings.
plt.barh(chart_data["service"], chart_data["mean_rating"], color="teal")

# Label the chart and use the full rating scale.
plt.title("Average service ratings - Tilak Nagar sample")
plt.xlabel("Average rating out of 5; see service_summary.csv for valid counts")
plt.xlim(0, 5)

# Fit the labels and save the image.
plt.tight_layout()
plt.savefig(project_folder + "/images/service_satisfaction.png", dpi=150)

# Display the chart and close it before the next chart.
plt.show()
plt.close()
```

## 7. Count the overall ratings
`value_counts()` counts each answer. `reindex()` includes all five ratings, even if nobody selected one. A zero **count** is valid; a missing **rating** is never changed to zero.

```python
# Count each overall rating.
rating_counts = overall_ratings.value_counts()

# Show ratings 1 to 5 in order, including any zero counts.
rating_counts = rating_counts.reindex([1, 2, 3, 4, 5], fill_value=0)

# Display the counts.
print(rating_counts)

# Draw the count chart.
plt.figure(figsize=(8, 4))
plt.bar(rating_counts.index, rating_counts.values, color="steelblue")

# Add the title and axis labels.
plt.title("Overall satisfaction - Tilak Nagar sample")
plt.xlabel("Rating: 1 = very dissatisfied, 5 = very satisfied")
plt.ylabel("Number of respondents")
plt.xticks([1, 2, 3, 4, 5])

# Save and display the chart.
plt.tight_layout()
plt.savefig(project_folder + "/images/overall_satisfaction.png", dpi=150)
plt.show()
plt.close()
```

## 8. Count ratings for each service
This uses the same counting method in a loop. Rows are services; columns are ratings 1 to 5.

```python
# Start an empty table for the rating counts.
distribution = pd.DataFrame()

# Count the five ratings for every service.
for column in services:

    # Count the ratings in this service column.
    counts = data[column].value_counts()

    # Include every rating category.
    counts = counts.reindex([1, 2, 3, 4, 5], fill_value=0)

    # Add these counts using the readable service name.
    distribution[services[column]] = counts

# Swap rows and columns so each row is one service.
distribution = distribution.T

# Display the counts.
distribution
```

## 9. Draw the service rating distributions
A stacked bar shows how the ratings are divided. Bar lengths differ because missing ratings are excluded.

```python
# Draw one stacked horizontal bar for each service.
distribution.plot(kind="barh", stacked=True, figsize=(10, 5))

# Add chart labels and put the legend outside the bars.
plt.title("Service rating counts - Tilak Nagar sample")
plt.xlabel("Number of valid ratings")
plt.ylabel("")
plt.legend(title="Rating", bbox_to_anchor=(1, 1))

# Save and display the chart.
plt.tight_layout()
plt.savefig(project_folder + "/images/rating_distribution.png", dpi=150)
plt.show()
plt.close()
```

## 10. Show online service non-use separately
A non-use answer is not dissatisfaction. The survey did not measure reasons for non-use.

```python
# Select respondents who explicitly said they had not used the service.
not_used_rows = data[data["online_services_response"] == "I have not used them"]

# Count non-use answers and valid ratings.
not_used_count = len(not_used_rows)
rated_count = data["online_services"].count()

# Count any remaining missing or not-applicable answers.
other_count = len(data) - not_used_count - rated_count

# Prepare labels and counts for the chart.
online_labels = ["Have not used", "Provided a rating", "Other or missing"]
online_counts = [not_used_count, rated_count, other_count]

# Print the exact counts.
print("Non-use:", not_used_count)
print("Provided a rating:", rated_count)
print("Other or missing:", other_count)

# Draw the chart and label it.
plt.figure(figsize=(8, 4))
plt.bar(online_labels, online_counts, color="teal")
plt.title("Online municipal services - Tilak Nagar sample")
plt.ylabel("Number of respondents")

# Save and display the chart.
plt.tight_layout()
plt.savefig(project_folder + "/images/online_service_use.png", dpi=150)
plt.show()
plt.close()
```

## 11. Save discussion priorities
We sort by dissatisfied percentage. This helps begin a discussion; it is not an official urgency or severity ranking.

```python
# Put the highest dissatisfied percentage first.
priority = summary.sort_values("dissatisfied_percent", ascending=False)

# Save the priority table for the website.
priority.to_csv(project_folder + "/data/processed/issue_priority.csv", index=False)

# Display the priority table.
priority
```

## 12. Draw the priority chart
The full percentage scale runs from 0 to 100. Use the valid count in the summary table when interpreting each percentage.

```python
# Reverse the order so the largest horizontal bar appears at the top.
chart_data = priority.sort_values("dissatisfied_percent")

# Draw the dissatisfied percentages.
plt.figure(figsize=(10, 5))
plt.barh(chart_data["service"], chart_data["dissatisfied_percent"], color="peru")

# Add labels and the full percentage scale.
plt.title("Discussion priorities - Tilak Nagar sample")
plt.xlabel("Ratings 1 or 2 as % of valid ratings; see issue_priority.csv for counts")
plt.xlim(0, 100)

# Save and display the chart.
plt.tight_layout()
plt.savefig(project_folder + "/images/issue_priority.png", dpi=150)
plt.show()
plt.close()
```

## What to tell your teacher

“I used counts, averages, and percentages. I removed missing ratings before calculating. Then I used bar charts to compare services.”

For the supplied data: overall average **3.81/5**, overall satisfied **14/26 = 53.85%**, and public toilet dissatisfaction **8/26 = 30.77%**. Public toilets have the lowest mean, **3.04/5**. Public cleanliness has the highest mean, **4.35/5**. Online services have only **12** valid ratings, so their mean uses 12, not 26.

The charts and summaries are saved. Continue with notebook 03. If the raw data changes, update these written interpretations and the report after rerunning the notebooks.

## notebooks/03_suggestion_analysis.ipynb

# 03 Suggestion analysis

Run notebooks 01 and 02 first. Here we read optional comments and count simple keywords. We use normal `if` statements so you can see exactly what is counted.

One comment may mention several topics. A blank comment means no suggestion was recorded, not that the resident had no concerns.

## 1. Read the clean data

```python
# Pandas helps us work with tables.
import pandas as pd

# os helps us check where the data folder is.
import os

# Start by looking in the project folder.
project_folder = "."

# A notebook may start inside the notebooks folder instead.
if not os.path.exists("data/raw/survey_responses_raw.csv"):

    # Two dots mean the folder one level above this one.
    project_folder = ".."

# Matplotlib creates the suggestion chart.
import matplotlib.pyplot as plt

# Read the clean Tilak Nagar data and keep empty comments as empty text.
data = pd.read_csv(project_folder + "/data/processed/tilak_nagar_clean.csv", keep_default_na=False)

# Select only recorded comments.
comments = data[data["suggestion"] != ""]["suggestion"]

# Show how many comments are available.
print("Recorded comments:", len(comments))
print("Blank comments:", len(data) - len(comments))
```

## 2. Read the comments yourself
Keywords can miss context or spelling. Review the comments before drawing conclusions. These comments are for private project review; clear this cell’s output before public sharing.

```python
# Visit each recorded comment.
for comment in comments:

    # Print the original suggestion.
    print(comment)

    # Add a blank line between suggestions.
    print()
```

## 3. Start every theme count at zero
A counter is a variable that increases when we find a matching comment.

```python
# Start a separate counter for each theme.
road_count = 0

toilet_count = 0

garbage_count = 0

cleanliness_count = 0

drainage_count = 0

lighting_count = 0

traffic_count = 0

complaint_count = 0
```

## 4. Count keyword matches
`lower()` changes capital letters to small letters. `in` checks whether a word appears. `or` means either keyword may match. Each `if` adds at most one to that theme for a comment. Separate `if` statements allow several themes in one comment.

```python
# Look at one comment at a time.
for comment in comments:

    # Use small letters so matching ignores capitalisation.
    comment = comment.lower()

    # Count a roads or footpaths mention.
    if "road" in comment or "footpath" in comment:
        road_count = road_count + 1

    # Count a public toilets mention.
    if "toilet" in comment:
        toilet_count = toilet_count + 1

    # Count a garbage collection mention.
    if "garbage" in comment or "dustbin" in comment:
        garbage_count = garbage_count + 1

    # Count a cleanliness mention.
    if "clean" in comment or "cleanness" in comment:
        cleanliness_count = cleanliness_count + 1

    # Count drainage words, including a spelling used in the source.
    if "drain" in comment or "guttar" in comment or "sewage" in comment:
        drainage_count = drainage_count + 1

    # Count a street lighting mention.
    if "street light" in comment:
        lighting_count = lighting_count + 1

    # Count a traffic or parking mention.
    if "traffic" in comment or "parking" in comment or "honking" in comment:
        traffic_count = traffic_count + 1

    # Count a complaint-system mention.
    if "complaint" in comment:
        complaint_count = complaint_count + 1
```

## 5. Save the theme table
Each inner list contains a theme name and its count. The table goes to the website.

```python
# Put each theme and count into a row.
theme_rows = [
    ["Roads and footpaths", road_count],
    ["Public toilets", toilet_count],
    ["Garbage collection", garbage_count],
    ["Cleanliness", cleanliness_count],
    ["Drainage", drainage_count],
    ["Street lighting", lighting_count],
    ["Traffic and parking", traffic_count],
    ["Complaint systems", complaint_count],
]

# Make a table with two named columns.
themes = pd.DataFrame(theme_rows, columns=["theme", "mentions"])

# Put the most-mentioned themes first.
themes = themes.sort_values("mentions", ascending=False)

# Save the results for the website.
themes.to_csv(project_folder + "/data/processed/suggestion_theme_counts.csv", index=False)

# Display the theme counts.
themes
```

## 6. Draw the theme chart
Theme counts can add up to more than the number of comments because one comment can match several themes.

```python
# Order the bars so the largest appear at the top.
chart_data = themes.sort_values("mentions")

# Draw one bar for each theme.
plt.figure(figsize=(10, 5))
plt.barh(chart_data["theme"], chart_data["mentions"], color="teal")

# Label the chart and use whole-number count marks.
plt.title("Suggestion themes - Tilak Nagar sample")
plt.xlabel("Comments mentioning a theme; multiple themes allowed")
plt.xticks(range(0, len(comments) + 1))

# Fit the chart, save it, and show it.
plt.tight_layout()
plt.savefig(project_folder + "/images/suggestion_themes.png", dpi=150)
plt.show()
plt.close()
```

## What to tell your teacher

“I read the comments and counted words such as toilet, road, garbage, and traffic. I used simple if statements. This is keyword counting, not machine learning.”

For the supplied data, **15** respondents left comments and **11** did not. Toilets, cleanliness, and traffic/parking each match **4** comments. Check the comments because keyword matches can miss context, negation, or spellings.

## Proposed community activities

1. Share aggregate findings with participating residents.
2. Ask which public toilet locations and service problems need attention.
3. Discuss garbage, lighting, roads, and the other reported concerns.
4. Prepare a summary for the appropriate representative or service office after verifying the contact.
5. Record actual meetings, submissions, feedback, and follow-up in `survey/community_activity_log.csv`.

These are proposals. No completed meeting, complaint submission, or improvement is claimed. Add only fieldwork details you can support with your actual records.

## Optional Power BI guide

# Optional Power BI dashboard without DAX code

The Streamlit website is the main dashboard. A Power BI file is not required to run it. A genuine `.pbix` file is not included.

If your teacher requires Power BI, use the already calculated CSV summaries:

1. Open Power BI Desktop.
2. Select **Get data > Text/CSV**.
3. Import `data/processed/service_summary.csv`.
4. Add a bar chart with `service` as the category and `mean_rating` as the value.
5. Add a table with `service`, `valid_ratings`, `mean_rating`, and `dissatisfied_percent`.
6. Import `data/processed/suggestion_theme_counts.csv`.
7. Add a bar chart with `theme` as the category and `mentions` as the value.
8. Add the title **Tilak Nagar survey results**.
9. Save the file in this folder as `citizen_satisfaction_dashboard.pbix`.

These summaries describe all Tilak Nagar respondents. Do not add an age filter to these precomputed summary charts; the tables have no age-level breakdown. The percentage columns already contain numbers such as `30.77`; label them with (%) and do not apply a percentage format that multiplies them by 100 again.

You do not need DAX formulas for these steps. They have not been executed in Power BI Desktop here.
