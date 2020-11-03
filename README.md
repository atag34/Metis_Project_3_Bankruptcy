# Metis Project 3
## Bankruptcy prediction using a binary classifier.

For this project I will be using Annual and Quarterly Balance sheet data reported through the SEC EDGAR database to predict if a company will file for bankruptcy in the next year.

**Sources**
	* [USLA Bankruptcy Database](https://lopucki.law.ucla.edu/spreadsheet.htm)
	* [SEC EDGAR Database](https://www.sec.gov/edgar/searchedgar/companysearch.html)

It is important to flag that the presentation was using a different model when it was made. Considering a mistake in sampling that led to test data leaking into the model, I have resolved the issue in the final Project_Walkthrough file. This resulted in a less accurate model unfortunately, however it may be more generalizable.

Ultimately the model suffers from sparse and imperfect data, though given the amount of signal present it could be worth while trying to perfect the data and try the model again.

-Project_Walkthrough.ipynb contains a more narrative example of the data cleaning and modeling process for the project.

-EDGAR_data_collection.ipynb shows the method of data collection from USCLA and EDGAR.

-Project_app.py contains a streamlit app to meet the projects interactive requirement. The app can be used to explore some of the data collected as well as model predictions for the future.
