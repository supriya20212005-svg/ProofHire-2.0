from app.services.scoring import ScoringEngine
def test_skill_score():
    e=ScoringEngine(); score,matched,missing=e.skill_score(['Java','Redis'],['Java','Kafka'])
    assert score==50.0 and 'java' in matched and 'kafka' in missing
def test_overall_score():
    e=ScoringEngine(); assert e.overall(80,70,90,75,85,80,70)>75
