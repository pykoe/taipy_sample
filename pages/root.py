from taipy.gui import Markdown

import numpy as np

from data.data import data


def to_text(val):
    return '{:,}'.format(int(val)).replace(',', ' ')

root = Markdown("pages/root.md")