# Verification of the simplified project

Checks performed on 5 October 2026:

- The original raw CSV is byte-for-byte unchanged from the supplied source.
- Both clean response tables contain the same values as the previous project.
- All three summary tables contain the same counts, averages, and percentages as before. Priority rows are now saved in descending dissatisfaction order.
- All 27 code cells in the three notebooks were executed from top to bottom, in notebook order, with no errors or warning outputs.
- The notebooks use no custom functions, lambda expressions, comprehensions, helper imports, or regular-expression matching. All cleaning, calculations, and keyword checks are visible in their cells.
- Notebook outputs were saved using in-process IPython execution. This does not constitute a separate Jupyter server or VS Code kernel test.
- Streamlit AppTest checked all four website pages without application exceptions.
- The app displays 32 total responses, 26 Tilak Nagar responses, six other-locality responses, mean overall satisfaction 3.81/5, and 53.85% overall satisfied.
- The first row in the priority table is public toilets, with 30.77% dissatisfied.
- Python syntax is valid. Every executable statement in `app.py` has a preceding explanatory comment.
- Six chart images were regenerated and visually reviewed.
- The Word report's description of the website and code was updated. It was rendered to a matching seven-page PDF, and every page was visually reviewed. Existing report figures retain their earlier presentation of the same verified results; the notebooks now create simpler chart designs.
- The final ZIP was checked for file integrity and includes the full source, data, notebooks, charts, guides, and reports. It excludes the removed helper file and Python caches.

The locality and age filters were deliberately removed from the simplified website. The website reads the processed CSV files. Run notebooks 01, 02, and 03 after any raw-data change. Written interpretations, recommendations, and the report need separate review after a data update.

Checked with Python 3.12, Streamlit 1.65.0, Pandas 2.2.3, and Matplotlib 3.10.8.

A live browser server, Windows setup, public hosting, and Power BI Desktop execution were not tested here. The project is supplied as local runnable source with setup instructions.
