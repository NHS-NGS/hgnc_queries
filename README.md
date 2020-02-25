# hgnc_queries.py 

Query HGNC for gene symbols.  
Created to attempt to rescue old gene symbols because of an old excel "database" that had to be converted in a Django database

## Installation

```
pip install hgnc_queries
```

## Examples:

Use HGNC queries to get:
```
>> import hgnc_queries
>> hgnc_queries.get_new_symbol("RN5S49", verbose = False)
RNA5SP49

>> hgnc_queries.get_gene_starting_with("BRCA", verbose = False)
["BRCA1", "BRCA1P1", "BRCA2", "BRCA3"]

>> hgnc_queries.get_alias("ARID1B", verbose = False)
["KIAA1235", "ELD/OSA1", "p250R", "BAF250b", "DAN15", "6A3-5"]

>> hgnc_queries.get_main_symbol(BRAF1)
BRAF

>> hgnc_queries.get_prev_symbol("COL2A1")
["SEDC", "AOM"]

>> hgnc_queries.get_id("BRAF")
HGNC:1097

>>hgnc_queries.get_symbol_from_id("1097")
BRAF
```