from nose import with_setup
from nose.tools import nottest,raises,assert_equal,assert_equals,assert_almost_equal


from src.ps_timeit import ps_timeit

thrdpool = None

@nottest
def setup():
    pass


@with_setup(setup)
def test_mapfunction():

    @ps_timeit
    def calc_square(x):
        return x**2

    calc_square(40000)
    #assert True