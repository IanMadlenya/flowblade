"""
    Flowblade Movie Editor is a nonlinear video editor.
    Copyright 2012 Janne Liljeblad.

    This file is part of Flowblade Movie Editor <http://code.google.com/p/flowblade>.

    Flowblade Movie Editor is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Flowblade Movie Editor is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Flowblade Movie Editor.  If not, see <http://www.gnu.org/licenses/>.
"""
"""
Module contains functions to build generic dialogs.
"""
import gtk

import guiutils

def _dialog_destroy(dialog, response):
    dialog.destroy()

def info_message(primary_txt, secondary_txt, parent_window):
    warning_message(primary_txt, secondary_txt, parent_window, is_info=True)

def warning_message(primary_txt, secondary_txt, parent_window, is_info=False):
    warning_message_with_callback(primary_txt, secondary_txt, parent_window, is_info,_dialog_destroy)

def warning_message_with_callback(primary_txt, secondary_txt, parent_window, is_info, callback):
    content = get_warning_message_dialog_panel(primary_txt, secondary_txt, is_info)
    dialog = gtk.Dialog("",
                        parent_window,
                        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                        ( _("OK").encode('utf-8'), gtk.RESPONSE_ACCEPT))
    dialog.vbox.pack_start(content, True, True, 0)
    dialog.set_has_separator(False)
    dialog.set_resizable(False)
    dialog.connect('response', callback)
    dialog.show_all()
    
def warning_confirmation(callback, primary_txt, secondary_txt, parent_window, data=None):
    content = get_warning_message_dialog_panel(primary_txt, secondary_txt)
    align = gtk.Alignment(0.5, 0.5, 1.0, 1.0)
    align.set_padding(0, 12, 0, 0)
    align.add(content)
    
    dialog = gtk.Dialog("",
                        parent_window,
                        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                        (_("Cancel").encode('utf-8'), gtk.RESPONSE_REJECT,
                         _("OK").encode('utf-8'), gtk.RESPONSE_ACCEPT))
    dialog.vbox.pack_start(align, True, True, 0)
    dialog.set_has_separator(False)
    dialog.set_resizable(False)
    if data == None:
        dialog.connect('response', callback)
    else:
        dialog.connect('response', callback, data)
    dialog.show_all()

def get_warning_message_dialog_panel(primary_txt, secondary_txt, is_info=False, alternative_icon=None):
    
    if is_info == True:
        icon = gtk.STOCK_DIALOG_INFO
    else:
        icon = gtk.STOCK_DIALOG_WARNING
    
    if alternative_icon != None:
        icon = alternative_icon

    warning_icon = gtk.image_new_from_stock(icon, gtk.ICON_SIZE_DIALOG)
    icon_box = gtk.VBox(False, 2)
    icon_box.pack_start(warning_icon, False, False, 0)
    icon_box.pack_start(gtk.Label(), True, True, 0)
    
    p_label = guiutils.bold_label(primary_txt)
    s_label = gtk.Label(secondary_txt)
    texts_pad = gtk.Label()
    texts_pad.set_size_request(12,12)

    pbox = gtk.HBox(False, 1)
    pbox.pack_start(p_label, False, False, 0)
    pbox.pack_start(gtk.Label(), True, True, 0)

    sbox = gtk.HBox(False, 1)
    sbox.pack_start(s_label, False, False, 0)
    sbox.pack_start(gtk.Label(), True, True, 0)
    
    text_box = gtk.VBox(False, 0)
    text_box.pack_start(pbox, False, False, 0)
    text_box.pack_start(texts_pad, False, False, 0)
    text_box.pack_start(sbox, False, False, 0)
    text_box.pack_start(gtk.Label(), True, True, 0)

    hbox = gtk.HBox(False, 12)
    hbox.pack_start(icon_box, False, False, 0)
    hbox.pack_start(text_box, True, True, 0)
    
    align = gtk.Alignment(0.5, 0.5, 1.0, 1.0)
    align.set_padding(12, 0, 12, 12)
    align.add(hbox)
    
    return align
