

import pytest
from hypothesis import given, strategies as st

from customs_duty import (
    parse_declaration,
    duty_amount,
    hs_chapter,
    main,
)


# 1. Property-based test for parse_declaration
@given(
    category=st.text(min_size=1),
    value=st.floats(
        allow_nan=False,
        allow_infinity=False,
    ),
)
def test_parse_declaration_no_crash(category, value):
    result = parse_declaration(f"{category}:{value}")
    assert result == (category.strip().lower(), value)


# 2. Property-based test for duty_amount
@given(
    value=st.floats(
        allow_nan=False,
        allow_infinity=False,
    ),
    rate=st.floats(
        allow_nan=False,
        allow_infinity=False,
    ),
)
def test_duty_amount_no_crash(value, rate):
    result = duty_amount(f"{value}@{rate}")
    assert result == value * rate / 100


# 3. Property-based test for hs_chapter
@given(
    chapter=st.integers(min_value=10, max_value=99)
)
def test_hs_chapter_no_crash(chapter):
    result = hs_chapter(f"{chapter}17.12")
    assert result == chapter


# 4. Normal input tests
def test_parse_declaration_valid():
    assert parse_declaration("Electronics:25000") == (
        "electronics",
        25000.0,
    )


def test_duty_amount_valid():
    assert duty_amount("25000@20") == 5000.0


def test_hs_chapter_valid():
    assert hs_chapter("8517.12") == 85


# 5. Invalid input tests
def test_parse_declaration_invalid():
    with pytest.raises(ValueError):
        parse_declaration("electronics")


def test_duty_amount_invalid():
    with pytest.raises(ValueError):
        duty_amount("invalid")


def test_hs_chapter_invalid():
    with pytest.raises(ValueError):
        hs_chapter("invalid")


# 6. Test the main function
def test_main(monkeypatch, capsys):
    inputs = iter([
        "electronics:25000",
        "25000@20",
        "8517.12",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main()

    output = capsys.readouterr().out

    assert "electronics" in output
    assert "5000.0" in output
    assert "85" in output
