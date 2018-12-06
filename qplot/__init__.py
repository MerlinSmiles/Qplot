
import qcodes

from qplot.data.data_set import DataSet
from qplot.plot.RemotePlot import Plot


qcodes.DataSet = DataSet
qcodes.data.data_set.DataSet = DataSet