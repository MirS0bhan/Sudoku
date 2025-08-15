# how_to_play_dialog.py
#
# Copyright 2025 sepehr-rs
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Gtk, Adw
from gettext import gettext as _


@Gtk.Template(resource_path="/io/github/sepehr_rs/Sudoku/gtk/how-to-play-dialog.ui")
class HowToPlayDialog(Adw.Dialog):
    __gtype_name__ = "HowToPlayDialog"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
