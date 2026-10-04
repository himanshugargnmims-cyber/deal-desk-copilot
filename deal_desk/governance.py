"""
Commercial Deal Desk Governance & Approval Engine
"""

from typing import Dict, List, Any, Optional


class DealDeskGovernance:
    """
    Evaluates enterprise B2B SaaS deal pricing structures against
    corporate discount authority matrices and governance rules.
    """

    APPROVAL_TIERS = [
        {"max_discount": 10.0, "level": "Level 0: Auto-Approved", "signoff": "Account Executive Discretion"},
        {"max_discount": 20.0, "level": "Level 1: Management Review", "signoff": "Regional Sales VP"},
        {"max_discount": 30.0, "level": "Level 2: RevOps Signoff", "signoff": "VP of Sales + Head of RevOps"},
        {"max_discount": 100.0, "level": "Level 3: Executive Escalation", "signoff": "Chief Revenue Officer (CRO) + CFO"}
    ]

    def __init__(self, target_gross_margin_pct: float = 80.0):
        self.target_gross_margin = float(target_gross_margin_pct)

    def evaluate_deal(
        self,
        list_price_annual: float,
        discount_pct: float,
        contract_years: int = 1,
        payment_terms: str = "Annual Upfront",
        has_non_standard_legal_clauses: bool = False
    ) -> Dict[str, Any]:
        """Evaluates pricing proposal and returns governance decision."""
        discount_pct = max(0.0, min(100.0, float(discount_pct)))
        annual_discount = list_price_annual * (discount_pct / 100.0)
        net_acv = list_price_annual - annual_discount
        tcv = net_acv * contract_years

        effective_margin = self.target_gross_margin * (1.0 - (discount_pct / 100.0))

        # Determine approval requirement
        required_tier = self.APPROVAL_TIERS[-1]
        for tier in self.APPROVAL_TIERS:
            if discount_pct <= tier["max_discount"]:
                required_tier = tier
                break

        escalations = []
        if discount_pct > 15.0:
            escalations.append(f"Discount rate ({discount_pct:.1f}%) exceeds standard 15% ceiling.")
        if payment_terms in ["Quarterly", "Monthly"]:
            escalations.append(f"Non-annual billing terms ({payment_terms}) reduce operating cash velocity.")
        if has_non_standard_legal_clauses:
            escalations.append("Non-standard contractual clauses detected (requires Legal signoff).")

        status = "Approved" if len(escalations) == 0 else "Requires Review"

        return {
            "list_price_annual": round(list_price_annual, 2),
            "discount_pct": round(discount_pct, 2),
            "net_acv": round(net_acv, 2),
            "contract_years": contract_years,
            "tcv": round(tcv, 2),
            "total_discount_tcv": round(annual_discount * contract_years, 2),
            "payment_terms": payment_terms,
            "effective_margin_pct": round(effective_margin, 2),
            "approval_level": required_tier["level"],
            "designated_approver": required_tier["signoff"],
            "status": status,
            "escalations": escalations
        }
