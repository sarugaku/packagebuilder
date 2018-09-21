# -*- coding=utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals

from ._pip import build_wheel, get_sdist, WheelBuildError
from ._pip_shims import get_sources


class BuiltDist(object):

    def __init__(self, ireq, sources=None, cache_dir=None):
        if not sources:
            sources = get_sources()
        self.ireq = ireq
        self.sources = sources
        self.built = None
        self.metadata = None
        self.cache_dir = cache_dir

    def build(self):
        try:
            wheel = build_wheel(self.ireq, sources=self.sources, cache_dir=self.cache_dir)
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


def build(ireq, sources=None, cache_dir=None):
    builder = BuiltDist(ireq, sources=sources, cache_dir=cache_dir)
    dist = builder.build()
    return dist
