import pytest
from src.parcel_fee import delivery_fee

@pytest.mark.parametrize(
    "weight_grams, expected_fee",
    [
        (1, 500),  # lowest weight allowed (band 1 lower boundary)
        (500, 500),  # middle of band 1
        (1000, 500),  # band 1 upper boundary
        (1001, 1000),  # band 2 lower boundary
        (10000, 1000),  # middle of band 2
        (20000, 1000),  # highest weight allowed (band 2 upper boundary)
    ],
)
def test_delivery_fee_valid_weight_returns_expected_fee(weight_grams, expected_fee):
    # Act
    result = delivery_fee(weight_grams)
    # Assert
    assert result == expected_fee and type(result) is int


# Correct type but outside 1 to 20000 -> ValueError
@pytest.mark.parametrize(
    "weight_grams",
    [
        0,  # just below the lowest weight
        -1,  # negative weight
        20001,  # just above the highest weight
    ],
)
def test_delivery_fee_out_of_range_weight_raises_value_error(weight_grams):
    with pytest.raises(ValueError):
        delivery_fee(weight_grams)


# Wrong data type -> TypeError (bool is not a valid int)
@pytest.mark.parametrize(
    "weight_grams",
    [
        "500",  # string
        500.0,  # float
        None,  # None
        True,  # bool is not accepted as an integer
    ],
)
def test_delivery_fee_invalid_type_raises_type_error(weight_grams):
    with pytest.raises(TypeError):
        delivery_fee(weight_grams)
