#!/usr/bin/python
__author__ = 'joel'


from gi.repository import Gtk, Gdk, GdkPixbuf
from gi.repository.GdkPixbuf import Pixbuf


DRAG_ACTION = Gdk.DragAction.COPY

TARGET_ENTRY_TEXT = 0
COLUMN_TEXT = 0

DRAG_ACTION = Gdk.DragAction.COPY

class DragDropWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drag and Drop Demo")
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        hbox = Gtk.Box()
        vbox.pack_start(hbox, True, True, 0)
        self.iconview = DragSourceIconView()
        self.drop_area = DropArea()
        hbox.pack_start(self.iconview, True, True, 0)
        hbox.pack_start(self.drop_area, True, True, 0)
        self.add_text_targets()

    def add_text_targets(self, button=None):
        self.drop_area.drag_dest_set_target_list(None)
        self.iconview.drag_source_set_target_list(None)
        self.drop_area.drag_dest_add_text_targets()
        self.iconview.drag_source_add_text_targets()

class DragSourceIconView(Gtk.IconView):
    def __init__(self):
        Gtk.IconView.__init__(self)
        self.set_text_column(COLUMN_TEXT)
        model = Gtk.ListStore(str)
        self.set_model(model)
        self.add_item("Item 1")
        self.add_item("Item 2")
        self.add_item("Item 3")
        self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [],
            DRAG_ACTION)
        self.connect("drag-data-get", self.on_drag_data_get)

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_path = self.get_selected_items()[0]
        selected_iter = self.get_model().get_iter(selected_path)
        if info == TARGET_ENTRY_TEXT:
            text = self.get_model().get_value(selected_iter, COLUMN_TEXT)
            data.set_text(text, -1)

    def add_item(self, text):
        self.get_model().append([text])


class ButtonDragging(Gtk.CellRendererText):
    def __init__(self):
        Gtk.CellRendererText.__init__(self)
#        self.set_text_column(COLUMN_TEXT)
#        model = Gtk.ListStore(str)
#        self.set_model(model)
#        self.add_item("~")
        self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
        self.connect("drag-data-get", self.on_drag_data_get)

    def on_drag_data_get(self, widget, drag_context, data, info, time):
        selected_path = self.get_selected_items()[0]
        selected_iter = self.get_model().get_iter(selected_path)
        text = self.get_model().get_value(selected_iter, COLUMN_TEXT)
        data.set_text(text, -1)

    def add_item(self, text):
        self.get_model().append([text])



class ButtonDrop(Gtk.Label):
    def __init__(self):
        Gtk.Label.__init__(self, "")
        self.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        self.connect("drag-data-received", self.on_drag_data_received)

    def on_drag_data_received(self, widget, drag_context, x,y, data,info, time):
        text = data.get_text()
        print("Received text: %s" % text)


class TableWindow(Gtk.Window):
    def text_edited(self, widget, path, text):
        self.liststore[path][1] = text

    def make_key(self, tl="",tr="",bl="",br=""):
        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append([tl,tr])
        self.liststore.append([bl,br])
        treeview = Gtk.TreeView(model=self.liststore)
        col1_cr = Gtk.CellRendererText()
        col1_cr.set_property("editable",True)
        col1 = Gtk.TreeViewColumn("l", col1_cr, text=0)
        treeview.append_column(col1)
        col2_cr = Gtk.CellRendererText()
        col2_cr.set_property("editable", True)
        col2 = Gtk.TreeViewColumn("r", col2_cr, text=1)
        treeview.append_column(col2)
        col2_cr.connect("edited", self.text_edited)
        treeview.set_headers_visible(False)
        return treeview


    def make_key_org(self, tl="",tr="",bl="",br=""):
        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append([tl,tr])
        self.liststore.append([bl,br])
        treeview = Gtk.TreeView(model=self.liststore)
        col1_cr = Gtk.CellRendererText()
        col1_cr.set_property("editable",True)
        col1 = Gtk.TreeViewColumn("l", col1_cr, text=0)
        treeview.append_column(col1)
        col2_cr = Gtk.CellRendererText()
        col2_cr.set_property("editable", True)
 #       col2_cr.set_property("alignment", Gtk.CellRendererText.pango.alignment.LEFT)
        col2 = Gtk.TreeViewColumn("r", col2_cr, text=1)
        treeview.append_column(col2)
        col2_cr.connect("edited", self.text_edited)
        treeview.set_headers_visible(False)
        return treeview

    def __init__(self):
        Gtk.Window.__init__(self, title="Table Example")
        fullgrid = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, row_spacing=1, column_spacing=1);
        self.add(fullgrid)
#        tlde =self.make_key( , )
#        tl = ButtonDragging()


        tlde = self.make_key(tl="~", tr="~")
        ae01 =self.make_key(tl="!",bl="1")
        ae02 =self.make_key(tl="@",bl="2")
        ae03 =self.make_key(tl="#",bl="3")
        ae04 =self.make_key(tl="$",bl="4")
        ae05 =self.make_key(tl="%",bl="5")
        ae06 =self.make_key(tl="^",bl="6")
        ae07 =self.make_key(tl="&",bl="7")
        ae08 =self.make_key(tl="*",bl="8")
        ae09 =self.make_key(tl="(",bl="9")
        ae10 =self.make_key(tl=")",bl="0")
        ae11 =self.make_key(tl="{",bl="[")
        ae12 =self.make_key(tl="}",bl="]")
        bksp =self.make_key(tl="bs",bl="bs")

        tab =self.make_key(tl="tab",bl="tab")
        ad01 =self.make_key(tl="\"",bl="'")
        ad02 =self.make_key(tl="<",bl=",")
        ad03 =self.make_key(tl=">",bl=".")
        ad04 =self.make_key(tl="P",bl="p")
        ad05 =self.make_key(tl="Y",bl="y")
        ad06 =self.make_key(tl="F",bl="f")
        ad07 =self.make_key(tl="G",bl="g")
        ad08 =self.make_key(tl="C",bl="c")
        ad09 =self.make_key(tl="R",bl="r")
        ad10 =self.make_key(tl="L",bl="l")
        ad11 =self.make_key(tl="",bl="/")
        ad12 =self.make_key(tl="+",bl="=")
        bksl =self.make_key(tl="|",bl="\\")

        caps =self.make_key(tl="cps",bl="cps")
        ac01 =self.make_key(tl="A",bl="a")
        ac02 =self.make_key(tl="O",bl="o")
        ac03 =self.make_key(tl="E",bl="e")
        ac04 =self.make_key(tl="U",bl="u")
        ac05 =self.make_key(tl="I",bl="i")
        ac06 =self.make_key(tl="D",bl="d")
        ac07 =self.make_key(tl="H",bl="h")
        ac08 =self.make_key(tl="T",bl="t")
        ac09 =self.make_key(tl="N",bl="n")
        ac10 =self.make_key(tl="S",bl="s")

        ac11 =self.make_key(tl="_",bl="-")
        rtrn =self.make_key(tl="rtrn",bl="rtrn")
        lfsh =self.make_key(tl="ls",bl="ls")
        ab01 =self.make_key(tl=":",bl=":")
        ab02 =self.make_key(tl="Q",bl="q")
        ab03 =self.make_key(tl="J",bl="j")
        ab04 =self.make_key(tl="K",bl="k")
        ab05 =self.make_key(tl="X",bl="x")
        ab06 =self.make_key(tl="B",bl="b")
        ab07 =self.make_key(tl="M",bl="m")
        ab08 =self.make_key(tl="W",bl="w")
        ab09 =self.make_key(tl="V",bl="v")
        ab10 =self.make_key(tl="Z",bl="z")
        rtsh =self.make_key(tl="ls",bl="ls")
        lctl =self.make_key(tl="lc",bl="lc")
        lwin =self.make_key(tl="lw",bl=" ")

        lalt =self.make_key(tl="la",bl=" ")
        spce =self.make_key(tl="sp",bl="sp")
        ralt =self.make_key(tl="ra",bl=" ")
        rwin =self.make_key(tl="rw",bl=" ")
        menu =self.make_key(tl="me",bl=" ")
        rctl =self.make_key(tl="rc",bl=" ")

        fullgrid.attach(tlde,  0, 0, 4, 4)
        fullgrid.attach(ae01,  4, 0, 4, 4)
        fullgrid.attach(ae02,  8, 0, 4, 4)
        fullgrid.attach(ae03, 12, 0, 4, 4)
        fullgrid.attach(ae04, 16, 0, 4, 4)
        fullgrid.attach(ae05, 20, 0, 4, 4)
        fullgrid.attach(ae06, 24, 0, 4, 4)
        fullgrid.attach(ae07, 28, 0, 4, 4)
        fullgrid.attach(ae08, 32, 0, 4, 4)
        fullgrid.attach(ae09, 36, 0, 4, 4)
        fullgrid.attach(ae10, 40, 0, 4, 4)
        fullgrid.attach(ae11, 44, 0, 4, 4)
        fullgrid.attach(ae12, 48, 0, 4, 4)
        fullgrid.attach(bksp, 52, 0, 8, 4)

        fullgrid.attach(tab,   0, 4, 6, 4)
        fullgrid.attach(ad01,  6, 4, 4, 4)
        fullgrid.attach(ad02, 10, 4, 4, 4)
        fullgrid.attach(ad03, 14, 4, 4, 4)
        fullgrid.attach(ad04, 18, 4, 4, 4)
        fullgrid.attach(ad05, 22, 4, 4, 4)
        fullgrid.attach(ad06, 26, 4, 4, 4)
        fullgrid.attach(ad07, 30, 4, 4, 4)
        fullgrid.attach(ad08, 34, 4, 4, 4)
        fullgrid.attach(ad09, 38, 4, 4, 4)
        fullgrid.attach(ad10, 42, 4, 4, 4)
        fullgrid.attach(ad11, 46, 4, 4, 4)
        fullgrid.attach(ad12, 50, 4, 4, 4)
        fullgrid.attach(bksl, 54, 4, 6, 4)

        fullgrid.attach(caps,  0, 8, 7, 4)
        fullgrid.attach(ac01,  7, 8, 4, 4)
        fullgrid.attach(ac02, 11, 8, 4, 4)
        fullgrid.attach(ac03, 15, 8, 4, 4)
        fullgrid.attach(ac04, 19, 8, 4, 4)
        fullgrid.attach(ac05, 23, 8, 4, 4)
        fullgrid.attach(ac06, 27, 8, 4, 4)
        fullgrid.attach(ac07, 31, 8, 4, 4)
        fullgrid.attach(ac08, 35, 8, 4, 4)
        fullgrid.attach(ac09, 39, 8, 4, 4)
        fullgrid.attach(ac10, 43, 8, 4, 4)
        fullgrid.attach(ac11, 47, 8, 4, 4)
        fullgrid.attach(rtrn, 51, 8, 9, 4)


        fullgrid.attach(lfsh,  0, 12, 9, 4)
        fullgrid.attach(ab01,  9, 12, 4, 4)
        fullgrid.attach(ab02, 13, 12, 4, 4)
        fullgrid.attach(ab03, 17, 12, 4, 4)
        fullgrid.attach(ab04, 21, 12, 4, 4)
        fullgrid.attach(ab05, 25, 12, 4, 4)
        fullgrid.attach(ab06, 29, 12, 4, 4)
        fullgrid.attach(ab07, 33, 12, 4, 4)
        fullgrid.attach(ab08, 37, 12, 4, 4)
        fullgrid.attach(ab09, 41, 12, 4, 4)
        fullgrid.attach(ab10, 45, 12, 4, 4)
        fullgrid.attach(rtsh, 49, 12, 11,4)

        fullgrid.attach(lctl, 0, 16, 5, 4)
        fullgrid.attach(lwin, 5, 16, 5, 4)
        fullgrid.attach(lalt, 10, 16, 5, 4)
        fullgrid.attach(spce, 15, 16, 25, 4)
        fullgrid.attach(ralt, 40, 16, 5, 4)
        fullgrid.attach(rwin, 45, 16, 5, 4)
        fullgrid.attach(menu, 50, 16, 5, 4)
        fullgrid.attach(rctl, 55, 16, 5, 4)
"""
        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["a", "b"])
        self.liststore.append(["c", "d"])

        self.treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("t", renderer_text, text=0)
        self.treeview.append_column(column_text)

        renderer_editabletext = Gtk.CellRendererText()
        renderer_editabletext.set_property("editable", True)

        column_editabletext = Gtk.TreeViewColumn("Editable Text",
            renderer_editabletext, text=1)
        self.treeview.append_column(column_editabletext)

        renderer_editabletext.connect("edited", self.text_edited)
        self.treeview.set_headers_visible(False)
"""



win = TableWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
