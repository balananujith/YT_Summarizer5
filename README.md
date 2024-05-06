# YouTube Video Summarizer

Welcome to our YouTube Video Summarizer project! This tool condenses the transcript of any YouTube video into a concise summary, highlighting the key points in under 250 words. Say goodbye to skimming through lengthy transcripts, and get the gist of the video content quickly and efficiently.

## How it Works

Our tool utilizes the YouTube Transcript API to extract the transcript text from a given YouTube video URL. Then, it leverages Google Generative AI to generate detailed notes based on the extracted transcript. The final output is a succinct summary of the video content, making it easier for you to understand the main points covered in the video.

## How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/balananujith/YT_Summarizer5.git
2. Navigate to the project directory:
    ```bash
   cd YT_Summarizer5.git
3. Install the required dependencies
    ```bash
    pip install -r requirements.txt
4. Set up your environment variables:
- Create a `.env` file in the project root directory.
- Add your Google API key to the `.env` file:
  ```bash
  GOOGLE_API_KEY=your_google_api_key

5. Run the Streamlit app:
    ```bash
   streamlit run app.py

## How to Contribute

Welcome contributions from the community to enhance the functionality and usability of our YouTube Video Summarizer tool. If you'd like to contribute, feel free to fork the repository, make your changes, and submit a pull request. Here's how you can do it:

1. Fork the repository by clicking the "Fork" button on the top right of this page.
2. Clone your forked repository to your local machine.
3. Create a new branch to work on your changes:
    ```bash
   git checkout -b feature/new-feature
4. Make your changes and commit them:
    ```bash
   git add .
   git commit -m "Add new feature"
6. Push your changes to your fork:
    ```bash
   git push origin feature/new-feature
7. Finally, submit a pull request from your forked repository on GitHub.




