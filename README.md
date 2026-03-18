# 🤖 AI HR Resume Screening System (Agentic AI)

An **Agentic AI-powered HR Assistant** built using **LangGraph + Groq (LLaMA 3)** that automates resume screening, skill matching, and candidate evaluation with an interactive dashboard.

---

## 🚀 Demo

<img width="1919" height="957" alt="image" src="https://github.com/user-attachments/assets/68356f37-fbd4-4248-b622-6fd08c1205ac" />

<img width="1485" height="479" alt="image" src="https://github.com/user-attachments/assets/de732784-61a1-4292-ab2d-bacb9bbd4f75" />



* Dashboard UI
* Resume Upload
* Skill Matching Chart

---

## 🧠 Features

✅ Upload Resume (PDF)
✅ Job Description Matching
✅ Skill Extraction Engine
✅ AI-Based Candidate Scoring
✅ Decision: Shortlist / Reject
✅ Explanation using LLM
✅ Interactive Dashboard (Streamlit)
✅ Skill Match Visualization 📊

---

## ⚙️ Tech Stack

* 🧠 LangGraph (Agent Workflow)
* 🔗 LangChain
* ⚡ Groq API (LLaMA 3 Model)
* 🐍 Python
* 📊 Streamlit Dashboard
* 📄 PyPDF (Resume Parsing)
* 📈 Matplotlib (Charts)

---

## 🧩 Architecture

User Input → Resume Parser → Skill Extractor → LLM Scorer → Decision Engine → Dashboard Output

---

## 📁 Project Structure

```
hr-agent-dashboard/
│── app.py          # Streamlit UI
│── agent.py        # LangGraph workflow
│── skills.py       # Skill extraction logic
│── utils.py        # PDF reader
│── .env            # API keys (ignored)
│── requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile
TEMPERATURE=0
```

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-hr-agent.git
cd ai-hr-agent

pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📊 Output Example

* Match Score: **78%**
* Decision: **SHORTLISTED**
* Skills Matched: Python, Flask, APIs
* Chart: Skill Match Visualization
* AI Explanation included

---

## 🔥 Key Highlights

* ⚡ Uses **Groq LLaMA 3 (fast inference)**
* 🧠 Built with **LangGraph Agentic Workflow**
* 📊 Combines **LLM + Rule-Based Skill Matching**
* 💼 Real-world **ATS (Applicant Tracking System) simulation**

---

## 🚀 Future Improvements

* 📄 Multiple Resume Ranking
* 🧠 Multi-Agent System (Parser + Evaluator + Interviewer)
* 🗂 Database Integration (MongoDB)
* 📧 Email Automation for shortlisted candidates
* 🌐 Full Stack (React + FastAPI)

---

## 🏆 Use Case

This project simulates a **real HR screening system**, helping recruiters:

* Filter candidates faster
* Reduce manual effort
* Improve hiring efficiency

---

## 👨‍💻 Author

**Mouli**
Final Year Student | AI & Full Stack Enthusiast

---

## ⭐ Support

If you like this project:

* ⭐ Star this repo
* 🍴 Fork it
* 📢 Share with others

---

## 📜 License

This project is open-source and available under the MIT License.
