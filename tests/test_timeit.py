from nose import with_setup
from nose.tools import nottest


from src.ps_timeit import ps_timeit,PSC_Timer

@nottest
def setup():
    pass


@with_setup(setup)
def test_timerdecor():
    import time
    @ps_timeit
    def calc_square(x):
        time.sleep(5)# just so we elapse
        return x**2

    calc_square(40000)

    assert True

@with_setup(setup)
def test_timerscope():
    import time
    def calc_square(x):
        return x**2

    with PSC_Timer() as t:
         calc_square(40000)
         time.sleep(5)# just so we elapse
         calc_square(1000000000)

    assert True

