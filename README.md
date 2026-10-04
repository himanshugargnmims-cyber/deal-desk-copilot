# ⚖️ Deal Desk Copilot

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/himanshugargnmims-cyber/deal-desk-copilot)
[![Follow on GitHub](https://img.shields.io/github/followers/himanshugargnmims-cyber?label=Follow&style=social)](https://github.com/himanshugargnmims-cyber)

**Commercial Deal Desk Governance, Discount Approval Workflows, Contract Terms Risk Scoring & Competitor Battlecards.**

</div>

---

## 🚀 Features

- **Multi-Tier Discount Approval Matrix**:
  - `0% - 10%`: Rep Discretion
  - `10.1% - 20%`: Regional Sales VP
  - `20.1% - 30%`: VP of Sales + Head of RevOps
  - `>30%`: Chief Revenue Officer (CRO) + CFO
- **Non-Standard Terms Detection**: Flags payment term anomalies (Quarterly/Monthly vs Annual Upfront) and liability exceptions.
- **Competitor Battlecard Generator**: Automatic discovery trap questions and differentiation wedges.

---

## 💻 Quick Start

### 1. Installation
```bash
git clone https://github.com/himanshugargnmims-cyber/deal-desk-copilot.git
cd deal-desk-copilot
pip install -r requirements.txt
```

### 2. CLI Usage
```bash
python deal_desk/cli.py --list-price 150000 --discount 22 --years 2 --battlecard legacy_enterprise
```

### 3. Python SDK
```python
from deal_desk import DealDeskGovernance, BattlecardEngine

gov = DealDeskGovernance(target_gross_margin_pct=80.0)
deal = gov.evaluate_deal(list_price_annual=150000.0, discount_pct=22.0, contract_years=2)
print("Approval Level:", deal["approval_level"])
print("Approver:", deal["designated_approver"])
```

## 📄 License
MIT License. See [`LICENSE`](LICENSE).
