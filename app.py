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
