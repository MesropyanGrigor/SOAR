from vendor.virus_total.client import VTClient

def test_the_client_will_be_one_instance():
    collection = set()

    clinet_1 = VTClient("base_url", "api_key")
    clinet_2 = VTClient("base_url", "api_key")

    collection.add(clinet_1)
    collection.add(clinet_2)

    assert len(collection) == 1