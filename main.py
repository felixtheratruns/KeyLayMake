#!/usr/bin/python
__author__ = 'joel'

from gi.repository import Gtk

class TableWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Table Example")
    #    Gtk.Window.maximize(self)
        grid1 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=1)
        grid2 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=1)
        grid3 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=1)
        grid4 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=1)
        grid5 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=1)

        parent = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=10)
        self.add(parent)


        tlde = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="~")
        tr = Gtk.Button()
        bl = Gtk.Button(label="`")
        br = Gtk.Button()
        tlde.attach(tl, 0, 0, 1, 1)
        tlde.attach(tr, 1, 0, 1, 1)
        tlde.attach(bl, 0, 1, 1, 1)
        tlde.attach(br, 1, 1, 1, 1)

        ae01 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="!")
        tr = Gtk.Button()
        bl = Gtk.Button(label="1")
        br = Gtk.Button()
        ae01.attach(tl, 0, 0, 1, 1)
        ae01.attach(tr, 1, 0, 1, 1)
        ae01.attach(bl, 0, 1, 1, 1)
        ae01.attach(br, 1, 1, 1, 1)

        ae02 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="@")
        tr = Gtk.Button()
        bl = Gtk.Button(label="2")
        br = Gtk.Button()
        ae02.attach(tl, 0, 0, 1, 1)
        ae02.attach(tr, 1, 0, 1, 1)
        ae02.attach(bl, 0, 1, 1, 1)
        ae02.attach(br, 1, 1, 1, 1)


        ae03 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="#")
        tr = Gtk.Button()
        bl = Gtk.Button(label="3")
        br = Gtk.Button()
        ae03.attach(tl, 0, 0, 1, 1)
        ae03.attach(tr, 1, 0, 1, 1)
        ae03.attach(bl, 0, 1, 1, 1)
        ae03.attach(br, 1, 1, 1, 1)

        ae04 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="$")
        tr = Gtk.Button()
        bl = Gtk.Button(label="4")
        br = Gtk.Button()
        ae04.attach(tl, 0, 0, 1, 1)
        ae04.attach(tr, 1, 0, 1, 1)
        ae04.attach(bl, 0, 1, 1, 1)
        ae04.attach(br, 1, 1, 1, 1)

        ae05 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="%")
        tr = Gtk.Button()
        bl = Gtk.Button(label="5")
        br = Gtk.Button()
        ae05.attach(tl, 0, 0, 1, 1)
        ae05.attach(tr, 1, 0, 1, 1)
        ae05.attach(bl, 0, 1, 1, 1)
        ae05.attach(br, 1, 1, 1, 1)

        ae06 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="^")
        tr = Gtk.Button()
        bl = Gtk.Button(label="6")
        br = Gtk.Button()
        ae06.attach(tl, 0, 0, 1, 1)
        ae06.attach(tr, 1, 0, 1, 1)
        ae06.attach(bl, 0, 1, 1, 1)
        ae06.attach(br, 1, 1, 1, 1)

        ae07 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="&")
        tr = Gtk.Button()
        bl = Gtk.Button(label="7")
        br = Gtk.Button()
        ae07.attach(tl, 0, 0, 1, 1)
        ae07.attach(tr, 1, 0, 1, 1)
        ae07.attach(bl, 0, 1, 1, 1)
        ae07.attach(br, 1, 1, 1, 1)

        ae08 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="*")
        tr = Gtk.Button()
        bl = Gtk.Button(label="8")
        br = Gtk.Button()
        ae08.attach(tl, 0, 0, 1, 1)
        ae08.attach(tr, 1, 0, 1, 1)
        ae08.attach(bl, 0, 1, 1, 1)
        ae08.attach(br, 1, 1, 1, 1)

        ae09 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="(")
        tr = Gtk.Button()
        bl = Gtk.Button(label="9")
        br = Gtk.Button()
        ae09.attach(tl, 0, 0, 1, 1)
        ae09.attach(tr, 1, 0, 1, 1)
        ae09.attach(bl, 0, 1, 1, 1)
        ae09.attach(br, 1, 1, 1, 1)

        ae10 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label=")")
        tr = Gtk.Button()
        bl = Gtk.Button(label="0")
        br = Gtk.Button()
        ae10.attach(tl, 0, 0, 1, 1)
        ae10.attach(tr, 1, 0, 1, 1)
        ae10.attach(bl, 0, 1, 1, 1)
        ae10.attach(br, 1, 1, 1, 1)

        ae11 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="{")
        tr = Gtk.Button()
        bl = Gtk.Button(label="[")
        br = Gtk.Button()
        ae11.attach(tl, 0, 0, 1, 1)
        ae11.attach(tr, 1, 0, 1, 1)
        ae11.attach(bl, 0, 1, 1, 1)
        ae11.attach(br, 1, 1, 1, 1)

        ae12 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="}")
        tr = Gtk.Button()
        bl = Gtk.Button(label="]")
        br = Gtk.Button()
        ae12.attach(tl, 0, 0, 1, 1)
        ae12.attach(tr, 1, 0, 1, 1)
        ae12.attach(bl, 0, 1, 1, 1)
        ae12.attach(br, 1, 1, 1, 1)

        bksp = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="backsp")
        tr = Gtk.Button()
        bl = Gtk.Button(label="backsp")
        br = Gtk.Button()
        bksp.attach(tl, 0, 0, 1, 1)
        bksp.attach(tr, 1, 0, 1, 1)
        bksp.attach(bl, 0, 1, 1, 1)
        bksp.attach(br, 1, 1, 1, 1)



        tab = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="tab")
        tr = Gtk.Button()
        bl = Gtk.Button(label="tab")
        br = Gtk.Button()
        tab.attach(tl, 0, 0, 1, 1)
        tab.attach(tr, 1, 0, 1, 1)
        tab.attach(bl, 0, 1, 1, 1)
        tab.attach(br, 1, 1, 1, 1)


        ad01 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="\"")
        tr = Gtk.Button()
        bl = Gtk.Button(label="'")
        br = Gtk.Button()
        ad01.attach(tl, 0, 0, 1, 1)
        ad01.attach(tr, 1, 0, 1, 1)
        ad01.attach(bl, 0, 1, 1, 1)
        ad01.attach(br, 1, 1, 1, 1)

        ad02 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="<")
        tr = Gtk.Button()
        bl = Gtk.Button(label=",")
        br = Gtk.Button()
        ad02.attach(tl, 0, 0, 1, 1)
        ad02.attach(tr, 1, 0, 1, 1)
        ad02.attach(bl, 0, 1, 1, 1)
        ad02.attach(br, 1, 1, 1, 1)

        ad03 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label=">")
        tr = Gtk.Button()
        bl = Gtk.Button(label=".")
        br = Gtk.Button()
        ad03.attach(tl, 0, 0, 1, 1)
        ad03.attach(tr, 1, 0, 1, 1)
        ad03.attach(bl, 0, 1, 1, 1)
        ad03.attach(br, 1, 1, 1, 1)


        ad04 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="P")
        tr = Gtk.Button()
        bl = Gtk.Button(label="p")
        br = Gtk.Button()
        ad04.attach(tl, 0, 0, 1, 1)
        ad04.attach(tr, 1, 0, 1, 1)
        ad04.attach(bl, 0, 1, 1, 1)
        ad04.attach(br, 1, 1, 1, 1)


        ad05 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="Y")
        tr = Gtk.Button()
        bl = Gtk.Button(label="y")
        br = Gtk.Button()
        ad05.attach(tl, 0, 0, 1, 1)
        ad05.attach(tr, 1, 0, 1, 1)
        ad05.attach(bl, 0, 1, 1, 1)
        ad05.attach(br, 1, 1, 1, 1)


        ad06 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="F")
        tr = Gtk.Button()
        bl = Gtk.Button(label="f")
        br = Gtk.Button()
        ad06.attach(tl, 0, 0, 1, 1)
        ad06.attach(tr, 1, 0, 1, 1)
        ad06.attach(bl, 0, 1, 1, 1)
        ad06.attach(br, 1, 1, 1, 1)

        ad07 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="G")
        tr = Gtk.Button()
        bl = Gtk.Button(label="g")
        br = Gtk.Button()
        ad07.attach(tl, 0, 0, 1, 1)
        ad07.attach(tr, 1, 0, 1, 1)
        ad07.attach(bl, 0, 1, 1, 1)
        ad07.attach(br, 1, 1, 1, 1)

        ad08 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="C")
        tr = Gtk.Button()
        bl = Gtk.Button(label="c")
        br = Gtk.Button()
        ad08.attach(tl, 0, 0, 1, 1)
        ad08.attach(tr, 1, 0, 1, 1)
        ad08.attach(bl, 0, 1, 1, 1)
        ad08.attach(br, 1, 1, 1, 1)


        ad09 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="R")
        tr = Gtk.Button()
        bl = Gtk.Button(label="r")
        br = Gtk.Button()
        ad09.attach(tl, 0, 0, 1, 1)
        ad09.attach(tr, 1, 0, 1, 1)
        ad09.attach(bl, 0, 1, 1, 1)
        ad09.attach(br, 1, 1, 1, 1)

        ad10 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="L")
        tr = Gtk.Button()
        bl = Gtk.Button(label="l")
        br = Gtk.Button()
        ad10.attach(tl, 0, 0, 1, 1)
        ad10.attach(tr, 1, 0, 1, 1)
        ad10.attach(bl, 0, 1, 1, 1)
        ad10.attach(br, 1, 1, 1, 1)

        ad11 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="?")
        tr = Gtk.Button()
        bl = Gtk.Button(label="/")
        br = Gtk.Button()
        ad11.attach(tl, 0, 0, 1, 1)
        ad11.attach(tr, 1, 0, 1, 1)
        ad11.attach(bl, 0, 1, 1, 1)
        ad11.attach(br, 1, 1, 1, 1)


        ad12 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="+")
        tr = Gtk.Button()
        bl = Gtk.Button(label="=")
        br = Gtk.Button()
        ad12.attach(tl, 0, 0, 1, 1)
        ad12.attach(tr, 1, 0, 1, 1)
        ad12.attach(bl, 0, 1, 1, 1)
        ad12.attach(br, 1, 1, 1, 1)

        bksl = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="|")
        tr = Gtk.Button()
        bl = Gtk.Button(label="\\")
        br = Gtk.Button()
        bksl.attach(tl, 0, 0, 1, 1)
        bksl.attach(tr, 1, 0, 1, 1)
        bksl.attach(bl, 0, 1, 1, 1)
        bksl.attach(br, 1, 1, 1, 1)









        caps = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="caps")
        tr = Gtk.Button()
        bl = Gtk.Button(label="caps")
        br = Gtk.Button()
        caps.attach(tl, 0, 0, 1, 1)
        caps.attach(tr, 1, 0, 1, 1)
        caps.attach(bl, 0, 1, 1, 1)
        caps.attach(br, 1, 1, 1, 1)

        ac01 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="A")
        tr = Gtk.Button()
        bl = Gtk.Button(label="a")
        br = Gtk.Button()
        ac01.attach(tl, 0, 0, 1, 1)
        ac01.attach(tr, 1, 0, 1, 1)
        ac01.attach(bl, 0, 1, 1, 1)
        ac01.attach(br, 1, 1, 1, 1)

        ac02 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="O")
        tr = Gtk.Button()
        bl = Gtk.Button(label="o")
        br = Gtk.Button()
        ac02.attach(tl, 0, 0, 1, 1)
        ac02.attach(tr, 1, 0, 1, 1)
        ac02.attach(bl, 0, 1, 1, 1)
        ac02.attach(br, 1, 1, 1, 1)


        ac03 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="E")
        tr = Gtk.Button()
        bl = Gtk.Button(label="e")
        br = Gtk.Button()
        ac03.attach(tl, 0, 0, 1, 1)
        ac03.attach(tr, 1, 0, 1, 1)
        ac03.attach(bl, 0, 1, 1, 1)
        ac03.attach(br, 1, 1, 1, 1)

        ac04 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="U")
        tr = Gtk.Button()
        bl = Gtk.Button(label="u")
        br = Gtk.Button()
        ac04.attach(tl, 0, 0, 1, 1)
        ac04.attach(tr, 1, 0, 1, 1)
        ac04.attach(bl, 0, 1, 1, 1)
        ac04.attach(br, 1, 1, 1, 1)

        ac05 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="I")
        tr = Gtk.Button()
        bl = Gtk.Button(label="i")
        br = Gtk.Button()
        ac05.attach(tl, 0, 0, 1, 1)
        ac05.attach(tr, 1, 0, 1, 1)
        ac05.attach(bl, 0, 1, 1, 1)
        ac05.attach(br, 1, 1, 1, 1)

        ac06 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="D")
        tr = Gtk.Button()
        bl = Gtk.Button(label="d")
        br = Gtk.Button()
        ac06.attach(tl, 0, 0, 1, 1)
        ac06.attach(tr, 1, 0, 1, 1)
        ac06.attach(bl, 0, 1, 1, 1)
        ac06.attach(br, 1, 1, 1, 1)

        ac07 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="H")
        tr = Gtk.Button()
        bl = Gtk.Button(label="h")
        br = Gtk.Button()
        ac07.attach(tl, 0, 0, 1, 1)
        ac07.attach(tr, 1, 0, 1, 1)
        ac07.attach(bl, 0, 1, 1, 1)
        ac07.attach(br, 1, 1, 1, 1)

        ac08 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="T")
        tr = Gtk.Button()
        bl = Gtk.Button(label="t")
        br = Gtk.Button()
        ac08.attach(tl, 0, 0, 1, 1)
        ac08.attach(tr, 1, 0, 1, 1)
        ac08.attach(bl, 0, 1, 1, 1)
        ac08.attach(br, 1, 1, 1, 1)

        ac09 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="N")
        tr = Gtk.Button()
        bl = Gtk.Button(label="n")
        br = Gtk.Button()
        ac09.attach(tl, 0, 0, 1, 1)
        ac09.attach(tr, 1, 0, 1, 1)
        ac09.attach(bl, 0, 1, 1, 1)
        ac09.attach(br, 1, 1, 1, 1)

        ac10 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="S")
        tr = Gtk.Button()
        bl = Gtk.Button(label="s")
        br = Gtk.Button()
        ac10.attach(tl, 0, 0, 1, 1)
        ac10.attach(tr, 1, 0, 1, 1)
        ac10.attach(bl, 0, 1, 1, 1)
        ac10.attach(br, 1, 1, 1, 1)

        ac11 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="_")
        tr = Gtk.Button()
        bl = Gtk.Button(label="-")
        br = Gtk.Button()
        ac11.attach(tl, 0, 0, 1, 1)
        ac11.attach(tr, 1, 0, 1, 1)
        ac11.attach(bl, 0, 1, 1, 1)
        ac11.attach(br, 1, 1, 1, 1)

        rtrn = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="rtrn")
        tr = Gtk.Button()
        bl = Gtk.Button(label="rtrn")
        br = Gtk.Button()
        rtrn.attach(tl, 0, 0, 1, 1)
        rtrn.attach(tr, 1, 0, 1, 1)
        rtrn.attach(bl, 0, 1, 1, 1)
        rtrn.attach(br, 1, 1, 1, 1)





        lfsh = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="lfsh")
        tr = Gtk.Button()
        bl = Gtk.Button(label="lfsh")
        br = Gtk.Button()
        lfsh.attach(tl, 0, 0, 1, 1)
        lfsh.attach(tr, 1, 0, 1, 1)
        lfsh.attach(bl, 0, 1, 1, 1)
        lfsh.attach(br, 1, 1, 1, 1)

        ab01 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label=":")
        tr = Gtk.Button()
        bl = Gtk.Button(label=";")
        br = Gtk.Button()
        ab01.attach(tl, 0, 0, 1, 1)
        ab01.attach(tr, 1, 0, 1, 1)
        ab01.attach(bl, 0, 1, 1, 1)
        ab01.attach(br, 1, 1, 1, 1)

        ab02 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="Q")
        tr = Gtk.Button()
        bl = Gtk.Button(label="q")
        br = Gtk.Button()
        ab02.attach(tl, 0, 0, 1, 1)
        ab02.attach(tr, 1, 0, 1, 1)
        ab02.attach(bl, 0, 1, 1, 1)
        ab02.attach(br, 1, 1, 1, 1)

        ab03 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="J")
        tr = Gtk.Button()
        bl = Gtk.Button(label="j")
        br = Gtk.Button()
        ab03.attach(tl, 0, 0, 1, 1)
        ab03.attach(tr, 1, 0, 1, 1)
        ab03.attach(bl, 0, 1, 1, 1)
        ab03.attach(br, 1, 1, 1, 1)

        ab04 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="K")
        tr = Gtk.Button()
        bl = Gtk.Button(label="k")
        br = Gtk.Button()
        ab04.attach(tl, 0, 0, 1, 1)
        ab04.attach(tr, 1, 0, 1, 1)
        ab04.attach(bl, 0, 1, 1, 1)
        ab04.attach(br, 1, 1, 1, 1)

        ab05 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="X")
        tr = Gtk.Button()
        bl = Gtk.Button(label="x")
        br = Gtk.Button()
        ab05.attach(tl, 0, 0, 1, 1)
        ab05.attach(tr, 1, 0, 1, 1)
        ab05.attach(bl, 0, 1, 1, 1)
        ab05.attach(br, 1, 1, 1, 1)


        ab06 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="B")
        tr = Gtk.Button()
        bl = Gtk.Button(label="b")
        br = Gtk.Button()
        ab06.attach(tl, 0, 0, 1, 1)
        ab06.attach(tr, 1, 0, 1, 1)
        ab06.attach(bl, 0, 1, 1, 1)
        ab06.attach(br, 1, 1, 1, 1)

        ab07 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="M")
        tr = Gtk.Button()
        bl = Gtk.Button(label="m")
        br = Gtk.Button()
        ab07.attach(tl, 0, 0, 1, 1)
        ab07.attach(tr, 1, 0, 1, 1)
        ab07.attach(bl, 0, 1, 1, 1)
        ab07.attach(br, 1, 1, 1, 1)

        ab08 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="W")
        tr = Gtk.Button()
        bl = Gtk.Button(label="w")
        br = Gtk.Button()
        ab08.attach(tl, 0, 0, 1, 1)
        ab08.attach(tr, 1, 0, 1, 1)
        ab08.attach(bl, 0, 1, 1, 1)
        ab08.attach(br, 1, 1, 1, 1)


        ab09 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="V")
        tr = Gtk.Button()
        bl = Gtk.Button(label="v")
        br = Gtk.Button()
        ab09.attach(tl, 0, 0, 1, 1)
        ab09.attach(tr, 1, 0, 1, 1)
        ab09.attach(bl, 0, 1, 1, 1)
        ab09.attach(br, 1, 1, 1, 1)


        ab10 = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="Z")
        tr = Gtk.Button()
        bl = Gtk.Button(label="z")
        br = Gtk.Button()
        ab10.attach(tl, 0, 0, 1, 1)
        ab10.attach(tr, 1, 0, 1, 1)
        ab10.attach(bl, 0, 1, 1, 1)
        ab10.attach(br, 1, 1, 1, 1)


        rtsh = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="ls")
        tr = Gtk.Button()
        bl = Gtk.Button(label="ls")
        br = Gtk.Button()
        rtsh.attach(tl, 0, 0, 1, 1)
        rtsh.attach(tr, 1, 0, 1, 1)
        rtsh.attach(bl, 0, 1, 1, 1)
        rtsh.attach(br, 1, 1, 1, 1)


        lctl = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="lc")
        tr = Gtk.Button()
        bl = Gtk.Button(label="lc")
        br = Gtk.Button()
        lctl.attach(tl, 0, 0, 1, 1)
        lctl.attach(tr, 1, 0, 1, 1)
        lctl.attach(bl, 0, 1, 1, 1)
        lctl.attach(br, 1, 1, 1, 1)


        lwin = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="lw")
        tr = Gtk.Button()
        bl = Gtk.Button(label="")
        br = Gtk.Button()
        lwin.attach(tl, 0, 0, 1, 1)
        lwin.attach(tr, 1, 0, 1, 1)
        lwin.attach(bl, 0, 1, 1, 1)
        lwin.attach(br, 1, 1, 1, 1)

        lalt = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="la")
        tr = Gtk.Button()
        bl = Gtk.Button(label="")
        br = Gtk.Button()
        lalt.attach(tl, 0, 0, 1, 1)
        lalt.attach(tr, 1, 0, 1, 1)
        lalt.attach(bl, 0, 1, 1, 1)
        lalt.attach(br, 1, 1, 1, 1)

        spce = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="SPCE")
        tr = Gtk.Button()
        bl = Gtk.Button(label="")
        br = Gtk.Button()
        spce.attach(tl, 0, 0, 1, 1)
        spce.attach(tr, 1, 0, 1, 1)
        spce.attach(bl, 0, 1, 1, 1)
        spce.attach(br, 1, 1, 1, 1)

        ralt = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="ra")
        tr = Gtk.Button()
        bl = Gtk.Button(label="")
        br = Gtk.Button()
        ralt.attach(tl, 0, 0, 1, 1)
        ralt.attach(tr, 1, 0, 1, 1)
        ralt.attach(bl, 0, 1, 1, 1)
        ralt.attach(br, 1, 1, 1, 1)

        rwin = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="rw")
        tr = Gtk.Button()
        bl = Gtk.Button(label="")
        br = Gtk.Button()
        rwin.attach(tl, 0, 0, 1, 1)
        rwin.attach(tr, 1, 0, 1, 1)
        rwin.attach(bl, 0, 1, 1, 1)
        rwin.attach(br, 1, 1, 1, 1)

        menu = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="me")
        tr = Gtk.Button()
        bl = Gtk.Button(label="")
        br = Gtk.Button()
        menu.attach(tl, 0, 0, 1, 1)
        menu.attach(tr, 1, 0, 1, 1)
        menu.attach(bl, 0, 1, 1, 1)
        menu.attach(br, 1, 1, 1, 1)

        rctl = Gtk.Grid(column_homogeneous=True, row_homogeneous=True)
        tl = Gtk.Button(label="rc")
        tr = Gtk.Button()
        bl = Gtk.Button(label="")
        br = Gtk.Button()
        rctl.attach(tl, 0, 0, 1, 1)
        rctl.attach(tr, 1, 0, 1, 1)
        rctl.attach(bl, 0, 1, 1, 1)
        rctl.attach(br, 1, 1, 1, 1)


        grid1.attach(tlde, 0, 0, 4, 1)
        grid1.attach(ae01, 4, 0, 4, 1)
        grid1.attach(ae02, 8, 0, 4, 1)
        grid1.attach(ae03, 12, 0, 4, 1)
        grid1.attach(ae04, 16, 0, 4, 1)
        grid1.attach(ae05, 20, 0, 4, 1)
        grid1.attach(ae06, 24, 0, 4, 1)
        grid1.attach(ae07, 28, 0, 4, 1)
        grid1.attach(ae08, 32, 0, 4, 1)
        grid1.attach(ae09, 36, 0, 4, 1)
        grid1.attach(ae10, 40, 0, 4, 1)
        grid1.attach(ae11, 44, 0, 4, 1)
        grid1.attach(ae12, 48, 0, 4, 1)
        grid1.attach(bksp, 52, 0, 8, 1)

        grid2.attach(tab, 0, 0, 6, 1)
        grid2.attach(ad01, 6, 0, 4, 1)
        grid2.attach(ad02, 10, 0, 4, 1)
        grid2.attach(ad03, 14, 0, 4, 1)
        grid2.attach(ad04, 18, 0, 4, 1)
        grid2.attach(ad05, 22, 0, 4, 1)
        grid2.attach(ad06, 26, 0, 4, 1)
        grid2.attach(ad07, 30, 0, 4, 1)
        grid2.attach(ad08, 34, 0, 4, 1)
        grid2.attach(ad09, 38, 0, 4, 1)
        grid2.attach(ad10, 42, 0, 4, 1)
        grid2.attach(ad11, 46, 0, 4, 1)
        grid2.attach(ad12, 50, 0, 4, 1)
        grid2.attach(bksl, 54, 0, 6, 1)

        grid3.attach(caps,  0, 0, 7, 1)
        grid3.attach(ac01,  7, 0, 4, 1)
        grid3.attach(ac02, 11, 0, 4, 1)
        grid3.attach(ac03, 15, 0, 4, 1)
        grid3.attach(ac04, 19, 0, 4, 1)
        grid3.attach(ac05, 23, 0, 4, 1)
        grid3.attach(ac06, 27, 0, 4, 1)
        grid3.attach(ac07, 31, 0, 4, 1)
        grid3.attach(ac08, 35, 0, 4, 1)
        grid3.attach(ac09, 39, 0, 4, 1)
        grid3.attach(ac10, 43, 0, 4, 1)
        grid3.attach(ac11, 47, 0, 4, 1)
        grid3.attach(rtrn, 51, 0, 9, 1)


        grid4.attach(lfsh,  0, 0, 9, 1)
        grid4.attach(ab01,  9, 0, 4, 1)
        grid4.attach(ab02, 13, 0, 4, 1)
        grid4.attach(ab03, 17, 0, 4, 1)
        grid4.attach(ab04, 21, 0, 4, 1)
        grid4.attach(ab05, 25, 0, 4, 1)
        grid4.attach(ab06, 29, 0, 4, 1)
        grid4.attach(ab07, 33, 0, 4, 1)
        grid4.attach(ab08, 37, 0, 4, 1)
        grid4.attach(ab09, 41, 0, 4, 1)
        grid4.attach(ab10, 45, 0, 4, 1)
        grid4.attach(rtsh, 49, 0, 11, 1)

        grid5.attach(lctl, 0, 0, 5, 1)
        grid5.attach(lwin, 5, 0, 5, 1)
        grid5.attach(lalt, 10, 0, 5, 1)
        grid5.attach(spce, 15, 0, 25, 1)
        grid5.attach(ralt, 40, 0, 5, 1)
        grid5.attach(rwin, 45, 0, 5, 1)
        grid5.attach(menu, 50, 0, 5, 1)
        grid5.attach(rctl, 55, 0, 5, 1)

        parent.attach(grid1, 0, 0, 1, 1)
        parent.attach(grid2, 0, 1, 1, 1)
        parent.attach(grid3, 0, 2, 1, 1)
        parent.attach(grid4, 0, 3, 1, 1)
        parent.attach(grid5, 0, 4, 1, 1)

"""
        grid1.attach(lctl, 0, 0, 4, 4)
        grid1.attach(lwin, 6, 0, 4, 4)
        grid1.attach(ae02, 8, 0, 4, 4)
        grid1.attach(ae03, 12, 0, 4, 4)
        grid1.attach(ae04, 16, 0, 4, 4)
        grid1.attach(ae05, 20, 0, 4, 4)
        grid1.attach(ae06, 24, 0, 4, 4)
        grid1.attach(ae07, 28, 0, 4, 4)
        grid1.attach(ae08, 32, 0, 4, 4)
        grid1.attach(ae09, 36, 0, 4, 4)
        grid1.attach(ae10, 40, 0, 4, 4)
        grid1.attach(ae11, 44, 0, 4, 4)
        grid1.attach(ae12, 48, 0, 4, 4)
        grid1.attach(bksp, 52, 0, 8, 4)
"""








"""
        grid1.attach(button3,)
        grid1.attach(button4,)
        grid1.attach(button5)
        grid1.attach(button6)
        grid1.attach(button7)
        grid1.attach(button8)
        grid1.attach(button9)
        grid1.attach(button10)
        grid1.attach(button11)
        grid1.attach(button12)
        grid1.attach(button13)
        grid1.attach(button14)
"""


"""
        grid1.add(button1)
        grid1.add(button2)
        grid1.add(button3)
        grid1.add(button4)
        grid1.add(button5)
        grid1.add(button6)
        grid1.add(button7)
        grid1.add(button8)
        grid1.add(button9)
        grid1.add(button10)
        grid1.add(button11)
        grid1.add(button12)
        grid1.add(button13)
        grid1.add(button14)
"""




    #    button1 = Gtk.Button(label="Button 1")
    #    button2 = Gtk.Button(label="Button 2")


    #    table.attach(button1, 4, 5, 0, 15)
    #    button3 = Gtk.Button(label="Button 3")
    #    button4 = Gtk.Button(label="Button 4")
    #    button5 = Gtk.Button(label="Button 5")
    #    button6 = Gtk.Button(label="Button 6")
    #    table.attach(button1,)


    #    table.attach(button2, 1, 3, 0, 1)
    #    table.attach(button3, 0, 1, 1, 3)
    #    table.attach(button4, 1, 3, 1, 2)
    #    table.attach(button5, 1, 2, 2, 3)
    #    table.attach(button6, 2, 3, 2, 3)

win = TableWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()


"""
    builder = Gtk.Builder()
    builder.add_from_file("example.glade")
    window = builder.get_object("window1")
    window.show_all()
"""
"""
    def __init__(self):
        Gtk.Window.__init__(self, title="Stack Demo")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        stack = Gtk.Stack()
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        checkbutton = Gtk.CheckButton("Click me!")
        stack.add_titled(checkbutton, "check", "Check Button")

        label = Gtk.Label()
        label.set_markup("<big>A fancy label</big>")
        stack.add_titled(label, "label", "A label")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)
        """

"""
    def __init__(self):
        Gtk.Window.__init__(self, title="ListBox Demo")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        hbox.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label1 = Gtk.Label("Automatic Date & Time", xalign=0)
        label2 = Gtk.Label("Requires internet access", xalign=0)
        vbox.pack_start(label1, True, True, 0)
        vbox.pack_start(label2, True, True, 0)

        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switch, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Enable Automatic Update", xalign=0)
        check = Gtk.CheckButton()
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(check, False, True, 0)

        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        label = Gtk.Label("Date Format", xalign=0)
        combo = Gtk.ComboBoxText()
        combo.insert(0, "0", "24-hour")
        combo.insert(1, "1", "AM/PM")
        hbox.pack_start(label, True, True, 0)
        hbox.pack_start(combo, False, True, 0)

        listbox.add(row)

"""
"""
#grid window
#Gtk.Grid is a container which arranges its child widgets in rows and columns,
 #but you do not need to specify the dimensions in the constructor. Children are added using Gtk.Grid.attach().
    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Example")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")

        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)
"""

"""

 # first example simple box with buttons
# While with Gtk.Box.pack_start() widgets are positioned from left to right, Gtk.Box.pack_end() positions them from right to left.
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Hello")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Goodbye")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Hello")

    def on_button2_clicked(self, widget):
        print("Goodbye")
"""

"""

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")
"""

"""
        tlde = Gtk.Button(label="`")
        ae01 = Gtk.Button(label="1")
        ae02 = Gtk.Button(label="2")
        ae03 = Gtk.Button(label="3")
        ae04 = Gtk.Button(label="4")
        ae05 = Gtk.Button(label="5")

        ae06 = Gtk.Button(label="6")
        ae07 = Gtk.Button(label="7")
        ae08 = Gtk.Button(label="8")
        ae09 = Gtk.Button(label="9")
        ae10 = Gtk.Button(label="0")
        ae11 = Gtk.Button(label="[")

        ae12 = Gtk.Button(label="]")
        bksp = Gtk.Button(label="backsp")
"""