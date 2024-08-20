from stdlib import utils


def test_is_ip_address():
    assert utils.is_ip_address("0.0.0.0")


def test_is_not_ip_address():
    assert utils.is_ip_address("https://www.example.com") == False


def test_is_url_address():
    assert utils.is_url_address("https://www.example.com")

def test_is_not_url_address():
    assert utils.is_url_address("0.0.0.0") == False
