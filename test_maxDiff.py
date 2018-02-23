import pytest


def test_max_diff():
    from listClass import listOb
    test_inputLists = ([3, 5, 8, 14, 100, 26, 42], [4, 10, 123, 50, 20],
                        [4, 10.3, 0, 2, 3, 5])
    test_outputValue = (86, 113, 10.3)
    for n, t in enumerate(test_inputLists):
        assert listOb(t).maxDiff == test_outputValue[n]
    test_badLists1 = ([1, 2, 3, 'poop'], [1, 5, 'poop', 'pizza', 65],
                       ['poop', 99, 8])
    test_badLists2 = ([], [24])
    for n, t in enumerate(test_badLists1):
        with pytest.raises(TypeError):
            listOb(t).maxDiff
    for n, t in enumerate(test_badLists2):
        with pytest.raises(ValueError):
            listOb(t).maxDiff


@pytest.mark.xfail(reason="Should not have module")
def test_import():
    from listClass import listOb
    with pytest.raises(ImportError):
        listOb().import_modules()
