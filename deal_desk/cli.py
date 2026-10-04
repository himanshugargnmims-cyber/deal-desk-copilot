#!/usr/bin/env python3
"""
CLI entry point for Deal Desk Copilot
"""

import argparse
from deal_desk.governance import DealDeskGovernance
from deal_desk.battlecards import BattlecardEngine


def main():
    parser = argparse.ArgumentParser(description="Deal Desk Copilot — Commercial Pricing Governance Engine")
    parser.add_argument("--list-price", type=float, default=120000.0, help="Annual List Price")
    parser.add_argument("--discount", type=float, default=18.0, help="Discount Percentage (0-100)")
    parser.add_argument("--years", type=int, default=2, help="Contract Term in Years")
    parser.add_argument("--terms", type=str, default="Annual Upfront", help="Payment terms")
    parser.add_argument("--battlecard", type=str, default=None, help="Competitor key (legacy_enterprise / low_cost_point_tool)")

    args = parser.parse_args()

    gov = DealDeskGovernance()
    res = gov.evaluate_deal(
        list_price_annual=args.list_price,
        discount_pct=args.discount,
        contract_years=args.years,
        payment_terms=args.terms
    )

    print("\n" + "=" * 72)
    print("                 COMMERCIAL DEAL DESK GOVERNANCE MEMO")
    print("=" * 72)
    print(f"  Annual List Price:         ${res['list_price_annual']:>12,.2f}")
    print(f"  Discount Rate:              {res['discount_pct']:>11.1f}%")
    print(f"  Net ACV (Annual ARR):      ${res['net_acv']:>12,.2f}")
    print(f"  Total Contract Value (TCV):${res['tcv']:>12,.2f} ({res['contract_years']} yrs)")
    print(f"  Payment Terms:              {res['payment_terms']}")
    print(f"  Effective Gross Margin:     {res['effective_margin_pct']:>11.1f}%")
    print("-" * 72)
    print(f"  DECISION STATUS:           {res['status'].upper()}")
    print(f"  Approval Level:            {res['approval_level']}")
    print(f"  Required Approver:         {res['designated_approver']}")
    if res['escalations']:
        print("  Escalation Triggers:")
        for t in res['escalations']:
            print(f"    ⚠️  {t}")
    print("=" * 72 + "\n")

    if args.battlecard:
        card = BattlecardEngine.get_card(args.battlecard)
        print("=" * 72)
        print(f"  COMPETITOR BATTLECARD: {card['name'].upper()}")
        print("=" * 72)
        print(f"  Vulnerabilities: {card['vulnerabilities']}")
        print(f"  Differentiator:  {card['differentiator']}")
        print("  Discovery Trap Questions:")
        for q in card['trap_questions']:
            print(f"    🎯 {q}")
        print("=" * 72 + "\n")


if __name__ == "__main__":
    main()
