# -*- coding: utf-8 -*-
"""Style.INITIALS 风格"""
from __future__ import unicode_literals

from ..constants import Style
from ..style import register
from ..style._utils import get_initials


@register(Style.INITIALS)
def convert(pinyin, **kwargs):
    strict = kwargs.get('strict')
    return get_initials(pinyin, strict)
