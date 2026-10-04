"""
Competitor Battlecard Generator & Discovery Trap Questions
"""

from typing import Dict, Any


class BattlecardEngine:
    """Generates structured battlecards and objection handling playbooks."""

    CARDS = {
        "legacy_enterprise": {
            "name": "Legacy Enterprise Incumbent",
            "vulnerabilities": "High professional services cost, 9-18 month implementation times, rigid schemas.",
            "trap_questions": [
                "What is your annual maintenance budget for dedicated consultants?",
                "How long does it take for your team to adjust a custom workflow?"
            ],
            "differentiator": "Rapid 3-week time-to-value, zero consultant lock-in, automated cloud sync."
        },
        "low_cost_point_tool": {
            "name": "Low-Cost Point Tool",
            "vulnerabilities": "Fragmented data silos, lacks enterprise RBAC and SOC2 compliance, no dedicated CS.",
            "trap_questions": [
                "How do you consolidate attribution reporting when data is locked in point tools?",
                "Does their security posture satisfy your Infosec audit standards?"
            ],
            "differentiator": "Unified GTM architecture, end-to-end telemetry, enterprise governance."
        }
    }

    @classmethod
    def get_card(cls, key: str) -> Dict[str, Any]:
        return cls.CARDS.get(key, {
            "name": key.title(),
            "vulnerabilities": "Slow product release cycles, higher total cost of ownership.",
            "trap_questions": ["What is your SLA for unresolved technical escalations?"],
            "differentiator": "Modern cloud-native agility and dedicated customer success."
        })
