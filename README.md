# AI Content Plagiarism & Authenticity Dispute Contract

An Intelligent Contract primitive built on **GenLayer** that provides decentralized, LLM-powered resolution for text plagiarism and content authenticity disputes.

## 💡 Overview
Traditional smart contracts cannot evaluate text semantic similarity or detect plagiarism natively. This contract leverages GenLayer's non-deterministic execution framework (`gl.exec_prompt`) to allow validator nodes to collaboratively agree on content overlap, similarity scoring, and final verdicts via AI consensus.

## ⚙️ How It Works
1. **Dispute Creation:** Users submit two text blocks (Original Content vs. Suspect Content).
2. **Validator Consensus:** GenLayer validators execute an LLM prompt assessing semantic overlap, structural paraphrasing, and direct plagiarism.
3. **Equivalence & Resolution:** Nodes reach consensus on the calculated similarity score. If similarity >= 60%, the contract marks the content as plagiarized.
