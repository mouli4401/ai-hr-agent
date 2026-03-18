import os
import re
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END

# Load env
load_dotenv()

# ----------------------------
# ✅ State definition
# ----------------------------
class AgentState(TypedDict):
    messages: Annotated[list, "conversation"]
    resume: str
    jd: str
    score: int
    decision: str


# ----------------------------
# ✅ LLM setup
# ----------------------------
llm = ChatGroq(
    model=os.getenv("MODEL_NAME", "llama-3.3-70b-versatile"),
    temperature=float(os.getenv("TEMPERATURE", 0)),
    groq_api_key=os.getenv("GROQ_API_KEY")
)


# ----------------------------
# ✅ Node 1: Extract Resume
# ----------------------------
def extract_resume(state: AgentState):
    return {
        "resume": state["resume"],
        "messages": state["messages"]
    }


# ----------------------------
# ✅ Node 2: Match JD (FIXED)
# ----------------------------
def match_jd(state: AgentState):
    prompt = f"""
You are an ATS system.

Rules:
- Return ONLY ONE integer between 0 and 100
- Do NOT return multiple numbers
- Do NOT explain

Resume:
{state['resume']}

Job Description:
{state['jd']}
"""

    response = llm.invoke([HumanMessage(content=prompt)])
    text = response.content.strip()

    # ✅ FIX: Extract only first valid number (0–100)
    match = re.search(r"\b(100|[1-9]?[0-9])\b", text)

    if match:
        score = int(match.group(0))
    else:
        score = 50  # fallback

    return {
        "score": score,
        "messages": state["messages"] + [response]
    }


# ----------------------------
# ✅ Node 3: Decision
# ----------------------------
def decision_node(state: AgentState):
    score = state["score"]

    decision = "SHORTLISTED" if score >= 70 else "REJECTED"

    explanation_prompt = f"""
Candidate Score: {score}

Explain in 3-4 lines why the candidate is {decision}.
"""

    explanation = llm.invoke([HumanMessage(content=explanation_prompt)])

    return {
        "decision": decision,
        "messages": state["messages"] + [
            AIMessage(content=f"{decision}\n\n{explanation.content}")
        ]
    }


# ----------------------------
# ✅ Build LangGraph App
# ----------------------------
def build_app():
    graph = StateGraph(AgentState)

    graph.add_node("extract", extract_resume)
    graph.add_node("match", match_jd)
    graph.add_node("decision", decision_node)

    graph.set_entry_point("extract")

    graph.add_edge("extract", "match")
    graph.add_edge("match", "decision")
    graph.add_edge("decision", END)

    return graph.compile()


# ----------------------------
# ✅ Run (for testing)
# ----------------------------
if __name__ == "__main__":
    app = build_app()

    jd = "Looking for Python developer with Flask, APIs, and ML basics"
    resume = "I have experience in Python, Flask, and building APIs."

    result = app.invoke({
        "messages": [HumanMessage(content=resume)],
        "resume": resume,
        "jd": jd,
        "score": 0,
        "decision": ""
    })

    print("\n===== RESULT =====")
    print("Score:", result["score"])
    print(result["messages"][-1].content)