""" HGNC.py

Fetch data from HGNC api
"""

import argparse
import requests
import sys
import json

URL = "http://rest.genenames.org"


def get_api_response(full_url):
    """ send request to HGNC and get json response """

    try:
        response = requests.get(full_url, headers = {"Accept": "application/json"})
    except Exception as e:
        print("Something wrong: {}".format(e))
        sys.exit(-1)
    else:
        data = json.loads(response.content.decode("utf-8"))

    return data


def get_new_symbol(gene_symbol, verbose = True):
    """ get the new symbol of a gene """

    ext = "search/prev_symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if res == []:
        if verbose:
            print("No new symbol found for {}".format(gene_symbol))
        return

    elif len(res) > 1:
        if verbose:
            print("2 or more different genes share this symbol {}:".format(gene_symbol))
        
        for gene in res:
            if verbose:
                print(gene)

        return
    else:
        if verbose:
            print("New symbol found for {}: {}".format(gene_symbol, res[0]["symbol"]))
        return res[0]["symbol"]


def get_gene_starting_with(gene_symbol, verbose = True):
    """ get the genes that start with the symbol given """

    ext = "search/symbol/{}*".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if res == []:
        if verbose:
            print("No gene found starting with {}".format(gene_symbol))
        return
    
    else:
        gene_symbols = [res[i]["symbol"] for i in range(len(res))]
        
        if verbose:
            print("Found these genes starting with {}:".format(gene_symbol))
        
        for symbol in gene_symbols:
            if verbose:
                print(symbol)

        return gene_symbols


def get_alias(gene_symbol, verbose = True):
    """ get the aliases of a gene """

    ext = "fetch/symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if len(res) == 1:
        if "alias_symbol" in res[0]:
            aliases = res[0]["alias_symbol"]
    
            if verbose:
                print("Alias symbols for {}: {}".format(gene_symbol, ", ".join(aliases)))
    
            return aliases
        else:
            if verbose:
                print("No aliases for {}".format(gene_symbol))
            return 
    else:
        if verbose:
            print("Couldn't get alias for {}".format(gene_symbol))
        return


def get_prev_symbol(gene_symbol, verbose = True):
    """ get the previous symbol of a gene """

    ext = "fetch/symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if len(res) == 1:
        if "prev_symbol" in res[0]:
            prev_symbol = res[0]["prev_symbol"]
            if verbose:
                print("Previous symbols for {}: {}".format(gene_symbol, ", ".join(prev_symbol)))
    
            return prev_symbol
        else:
            if verbose:
                print("No previous symbol for {}".format(gene_symbol))

            return 
    else:
        if verbose:
            print("Couldn't get prev symbols for {}".format(gene_symbol))

        return 


def get_id(gene_symbol, verbose = True):
    """ get the id of gene symbol """

    ext = "search/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if len(res) == 1:
        gene_id = res[0]["hgnc_id"]
        
        if verbose:
            print("{}\t{}".format(gene_symbol, gene_id))
    
        return gene_id
    else:
        if verbose:
            print("Couldn't get the id for {}".format(gene_symbol))
            
        return 


def get_symbol_from_id(gene_id, verbose = True):
    """ get the gene symbol from a gene id """

    ext = "search/hgnc_id/{}".format(gene_id)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if len(res) == 1:
        gene_symbol = res[0]["symbol"]

        if verbose:
            print("{}\t{}".format(gene_id, gene_symbol))

        return gene_symbol
    elif len(res) == 0:
        if verbose:
            print("Got not symbol for {}".format(gene_id))

        return


def main(path):
    pass


if __name__ == "__main__":
    # get_new_symbol("KAL1")
    parser = argparse.ArgumentParser(description = "HGNC api interface (kinda)")
    subparsers = parser.add_subparsers(help = "Commands")

    new_symbol = subparsers.add_parser("new_symbol", help = "Get the new symbol")
    new_symbol.add_argument("gene_symbol", help = "Gene symbol")
    new_symbol.set_defaults(func = get_new_symbol)

    alias = subparsers.add_parser("alias", help = "Get the aliases")
    alias.add_argument("gene_symbol", help = "Gene symbol")
    alias.set_defaults(func = get_alias)

    prev_symbol = subparsers.add_parser("prev_symbol", help = "Get the previous symbol")
    prev_symbol.add_argument("gene_symbol", help = "Gene symbol")
    prev_symbol.set_defaults(func = get_prev_symbol)    

    gene_symbol = subparsers.add_parser("gene", help = "Get the gene symbols starting with")
    gene_symbol.add_argument("gene_symbol", help = "Gene symbol")
    gene_symbol.set_defaults(func = get_gene_starting_with)

    gene_id = subparsers.add_parser("id", help = "Get the ID from a gene symbol")
    gene_id.add_argument("gene_symbol", help = "Gene symbol")
    gene_id.set_defaults(func = get_id)

    id2symbol = subparsers.add_parser("id2symbol", help = "Get the gene symbol from the id")
    id2symbol.add_argument("gene_id", help = "Gene ID")
    id2symbol.set_defaults(func = get_symbol_from_id)

    args = parser.parse_args()
    
    if hasattr(args, "gene_symbol"):
        gene_symbol = args.gene_symbol
        args.func(gene_symbol)

    elif hasattr(args, "gene_id"):
        gene_id = args.gene_id
        args.func(gene_id)
