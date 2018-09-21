# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from ._pip import build_wheel, get_sdist, WheelBuildError


class BuiltDist(object):

    def __init__(self, ireq, sources=None):
        self.ireq = ireq
        self.sources = sources
        self.built = None
        self.metadata = None

    def build(self):
        try:
            wheel = build_wheel(self.ireq, sources=self.sources)
            self.built = wheel
            metadata = wheel.metadata
        except WheelBuildError:
        # XXX: This depends on a side effect of `build_wheel`. This block is
        # reached when it fails to build an sdist, where the sdist would have
        # been downloaded, extracted into `ireq.source_dir`, and partially
        # built (hopefully containing .egg-info).
            sdist = get_sdist(self.ireq)
            self.built = sdist
            metadata = sdist.metadata
            if not metadata:
                raise
        else:
            metadata = wheel.metadata
        self.metadata = metadata
        return self.built
