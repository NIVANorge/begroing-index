from begroing_index.indicator_values import (
    iv_files,
    load_indicator_values,
    calc_min_iv,
    calc_max_iv,
)


def test_indicator_values_csv_file_format_check():
    for index_name, iv_file in iv_files.items():
        iv_values = load_indicator_values(index_name)
        for specie, val in iv_values.items():
            assert isinstance(val, float)
            assert len(specie) > 1

        min_iv = calc_min_iv(iv_values, min_species_count=3)
        assert min_iv > 0

        max_iv = calc_max_iv(iv_values, min_species_count=2)
        assert max_iv > 0
