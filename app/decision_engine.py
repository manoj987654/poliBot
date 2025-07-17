# app/decision_engine.py

def make_decision(parsed_query, relevant_clauses):
    age = parsed_query.get("age", 0)
    duration = parsed_query.get("policy_duration_months", 0)
    procedure = parsed_query.get("procedure", "").lower()

    # Dummy logic — replace with actual clause logic
    if "knee" in procedure and age < 60 and duration >= 3:
        return {
            "Decision": "Approved",
            "Amount": "₹50,000",
            "Justification": "Knee surgery covered after 3 months for under-60"
        }
    else:
        return {
            "Decision": "Rejected",
            "Amount": "₹0",
            "Justification": "Policy does not cover this scenario based on current clause"
        }
