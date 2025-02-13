from requests import get, post, put, delete, HTTPError


def test_api():
    """
    An automated version of the manual testing I've been doing,
    testing the lifecycle of an inserted document.
    """
    root = "http://localhost:8000/"
    exampleitem_root = f"{root}exampleitems/"


    new_exampleitem = {
        "title": "Lorem ipsum",
        "value": 100,
        "code": "LIPS01",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }

    try:
        response = get(root)
        response.raise_for_status()

        # # Insert a exampleitem
        response = post(exampleitem_root, json=new_exampleitem)
        response.raise_for_status()
        doc = response.json()
        print(doc)
        inserted_example_id = doc["id"]
        print(f"Inserted document with id: {inserted_example_id}")
        assert doc["title"] == "Lorem ipsum"
        assert doc["value"] == 100
        assert doc["code"] == "LIPS01"
        assert doc["description"] == "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

        # # List exampleitem and ensure it's present
        response = get(exampleitem_root)
        response.raise_for_status()
        examples = response.json()
        print(examples)
        example_ids = [s["id"] for s in examples.get('exampleitems')]
        assert inserted_example_id in example_ids


        # Get the exampleitem doc
        response = get(exampleitem_root + inserted_example_id)
        response.raise_for_status()
        doc = response.json()
        print(doc)

        # # Delete exampleitem
        response = delete(exampleitem_root + inserted_example_id)
        response.raise_for_status()

    except HTTPError as he:
        print(he.response.json())
        raise

if __name__ == "__main__":
    test_api()