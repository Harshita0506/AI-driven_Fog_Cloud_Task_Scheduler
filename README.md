# AI-Driven Fog–Cloud Task Scheduler (Explainable ML)

An **AI-based task scheduling system** that uses a **Neural Network (MLP)** to decide whether an IoT task should be executed on **Fog** or **Cloud**, with **Explainable AI (XAI)** support using **LLMs**.

---

## 🚀 Key Features
- ML-driven Fog vs Cloud scheduling  
- Neural Network (MLPClassifier) for decision making  
- Feasibility checking using deadline & load constraints  
- Min-Heap based node allocation  
- Explainable AI using **LLM** (with rule-based fallback)  
- Performance visualization (acceptance, rejection, priority)

---

## 🧠 Technologies Used
- Python  
- Machine Learning (Neural Networks)  
- Explainable AI (LLM + rule-based explanations)  
- Scikit-learn  
- Matplotlib  

---

## ⚙️ How It Works
1. Tasks are generated with CPU, data size, deadline, and priority  
2. Neural Network predicts **Fog or Cloud**  
3. Feasibility is checked based on system load & deadline  
4. Tasks are accepted/rejected and assigned to least-loaded node  
5. LLM generates **human-readable explanation** for each decision  

---

## 📊 Sample Results
- Balanced Fog–Cloud task distribution  
- Clear acceptance vs rejection analysis  
- Priority-wise scheduling insights  

---

