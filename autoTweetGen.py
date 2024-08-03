import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import google.generativeai as genai
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def post_to_twitter(news: str):
    client = tweepy.Client(
        consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
        consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
        access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
        access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
    )
    auth = tweepy.OAuth1UserHandler(
        os.getenv('TWITTER_CONSUMER_KEY'),
        os.getenv('TWITTER_CONSUMER_SECRET'),
        os.getenv('TWITTER_ACCESS_TOKEN'),
        os.getenv('TWITTER_ACCESS_SECRET')
    )
    api = tweepy.API(auth)
    client.create_tweet(text=news)
    st.success("Posted successfully!")

# Page setup
st.set_page_config(page_title="AutoTweetGen", page_icon="📺", layout="centered")

# Use Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open('News_Data_Final').worksheet("Data1")

st.title("📤Automatic Post Generation📤")
st.subheader("To send News Post on the tweeter enter news details🚀")

def main():
    # Input fields for new data
    st.subheader("Enter New News Data")
    title = st.text_input("Title")
    summary = st.text_area("Summary")
    no_of_hashtags = st.number_input("No. of Hashtags", min_value=0, step=1)
    link = st.text_input("Link")
    Button = st.button("POST 🏑")
    # Button to add new data
    if Button:
        response = model.generate_content([f"Generate a Short X Post (Twitter) Based on the following fields\
                                            {title} : {summary}. generate {no_of_hashtags} and add this link at \
                                            bottom : {link} | Output a Post without Markdown and only one Post which should be less than 280 characters (including the length of link text)"])
        st.write(response.text)
        post_to_twitter(response.text)            
        # Prepare new data row
        new_row = [title, summary, int(no_of_hashtags), link]
        # Append new data to Google Sheet
        sheet.append_row(new_row)

if __name__ == "__main__":
    main()