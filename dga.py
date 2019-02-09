import math
import pickle
import string
from collections import Counter

import tldextract
import numpy as np
from scipy.stats import describe

## Utils
def chunks(l, n, slide=None):
    """Yield successive n-sized chunks from l with a sliding window of slide
    indexes. Default value of slide has non-overlapping chunks."""
    if slide is None: slide = n
    for i in range(0, len(l), slide):
        yield l[i:i+n]

def H(s):
    p, lns = Counter(s), float(len(s))
    return -sum(count/lns * math.log(count/lns, 2) for count in p.values())

## Classification stuff
# Doing this is a higher priority than getting the spectral clustering working.
def _load_ground_truth(dgapath='../data/dga'):
    pass

def _ngrams(domains, ns=[1, 2, 3, 4]):
    def stats(counter, n):
        # you can use the below to see this w.r.t. all possibilities.
        #possibilities = len(string.ascii_lowercase + string.digits + '-.')**n
        l = list(counter.values())
        res = describe(l)
        median = np.median(l)

        return [res.mean, median, math.sqrt(res.variance)]

    features = []
    for n in ns:
        for domain in domains:
            domain = domain.lower()
            c = Counter([chunk for chunk in chunks(domain, n, slide=1) if len(chunk) == n])
            features.extend(stats(c, n))

    return features

def _e2and3ld_entropy(domain):
    def onlylast(domain):
        return domain.split('.')[-1]
    domain = domain.lower()
    res = tldextract.extract(domain)
    e2ld = '%s.%s' % (res.domain, res.suffix)
    if res.subdomain:
        e3ld = '%s.%s.%s' % (onlylast(res.subdomain),
                             res.domain,
                             res.suffix)
    else:
        e3ld = e2ld

    return H(e2ld), H(e3ld)

def _entropy(domains):
    perdomain = {domain: _e2and3ld_entropy(domain) for domain in domains}
    e2ld_h = [x[0] for x in perdomain.values()]
    e3ld_h = [x[1] for x in perdomain.values()]

    return (perdomain, [describe(e2ld_h).mean, np.median(e2ld_h),
                        describe(e3ld_h).mean, np.median(e3ld_h)])

def _len(domains):
    lengths = list(map(len, domains))
    res = describe(lengths)
    return [res.mean, np.median(lengths), math.sqrt(res.variance), res.variance]

def _levels(domains):
    def numlevels(d):
        return len(list(filter(lambda x: x == '.', d))) + 1
    numlds = [numlevels(d) for d in domains]
    res = describe(numlds)
    return [res.mean, np.median(numlds), math.sqrt(res.variance), res.variance]

def _tlds(domains):
    return len(Counter([x.split('.')[-1] for x in domains]))

def _distinctchars(domains):
    return len(Counter(''.join(domains)))

def vectorize(domains):
    pass

def train():
    pass

# * Generate feature vector from set of domains
# ** Important to note that it needs to chunk em up for the classifier to work. Refer to Pleiades paper.
# ** Chunks into groups of alpha = 10
# ** 1,2,3,4-gram. get mean, median, std. dev. (4 x 3 = 12 features)
# ** shannon entropy of 2ld/3ld. exact value per domain (2x), mean/median of group (2 x 2) total of 6 features.
# ** mean, med, std. dev, var of length, # of domain levels, distinct chars, # distinct TLDs, # .com, # .other, ratio of #.com/#.other, mean/med/stddev TLDs
# * Train model
# * Fit cluster
# * Output as JSON maybe huh

def save(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def load(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
