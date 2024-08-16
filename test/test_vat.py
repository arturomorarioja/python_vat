import pytest

from app.vat import calculate_vat

# Positive testing
@pytest.mark.parametrize(
    'vat_passes, expected_result', 
    [
        (10000, 12500),
        (20000, 25000),
        (14000.78, 17500.98),
        (0, 0),
        (-10000, 0)
    ]
)
def test_vat_passes(vat_passes, expected_result):
    assert calculate_vat(vat_passes) == expected_result

# Negative testing: TypeError exceptions
@pytest.mark.parametrize(
    'vat_fails',
    [
        'A',
        (0, 3),
        [4, 5]
    ]
)
def test_vat_exception(vat_fails):
    with pytest.raises(TypeError):
        calculate_vat(vat_fails)