"""
Main Pathway Device Class
=========================
"""

__all__ = ['Pathway']
__author__ = ["Cosan Lab"]
__license__ = "MIT"
import socket
import time
import numpy as np
from collections import OrderedDict


class Pathway:
    """
    Pathway is a class to communicate with the Medoc Pathway thermal stimulation machine.

    Args:
        ip (str): device ip address
        port_number (int): port the device is listening on
        timeout (float): seconds until connection timeouts; default 5s
        verbose (bool): flag whether to print responses; default True
        buffer_size (int): size of connection buffer; default 1024
    """

    def __init__(self, ip, port_number, timeout=5.0, verbose=True, buffer_size=1024):
        assert isinstance(ip, str), "IP address must be a string."
        assert isinstance(port_number, int), "Port must be an integer."

        self.ip = ip
        self.port_number = port_number
        self.BUFFER_SIZE = buffer_size
        self.timeout = timeout
        self.verbose = verbose
        self.socket = None
        self.test_states = {
            0: 'IDLE',
            1: 'RUNNING',
            2: 'PAUSED',
            3: 'READY'
        }
        self.state_codes = {
            0: 'IDLE',
            1: 'READY',
            2: 'TEST'
        }
        self.command_codes = {
            0: 'STATUS',
            1: 'TEST_PROGRAM',
            2: 'START',
            3: 'PAUSE',
            4: 'TRIGGER',
            5: 'STOP',
            6: 'ABORT',
            7: 'YES',
            8: 'NO'
        }
        self.response_codes = {
            0: 'RESULT_OK',
            1: 'RESULT_ILLEGAL_ARG',
            2: 'RESULT_ILLEGAL_STATE',
            3: 'RESULT_ILLEGAL_TEST_STATE',
            4096: 'RESULT_DEVICE_COMM_ERROR',
            8192: 'RESULT_SAFETY_WARNING',
            16384: 'RESULT_SAFETY_ERROR'
        }
        self.segmentation_points = OrderedDict({
            'LENGTH_OFFSET': (0, 4),
            'TIMESTAMP_OFFSET': (4, 8),
            'COMMAND_OFFSET': 8,
            'SYSTEM_STATE_OFFSET': 9,
            'TEST_STATE_OFFSET': 10,
            'RESULT_OFFSET': (11, 13),
            'TEST_TIME_OFFSET': (13, 17),
            'ERROR_MESSAGE_OFFSET': 17
        })
        try:
            _ = self.call('STATUS', verbose=False)
            print('Connection to Pathway successful')
        except Exception as e:
            raise IOError(f"Cannot establish connection, check IP and port number: {e}")

    def _create_connection(self):
        """Create and return new socket connection"""
        socket.setdefaulttimeout(self.timeout)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.ip, self.port_number))
        return s

    def call(self, command, protocol=None, reuse_socket=False, verbose=False):
        """Send command to device."""
        if reuse_socket:
            raise NotImplementedError("Reusing sockets does not currently work.")

        s = self._create_connection()
        self.socket = s

        if isinstance(command, str):
            command = list(self.command_codes.keys())[list(self.command_codes.values()).index(command)]

        if command == 1 and protocol is None:
            raise ValueError('TEST_PROGRAM command requires a protocol number')

        MESSAGE = self._format_command(command, protocol)
        s.send(MESSAGE)
        time.sleep(0.5)
        data = s.recv(self.BUFFER_SIZE)

        response = self._format_response(data)
        if not response:
            return self.call(command, protocol, verbose=verbose)

        if verbose or self.verbose:
            print(response)

        return response

    def _format_command(self, command, protocol):
        """Format calls to device."""
        bin32 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(32)]))

        curtime = bin32(int(time.time()))
        timelist = [int(curtime[i*8:(i+1)*8], 2) for i in range(4)]
        timelist.reverse()

        cmd = [command]

        protocollist = []
        if command == 1 and protocol:
            protocol_bin = bin32(protocol)
            protocollist = [int(protocol_bin[i*8:(i+1)*8], 2) for i in range(4)]
            protocollist.reverse()

        MESSAGE = timelist + cmd + protocollist

        sizelist = [int(bin32(len(MESSAGE))[i*8:(i+1)*8], 2) for i in range(4)]
        sizelist.reverse()

        MESSAGE = np.array(sizelist + MESSAGE, dtype=np.uint8).tobytes()
        return MESSAGE

    def _format_response(self, data):
        """Format responses from device."""
        data_int = [int.from_bytes(bytes([elem]), 'big') for elem in data]

        response_dict = {}
        try:
            response_dict['response_length'] = self._decode(data_int, 'LENGTH_OFFSET')
            response_dict['time_stamp'] = time.ctime(self._decode(data_int, 'TIMESTAMP_OFFSET'))
            response_dict['command_id'] = self.command_codes[data_int[self.segmentation_points['COMMAND_OFFSET']]]
            response_dict['pathway_state'] = self.state_codes[data_int[self.segmentation_points['SYSTEM_STATE_OFFSET']]]
            response_dict['test_state'] = self.test_states[data_int[self.segmentation_points['TEST_STATE_OFFSET']]]
            response_dict['response'] = self.response_codes[self._decode(data_int, 'RESULT_OFFSET')]
            response_dict['test_time_stamp'] = self._decode_test_time(data_int)

            if response_dict['response_length'] > 13:
                response_dict['error_message'] = data[self.segmentation_points['ERROR_MESSAGE_OFFSET']:]
        except Exception as e:
            print(f"ERROR FORMATTING RESPONSE: {e}")
            print(f"data_int: {data_int}")
            print(f"data: {data}")

        return response_dict

    def _decode(self, data_int, whichtime):
        """Helper function to decode response."""
        bin8 = lambda x: ''.join(reversed([str((x >> i) & 1) for i in range(8)]))
        dat_int = data_int[self.segmentation_points[whichtime][0]:self.segmentation_points[whichtime][1]]
        dat_bin = [bin8(d) for d in dat_int]
        dat_bin.reverse()
        return int("".join(dat_bin), 2)

    def _decode_test_time(self, data_int):
        """Helper function to decode response time."""
        test_time = self._decode(data_int, 'TEST_TIME_OFFSET')

        hours = test_time // 3600000
        mins = (test_time % 3600000) // 60000
        secs = (test_time % 60000) // 1000
        msecs = test_time % 1000
        return f'{hours:02}:{mins:02}:{secs:02}.{msecs:03}'

    # Convenience wrappers
    def status(self):
        return self.call('STATUS')

    def program(self, protocol):
        return self.call('TEST_PROGRAM', protocol=protocol)

    def start(self):
        return self.call('START')

    def pause(self):
        return self.call('PAUSE')

    def trigger(self):
        return self.call('TRIGGER')

    def stop(self):
        return self.call('STOP')

    def abort(self):
        return self.call('ABORT')

    def yes(self):
        return self.call('YES')

    def no(self):
        return self.call('NO')
