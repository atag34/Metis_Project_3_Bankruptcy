import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pickle
import streamlit.components.v1 as components
import urllib.parse

X_cols=['current assets', 'cash and cash equivalents',
       'accounts receivable net', 'prepaid expenses', 'other current assets',
       'total current assets', 'property and equipment net', 'goodwill',
       'other assets', 'total assets', 'current liabilities',
       'accounts payable', 'accrued expenses',
       'current maturities of longterm debt', 'total current liabilities',
       'other longterm liabilities','accumulated deficit', 'accumulated other comprehensive loss',
       'inventories', 'restricted cash',
       'prepaid expenses and other current assets', 'deferred income taxes',
       'other noncurrent liabilities', 'total liabilities',
       'retained earnings', 'total stockholders equity',
       'total liabilities and stockholders equity', 'preferred stock',
       'current portion of longterm debt', 'other liabilities',
       'additional paidin capital', 'total stockholders’ equity',
       'total liabilities and stockholders’ equity', 'longterm debt',
       'accumulated other comprehensive income', 'noncontrolling interest',
       'intangible assets net', 'accounts payable and accrued expenses',
       'assets held for sale', 'other noncurrent assets', 'common stock',
       'noncontrolling interests', 'total equity',
       'total liabilities and equity', 'property plant and equipment net',
       'other longterm assets', 'deferred revenue', 'other',
       'accrued interest','inventory', 'asset retirement obligations', 'retained deficit',
       'accounts payable and accrued liabilities', 'accrued liabilities',
       'accounts receivable', 'other current liabilities']

dat=pd.read_pickle('FINAL_ALL_DAT.pkl')

st.title('Bankruptcy Prediction (NYSE)')

#select a company to focus on
st.text('Show company filling predictions')
more_cols = st.checkbox(label='Financial Data',key='co')
	

Companies = dat['Name'].unique()
company_selected = st.sidebar.multiselect('Select Company', Companies)

#return a dataframe for select company
if more_cols:
	m1 = dat['Name'].isin(company_selected)
	dat.loc[m1][['CIK','Name','Filings','Filing Date','predict','banruptcy_6_mo','d_to_bankruptcy']+X_cols]
else:
	m1 = dat['Name'].isin(company_selected)
	dat.loc[m1][['CIK','Name','Filings','Filing Date','predict','banruptcy_6_mo','d_to_bankruptcy']]

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
	year_dat1=year_dat[['CIK','Name','Filings','Filing Date','predict','banruptcy_6_mo','d_to_bankruptcy']+X_cols].head()
else:
	year_dat1=year_dat[['CIK','Name','Filings','Filing Date','predict','banruptcy_6_mo','d_to_bankruptcy']]

	st.dataframe(year_dat1)
