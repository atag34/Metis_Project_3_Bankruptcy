import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pickle
import streamlit.components.v1 as components
import urllib.parse

X_cols=['common stock', 'current portion of longterm debt_cumsum',
       'other noncurrent liabilities', 'total stockholders equity_cumsum',
       'assets held for sale_cumsum', 'property and equipment net_cumsum',
       'preferred stock', 'total stockholders’ equity_cumsum',
       'deferred revenue', 'current portion of longterm debt_diff',
       'prepaid expenses', 'retained earnings',
       'prepaid expenses and other current assets_cumsum',
       'accounts receivable_diff', 'goodwill_cumsum',
       'current maturities of longterm debt', 'goodwill', 'retained deficit',
       'property and equipment net_diff',
       'total liabilities and stockholders’ equity_diff',
       'asset retirement obligations', 'current portion of longterm debt',
       'retained earnings_cumsum', 'total assets_cumsum',
       'retained deficit_diff', 'accumulated deficit', 'current liabilities',
       'retained earnings_diff', 'other assets_cumsum',
       'accumulated deficit_diff']

dat=pd.read_pickle('FINAL_data_for_app.pkl')

st.title('./Data Files/Bankruptcy Prediction (NYSE)')

#select a company to focus on
st.text('Show company filling predictions')
more_cols = st.checkbox(label='Financial Data',key='co')
	

Companies = dat['Name'].unique()
company_selected = st.sidebar.multiselect('Select Company', Companies)

#return a dataframe for select company
if more_cols:
	m1 = dat['Name'].isin(company_selected)
	dat.loc[m1][['CIK','Name','Filings','Filing Date','predicted','bankruptcy_1_yr','d_to_bankruptcy']+X_cols]
else:
	m1 = dat['Name'].isin(company_selected)
	dat.loc[m1][['CIK','Name','Filings','Filing Date','predicted','bankruptcy_1_yr','d_to_bankruptcy']]

st.dataframe(dat)

st.text('News Sentiment Timeline (1 year)')
components.iframe('https://api.gdeltproject.org/api/v2/doc/doc?format=html&timespan=1Y&query=%22'+urllib.parse.quote(company_selected[0])+'%22%20sourcecountry:US%20sourcelang:eng&mode=timelinetone',height=300)

st.title('Current Watchlist Companies')

more_cols_watch = st.checkbox(label='Financial Data',key='watch')
mask = dat['Filing Date']>= datetime.datetime.now() - datetime.timedelta(days=500)

year_dat = dat[mask]
watchlist = year_dat.groupby(['CIK']).sum()[['predict','d_to_bankruptcy']]
m_watch = (watchlist['predict']>0) &  (watchlist['d_to_bankruptcy']==0)
year_dat=year_dat[year_dat.CIK.isin(watchlist[m_watch].index.tolist())].groupby(['Name','Filing Date','Filings'],as_index=False).sum()

if more_cols_watch:
	year_dat1=year_dat[['CIK','Name','Filings','Filing Date','predicted','bankruptcy_1_yr','d_to_bankruptcy']+X_cols].head()
else:
	year_dat1=year_dat[['CIK','Name','Filings','Filing Date','predicted','bankruptcy_1_yr','d_to_bankruptcy']]

	st.dataframe(year_dat1)
