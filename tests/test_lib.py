from toto.lib import who_am_i


def test_whoami():

    res = who_am_i()

    assert "Santiago" in res.split()


def test_whoami_fail():

    res = who_am_i()

    assert "Pepe" in res.split()
