<p align="center">
  <img src=assets/RateliaLogo.png" alt="Ratelia Labs logo" width="260">
</p>
___

# Solo-AI - Ratelia Labs
# Copyright © 2025 Gilles C. Obellianne
# License: Apache 2.0

# 🧠 Solo-AI Lite  
**Frugal Compute · Deterministic Agents · Adaptive Intelligence**  
**Ratelia Labs — by Gilles C. Obellianne**

![Ratelia Labs Logo](assets/RateliaLogo.png)

---

## 🌍 Présentation

**Solo-AI Lite** est la version publique, minimaliste et ouverte du framework **Solo-AI** développé par **Ratelia Labs**.

Cette version *Lite* n’expose **aucun code stratégique**, mais présente :

- l’architecture générale du système,
- le pipeline conceptuel complet,
- la structure des modules,
- la philosophie fondatrice du projet,
- un exemple simple de fonctionnement frugal & déterministe.

Elle sert de **preuve d’antériorité**, de base d’exploration pour chercheurs et ingénieurs, et de porte d’entrée vers le projet complet Solo-AI (privé).

---

## 🎯 Objectifs

- Montrer qu’un pipeline IA **complet** (données → décision → rapport humain) peut être réalisé de façon :
  - frugale (sans GPU massif),
  - déterministe (traçable, reproductible),
  - modulaire (chaque brique est isolée et testable).

- Offrir un **squelette de framework** que d’autres puissent étudier, forker, étendre.

Le pipeline schématique est :

```text
Ingest → Metrics → Patterns → Scores → Risk Daemon → Insight


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
└── LICENSE # Licence APACHE 2.0

---

# 🧬 Pipeline Solo-AI Lite

Voici comment fonctionne un run complet :

### 1️⃣ **Ingest (mock)**
Module: ingest/ingest_sample.py  
Rôle :
* Simuler un flux de données OHLCV (ex.: BTCUSDT, 1h),
* Écrire un fichier JSON simple dans data/raw/sample_ohlcv.json.

Sortie (exemple) :

###{
     "symbol": "BTCUSDT",
     "timeframe": "1h",
     "data": [
       [1700000000, 35000, 35100, 34900, 35050, 123.45],
       [1700003600, 35050, 35200, 35000, 35120, 150.12]
    ]
###}

### 2️⃣ **Metrics/**
Module : metrics/metrics_sample.py
Rôle :
Calculer quelques métriques globales simplifiées :

* volatilité,
* retour moyen,
* nombre de bougies haussières / baissières.
Sortie (exemple) :
  
Calcul de métriques simplifiées (volatilité, retours, bull/bear…).

###{
     "volatility": 0.0123,
     "mean_return": 0.00042,
     "bullish_candles": 55,
     "bearish_candles": 45
###}

### 3️⃣ **Patterns**  
Détection factice (FVG, MA, RSI simplifiés).
Module : patterns/pattern_sample.py
Rôle :
Fournir un exemple de structure de détection de patterns :

* gaps de prix (FVG),
* croisements de moyennes mobiles (MA),
* signaux RSI.
Sortie (exemple) :

###{
  "FVG_total": 12,
  "MA_cross_total": 3,
  "RSI_signals": 5
###}

### 4️⃣ **Score Engine**
Module : scores/score_engine_sample.py  
Rôle:
* Combiner les métriques et les patterns pour produire une valeur synthétique de sentiment (démonstration).
* Dans Solo-AI Lite, ce sentiment est volontairement statique (ex.: 0.1), simplement pour illustrer le flux de données.
Sortie (exemple) :

###{
   "pattern_scores": {
      "FVG_total": 12,
      "MA_cross_total": 3,
      "RSI_signals": 5
   },
   "market_scores": {
      "volatility": 0.0123,
      "mean_return": 0.00042,
      "bullish_candles": 55,
      "bearish_candles": 45
   },
   "sentiment": 0.1
###}





### 5️⃣ **Risk Daemon**  
Module : runtime/risk_daemon_sample.py
Rôle :
* Produit une décision minimale : BUY / HOLD / SELL mais comment ?
* Lire le sentiment et le transformer en une décision minimaliste :
Règles dans la version Lite :
sentiment > 0.2 → BUY
sentiment < -0.2 → SELL
sinon → HOLD
La décision est loguée dans logs/risk_daemon_lite.log.
Exemple de ligne de log :

2025-01-01 12:00:00.000000 | sentiment=0.1 | action=HOLD




### 6️⃣ **Insight**  
Création d’un rapport Markdown simple.
Module : insight/insight_sample.py
Rôle :
* Générer un rapport Markdown minimal dans data/insights/sample_report.md,
* Montrer comment, dans la version complète, Solo-AI produit des analyses lisibles par un humain.

Exécution de toutes les étapes orchestré par la commande 'python soloai_run_lite.py' :


           +------------------------+
           |    ingest_sample.py    |
           |   (mock OHLCV data)    |
           +-----------+------------+
                       |
                       v
             +---------+----------+
             | metrics_sample.py  |
             |  (basic metrics)   |
             +---------+----------+
                       |
                       v
             +---------+----------+
             | pattern_sample.py  |
             |  (patterns mock)   |
             +---------+----------+
                       |
                       v
             +---------+----------+
             | score_engine_...   |
             |   (sentiment)      |
             +---------+----------+
                       |
                       v
             +---------+----------+
             | risk_daemon_...    |
             | (BUY/HOLD/SELL)    |
             +---------+----------+
                       |
                       v
             +---------+----------+
             | insight_sample.py  |
             | (Markdown report)  |
             +--------------------+

Exemple d'utilisation:

Cloner le dépôt suivant:
git clone https://github.com/ratelialabs/solo-ai-lite.git
cd solo-ai-lite

Lancer le pipeline Lite:
python soloai_run_lite.py

Sortie typique:

=== Running: ingest/ingest_sample.py ===
Sample ingest OK -> data/raw/sample_ohlcv.json

=== Running: metrics/metrics_sample.py ===
Sample metrics OK -> data/metrics/sample_metrics.json

=== Running: patterns/pattern_sample.py ===
Sample patterns OK -> data/patterns/sample_patterns.json

=== Running: scores/score_engine_sample.py ===
Sample score engine OK -> data/scores/sample_scores.json

=== Running: runtime/risk_daemon_sample.py ===
Risk Daemon Lite OK -> action: HOLD

=== Running: insight/insight_sample.py ===
Sample insight OK -> data/insights/sample_report.md

Solo-AI Lite pipeline complete.




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

Mais dont voici la roadmap détaillée mais partielle:

🔭 Roadmap (pour le projet complet Solo-AI)
Cette roadmap concerne le projet complet Solo-AI (privé), dont Solo-AI Lite n’est qu’une vitrine structurante. 

Phase 1 — Stable Core (V1)
* Pipeline complet BTCUSDT 1h (réalisé, version privée)
* Calculs de métriques avancées (volatilité, regimes de marché)
* Détection de patterns (FVG, MA, RSI, etc.)
* Risk Engine V1 (profil de risque adaptatif)
* Risk Daemon V1 (BUY/HOLD/SELL + logs append-only)

Phase 2 — Stress Tests & Backtests
* Stress tests intensifs (multi-runs)
* Backtests de stratégies basées sur les signaux Solo-AI
* Reporting de performance (P&L simulé)

Phase 3 — Aion Node & IA locale
* Intégration d’un nœud d’analyse IA (LLM local, frugal)
* Lecture et interprétation des logs
* Ajustement des paramètres de risque (boucle adaptative)
* Expérimentation d’un agent inspiré du comportement d’un chat (module ratelia_core, privé)

Phase 4 — Front-end & Observabilité
* CLI avancée ou mini-dashboard
* Visualisation des signaux et de l’historique
* Observabilité (metrics system + logs structurés)

🧭 Philosophie Ratelia Labs
* Ratelia Labs explore des IA :
* frugales (exécutables sur une machine personnelle),
* déterministes (comportement reproductible),
* bio-inspirées (modèles d’agents dérivés du vivant plutôt que des méga-modèles “magiques”).

Solo-AI est un terrain d’expérimentation pour :
* des boucles de décision adaptative,
* des agents autonomes minimalistes,
* des architectures de trading transparentes et auditables.

L’architecture de Solo-AI, initialement conçue pour l’analyse de marchés financiers et la
gestion du risque, est volontairement générique. Le schéma de boucle adaptative 
(ingestion → scoring → décision → retour d’expérience) pourra être étendu à d’autr
domaines où la surveillance continue et l’ajustement automatique sont critiques, notamment 
la cybersécurité, la surveillance médicale, la maintenance prédictive et la supervision de 
systèmes industriels.

En voici quelques exemples plus détaillés:

Extensions possibles du cadre Solo-AI
Solo-AI n’est pas limité au trading. La boucle adaptative qui le structure (ingestion de 
signaux, extraction de métriques, détection de patterns, scoring, décision, retour 
d’expérience) est applicable à tout environnement où il faut :

* observer un système en continu,
* qualifier son état,
* décider d’actions correctives ou préventives,
* apprendre de l’impact de ces actions.

À ce titre, Ratelia Labs se réserve le droit d’étendre le cadre Solo-AI à d’autres 
domaines stratégiques, notamment :

* Cybersécurité adaptative
	Surveillance de logs réseau / systèmes, détection de comportements anormaux, 
	ajustement dynamique des règles de filtrage, des niveaux d’alerte ou des 
	politiques de pare-feu.

* Surveillance médicale et télémédecine
	Analyse de séries temporelles (rythme cardiaque, SpO₂, tension, glycémie), 
	détection de dérives, génération de signaux d’alerte ou de recommandations, 
	adaptation des seuils en fonction du profil patient.

* Maintenance prédictive (industrie / transports)
	Exploitation de capteurs (vibrations, températures, courants moteurs), 
	détection de patterns avant-panne, ajustement des plans de maintenance, 
	priorisation des interventions.

* Supervision de systèmes industriels et IoT
	Pilotage de flottes de dispositifs (capteurs, micro-contrôleurs, passerelles), 
	remontée d’anomalies, adaptation des politiques de mise à jour, 
	gestion d’énergie et de charge.

* Gestion énergétique et smart grids
	Analyse de consommation, prévision de charges, détection de pics anormaux, 
	adaptation des consignes (stockage, délestage, bascule de sources).

* Logistique et supply chain
	Suivi de flux de marchandises, détection de goulets d’étranglement, ajustement 
	dynamique des priorités d’expédition, réallocation de stocks.

* Détection de fraude et conformité
	Analyse de transactions (finance, e-commerce, assurances), détection de profils 
	atypiques, ajustement des niveaux de vérification et des scores de risque.

* Pilotage de systèmes autonomes légers
	Intégration dans de petits agents logiciels (bots, micro-services, nœuds edge) 
	capables de prendre des décisions locales avec retour d’expérience.

Dans tous ces cas, ce n’est pas le domaine qui change, mais uniquement :
	- la nature des données ingérées,
	- les métriques calculées,
	- les patterns surveillés,
	- la politique de décision.

Le cœur de la boucle adaptative Solo-AI (architecture, enchaînement, logique de 
retour d’expérience) reste, lui, générique et réutilisable.


---


🛡 Licene

Copyright 2025 Gilles C. Obellianne — Ratelia Labs

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0


Ratelia Labs — Nov 2025
Created by Gilles C. Obellianne

“Small machine. Serious brain.”
