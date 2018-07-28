This repository contains RPM source packages that aren't included
in Fedora, yet.

2018, Georg Sauthoff <mail@gms.tf>


## Design Decisions

Similar to the packages in the [copr-epel repository][1] and for
the same reasons, the packages are built using the makefile
method in the COPR-environment. That means that `.copr/Makefile`
calls the `build.py` script which downloads all sources, verifies
the checksums against the ones included in the spec files and
only if they match calls `rpmbuild`.

The checksums are specified as special comments in the spec
files.

[1]: https://github.com/gsauthof/copr-epel#design-decisions
