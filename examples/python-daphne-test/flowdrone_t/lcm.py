"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class lcm(object):
    __slots__ = ["timestamp", "drone_state", "thrust_sp", "body_rate_sp", "wind_magnitude_estimate", "wind_angle_estimate"]

    __typenames__ = ["int64_t", "double", "double", "double", "double", "double"]

    __dimensions__ = [None, [20], None, [3], None, None]

    def __init__(self):
        self.timestamp = 0
        self.drone_state = [ 0.0 for dim0 in range(20) ]
        self.thrust_sp = 0.0
        self.body_rate_sp = [ 0.0 for dim0 in range(3) ]
        self.wind_magnitude_estimate = 0.0
        self.wind_angle_estimate = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(lcm._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.timestamp))
        buf.write(struct.pack('>20d', *self.drone_state[:20]))
        buf.write(struct.pack(">d", self.thrust_sp))
        buf.write(struct.pack('>3d', *self.body_rate_sp[:3]))
        buf.write(struct.pack(">dd", self.wind_magnitude_estimate, self.wind_angle_estimate))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != lcm._get_packed_fingerprint():
            raise ValueError("Decode error")
        return lcm._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = lcm()
        self.timestamp = struct.unpack(">q", buf.read(8))[0]
        self.drone_state = struct.unpack('>20d', buf.read(160))
        self.thrust_sp = struct.unpack(">d", buf.read(8))[0]
        self.body_rate_sp = struct.unpack('>3d', buf.read(24))
        self.wind_magnitude_estimate, self.wind_angle_estimate = struct.unpack(">dd", buf.read(16))
        return self
    _decode_one = staticmethod(_decode_one)

    def _get_hash_recursive(parents):
        if lcm in parents: return 0
        tmphash = (0xbc09720274796d43) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if lcm._packed_fingerprint is None:
            lcm._packed_fingerprint = struct.pack(">Q", lcm._get_hash_recursive([]))
        return lcm._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

    def get_hash(self):
        """Get the LCM hash of the struct"""
        return struct.unpack(">Q", lcm._get_packed_fingerprint())[0]

