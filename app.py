import streamlit as st
from agent import build_app
from utils import read_pdf
from langchain_core.messages import HumanMessage

# Build graph
app = build_app()

st.set_page_config(page_title="AI HR Dashboard", layout="wide")

st.title("🤖 AI HR Resume Screening Dashboard")

# Sidebar
st.sidebar.header("⚙️ Settings")
threshold = st.sidebar.slider("Shortlist Threshold", 50, 100, 70)

# Main layout
col1, col2 = st.columns(2)

# Upload Resume
with col1:
    st.subheader("📄 Upload Resume (PDF)")
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

    resume_text = ""
    if uploaded_file:
        resume_text = read_pdf(uploaded_file)
        st.success("Resume uploaded successfully!")

# Job Description
with col2:
    st.subheader("📝 Job Description")
    jd = st.text_area("Enter JD", height=200)

# Run Button
if st.button("🚀 Evaluate Candidate"):
    if not resume_text or not jd:
        st.warning("Please upload resume and enter JD")
    else:
        with st.spinner("Analyzing..."):
            result = app.invoke({
                "messages": [HumanMessage(content=resume_text)],
                "resume": resume_text,
                "jd": jd,
                "score": 0,
                "decision": ""
            })

        output = result["messages"][-1].content
        score = result["score"]

        st.divider()

        # Results
        st.subheader("📊 Evaluation Result")

        col3, col4 = st.columns(2)

        with col3:
            st.metric("Match Score", f"{score}%")

        with col4:
            decision = "SHORTLISTED" if score >= threshold else "REJECTED"
            st.metric("Decision", decision)

        st.subheader("💬 AI Explanation")
        st.write(output)