import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import PyPDF2
import io

nltk.download('punkt')

#Summarizer Function
def tfidf_summarize(text, num_sentences=3):
    sentences = sent_tokenize(text)
    if len(sentences) <= num_sentences:
        return text
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(sentences)
    doc_vector = np.asarray(tfidf_matrix.mean(axis=0)).reshape(1, -1)
    similarities = cosine_similarity(tfidf_matrix, doc_vector)
    ranked_sentences = [sentences[i] for i in np.argsort(similarities.flatten())[::-1]]
    summary = ' '.join(ranked_sentences[:num_sentences])
    return summary

#Streamlit UI 
st.set_page_config(page_title="🧠 Smart Text Summarizer", layout="centered")
st.markdown("""
    <style>
        .main { background-color: #f5f7fa; }
        .stTextArea textarea { font-size: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Smart Text Summarizer")
st.subheader("Summarize large text or PDFs using extractive TF-IDF logic")

#Text Input Area
input_text = ""
summary = ""

with st.expander("📤 Upload .txt or .pdf file, or paste text"):
    file = st.file_uploader("Upload a `.txt` or `.pdf` file", type=["txt", "pdf"])
    if file:
        if file.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                input_text += page.extract_text()
        else:
            input_text = file.read().decode("utf-8")
    else:
        input_text = st.text_area("Or paste your text here 👇", height=250)

#Summary Length 
st.markdown("---")
summary_length = st.slider("Choose summary length (sentences)", 1, 20, 3, help="Select how many sentences you want in your summary")
st.markdown("---")

#Generate Summary
if st.button("📝 Generate Summary"):
    if input_text.strip() == "":
        st.warning("⚠️ Please upload or paste some text first.")
    else:
        summary = tfidf_summarize(input_text, num_sentences=summary_length)
        st.success("✅ Summary Generated!")
        edited_summary = st.text_area("✍️ Edit your summary here", summary, height=200, key="editable_summary")
        
        st.markdown(f"🧾 **Original Text:** {len(input_text.split())} words  \n✂️ **Summary:** {len(summary.split())} words")

        # Download Button
        st.download_button(
            label="Download Summary",
            data=edited_summary,
            file_name="summary.txt",
            mime="text/plain"
        )

# Footer
st.markdown("<br><hr><center>Made by Ananya</center>", unsafe_allow_html=True)
