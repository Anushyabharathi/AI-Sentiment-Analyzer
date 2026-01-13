AI-BASED SENTIMENT ANALYZER:

A lightweight web application that analyzes user-entered text and determines its sentiment — Positive, Negative, or Neutral — using basic Natural Language Processing (NLP) techniques.
This project is designed to be simple, fast, and beginner-friendly, making it ideal for mini-projects, assignments, and demos.

------------------------------------------------------------------------------------------------------------------------

PROJECT OBJECTIVE:
      
      * Accept textual input from users (reviews, comments, feedback)
      * Analyze the emotional polarity of the text
      * Display the sentiment result visually using emojis, colors, and a polarity bar

----------------------------------------------------------------------------------------------------------------------
FEATURES

      * Sentiment classification (Positive / Negative / Neutral)
      * Emoji-based sentiment indication
      * Color-coded sentiment result
      * Dark mode functionality
      * Polarity strength progress bar
      * Simple and clean web interface
      * Fast response without heavy ML models
      * Works offline (no API or internet required)

-----------------------------------------------------------------------------------------------------------------------

TECHNOLOGIES USED

      Python – Backend logic
      Flask – Web framework
      TextBlob – NLP sentiment analysis
      HTML – Frontend structure
      CSS – Styling and UI

-----------------------------------------------------------------------------------------------------------------------

APPLICATION WORKFLOW

      1. User enters text in the web form
      2. Flask backend receives the input
      3. TextBlob analyzes the sentiment polarity
      4. Text is classified as Positive, Negative, or Neutral
      5. Result is displayed with emoji and visual indicators

------------------------------------------------------------------------------------------------------------------------

SENTIMENT LOGIC:
    Polarity Range: -1.0 to +1.0
    
    * Polarity > 0 → Positive
    * Polarity < 0 → Negative
    * Polarity = 0 → Neutral
    
    The polarity strength is shown using a percentage-based progress bar.

------------------------------------------------------------------------------------------------------------------------

SAMPLE OUTPUTS:
    <img width="1919" height="920" alt="image" src="https://github.com/user-attachments/assets/fb95e4b2-5303-4ddf-b0b8-722c4bda0609" />
    <img width="1915" height="858" alt="image" src="https://github.com/user-attachments/assets/9d1daf02-a2b6-41ea-ab5a-6beda769b806" />
    <img width="1912" height="876" alt="image" src="https://github.com/user-attachments/assets/9c464e34-e9ef-426a-8421-42cbf262ad1c" />
    
-----------------------------------------------------------------------------------------------------------------------

FUTURE ENHANCEMENTS:
    * Store results in a database
    * Sentiment analytics dashboard
    * Multilingual sentiment analysis
    * User authentication system

