import pytest
import sys

sys.path.append("../bin/")

import hgnc_queries



def test_get_new_symbol_no_res():
    assert(
        hgnc_queries.get_new_symbol("BRCA1P", False) == None
    )


def test_get_new_symbol_one_res():
    assert(
        hgnc_queries.get_new_symbol("RN5S49", False) == "RNA5SP49"
    )

###########################################################################

def test_get_gene_starting_with_no_res():
    assert(
        hgnc_queries.get_gene_starting_with("AIFJAEIGJI", False) == None
    )


def test_get_gene_starting_with_single_res():
    truth = ["BRCA1P1"]
    assert(
        hgnc_queries.get_gene_starting_with("BRCA1P", False) == truth
    )

def test_get_gene_starting_with_multiple_res():
    truth_list = ["BRCA1", "BRCA1P1", "BRCA2", "BRCA3"]
    assert(
        hgnc_queries.get_gene_starting_with("BRCA", False) == truth_list
    )

###########################################################################

def test_get_alias_of_main_symbol_one_alias():
    truth = ["DA9"]
    assert(
        hgnc_queries.get_alias_of_main_symbol("FBN2", False) == truth
    )
    

def test_get_alias_of_main_symbol_multiple_aliases():
    truth = ["KIAA1235", "ELD/OSA1", "p250R", "BAF250b", "DAN15", "6A3-5"]
    assert(
        hgnc_queries.get_alias_of_main_symbol("ARID1B", False) == truth
    )

###########################################################################

def test_get_main_symbol_of_alias_no_res():
    assert(
        hgnc_queries.get_main_symbol_of_alias("CARD9", False) == None
    )


def test_get_main_symbol_of_alias_res():
    truth = "BRAF"
    assert(
        hgnc_queries.get_main_symbol_of_alias("BRAF1", False) == truth
    )

###########################################################################

def test_get_prev_symbol_no_res():
    assert(
        hgnc_queries.get_prev_symbol("ARID1B", False) == None
    )


def test_get_prev_symbol_one_res():
    truth = ["CCA"]
    assert(
        hgnc_queries.get_prev_symbol("FBN2", False) == truth
    )


def test_get_prev_symbol_multiple_res():
    truth = ["SEDC", "AOM"]
    assert(
        hgnc_queries.get_prev_symbol("COL2A1", False) == truth
    )

###########################################################################

def test_get_id_no_res():
    assert(
        hgnc_queries.get_id("No exist", False) == None
    )


def test_get_id_one_res():
    truth = "HGNC:1097"
    assert(
        hgnc_queries.get_id("BRAF", False) == truth
    )

###########################################################################

def test_get_symbol_from_id_no_res():
    assert(
        hgnc_queries.get_symbol_from_id("No exist", False) == None
    )    

def test_get_symbol_from_id_one_res():
    truth = "BRAF"
    assert(
        hgnc_queries.get_symbol_from_id("1097", False) == truth
    )