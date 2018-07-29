#!/usr/bin/env python3

# Download and verify .spec file sources - e.g. in the COPR environment.
#
# 2018, Georg Sauthoff <mail@gms.tf>, GPLv3+

import glob
import hashlib
import os
import subprocess
import sys

def print_git():
    changeset = open('../.git/refs/heads/master').read().strip()
    print('Git repo at: {}'.format(changeset))

def download(url):
    print('Fetching {} ... '.format(url), end='')
    filename = url[url.rindex('/')+1:]
    just_https = ([ '--proto-redir', '=https' ] if url.startswith('https://')
        else [])
    subprocess.run(['curl'] + just_https + ['--silent', '--show-error',
        '--fail', '-L', '-o', filename, url], check=True)
    print('done.')
    return filename

def get_sources(specfile):
    xs = subprocess.check_output(['spectool', specfile],
            universal_newlines=True)
    return [ (x[0].strip(':'), x[1])
            for x in (x.split() for x in xs.splitlines() )
            if x[0].startswith('Source') ]

def get_checksums(specfile):
    d = {}
    with open(specfile) as f:
        for line in f:
            if line.startswith('#sha256('):
                i = line.index('(')
                j = line.index(')')
                k = line.index('=')
                key = line[i+1:j]
                checksum = line[k+1:].strip()
                d[key] = checksum
    return d

# cf. https://stackoverflow.com/a/44873382/427158
def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()

def verify_sources(sources, checksums):
    for key, url in sources:
        filename = download(url)
        checksum = sha256sum(filename)
        if checksum != checksums[key]:
            raise RuntimeError(('sha256 checksum of {} ({}) {} '
                'does NOT match the recorded one: {}').format(filename, key,
                    checksum, checksums[key]))

def build_srpm(specdir, outdir, specfile):
    subprocess.run(['rpmbuild', '--define', '_sourcedir {}'.format(specdir),
        '--define', '_specdir {}'.format(specdir),
        '--define', '_rpmdir {}'.format(outdir),
        '--define', '_srcrpmdir {}'.format(outdir),
        '-bs', specfile], check=True)

def main():
    # specdir equals $PWD
    outdir = sys.argv[1]
    # specdir = sys.argv[2]
    specdir = os.getcwd()
    specfile = glob.glob('*.spec')[0]
    print_git()
    sources = get_sources(specfile)
    checksums = get_checksums(specfile)
    verify_sources(sources, checksums)
    build_srpm(specdir, outdir, specfile)

if __name__ == '__main__':
    sys.exit(main())

