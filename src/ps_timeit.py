def ps_timeit(function):
    '''
    Phani Sarma : decorator for timing a particular function execution
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

        duration = int((end - start) * 1000)
        funcname = function.__name__
        msg      = '%s took %d secs' % (funcname, duration)
        if 'app_name_log' in kwargs:
            import logging
            log_name = kwargs.get('app_name_log')
            logger = logging.getLogger(log_name)
            logger.info(msg)
        else:
            print(msg)
        return result
    return timer
