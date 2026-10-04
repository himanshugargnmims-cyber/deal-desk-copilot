from deal_desk.governance import DealDeskGovernance
from deal_desk.battlecards import BattlecardEngine


def test_deal_governance_evaluation():
    gov = DealDeskGovernance()
    res = gov.evaluate_deal(list_price_annual=100000.0, discount_pct=15.0, contract_years=2)
    assert res["net_acv"] == 85000.0
    assert res["tcv"] == 170000.0
    assert "Level 1" in res["approval_level"]


def test_battlecard_retrieval():
    card = BattlecardEngine.get_card("legacy_enterprise")
    assert "name" in card
    assert len(card["trap_questions"]) > 0
