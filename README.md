# hgnc_queries.py 

Query HGNC for gene symbols.  
Created to attempt to rescue old gene symbols because of an old excel "database" that had to be converted in a Django database

## Installation

```
pip install hgnc_queries
```

## Examples:

Use HGNC api to get:
```
# Get new symbol
python hgnc_queries.py new_symbol $gene
# Get aliases of given symbol
python hgnc_queries.py alias $gene
# Get main symbol of alias
python hgnc_queries.py main_symbol $gene
# Get previous symbol
python hgnc_queries.py prev_symbol $gene
# Get genes starting with
python hgnc_queries.py gene $gene
# Get HGNC id of given symbol
python hgnc_queries.py id $gene
# Get symbol of given id
python hgnc_queries.py id2symbol $gene_id
```