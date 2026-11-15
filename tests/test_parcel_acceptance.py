import pytest
from src.parcel_acceptance import is_parcel_accepted

# Both limits met -> True
@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (1, 1),  # lowest weight and length
        (5000, 100),  # typical parcel
        (20000, 200),  # highest weight and length
        (20000, 1),  # highest weight, lowest length
        (1, 200),  # lowest weight, highest length
    ],
)
def test_is_parcel_accepted_within_limits_returns_true(weight_grams, length_cm):
    # Act
    result = is_parcel_accepted(weight_grams, length_cm)
    # Assert
    assert result is True


# Zero or above a limit -> False
@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (0, 100),  # zero weight
        (5000, 0),  # zero length
        (0, 0),  # both zero
        (20001, 100),  # weight just above limit
        (5000, 201),  # length just above limit
        (20001, 201),  # both above limits
    ],
)
def test_is_parcel_accepted_zero_or_over_limit_returns_false(weight_grams, length_cm):
    # Act
    result = is_parcel_accepted(weight_grams, length_cm)
    # Assert
    assert result is False


# Negative measurement -> ValueError
@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        (-1, 100),  # negative weight
        (5000, -1),  # negative length
        (-1, -1),  # both negative
    ],
)
def test_is_parcel_accepted_negative_measurement_raises_value_error(weight_grams, length_cm):
    with pytest.raises(ValueError):
        is_parcel_accepted(weight_grams, length_cm)


# Wrong data type -> TypeError
@pytest.mark.parametrize(
    "weight_grams, length_cm",
    [
        ("5000", 100),  # weight is a string
        (5000, "100"),  # length is a string
        (5000.0, 100),  # weight is a float
        (5000, 100.5),  # length is a float
        (None, 100),  # weight is None
        (True, 100),  # weight is a bool
        (5000, False),  # length is a bool
    ],
)
def test_is_parcel_accepted_invalid_type_raises_type_error(weight_grams, length_cm):
    with pytest.raises(TypeError):
        is_parcel_accepted(weight_grams, length_cm)
