""" Models for various kinds of arrow heads that can be added to
Arrow annotations

"""
from __future__ import absolute_import

from ..core.properties import abstract
from ..core.properties import Float, Include, Override
from ..core.property_mixins import LineProps, FillProps
from .renderers import Renderer

@abstract
class ArrowHead(Renderer):
    """ Base class for arrow heads.

    """

class OpenHead(ArrowHead):
    """ Render an open-body arrow head.

    """

    size = Float(default=25, help="""
    The size, in pixels, of the arrow head.
    """)

    line_props = Include(LineProps, use_prefix=False, help="""
    The %s values for the arrow head outline.
    """)

class NormalHead(ArrowHead):
    """ Render a closed-body arrow head.

    """

    size = Float(default=25, help="""
    The size, in pixels, of the arrow head.
    """)

    line_props = Include(LineProps, use_prefix=False, help="""
    The %s values for the arrow head outline.
    """)

    fill_props = Include(FillProps, use_prefix=False, help="""
    The %s values for the arrow head interior.
    """)

    fill_color = Override(default="black")

class VeeHead(ArrowHead):
    """ Render an vee-style arrow head.

    """

    size = Float(default=25, help="""
    The size, in pixels, of the arrow head.
    """)

    line_props = Include(LineProps, use_prefix=False, help="""
    The %s values for the arrow head outline.
    """)

    fill_props = Include(FillProps, use_prefix=False, help="""
    The %s values for the arrow head interior.
    """)

    fill_color = Override(default="black")
