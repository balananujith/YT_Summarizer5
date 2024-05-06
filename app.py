import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Welcome prompt
prompt = """
Welcome to our YouTube Video Summarizer tool! Our goal is to condense the transcript of any video into a concise summary, highlighting the key points in under 250 words. We're here to make sure you get the gist of the video without having to go through the entire transcript.
"""

# Function to extract transcript text from YouTube video
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript
    except Exception as e:
        raise e

# Function to generate detailed notes using Google Generative AI
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit app
def main():
    st.title("YouTube Transcript to Detailed Notes Converter")

    # Input field for YouTube video link
    youtube_link = st.text_input("Enter YouTube Video Link:")

    # Display YouTube video thumbnail
    if youtube_link:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    # Button to trigger summarization process
    if st.button("Get Detailed Notes"):
        if youtube_link:
            # Extract transcript from YouTube video
            transcript_text = extract_transcript_details(youtube_link)

            if transcript_text:
                # Generate detailed notes using Google Generative AI
                summary = generate_gemini_content(transcript_text, prompt)

                # Display the summary
                st.markdown("## Detailed Notes:")
                st.write(summary)
            else:
                st.error("Failed to retrieve transcript.")
        else:
            st.warning("Please enter a YouTube video link.")

if __name__ == "__main__":
    main()
