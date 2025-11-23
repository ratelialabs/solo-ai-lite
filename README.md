# 🧠 Solo-AI Lite  
### Frugal Compute · Deterministic Agents · Adaptive Intelligence  
**Ratelia Labs — by Gilles C. Obellianne**

---

## 🌍 Présentation

**Solo-AI Lite** est la version publique, minimaliste et ouverte du framework **Solo-AI** développé par **Ratelia Labs**.

Cette version *Lite* n’expose **aucun code stratégique**, mais présente :

- l’architecture générale du système,
- le pipeline conceptuel complet,
- la structure des modules,
- la philosophie à l’origine du projet,
- un exemple de fonctionnement frugal & déterministe.

Elle sert de **preuve d’antériorité**, de base d’exploration pour chercheurs et ingénieurs, et de porte d’entrée vers le projet complet Solo-AI (privé).

---

# 🎯 Objectifs

### ⭐ Démontrer un pipeline IA minimaliste mais cohérent  
Solo-AI Lite fournit un pipeline complet, simplifié :

Ingest ---> Metrics ---> Patterns ---> Scores ---> Risk Daemon ---> Insight


Chaque module est un *mock* ou une *démo* autonome.

---

## 📁 Architecture Solo-AI Lite

solo-ai-lite/
│
├── ingest/ # Démonstration d’ingestion de données
│ └── ingest_sample.py
│
├── metrics/ # Exemple de calcul de métriques
│ └── metrics_sample.py
│
├── patterns/ # Démonstration de détection de patterns
│ └── pattern_sample.py
│
├── scores/ # Exemple de score engine
│ └── score_engine_sample.py
│
├── runtime/ # Démonstration du Risk Daemon
│ └── risk_daemon_sample.py
│
├── insight/ # Génération d’un rapport humain simple
│ └── insight_sample.py
│
├── soloai_run_lite.py # Pipeline Lite complet
│
├── README.md # Ce document
└── LICENSE # Licence Open-Source (MIT)


---

# 🧬 Pipeline Solo-AI Lite

Voici comment fonctionne un run complet :

### 1️⃣ **Ingest (mock)**  
Simule un flux OHLCV BTCUSDT (exemple statique).

### 2️⃣ **Metrics**  
Calcul de métriques simplifiées (volatilité, retours, bull/bear…).

### 3️⃣ **Patterns**  
Détection factice (FVG, MA, RSI simplifiés).

### 4️⃣ **Score Engine**  
Combine metrics + patterns → sentiment fixe (démonstration).

### 5️⃣ **Risk Daemon**  
Produit une décision minimale : BUY / HOLD / SELL.

### 6️⃣ **Insight**  
Création d’un rapport Markdown simple.

### 7️⃣ **Console Pipeline**  
Exécution de toutes les étapes via `soloai_run_lite.py`.

---

# 🔥 Philosophie de Solo-AI  

### Frugal Compute — Deterministic Core — Adaptive Intelligence

Solo-AI repose sur trois principes fondamentaux :

### **1. Frugalité**
Le système doit fonctionner sur une machine personnelle
(Mac Mini, Laptop) sans GPU massif.

### **2. Déterminisme**
Chaque étape produit une sortie stable, traçable, reproductible.

### **3. Intelligence Adaptative**
Solo-AI complet (version privée) utilise :
- un sentiment très pondéré,
- des agents autonomes (risk daemon),
- un moteur adaptatif inspiré du comportement animal (V2).

---

# 🧭 Vision Ratelia Labs

Ratelia Labs explore des IA **bio-inspirées**,  
non pas par les grands modèles de langage,  
mais par les **mécanismes fondamentaux du vivant** :

- mémoire structurée,  
- signaux faibles,  
- boucle sensorielle → décision,  
- adaptation progressive,  
- frugalité énergétique.

Les futures versions de Solo-AI (V2, V3…) intégreront un module expérimental :  
🧬 **ratelia_core** — un agent minimal inspiré du comportement d’un chat.  
*(Version privée, non incluse ici.)*

---

# ▶️ Utilisation (Solo-AI Lite)

Dans le terminal :

```bash
python soloai_run_lite.py

Sortie attendue :
génération de données mock
metrics mock
patterns mock
score mock
décision BUY/HOLD/SELL
insight minimal

🛡 Licenc

Solo-AI Lite est publié sous licence MIT.
Le code peut être réutilisé librement à des fins non commerciales ou d’expérimentation.
La version complète Solo-AI (pipeline réel, risk engine, Aion Node, ratelia_core)
reste propriété exclusive de Ratelia Labs — Gilles C. Obellianne.


Ratelia Labs — Nov 2025
Created by Gilles C. Obellianne
“Small machine. Serious brain.”
