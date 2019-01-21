#!/usr/bin/env python3
#
# This script generates mock binary syscall traces which are used for the
# monotonic classifier exercises.

import sys
import random
import os
from optparse import OptionParser

from tqdm import tqdm

BENIGN_SYSCALLS = [
    'NtCreateUserProcess',
    'NtDrawText',
    'NtDisplayString',
    'NtOpenKeyEx',
    'NtOpenFile',
    'NtOpenTimer',
    'NtQueryDirectoryFile',
    'NtReadFile',
    'NtWriteFile',
]

MAL_SYSCALLS = [
    'RegCreateKeyEx',
    'RegSaveKeyEx',
    'NtCreateProcessEx',
    'NtCreateThreadEx',
    'NtModifyBootEntry',
    'NtSaveKeyEx',
    'NtSetTimerEx',
    'NtWriteFile',
]

def choose_between_by_p(l1, l2, p, count):
    """
    Choose `count` elements from `l1` (w/ prob `p`) and `l2` (w/ prob `p`-1).
    """
    assert 0 <= p
    assert p <= 1
    return [random.choice(l1) if random.random() <= p else random.choice(l2) for _ in range(count)]


def create_traces(numsamples, minlength, maxlength,
                  benignp=0.9,
                  benigndir='/zfs/home/yacin/work/oreilly/hands-on-adversarial-machine-learning/data/01-monotonic-classifiers/benign-traces',
                  maldir='/zfs/home/yacin/work/oreilly/hands-on-adversarial-machine-learning/data/01-monotonic-classifiers/malicious-traces'):
    """
    Generate synthetic syscall traces for benign and malicious binaries.

    Arguments:
    - `numsamples`: number of positive and negative samples to generate
    - `minlength`: minimum number of syscalls per trace
    - `maxlength`: maximum number of syscalls per traces
    - `benignp`: probability a syscall from a benign sample is from BENIGN_SYSCALLS
    - `benigndir`: directory for benign samples
    - `maldir`: directory for malicious samples
    """
    width = len(str(numsamples))
    for i in tqdm(range(numsamples)):
        name = ('{:0%d}.trace' % width).format(i)
        # benign
        with open(os.path.join(benigndir, name), 'w') as out:
            count = random.randrange(minlength, maxlength)
            for syscall in choose_between_by_p(BENIGN_SYSCALLS, MAL_SYSCALLS, benignp, count):
                out.write(syscall)
                out.write('\n')
        # malicious
        with open(os.path.join(maldir, name), 'w') as out:
            count = random.randrange(minlength, maxlength)
            for syscall in choose_between_by_p(BENIGN_SYSCALLS, MAL_SYSCALLS, 1 - benignp, count):
                out.write(syscall)
                out.write('\n')

def main():
    """main function for standalone usage"""
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    (options, args) = parser.parse_args()

    if len(args) != 0:
        parser.print_help()
        return 2

    # do stuff
    create_traces(1000, 500, 50000)

if __name__ == '__main__':
    sys.exit(main())
