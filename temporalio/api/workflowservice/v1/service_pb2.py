# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporal/api/workflowservice/v1/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from temporalio.api.workflowservice.v1 import (
    request_response_pb2 as temporal_dot_api_dot_workflowservice_dot_v1_dot_request__response__pb2,
)

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n-temporal/api/workflowservice/v1/service.proto\x12\x1ftemporal.api.workflowservice.v1\x1a\x36temporal/api/workflowservice/v1/request_response.proto2\x98\x44\n\x0fWorkflowService\x12\x8c\x01\n\x11RegisterNamespace\x12\x39.temporal.api.workflowservice.v1.RegisterNamespaceRequest\x1a:.temporal.api.workflowservice.v1.RegisterNamespaceResponse"\x00\x12\x8c\x01\n\x11\x44\x65scribeNamespace\x12\x39.temporal.api.workflowservice.v1.DescribeNamespaceRequest\x1a:.temporal.api.workflowservice.v1.DescribeNamespaceResponse"\x00\x12\x83\x01\n\x0eListNamespaces\x12\x36.temporal.api.workflowservice.v1.ListNamespacesRequest\x1a\x37.temporal.api.workflowservice.v1.ListNamespacesResponse"\x00\x12\x86\x01\n\x0fUpdateNamespace\x12\x37.temporal.api.workflowservice.v1.UpdateNamespaceRequest\x1a\x38.temporal.api.workflowservice.v1.UpdateNamespaceResponse"\x00\x12\x8f\x01\n\x12\x44\x65precateNamespace\x12:.temporal.api.workflowservice.v1.DeprecateNamespaceRequest\x1a;.temporal.api.workflowservice.v1.DeprecateNamespaceResponse"\x00\x12\x9b\x01\n\x16StartWorkflowExecution\x12>.temporal.api.workflowservice.v1.StartWorkflowExecutionRequest\x1a?.temporal.api.workflowservice.v1.StartWorkflowExecutionResponse"\x00\x12\xaa\x01\n\x1bGetWorkflowExecutionHistory\x12\x43.temporal.api.workflowservice.v1.GetWorkflowExecutionHistoryRequest\x1a\x44.temporal.api.workflowservice.v1.GetWorkflowExecutionHistoryResponse"\x00\x12\xbf\x01\n"GetWorkflowExecutionHistoryReverse\x12J.temporal.api.workflowservice.v1.GetWorkflowExecutionHistoryReverseRequest\x1aK.temporal.api.workflowservice.v1.GetWorkflowExecutionHistoryReverseResponse"\x00\x12\x98\x01\n\x15PollWorkflowTaskQueue\x12=.temporal.api.workflowservice.v1.PollWorkflowTaskQueueRequest\x1a>.temporal.api.workflowservice.v1.PollWorkflowTaskQueueResponse"\x00\x12\xad\x01\n\x1cRespondWorkflowTaskCompleted\x12\x44.temporal.api.workflowservice.v1.RespondWorkflowTaskCompletedRequest\x1a\x45.temporal.api.workflowservice.v1.RespondWorkflowTaskCompletedResponse"\x00\x12\xa4\x01\n\x19RespondWorkflowTaskFailed\x12\x41.temporal.api.workflowservice.v1.RespondWorkflowTaskFailedRequest\x1a\x42.temporal.api.workflowservice.v1.RespondWorkflowTaskFailedResponse"\x00\x12\x98\x01\n\x15PollActivityTaskQueue\x12=.temporal.api.workflowservice.v1.PollActivityTaskQueueRequest\x1a>.temporal.api.workflowservice.v1.PollActivityTaskQueueResponse"\x00\x12\xaa\x01\n\x1bRecordActivityTaskHeartbeat\x12\x43.temporal.api.workflowservice.v1.RecordActivityTaskHeartbeatRequest\x1a\x44.temporal.api.workflowservice.v1.RecordActivityTaskHeartbeatResponse"\x00\x12\xb6\x01\n\x1fRecordActivityTaskHeartbeatById\x12G.temporal.api.workflowservice.v1.RecordActivityTaskHeartbeatByIdRequest\x1aH.temporal.api.workflowservice.v1.RecordActivityTaskHeartbeatByIdResponse"\x00\x12\xad\x01\n\x1cRespondActivityTaskCompleted\x12\x44.temporal.api.workflowservice.v1.RespondActivityTaskCompletedRequest\x1a\x45.temporal.api.workflowservice.v1.RespondActivityTaskCompletedResponse"\x00\x12\xb9\x01\n RespondActivityTaskCompletedById\x12H.temporal.api.workflowservice.v1.RespondActivityTaskCompletedByIdRequest\x1aI.temporal.api.workflowservice.v1.RespondActivityTaskCompletedByIdResponse"\x00\x12\xa4\x01\n\x19RespondActivityTaskFailed\x12\x41.temporal.api.workflowservice.v1.RespondActivityTaskFailedRequest\x1a\x42.temporal.api.workflowservice.v1.RespondActivityTaskFailedResponse"\x00\x12\xb0\x01\n\x1dRespondActivityTaskFailedById\x12\x45.temporal.api.workflowservice.v1.RespondActivityTaskFailedByIdRequest\x1a\x46.temporal.api.workflowservice.v1.RespondActivityTaskFailedByIdResponse"\x00\x12\xaa\x01\n\x1bRespondActivityTaskCanceled\x12\x43.temporal.api.workflowservice.v1.RespondActivityTaskCanceledRequest\x1a\x44.temporal.api.workflowservice.v1.RespondActivityTaskCanceledResponse"\x00\x12\xb6\x01\n\x1fRespondActivityTaskCanceledById\x12G.temporal.api.workflowservice.v1.RespondActivityTaskCanceledByIdRequest\x1aH.temporal.api.workflowservice.v1.RespondActivityTaskCanceledByIdResponse"\x00\x12\xb3\x01\n\x1eRequestCancelWorkflowExecution\x12\x46.temporal.api.workflowservice.v1.RequestCancelWorkflowExecutionRequest\x1aG.temporal.api.workflowservice.v1.RequestCancelWorkflowExecutionResponse"\x00\x12\x9e\x01\n\x17SignalWorkflowExecution\x12?.temporal.api.workflowservice.v1.SignalWorkflowExecutionRequest\x1a@.temporal.api.workflowservice.v1.SignalWorkflowExecutionResponse"\x00\x12\xb9\x01\n SignalWithStartWorkflowExecution\x12H.temporal.api.workflowservice.v1.SignalWithStartWorkflowExecutionRequest\x1aI.temporal.api.workflowservice.v1.SignalWithStartWorkflowExecutionResponse"\x00\x12\x9b\x01\n\x16ResetWorkflowExecution\x12>.temporal.api.workflowservice.v1.ResetWorkflowExecutionRequest\x1a?.temporal.api.workflowservice.v1.ResetWorkflowExecutionResponse"\x00\x12\xa7\x01\n\x1aTerminateWorkflowExecution\x12\x42.temporal.api.workflowservice.v1.TerminateWorkflowExecutionRequest\x1a\x43.temporal.api.workflowservice.v1.TerminateWorkflowExecutionResponse"\x00\x12\x9e\x01\n\x17\x44\x65leteWorkflowExecution\x12?.temporal.api.workflowservice.v1.DeleteWorkflowExecutionRequest\x1a@.temporal.api.workflowservice.v1.DeleteWorkflowExecutionResponse"\x00\x12\xa7\x01\n\x1aListOpenWorkflowExecutions\x12\x42.temporal.api.workflowservice.v1.ListOpenWorkflowExecutionsRequest\x1a\x43.temporal.api.workflowservice.v1.ListOpenWorkflowExecutionsResponse"\x00\x12\xad\x01\n\x1cListClosedWorkflowExecutions\x12\x44.temporal.api.workflowservice.v1.ListClosedWorkflowExecutionsRequest\x1a\x45.temporal.api.workflowservice.v1.ListClosedWorkflowExecutionsResponse"\x00\x12\x9b\x01\n\x16ListWorkflowExecutions\x12>.temporal.api.workflowservice.v1.ListWorkflowExecutionsRequest\x1a?.temporal.api.workflowservice.v1.ListWorkflowExecutionsResponse"\x00\x12\xb3\x01\n\x1eListArchivedWorkflowExecutions\x12\x46.temporal.api.workflowservice.v1.ListArchivedWorkflowExecutionsRequest\x1aG.temporal.api.workflowservice.v1.ListArchivedWorkflowExecutionsResponse"\x00\x12\x9b\x01\n\x16ScanWorkflowExecutions\x12>.temporal.api.workflowservice.v1.ScanWorkflowExecutionsRequest\x1a?.temporal.api.workflowservice.v1.ScanWorkflowExecutionsResponse"\x00\x12\x9e\x01\n\x17\x43ountWorkflowExecutions\x12?.temporal.api.workflowservice.v1.CountWorkflowExecutionsRequest\x1a@.temporal.api.workflowservice.v1.CountWorkflowExecutionsResponse"\x00\x12\x92\x01\n\x13GetSearchAttributes\x12;.temporal.api.workflowservice.v1.GetSearchAttributesRequest\x1a<.temporal.api.workflowservice.v1.GetSearchAttributesResponse"\x00\x12\xa4\x01\n\x19RespondQueryTaskCompleted\x12\x41.temporal.api.workflowservice.v1.RespondQueryTaskCompletedRequest\x1a\x42.temporal.api.workflowservice.v1.RespondQueryTaskCompletedResponse"\x00\x12\x95\x01\n\x14ResetStickyTaskQueue\x12<.temporal.api.workflowservice.v1.ResetStickyTaskQueueRequest\x1a=.temporal.api.workflowservice.v1.ResetStickyTaskQueueResponse"\x00\x12\x80\x01\n\rQueryWorkflow\x12\x35.temporal.api.workflowservice.v1.QueryWorkflowRequest\x1a\x36.temporal.api.workflowservice.v1.QueryWorkflowResponse"\x00\x12\xa4\x01\n\x19\x44\x65scribeWorkflowExecution\x12\x41.temporal.api.workflowservice.v1.DescribeWorkflowExecutionRequest\x1a\x42.temporal.api.workflowservice.v1.DescribeWorkflowExecutionResponse"\x00\x12\x8c\x01\n\x11\x44\x65scribeTaskQueue\x12\x39.temporal.api.workflowservice.v1.DescribeTaskQueueRequest\x1a:.temporal.api.workflowservice.v1.DescribeTaskQueueResponse"\x00\x12\x83\x01\n\x0eGetClusterInfo\x12\x36.temporal.api.workflowservice.v1.GetClusterInfoRequest\x1a\x37.temporal.api.workflowservice.v1.GetClusterInfoResponse"\x00\x12\x80\x01\n\rGetSystemInfo\x12\x35.temporal.api.workflowservice.v1.GetSystemInfoRequest\x1a\x36.temporal.api.workflowservice.v1.GetSystemInfoResponse"\x00\x12\x9e\x01\n\x17ListTaskQueuePartitions\x12?.temporal.api.workflowservice.v1.ListTaskQueuePartitionsRequest\x1a@.temporal.api.workflowservice.v1.ListTaskQueuePartitionsResponse"\x00\x12\x83\x01\n\x0e\x43reateSchedule\x12\x36.temporal.api.workflowservice.v1.CreateScheduleRequest\x1a\x37.temporal.api.workflowservice.v1.CreateScheduleResponse"\x00\x12\x89\x01\n\x10\x44\x65scribeSchedule\x12\x38.temporal.api.workflowservice.v1.DescribeScheduleRequest\x1a\x39.temporal.api.workflowservice.v1.DescribeScheduleResponse"\x00\x12\x83\x01\n\x0eUpdateSchedule\x12\x36.temporal.api.workflowservice.v1.UpdateScheduleRequest\x1a\x37.temporal.api.workflowservice.v1.UpdateScheduleResponse"\x00\x12\x80\x01\n\rPatchSchedule\x12\x35.temporal.api.workflowservice.v1.PatchScheduleRequest\x1a\x36.temporal.api.workflowservice.v1.PatchScheduleResponse"\x00\x12\xa4\x01\n\x19ListScheduleMatchingTimes\x12\x41.temporal.api.workflowservice.v1.ListScheduleMatchingTimesRequest\x1a\x42.temporal.api.workflowservice.v1.ListScheduleMatchingTimesResponse"\x00\x12\x83\x01\n\x0e\x44\x65leteSchedule\x12\x36.temporal.api.workflowservice.v1.DeleteScheduleRequest\x1a\x37.temporal.api.workflowservice.v1.DeleteScheduleResponse"\x00\x12\x80\x01\n\rListSchedules\x12\x35.temporal.api.workflowservice.v1.ListSchedulesRequest\x1a\x36.temporal.api.workflowservice.v1.ListSchedulesResponse"\x00\x12\xaa\x01\n\x1bUpdateWorkerBuildIdOrdering\x12\x43.temporal.api.workflowservice.v1.UpdateWorkerBuildIdOrderingRequest\x1a\x44.temporal.api.workflowservice.v1.UpdateWorkerBuildIdOrderingResponse"\x00\x12\xa1\x01\n\x18GetWorkerBuildIdOrdering\x12@.temporal.api.workflowservice.v1.GetWorkerBuildIdOrderingRequest\x1a\x41.temporal.api.workflowservice.v1.GetWorkerBuildIdOrderingResponse"\x00\x12\x83\x01\n\x0eUpdateWorkflow\x12\x36.temporal.api.workflowservice.v1.UpdateWorkflowRequest\x1a\x37.temporal.api.workflowservice.v1.UpdateWorkflowResponse"\x00\x12\x92\x01\n\x13StartBatchOperation\x12;.temporal.api.workflowservice.v1.StartBatchOperationRequest\x1a<.temporal.api.workflowservice.v1.StartBatchOperationResponse"\x00\x12\x8f\x01\n\x12StopBatchOperation\x12:.temporal.api.workflowservice.v1.StopBatchOperationRequest\x1a;.temporal.api.workflowservice.v1.StopBatchOperationResponse"\x00\x12\x9b\x01\n\x16\x44\x65scribeBatchOperation\x12>.temporal.api.workflowservice.v1.DescribeBatchOperationRequest\x1a?.temporal.api.workflowservice.v1.DescribeBatchOperationResponse"\x00\x12\x92\x01\n\x13ListBatchOperations\x12;.temporal.api.workflowservice.v1.ListBatchOperationsRequest\x1a<.temporal.api.workflowservice.v1.ListBatchOperationsResponse"\x00\x42\xb2\x01\n"io.temporal.api.workflowservice.v1B\x0cServiceProtoP\x01Z5go.temporal.io/api/workflowservice/v1;workflowservice\xaa\x02\x1fTemporal.Api.WorkflowService.V1\xea\x02"Temporal::Api::WorkflowService::V1b\x06proto3'
)


_WORKFLOWSERVICE = DESCRIPTOR.services_by_name["WorkflowService"]
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n"io.temporal.api.workflowservice.v1B\014ServiceProtoP\001Z5go.temporal.io/api/workflowservice/v1;workflowservice\252\002\037Temporal.Api.WorkflowService.V1\352\002"Temporal::Api::WorkflowService::V1'
    _WORKFLOWSERVICE._serialized_start = 139
    _WORKFLOWSERVICE._serialized_end = 8867
# @@protoc_insertion_point(module_scope)
