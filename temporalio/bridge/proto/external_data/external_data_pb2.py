# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/sdk/core/external_data/external_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n3temporal/sdk/core/external_data/external_data.proto\x12\x15\x63oresdk.external_data\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfe\x01\n\x17LocalActivityMarkerData\x12\x0b\n\x03seq\x18\x01 \x01(\r\x12\x0f\n\x07\x61ttempt\x18\x02 \x01(\r\x12\x13\n\x0b\x61\x63tivity_id\x18\x03 \x01(\t\x12\x15\n\ractivity_type\x18\x04 \x01(\t\x12\x31\n\rcomplete_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x07\x62\x61\x63koff\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x12:\n\x16original_schedule_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3'
)


_LOCALACTIVITYMARKERDATA = DESCRIPTOR.message_types_by_name["LocalActivityMarkerData"]
LocalActivityMarkerData = _reflection.GeneratedProtocolMessageType(
    "LocalActivityMarkerData",
    (_message.Message,),
    {
        "DESCRIPTOR": _LOCALACTIVITYMARKERDATA,
        "__module__": "temporal.sdk.core.external_data.external_data_pb2"
        # @@protoc_insertion_point(class_scope:coresdk.external_data.LocalActivityMarkerData)
    },
)
_sym_db.RegisterMessage(LocalActivityMarkerData)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _LOCALACTIVITYMARKERDATA._serialized_start = 144
    _LOCALACTIVITYMARKERDATA._serialized_end = 398
# @@protoc_insertion_point(module_scope)
