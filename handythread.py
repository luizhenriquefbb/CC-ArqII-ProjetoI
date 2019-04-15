import sys
import time
import threading
from itertools import izip, count

def foreach(fun,items,threads=3,return_=False):
    """
    Apply fun to each element of l, in parallel

    params:
        fun     : function
        items   : array
        Thread  : number of threads to create
        return_ : return array if has return
    """

    if threads>1:
        iteratorlock = threading.Lock()
        exceptions = []
        if return_:
            n = 0
            d = {}
            i = izip(count(),items.__iter__())
        else:
            i = items.__iter__()


        def runall():
            while True:
                iteratorlock.acquire()
                try:
                    try:
                        if exceptions:
                            return
                        v = i.next()
                    finally:
                        iteratorlock.release()
                except StopIteration:
                    return
                try:
                    if return_:
                        n,x = v
                        d[n] = fun(x)
                    else:
                        fun(v)
                except:
                    e = sys.exc_info()
                    iteratorlock.acquire()
                    try:
                        exceptions.append(e)
                    finally:
                        iteratorlock.release()

        threadlist = [threading.Thread(target=runall) for j in xrange(threads)]
        for t in threadlist:
            t.start()
        for t in threadlist:
            t.join()
        if exceptions:
            a, b, c = exceptions[0]
            # raise a, b, c
        if return_:
            r = d.items()
            r.sort()
            return [v for (n,v) in r]
    else:
        if return_:
            return [fun(v) for v in items]
        else:
            for v in items:
                fun(v)
            return

def parallel_map(f,l,threads=4):
    return foreach(f,l,threads=threads,return_=True)
