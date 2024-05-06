import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv() ##load all the environment variables
import os
import google.generativeai  as genai

genai.configure(apikey=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Youtube Video Summarizer. You will be taking the transcript text and summarizing the entire video and providing the important summary in points withing 250 words. The transcript text will be appended here : """

#getting transcript details from  youtube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript_text += " " + i["text"]
        return transcript
    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_context(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_context(prompt+transcript_text)
    return response.text