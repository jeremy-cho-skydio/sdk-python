# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/sdk/core/activity_task/activity_task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from temporalio.bridge.proto.common import (
    common_pb2 as temporal_dot_sdk_dot_core_dot_common_dot_common__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n3temporal/sdk/core/activity_task/activity_task.proto\x12\x15\x63oresdk.activity_task\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a%temporal/sdk/core/common/common.proto"\x8d\x01\n\x0c\x41\x63tivityTask\x12\x12\n\ntask_token\x18\x01 \x01(\x0c\x12-\n\x05start\x18\x03 \x01(\x0b\x32\x1c.coresdk.activity_task.StartH\x00\x12/\n\x06\x63\x61ncel\x18\x04 \x01(\x0b\x32\x1d.coresdk.activity_task.CancelH\x00\x42\t\n\x07variant"\xc5\x06\n\x05Start\x12\x1a\n\x12workflow_namespace\x18\x01 \x01(\t\x12\x15\n\rworkflow_type\x18\x02 \x01(\t\x12=\n\x12workflow_execution\x18\x03 \x01(\x0b\x32!.coresdk.common.WorkflowExecution\x12\x13\n\x0b\x61\x63tivity_id\x18\x04 \x01(\t\x12\x15\n\ractivity_type\x18\x05 \x01(\t\x12\x45\n\rheader_fields\x18\x06 \x03(\x0b\x32..coresdk.activity_task.Start.HeaderFieldsEntry\x12&\n\x05input\x18\x07 \x03(\x0b\x32\x17.coresdk.common.Payload\x12\x32\n\x11heartbeat_details\x18\x08 \x03(\x0b\x32\x17.coresdk.common.Payload\x12\x32\n\x0escheduled_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x42\n\x1e\x63urrent_attempt_scheduled_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cstarted_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x61ttempt\x18\x0c \x01(\r\x12<\n\x19schedule_to_close_timeout\x18\r \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x39\n\x16start_to_close_timeout\x18\x0e \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x34\n\x11heartbeat_timeout\x18\x0f \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x31\n\x0cretry_policy\x18\x10 \x01(\x0b\x32\x1b.coresdk.common.RetryPolicy\x12\x10\n\x08is_local\x18\x11 \x01(\x08\x1aL\n\x11HeaderFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.coresdk.common.Payload:\x02\x38\x01"E\n\x06\x43\x61ncel\x12;\n\x06reason\x18\x01 \x01(\x0e\x32+.coresdk.activity_task.ActivityCancelReason*C\n\x14\x41\x63tivityCancelReason\x12\r\n\tNOT_FOUND\x10\x00\x12\r\n\tCANCELLED\x10\x01\x12\r\n\tTIMED_OUT\x10\x02\x62\x06proto3'
)

_ACTIVITYCANCELREASON = DESCRIPTOR.enum_types_by_name["ActivityCancelReason"]
ActivityCancelReason = enum_type_wrapper.EnumTypeWrapper(_ACTIVITYCANCELREASON)
NOT_FOUND = 0
CANCELLED = 1
TIMED_OUT = 2


_ACTIVITYTASK = DESCRIPTOR.message_types_by_name["ActivityTask"]
_START = DESCRIPTOR.message_types_by_name["Start"]
_START_HEADERFIELDSENTRY = _START.nested_types_by_name["HeaderFieldsEntry"]
_CANCEL = DESCRIPTOR.message_types_by_name["Cancel"]
ActivityTask = _reflection.GeneratedProtocolMessageType(
    "ActivityTask",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACTIVITYTASK,
        "__module__": "temporal.sdk.core.activity_task.activity_task_pb2"
        # @@protoc_insertion_point(class_scope:coresdk.activity_task.ActivityTask)
    },
)
_sym_db.RegisterMessage(ActivityTask)

Start = _reflection.GeneratedProtocolMessageType(
    "Start",
    (_message.Message,),
    {
        "HeaderFieldsEntry": _reflection.GeneratedProtocolMessageType(
            "HeaderFieldsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _START_HEADERFIELDSENTRY,
                "__module__": "temporal.sdk.core.activity_task.activity_task_pb2"
                # @@protoc_insertion_point(class_scope:coresdk.activity_task.Start.HeaderFieldsEntry)
            },
        ),
        "DESCRIPTOR": _START,
        "__module__": "temporal.sdk.core.activity_task.activity_task_pb2"
        # @@protoc_insertion_point(class_scope:coresdk.activity_task.Start)
    },
)
_sym_db.RegisterMessage(Start)
_sym_db.RegisterMessage(Start.HeaderFieldsEntry)

Cancel = _reflection.GeneratedProtocolMessageType(
    "Cancel",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCEL,
        "__module__": "temporal.sdk.core.activity_task.activity_task_pb2"
        # @@protoc_insertion_point(class_scope:coresdk.activity_task.Cancel)
    },
)
_sym_db.RegisterMessage(Cancel)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _START_HEADERFIELDSENTRY._options = None
    _START_HEADERFIELDSENTRY._serialized_options = b"8\001"
    _ACTIVITYCANCELREASON._serialized_start = 1237
    _ACTIVITYCANCELREASON._serialized_end = 1304
    _ACTIVITYTASK._serialized_start = 183
    _ACTIVITYTASK._serialized_end = 324
    _START._serialized_start = 327
    _START._serialized_end = 1164
    _START_HEADERFIELDSENTRY._serialized_start = 1088
    _START_HEADERFIELDSENTRY._serialized_end = 1164
    _CANCEL._serialized_start = 1166
    _CANCEL._serialized_end = 1235
# @@protoc_insertion_point(module_scope)