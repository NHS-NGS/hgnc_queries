# hgnc_queries.py 

Query HGNC for gene symbols.  
Created to attempt to rescue old gene symbols because of an old excel "database" that had to be converted in a Django database

Use HGNC api to get:
- New symbol --> `python hgnc_queries.py new_symbol $gene`
- Alias of given gene --> `python hgnc_queries.py alias $gene`
- Main symbol of given gene (for an alias) --> `python hgnc_queries.py main_symbol $gene`
- Previous symbol --> `python hgnc_queries.py prev_symbol $gene`
- Gene starting with --> `python hgnc_queries.py gene $gene`
- HGNC id --> `python hgnc_queries.py id $gene`
- Symbol from id --> `python hgnc_queries.py id2symbol $gene_id`
