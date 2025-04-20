# Smart Text Summarizer

A Streamlit-based application that summarizes text and PDF documents using TF-IDF extractive summarization.

## Features
- Upload text files (.txt) or PDF files
- Paste text directly
- Adjustable summary length
- Download summary as text file
- Word count statistics
- Clean, modern interface

## Technologies Used
- Python 3.12
- Streamlit
- NLTK
- scikit-learn
- PyPDF2
- Docker

## How to Run Locally
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the app:
```bash
streamlit run main_code.py
```

## Docker Support
Build and run with Docker:
```bash
docker build -t summarizer-app .
docker run -p 8501:8501 summarizer-app
```

## Created By
Ananya Gupta
