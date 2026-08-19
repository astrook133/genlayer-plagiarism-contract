# GenLayer Intelligent Contract: AI Plagiarism & Dispute Resolution
from genlayer import *

@gl.contract
class PlagiarismDisputeContract:
    def __init__(self, admin: Address):
        self.admin = admin
        self.disputes_count = 0
        self.disputes = gl.mapping(int, dict)

    @gl.public
    def create_dispute(self, original_text: str, suspect_text: str) -> int:
        dispute_id = self.disputes_count
        self.disputes[dispute_id] = {
            "original_text": original_text,
            "suspect_text": suspect_text,
            "status": "PENDING",
            "similarity_score": 0,
            "verdict": "UNRESOLVED"
        }
        self.disputes_count += 1
        return dispute_id

    @gl.public
    def resolve_dispute(self, dispute_id: int) -> dict:
        assert dispute_id < self.disputes_count, "Invalid dispute ID"
        dispute = self.disputes[dispute_id]
        assert dispute["status"] == "PENDING", "Dispute already resolved"

        original = dispute["original_text"]
        suspect = dispute["suspect_text"]

        prompt = f"""
        You are an impartial academic and content integrity validator.
        Compare the following two texts for plagiarism or heavy paraphrasing:
        
        Original Text: "{original}"
        Suspect Text: "{suspect}"
        
        Respond ONLY with a JSON-formatted response:
        {{
            "similarity_score": <number between 0 and 100>,
            "is_plagiarized": <true if score >= 60 else false>,
            "reasoning": "<short explanation>"
        }}
        """

        result = gl.exec_prompt(prompt)
        
        score = result.get("similarity_score", 0)
        is_plagiarized = result.get("is_plagiarized", False)

        dispute["similarity_score"] = score
        dispute["verdict"] = "PLAGIARIZED" if is_plagiarized else "ORIGINAL"
        dispute["status"] = "RESOLVED"
        
        self.disputes[dispute_id] = dispute
        return dispute
