
import pytest

from customs_duty import clearance_channel, duty_rate, total_duty


@pytest.mark.parametrize(
    ("category", "origin", "expected"),
    [
        ("electronics", "FTA", 0.10),
        ("electronics", "US", 0.20),
        ("clothing", "FTA", 0.05),
        ("clothing", "US", 0.12),
        ("books", "US", 0),
        ("furniture", "US", 0.15),
    ],
)
def test_duty_rate_categories(category, origin, expected):
    assert duty_rate(category, origin) == expected


@pytest.mark.parametrize("category", ["weapons", "narcotics"])
def test_prohibited_duty_rate(category):
    with pytest.raises(ValueError, match="prohibited item"):
        duty_rate(category, "US")


def test_negative_value():
    with pytest.raises(ValueError, match="negative value"):
        total_duty("electronics", -1, "US", False)


def test_low_value_personal_import():
    assert total_duty("books", 500, "US", False) == 0


def test_gift_below_threshold():
    assert total_duty("electronics", 5000, "US", True) == 0


def test_gift_above_threshold():
    assert total_duty("electronics", 6000, "FTA", True) == 100


def test_minimum_duty():
    assert total_duty("electronics", 1100, "FTA", False) == 110.0
    
def test_normal_duty():
    assert total_duty("electronics", 2000, "FTA", False) == 200


@pytest.mark.parametrize("category", ["weapons", "narcotics"])
def test_prohibited_clearance(category):
    assert clearance_channel(500, category, True) == "refuse"


def test_high_value_clearance():
    assert clearance_channel(100001, "books", True) == "inspect"


def test_missing_documents_clearance():
    assert clearance_channel(25000, "books", False) == "inspect"


def test_documents_present_clearance():
    assert clearance_channel(25000, "books", True) == "green"


def test_value_at_inspection_threshold():
    assert clearance_channel(20000, "books", False) == "green"


def test_low_value_clearance():
    assert clearance_channel(1000, "books", False) == "green"
