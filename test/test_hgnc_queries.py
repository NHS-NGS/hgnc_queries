import pytest
import sys

from hgnc_queries import queries


def test_get_new_symbol_no_res():
    assert(
        queries.get_new_symbol("BRCA1P", False) is None
    )


def test_get_new_symbol_one_res():
    assert(
        queries.get_new_symbol("RN5S49", False) == "RNA5SP49"
    )


###########################################################################


def test_get_gene_starting_with_no_res():
    assert(
        queries.get_gene_starting_with("AIFJAEIGJI", False) is None
    )


def test_get_gene_starting_with_single_res():
    truth = ["BRCA1P1"]
    assert(
        queries.get_gene_starting_with("BRCA1P", False) == truth
    )


def test_get_gene_starting_with_multiple_res():
    truth_list = ["BRCA1", "BRCA1P1", "BRCA2", "BRCA3"]
    assert(
        queries.get_gene_starting_with("BRCA", False) == truth_list
    )


###########################################################################


def test_get_alias_no_alias():
    assert(
        queries.get_alias("CARD9", False) is None
    )


def test_get_alias_one_alias():
    truth = ["DA9"]
    assert(
        queries.get_alias("FBN2", False) == truth
    )


def test_get_alias_multiple_aliases():
    truth = ["KIAA1235", "ELD/OSA1", "p250R", "BAF250b", "DAN15", "6A3-5"]
    assert(
        queries.get_alias("ARID1B", False) == truth
    )


###########################################################################


def test_get_main_symbol_no_res():
    assert(
        queries.get_main_symbol("CARD9", False) is None
    )


def test_get_main_symbol_res():
    truth = "BRAF"
    assert(
        queries.get_main_symbol("BRAF1", False) == truth
    )


###########################################################################


def test_get_prev_symbol_no_res():
    assert(
        queries.get_prev_symbol("No exist", False) is None
    )


def test_get_prev_symbol_one_res():
    truth = ["CCA"]
    assert(
        queries.get_prev_symbol("FBN2", False) == truth
    )


def test_get_prev_symbol_multiple_res():
    truth = ["SEDC", "AOM"]
    assert(
        queries.get_prev_symbol("COL2A1", False) == truth
    )


###########################################################################


def test_get_id_no_res():
    assert(
        queries.get_id("No exist", False) is None
    )


def test_get_id_one_res():
    truth = "HGNC:1097"
    assert(
        queries.get_id("BRAF", False) == truth
    )


###########################################################################


def test_get_symbol_from_id_not_ID():
    assert(
        queries.get_symbol_from_id("No exist", False) is None
    )


def test_get_symbol_from_id_no_res():
    assert(
        queries.get_symbol_from_id("54974894564156", False) is None
    )


def test_get_symbol_from_id_one_res():
    truth = "BRAF"
    assert(
        queries.get_symbol_from_id("1097", False) == truth
    )


###########################################################################


def test_get_hgnc_symbol_none():
    assert(
        queries.get_hgnc_symbol("BRCA") is None
    )


def test_get_hgnc_symbol_use_new():
    assert(
        queries.get_hgnc_symbol("RN5S49") == "RNA5SP49"
    )


def test_get_hgnc_symbol_use_main():
    assert(
        queries.get_hgnc_symbol("BRAF1") == "BRAF"
    )
