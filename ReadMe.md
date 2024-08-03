
# AutoTweetGen 📤

AutoTweetGen is a Streamlit-based web application that automatically generates and posts tweets based on news data. It uses the Gemini AI model to create engaging tweets and interacts with Google Sheets to store news data.

## 🚀 Features

- Generate AI-powered tweets from news data
- Post tweets directly to Twitter
- Store news data in Google Sheets
- User-friendly Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Sheets API
- Google Generative AI (Gemini model)
- Twitter API (via Tweepy)
- pandas

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10
- A Google Cloud Platform account with Google Sheets API enabled
- A Twitter Developer account with API access
- Gemini AI API key

## 🔧 Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/AutoTweetGen.git
   cd AutoTweetGen
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add the following:
   ```
   API_KEY=your_gemini_api_key
   TWITTER_CONSUMER_KEY=your_twitter_consumer_key
   TWITTER_CONSUMER_SECRET=your_twitter_consumer_secret
   TWITTER_ACCESS_TOKEN=your_twitter_access_token
   TWITTER_ACCESS_SECRET=your_twitter_access_secret
   ```

4. Set up Google Sheets credentials:
   - Create a service account in Google Cloud Console
   - Download the JSON key file and rename it to `creds.json`
   - Place `creds.json` in the project root

## 📊 Google Sheets Setup

1. Create a new Google Sheet named "News_Data_Final"
2. Create a worksheet named "Data1" within the sheet
3. Share the Google Sheet with the email address in your `creds.json` file

## 🚀 Usage

1. Run the Streamlit app using command:
   ```
   streamlit run autoTweetGen.py
   ```

2. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`)

3. Enter the news details:
   - Title
   - Summary
   - Number of hashtags
   - Link

4. Click the "POST 🏑" button to generate and post the tweet

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/yourusername/AutoTweetGen/issues).

## 📝 License

This project is [MIT] licensed.

## 👤 Author

Your Name
- GitHub: [@Sandesh Tangade](https://github.com/TangadeSandesh)
- Twitter: [@tangadesandesh](https://twitter.com/tangadesandesh)

```