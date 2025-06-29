import pytest
from chatstream.summarize import RollingSummary


def test_rolling_summary_basic():
    rs = RollingSummary(window_size=5)
    messages = ["I love this", "Great work", "Not good", "Could be better"]
    for m in messages:
        rs.add(m)
    summary, sentiment, confidence = rs.compute()
    assert isinstance(summary, str)
    assert -1.0 <= sentiment <= 1.0
    assert 0.0 <= confidence <= 1.0
    assert summary
