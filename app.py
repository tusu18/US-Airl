import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
os.environ["NUMEXPR_MAX_THREADS"]="16"
os.environ["NUMEXPR_NUM_THREADS"]="16"


st.title("US airlines")
st.markdown("![Alt Text](https://akm-img-a-in.tosshub.com/sites/btmt/images/stories/jet-(5)-660_041919081440.jpg)")
st.sidebar.title("Sentiment Analysis of US airlines")
st.markdown("This application is used to analyze Tweets sentiment")
st.sidebar.markdown("Filters")
DATA_URL=(r"C:\Users\tusman\Documents\Vspy\Tweets.csv")
@st.cache(persist=True)
def load_dat():
    data=pd.read_csv(DATA_URL)
    data["tweet_created"]=pd.to_datetime(data["tweet_created"]) 
    return dataE3SD
    
data=load_dat()  
   
st.sidebar.subheader("Show Tweets")
random_tweet=st.sidebar.radio("Sentiment",('positive','neutral','negative')) 
st.sidebar.markdown(data.query('airline_sentiment== @random_tweet')[['text']].sample(n=1).iat[0,0])

st.sidebar.markdown("### No. of tweets by sentiments")
select=st.sidebar.selectbox("Visualization type",["Histogram","Piechart"],key="1")

sentiment_count=data['airline_sentiment'].value_counts()
sentiment_count=pd.DataFrame({"Sentiment":sentiment_count.index,"Tweets":sentiment_count.values})

if not st.sidebar.checkbox("Hide",True):
    st.markdown("### No of Tweets by sentiment")
    if select=="Histogram":
        fig=px.bar(sentiment_count,x="Sentiment",y="Tweets",color="Tweets",height=500)
        st.plotly_chart(fig)
    elif select=="Piechart":
        fig=px.pie(sentiment_count,values="Tweets",names="Sentiment")
        st.plotly_chart(fig)    

st.sidebar.subheader("Time and Position stats of the tweets")
hour=st.sidebar.slider("Hour od days",0,23)
mod_data=data[data['tweet_created'].dt.hour == hour]
if not st.sidebar.checkbox("Close",True,key='1'):
    st.markdown("### Tweet locations based on time of given Day")
    st.markdown("%i tweets between %i:00 and %i:00"%(len(mod_data),hour,(hour+1)%24))
st.sidebar.subheader("Breakdown of tweets by sentiment0")
choice=st.sidebar.multiselect("Pick Airlines",("US Airways","United","American","Southwest","Delta","Virgin America"),key="0")
if len(choice)>0:
    choic_dat=data[data.airline.isin(choice)]
    fig_choic=px.histogram(choic_dat,x="airline",y="airline_sentiment",histfunc="count",color="airline_sentiment",facet_col="airline_sentiment",
    labels={"airline_sentiment":"tweets"},height=600,width=800)
    st.plotly_chart(fig_choic)

st.header("Word Cloud")
wrd_sent=st.sidebar.radio("Display world cloud for sentiment?",("positive","negative","neutral"))
if not st.sidebar.checkbox("Close",True,key=0):
    st.header("Word cloud for %s sentiment"%(wrd_sent))
    df=data[data['airline_sentiment']==wrd_sent]
    words=" ".join(df["text"])
    prcsd_word=" ".join([word for word in words.split() if 'http' not in word and not word.startswith("@") and word !="RT"])
    wordcloud=WordCloud(stopwords=STOPWORDS,background_color="white",height=640,width=800).generate(prcsd_word)
    plt.imshow(wordcloud)
    plt.xticks([])
    plt.yticks([])
    st.pyplot()
    
