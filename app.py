import streamlit as st
from dotenv import load_dotenv
load_dotenv() ##load all the environment variables
import os
import google.generativeai  as genai
genai.configure(apikey=os.getenv("GOOGLE_API_KEY"))
prompt="""You are Youtube Video Summarizer. You will be taking the transcript text and summarizing the entire video and providing the important summary in points withing 250 words"""
def generate_gemini_context(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")