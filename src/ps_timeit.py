def _redirect_out(message,**kwargs):
    if kwargs and 'app_name_log' in kwargs:
        import logging
        log_name = kwargs.get('app_name_log')
        logger = logging.getLogger(log_name)
        logger.info(message)
    else:
        print(message)

def ps_timeit(function):
    '''
    Phani Sarma timeit : decorator for timing a particular function execution
    everytime a function is executed, its execution is measured in secs
    if app_name_log is specified, timing is redirected to the respective app logger so there is continuity
    else: standard print redirection of message

    :param function: function to be decorated
    :return: str to stdout or logger
    '''
    import time
    def timer(*args,**kwargs):
        start  = time.time()
        result = function(*args,**kwargs)
        end    = time.time()

        duration = int((end - start))
        funcname = function.__name__
        msg      = '%s took %d secs' % (funcname, duration)
        _redirect_out(msg,**kwargs)
        return result
    return timer


class PSC_Timer():
    def __init__(self,app_name_log=None):
        self.app_name_log = app_name_log

    def __enter__(self):
        import time
        from inspect import currentframe,getouterframes

        calframe  =  getouterframes(currentframe(), 2)
        self.msg = 'function: %s line_no_begin: %d '%(calframe[1][3],calframe[1][2])
        self.start_time = time.clock()

    def __exit__(self, *args):
        import time
        from inspect import currentframe, getframeinfo,getouterframes

        self.end_time = time.clock()
        self.duration = self.end_time - self.start_time
        calframe  =  getouterframes(currentframe(), 2)
        self.msg += ' line_no_end: %d took %d secs '%(calframe[1][2],self.duration)

        kwargs = {'app_name_log':self.app_name_log } if self.app_name_log else {}
        _redirect_out(self.msg,**kwargs)











