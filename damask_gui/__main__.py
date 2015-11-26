#!/usr/bin/env python
progname="DAMASK GUI"
__copyright__ = "Copyright (C) 2015 Mingxuan Lin \n"

__license__   = """
DAMASK_GUI License Agreement (MIT License)
------------------------------------------

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import sys
from . import QtGui, ApplicationWindow
from  .plugin import stdout_parser as sp
from  .plugin import plotdat as pd

if __name__ == "__main__":
    #show_example(progname)

    qApp = QtGui.QApplication(sys.argv)

    # 'creating ApplicationWindow ...'
    m = sp.SO_Reader()
    aw = ApplicationWindow( [ m , pd.PlotXY(m)] )
    aw.setWindowTitle("DAMASK_GUI")

    # 'show window'
    aw.show()
    sys.exit(qApp.exec_()) # execute the window/app.