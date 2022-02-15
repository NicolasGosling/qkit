import string
import numpy as np
from zhinst.toolkit.control.drivers import UHFQA as _UHFQA
from zhinst.toolkit.control.node_tree import Node, Parameter
from qkit.core.instrument_base import Instrument
from qkit.drivers.ZHInst_Abstract import ZHInst_Abstract


class ZHInst_UHFQA(ZHInst_Abstract):
    def __init__(self, name, serialnumber, host="129.13.93.38",  **kwargs):
        super().__init__(name, **kwargs)
        self._uhfqa = _UHFQA(name, serialnumber, host=host)
        self._uhfqa.setup()
        self._uhfqa.connect_device()
        
        # Iterate node tree for readable entries and hook them into QKit
        self.blacklist = ["awg_sequencer", "awg_waveform", "awg_elf", "awg_dio", "elf", "qa_result_statistics",
                          "scope_wave", "auxin_sample", "dio_input", "system_fwlog", "features_code"]
        with open("node_dump_uhfqa.txt", "w", encoding="utf-8") as f:
            self._recursive_qkit_hook(self._uhfqa.nodetree, f)

        # Register readout methods
        self.add_function("get_qubit_result", channels=(0, 9))
        self.add_function("enable_channel", channels=(0, 9))
        self.add_function("disable_channel", channels=(0, 9))
        self.add_function("arm")
        self.add_function("compile_program")
        self.add_function("run")
        self.add_parameter("readout_frequency", flags=Instrument.FLAG_GETSET, channels=(0, 9), type=float)
        self.add_parameter("readout_amplitude", flags=Instrument.FLAG_GETSET, channels=(0, 9), type=float)

    def compile_program(self, *args, **kwargs):
        self._uhfqa.awg.set_sequence_params(*args, **kwargs)
        self._uhfqa.awg.compile()

    def get_qubit_result(self, channel=None):
        if channel == None: # FIXME: Register this correctly in QKit?
            return [self._uhfqa.channels[i].result() for i in range(10)]
        return self._uhfqa.channels[channel].result()

    def enable_channel(self, channel):
        self._uhfqa.channels[channel].enable()

    def disable_channel(self, channel):
        self._uhfqa.channels[channel].disable()

    def arm(self, *args, **kwargs):
        self._uhfqa.arm(*args, **kwargs)

    def run(self):
        self._uhfqa.awg.run()

    def _do_set_readout_frequency(self, frequency, channel):
        self._uhfqa.channels[channel].readout_frequency(frequency)

    def _do_set_readout_amplitude(self, amplitude, channel):
        self._uhfqa.channels[channel].readout_frequency(amplitude)

    def _do_get_readout_frequency(self, channel):
        return self._uhfqa.channels[channel].readout_frequency()

    def _do_get_readout_amplitude(self, channel):
        return self._uhfqa.channels[channel].readout_frequency()
    
        
