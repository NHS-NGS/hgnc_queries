import pytest

from hgnc_queries.conversion import (
    convert_ensembl2refseq, convert_refseq2ensembl
)
from hgnc_queries.queries import (
    get_new_symbol, get_gene_starting_with, get_alias,
    get_main_symbol, get_prev_symbol, get_id,
    get_symbol_from_id, get_hgnc_symbol,
    get_ensembl, get_refseq
)


def test_get_new_symbol_no_res():
    assert(
        get_new_symbol("BRCA1P", False) is None
    )


def test_get_new_symbol_one_res():
    assert(
        get_new_symbol("RN5S49", False) == "RNA5SP49"
    )


###########################################################################


def test_get_gene_starting_with_no_res():
    assert(
        get_gene_starting_with("AIFJAEIGJI", False) is None
    )


def test_get_gene_starting_with_single_res():
    truth = ["BRCA1P1"]
    assert(
        get_gene_starting_with("BRCA1P", False) == truth
    )


def test_get_gene_starting_with_multiple_res():
    truth_list = ["BRCA1", "BRCA1P1", "BRCA2", "BRCA3"]
    assert(
        get_gene_starting_with("BRCA", False) == truth_list
    )


###########################################################################


def test_get_alias_no_alias():
    assert(
        get_alias("CARD9", False) is None
    )


def test_get_alias_one_alias():
    truth = ["DA9"]
    assert(
        get_alias("FBN2", False) == truth
    )


def test_get_alias_multiple_aliases():
    truth = ["KIAA1235", "ELD/OSA1", "p250R", "BAF250b", "DAN15", "6A3-5"]
    assert(
        get_alias("ARID1B", False) == truth
    )


###########################################################################


def test_get_main_symbol_no_res():
    assert(
        get_main_symbol("CARD9", False) is None
    )


def test_get_main_symbol_res():
    truth = "BRAF"
    assert(
        get_main_symbol("BRAF1", False) == truth
    )


###########################################################################


def test_get_prev_symbol_no_res():
    assert(
        get_prev_symbol("No exist", False) is None
    )


def test_get_prev_symbol_one_res():
    truth = ["CCA"]
    assert(
        get_prev_symbol("FBN2", False) == truth
    )


def test_get_prev_symbol_multiple_res():
    truth = ["SEDC", "AOM"]
    assert(
        get_prev_symbol("COL2A1", False) == truth
    )


###########################################################################


def test_get_id_no_res():
    assert(
        get_id("No exist", False) is None
    )


def test_get_id_one_res():
    truth = "HGNC:1097"
    assert(
        get_id("BRAF", False) == truth
    )


###########################################################################


def test_get_symbol_from_id_not_ID():
    assert(
        get_symbol_from_id("No exist", False) is None
    )


def test_get_symbol_from_id_no_res():
    assert(
        get_symbol_from_id("54974894564156", False) is None
    )


def test_get_symbol_from_id_one_res():
    truth = "BRAF"
    assert(
        get_symbol_from_id("1097", False) == truth
    )


###########################################################################


def test_get_hgnc_symbol_none():
    assert(
        get_hgnc_symbol("BRCA") is None
    )


def test_get_hgnc_symbol_use_new():
    assert(
        get_hgnc_symbol("RN5S49") == "RNA5SP49"
    )


def test_get_hgnc_symbol_use_main():
    assert(
        get_hgnc_symbol("BRAF1") == "BRAF"
    )


###########################################################################


def test_convert_refseq2ensembl_wrong_id():
    assert(
        convert_refseq2ensembl("Not_ENSG") is None
    )


def test_convert_refseq2ensembl_no_res():
    assert(
        convert_refseq2ensembl("ENSG09184875872") is None
    )


def test_convert_refseq2ensembl_res():
    assert(
        convert_refseq2ensembl("NM_007294", False) == "ENSG00000012048"
    )


###########################################################################


def test_convert_ensembl2refseq_wrong_id():
    assert(
        convert_ensembl2refseq("Not_NM") is None
    )


def test_convert_ensembl2refseq_no_res():
    assert(
        convert_ensembl2refseq("NM_9189483857") is None
    )


def test_convert_ensembl2refseq_res():
    assert(
        convert_ensembl2refseq("ENSG00000012048") == ['NM_007294']
    )


###########################################################################


def test_get_refseq_wrong_id():
    assert(
        get_refseq("thingy") is None
    )


def test_get_refseq_res():
    assert(
        get_refseq("BRCA1") == ['NM_007294']
    )


###########################################################################


def test_get_ensembl_wrong_id():
    assert(
        get_ensembl("thingy") is None
    )


def test_get_ensembl_res():
    assert(
        get_ensembl("BRCA1") == "ENSG00000012048"
    )
