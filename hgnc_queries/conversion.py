from .api import get_api_response, URL


def convert_refseq2ensembl(refseq: str, verbose: bool = True):
    """ Convert refseq number to ensembl gene id

    Args:
        refseq (str): Refseq accession number
        verbose (bool, optional): Print output. Defaults to True.

    Returns:
        None
        ensembl_id (str)
    """

    refseq = refseq.strip().upper()

    if not refseq.startswith("NM"):
        print("Refseq given: {} doesn't start with \"NM\"".format(refseq))
        return

    ext = "fetch/refseq_accession/{}".format(refseq)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if not res:
        if verbose:
            print("Refseq \"{}\" not found".format(refseq))

        return
    else:
        ensembl_id = res[0]["ensembl_gene_id"]

        if verbose:
            print("Refseq \"{}\" -> Ensembl \"{}\"".format(refseq, ensembl_id))

        return ensembl_id


def convert_ensembl2refseq(ensembl_id: str, verbose: bool = True):
    """ Convert Ensembl id to refseq number

    Args:
        ensembl_id (str): Ensembl id
        verbose (bool, optional): Prints the output. Defaults to True.

    Returns:
        None
        refseq (str)
    """

    ensembl_id = ensembl_id.strip().upper()

    if not ensembl_id.startswith("ENSG"):
        print("Ensembl_id given: {} doesn't start with \"NM\"".format(
            ensembl_id
        ))
        return

    ext = "fetch/ensembl_gene_id/{}".format(ensembl_id)
    data = get_api_response("{}/{}".format(URL, ext))
    res = data["response"]["docs"]

    if not res:
        if verbose:
            print("Ensembl_id \"{}\" not found".format(ensembl_id))

        return
    else:
        refseq = res[0]["refseq_accession"]

        if verbose:
            print("Ensembl_id \"{}\" -> Refseq \"{}\"".format(
                ensembl_id,
                refseq
            ))

        return refseq
