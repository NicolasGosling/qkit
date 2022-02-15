import string
import numpy as np
from zhinst.toolkit.control.drivers import SHFSG as _SHFSG
from zhinst.toolkit.control.node_tree import Node, Parameter
from qkit.core.instrument_base import Instrument
from qkit.drivers.ZHInst_Abstract import ZHInst_Abstract


class ZHInst_SHFSG(ZHInst_Abstract):
    def __init__(self, name, serialnumber, host="129.13.93.38",  **kwargs):
        super().__init__(name, **kwargs)
        self._shfsg = _SHFSG(name, serialnumber, host=host)
        self._shfsg.setup()
        self._shfsg.connect_device()
        
        # Iterate node tree for readable entries and hook them into QKit
        self.blacklist = ["system_fwlog", "features_code"]
        with open("node_dump_shfsg.txt", "w", encoding="utf-8") as f:
            self._recursive_qkit_hook(self._shfsg.nodetree, f)

        # Register readout methods

    
        
