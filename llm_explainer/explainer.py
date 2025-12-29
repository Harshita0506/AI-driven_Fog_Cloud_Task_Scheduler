import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -------------------------------------------------
# RULE-BASED FALLBACK (YOUR EXACT RULE STYLE)
# -------------------------------------------------
def rule_based_explanation(task, decision, feasible):
    cpu = task["cpu_cycles"]
    deadline = task["deadline"]
    fog_load = task["fog_load"]
    cloud_load = task["cloud_load"]

    # Rejected task rules
    if not feasible:
        if deadline <= 3:
            return "Deadline is too tight to be satisfied under current load."
        elif fog_load > 0.8 and cloud_load > 0.8:
            return "Both fog and cloud resources are heavily loaded."
        else:
            return "Deadline or resource constraints were violated."

    # Accepted task rules
    if cpu > 700:
        return "High computational demand influenced the scheduling decision."
    elif deadline <= 6:
        return "Low deadline urgency influenced execution closer to the edge."
    elif cloud_load < fog_load:
        return "Lower load influenced the resource selection."
    else:
        return "Balanced workload and timing constraints influenced the decision."


# -------------------------------------------------
# OPENAI-BASED EXPLANATION (PRIMARY)
# -------------------------------------------------
def llm_explanation(task, decision, feasible):
    env = "Fog" if decision == 0 else "Cloud"

    prompt = f"""
Give a ONE-LINE technical explanation for the scheduling outcome.

Rules:
- Do NOT contradict the decision.
- Do NOT suggest another environment.
- Be concise and factual.

Task details:
CPU cycles: {task['cpu_cycles']}
Data size: {task['data_size']}
Deadline: {task['deadline']}
Priority: {task['priority']}
Fog load: {task['fog_load']}
Cloud load: {task['cloud_load']}

Decision:
{"Rejected" if not feasible else f"Accepted and assigned to {env}"}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=40
    )

    text = response.choices[0].message.content.strip()

    # Safety check to prevent contradiction
    if feasible and env.lower() not in text.lower():
        raise ValueError("LLM explanation inconsistent with decision")

    return text


# -------------------------------------------------
# PUBLIC FUNCTION USED BY SCHEDULER
# -------------------------------------------------
def explain_task(task, decision, feasible):
    """
    Returns a one-line explanation.
    Uses OpenAI first, rule-based fallback if needed.
    """

    prefix = (
        "Rejected: "
        if not feasible
        else "Scheduled: "
    )

    try:
        explanation = llm_explanation(task, decision, feasible)
        return prefix + explanation
    except Exception:
        fallback = rule_based_explanation(task, decision, feasible)
        return prefix + fallback
