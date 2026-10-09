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
