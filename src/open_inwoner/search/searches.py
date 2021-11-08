from .documents import ProductDocument


def search_products(value: str):
    s = ProductDocument.search()
    s = s.query("multi_match", query=value, fields=["name^4", "summary", "content"])
    result = s.execute()

    return result.hits
