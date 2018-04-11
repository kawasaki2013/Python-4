#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from optparse import OptionParser
from optparse import OptionGroup

def main():
    psr = OptionParser(version='0.1')
    psr.add_option('-a', '--apple', dest='apple',
                   help = u'りんご')
    psr.add_option('-b', '--banana', action='store_true', dest = 'banana',
                   help = u'ばなな')
    psr.add_option('-c', '--cherry', action='count', dest = 'cherry',
                   help = u'さくらんぼ')
    grp = OptionGroup(psr, 'Note',
                      u'くだものぱくぱく。')
    psr.add_option_group(grp)
   
    (opts, args) = psr.parse_args()
    if opts.apple != None:
        print(u'りんごの感想: %s' % opts.apple)
    if opts.banana:
        print(u'そんなばななー')
    if opts.cherry != None:
        print('いやしんぼめ、もう%d粒も食べおって' % opts.cherry)
   
    sys.exit(0)

if __name__ == '__main__':
    main()
