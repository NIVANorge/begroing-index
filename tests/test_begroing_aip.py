from typing import Dict

import pytest

from begroing_index.begroing.aip import calc_aip, calc_aip_eqr
from begroing_index.indicator_values import load_indicator_values, calc_min_iv


@pytest.fixture(scope="module")
def indicator_values() -> Dict[str, float]:
    return load_indicator_values("AIP")


def test_aip_case1(indicator_values):
    """

    Example case given in veileder attachments page 75

    Yndesdalsvassdraget i Hordaland og Sogn og Fjordane har blitt kalket siden 1991.
    Kalsium konsentrasjonen i elvene ovenfor kalkingsanlegget er < 1 mg Ca/l og er dermed svært kalkfattige.
    I kalkede vassdrag er det viktig å måle Ca-konsentrasjonen oppstrøms kalkingen for å finne ut hva den naturlige
    Cakonsentrasjonen i vassdraget er. Det er den naturlige Cakonsentrasjonen som er avgjørende for å bestemme
    elvetype.

    I Yndesdalsvassdraget ble det tatt begroingsprøver i Botnanebekken sommeren 2010. Det ble funnet 12 algetaksa,
    deriblant 8 som har AIP indikatorverdi i tabell
    1 (Binuclearia tectorum, Bulbochaete sp., Klebsormidium rivulare, Microspora palustris,
    Microspora palustris var minor, Mougeotia a/b, Scytonematopsis starmachii, Zygogonium sp3).

    AIP indeksen ble beregnet til 5,72.

    Botnanebekken har en Ca-konsentrasjon som er lavere enn 1 mg/l, og en gjennomsnittlig TOC-konsentrasjon som er
    høyere enn 2 mg/l. Vi må derfor bruke den venstre kolonnen i tabell 2. En indeksverdi på 5,72 betyr dermed at
    stasjonen er i moderat tilstand med hensyn til forsuring, men at den ligger tett opptil grensen mellom god og
    moderat tilstand (som ligger på AIP = 5,75 for denne elvetypen; se veilederens tabell V5.2).
    """

    observed = [
        "Binuclearia tectorum",
        "Bulbochaete spp.",
        "Klebsormidium rivulare",
        "Microspora palustris",
        "Microspora palustris var minor",
        "Mougeotia a/b (10-18μ)",
        "Scytonematopsis starmachii",
        "Zygogonium sp3 (16-20μ)",
    ]

    ivs = [indicator_values[s] for s in observed]
    min_aip = calc_min_iv(indicator_values=indicator_values, min_species_count=3)

    aip = calc_aip(ivs)
    assert aip == 5.7162500000000005

    aip_eqr = calc_aip_eqr(aip=aip, min_aip=min_aip, calc=0.5, toc=2.1)
    assert aip_eqr == 0.6426470588235303
