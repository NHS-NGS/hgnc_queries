from .api import get_api_response, URL


def get_new_symbol(gene_symbol: str, verbose: bool = True):
    """ get the new symbol of a gene

    Args:
    - gene_symbol: str
    - verbose: bool

    Returns:
    - str
    - None
    """

    gene_symbol = gene_symbol.strip().upper()

    ext = "search/prev_symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if res == []:
        if verbose:
            print("No new symbol found for {}".format(gene_symbol))
        return

    elif len(res) > 1:
        if verbose:
            print("2 or more different genes share this symbol {}:".format(
                gene_symbol
            ))

            for gene in res:
                print(gene)

        return
    else:
        if verbose:
            print("New symbol found for {}: {}".format(
                gene_symbol,
                res[0]["symbol"]
            ))
        return res[0]["symbol"]


def get_gene_starting_with(gene_symbol: str, verbose: bool = True):
    """ get the genes that start with the symbol given

    Args:
    - gene_symbol: str
    - verbose: bool

    Returns:
    - list of str
    - None
    """

    gene_symbol = gene_symbol.strip().upper()

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
                print(symbol)

        return gene_symbols


def get_alias(gene_symbol: str, verbose: bool = True):
    """ get aliases of given symbol

    Args:
    - gene_symbol: str
    - verbose: bool

    Returns:
    - list of str
    - None
    """

    gene_symbol = gene_symbol.strip().upper()

    ext = "fetch/symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if len(res) == 1:
        if "alias_symbol" in res[0]:
            aliases = res[0]["alias_symbol"]

            if verbose:
                if isinstance(aliases, list):
                    display_aliases = ", ".join(aliases)
                else:
                    display_aliases = aliases

                print("Alias symbols for {}: {}".format(
                    gene_symbol,
                    display_aliases
                ))

            return aliases

        else:
            if verbose:
                print("No aliases for {}".format(gene_symbol))

            return
    else:
        if verbose:
            print("Couldn't get alias for {}".format(gene_symbol))

        return


def get_main_symbol(gene_symbol: str, verbose: bool = True):
    """ get the main symbol of given symbol

    Returns None if symbol is already the "main" symbol

    Args:
    - gene_symbol: str
    - verbose: bool

    Returns:
    - list of str
    - None
    """

    gene_symbol = gene_symbol.strip().upper()

    ext = "search/alias_symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if len(res) == 1:
        if "symbol" in res[0]:
            main_symbol = res[0]["symbol"]

            if verbose:
                print("Main symbol for {}: {}".format(
                    gene_symbol,
                    main_symbol
                ))

            return main_symbol
        else:
            if verbose:
                print("No main_symbol for {}".format(gene_symbol))

            return
    else:
        return


def get_prev_symbol(gene_symbol: str, verbose: bool = True):
    """ get the previous symbol of a gene

    Args:
    - gene_symbol: str
    - verbose: bool

    Returns:
    - list of str
    - None
    """

    gene_symbol = gene_symbol.strip().upper()

    ext = "fetch/symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if len(res) == 1:
        if "prev_symbol" in res[0]:
            prev_symbol = res[0]["prev_symbol"]

            if verbose:
                print("Previous symbols for {}: {}".format(
                    gene_symbol,
                    ", ".join(prev_symbol)
                ))

            return prev_symbol
        else:
            if verbose:
                print("No previous symbol for {}".format(gene_symbol))

            return
    else:
        if verbose:
            print("Couldn't get prev symbols for {}".format(gene_symbol))

        return


def get_id(gene_symbol: str, verbose: bool = True):
    """ get the id of gene symbol

    Args:
    - gene_symbol: str
    - verbose: bool

    Returns:
    - str
    - None
    """

    gene_symbol = gene_symbol.strip().upper()

    ext = "fetch/symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if len(res) == 1:
        gene_id = res[0]["hgnc_id"]

        if verbose:
            print("{}\t{}".format(gene_symbol, gene_id))

        return gene_id
    else:
        for data in res:
            if data["symbol"] == gene_symbol:
                return data["hgnc_id"]

        if verbose:
            print("Couldn't get the id for {}".format(gene_symbol))

    return


def get_symbol_from_id(gene_id: str, verbose: bool = True):
    """ get the gene symbol from a gene id

    Args:
    - gene_id: str
    - verbose: bool

    Returns:
    - str
    - None
    """

    if not gene_id[0].isdigit():
        if verbose:
            print("{} doesn't start with a digit".format(gene_id))

        return

    gene_id = gene_id.strip()

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
            print("Got no symbol for {}".format(gene_id))

        return


def get_hgnc_symbol(gene_symbol: str):
    """ get the official hgnc symbol from a gene symbol

    Args:
    - gene_id: str
    - verbose: bool

    Returns:
    - str
    - None
    """

    gene_symbol = gene_symbol.strip()

    new_symbol = get_new_symbol(gene_symbol, False)

    if new_symbol:
        return new_symbol
    else:
        main_symbol = get_main_symbol(gene_symbol, False)

        if main_symbol:
            return main_symbol
        else:
            return


def get_refseq(gene_symbol: str, verbose: bool = True):
    """ Get refseq given a gene symbol

    Args:
        gene_symbol (str): Gene symbol
        verbose (bool, optional): Prints the output. Defaults to True.

    Returns:
        None
        refseq (str)
    """

    gene_symbol = gene_symbol.strip().upper()

    ext = "fetch/symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if not res:
        if verbose:
            print("Gene \"{}\" not found".format(gene_symbol))

        return
    else:
        refseq = res[0]["refseq_accession"]

        if verbose:
            print("Refseq for \"{}\": {}".format(gene_symbol, refseq))

        return refseq


def get_ensembl(gene_symbol: str, verbose: bool = True):
    """ Get the ensembl id for given gene symbol

    Args:
        gene_symbol (str): Gene symbol
        verbose (bool, optional): Prints the output. Defaults to True.

    Returns:
        None
        ensembl_id (str)
    """

    gene_symbol = gene_symbol.strip().upper()

    ext = "fetch/symbol/{}".format(gene_symbol)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if not res:
        if verbose:
            print("Gene \"{}\" not found".format(gene_symbol))

        return
    else:
        ensembl_id = res[0]["ensembl_gene_id"]

        if verbose:
            print("Ensembl_id for \"{}\": {}".format(gene_symbol, ensembl_id))

        return ensembl_id
