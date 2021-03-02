from typing import Dict

import pytest

from niva_index.exceptions import UncertainIndexException
from niva_index.begroing.pit import calc_pit, calc_pit_eqr
from niva_index.indicator_values import load_indicator_values, calc_max_iv


@pytest.fixture(scope="module")
def indicator_values() -> Dict[str, float]:
    return load_indicator_values("PIT")


def test_pit(indicator_values):
    max_iv = calc_max_iv(indicator_values, min_species_count=2)
    assert max_iv > 0
    assert isinstance(max_iv, float)

    """
    Zygnema b (22-25u);4.76
    Rivularia spp.;4.99
    Zygnema c (30-40u);5.07
    Schizothrix lacustris;4.35
    """
    observed = [4.76, 4.99, 5.07, 4.35]
    print(observed)
    pit_value = calc_pit(indicator_values=observed)
    assert pit_value == 4.7925


def test_pit_eqr():
    pit_eqr = calc_pit_eqr(pit_value=4.7925, max_pit=60.84, calc_consentration=0.5)
    assert pit_eqr == 1.0010269691016251

    # calc values above 1 uses different reference value
    pit_eqr = calc_pit_eqr(pit_value=4.7925, max_pit=60.84, calc_consentration=1.0)
    assert pit_eqr == 1.0354239793090707


def test_pit_should_error_if_too_few_values():
    with pytest.raises(UncertainIndexException):
        calc_pit([3.23])
        calc_pit([])


def test_pit_case1(indicator_values):
    """
    Test of case described in veileder attachment page 71

    Not all species described in the case use the exact same latin name (sp vs spp)
    """
    observed_species = [
        # "Batrachospermum sp.",
        "Batrachospermum spp.",
        "Binuclearia tectorum",
        "Bulbochaete spp.",
        "Cosmarium spp.",
        "Klebsormidium rivulare",
        "Microspora palustris",
        "Microspora palustris var. minor",
        "Mougeotia a (6 -12μ)",
        "Mougeotia a/b (10-18μ)",
        "Scytonematopsis starmachii",
        "Zygogonium spp.",
    ]

    observed_ivs = [indicator_values[s] for s in observed_species]
    assert len(observed_ivs) == 11
    pit = calc_pit(observed_ivs)
    assert pit == 4.632727272727273


def test_pit_case2(indicator_values):

    observed_species = [
        "Leptolyngbya spp.",
        "Sphaerotilus natans",
        "Vaucheria spp.",
        "Audouinella chalybea",
    ]

    observed_ivs = [indicator_values[s] for s in observed_species]
    pit = calc_pit(observed_ivs)
    assert pit == 30.42
