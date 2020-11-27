### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from minknow_api.protocol_pb2_grpc import *
import minknow_api.protocol_pb2 as protocol_pb2
from minknow_api.protocol_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging
import sys

__all__ = [
    "ProtocolService",
    "BarcodeUserData",
    "ProtocolRunUserInfo",
    "StartProtocolRequest",
    "StartProtocolResponse",
    "StopProtocolRequest",
    "StopProtocolResponse",
    "ListProtocolsRequest",
    "ProtocolInfo",
    "ListProtocolsResponse",
    "WaitForFinishedRequest",
    "GetRunInfoRequest",
    "Epi2meWorkflowReference",
    "ProtocolRunInfo",
    "ListProtocolRunsRequest",
    "ListProtocolRunsResponse",
    "GetCurrentProtocolRunRequest",
    "GetCurrentProtocolRunResponse",
    "WatchCurrentProtocolRunRequest",
    "GetContextInfoRequest",
    "GetContextInfoResponse",
    "SetContextInfoRequest",
    "SetContextInfoResponse",
    "GetProtocolPurposeRequest",
    "GetProtocolPurposeResponse",
    "SetProtocolPurposeRequest",
    "SetProtocolPurposeResponse",
    "AddEpi2meWorkflowRequest",
    "AddEpi2meWorkflowResponse",
    "ListProtocolGroupIdsRequest",
    "ListProtocolGroupIdsResponse",
    "ProtocolState",
    "PROTOCOL_RUNNING",
    "PROTOCOL_WAITING_FOR_TEMPERATURE",
    "PROTOCOL_WAITING_FOR_ACQUISITION",
    "PROTOCOL_COMPLETED",
    "PROTOCOL_STOPPED_BY_USER",
    "PROTOCOL_FINISHED_WITH_ERROR",
    "PROTOCOL_FINISHED_WITH_DEVICE_ERROR",
    "PROTOCOL_FINISHED_UNABLE_TO_SEND_TELEMETRY",
]

def run_with_retry(method, message, timeout, unwraps, full_name):
    retry_count = 20
    error = None
    for i in range(retry_count):
        try:
            result = MessageWrapper(method(message, timeout=timeout), unwraps=unwraps)
            return result
        except grpc.RpcError as e:
            # Retrying unidentified grpc errors to keep clients from crashing
            retryable_error = (e.code() == grpc.StatusCode.UNKNOWN and "Stream removed" in e.details() or \
                                (e.code() == grpc.StatusCode.INTERNAL and "RST_STREAM" in e.details()))
            if retryable_error:
                logging.info('Bypassed ({}: {}) error for grpc: {}. Attempt {}.'.format(e.code(), e.details(), full_name, i))
            else:
                raise
            error = e
        time.sleep(1)
    raise error


class ProtocolService(object):
    def __init__(self, channel):
        self._stub = ProtocolServiceStub(channel)
        self._pb = protocol_pb2
    def start_protocol(self, _message=None, _timeout=None, **kwargs):
        """Initiates a python instance that runs the script specified by the `path` argument.
        `list_protocols` will give back a list of protocol scripts that can be started by this call

        

        Args:
            _message (minknow_api.protocol_pb2.StartProtocolRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            identifier (str): The identifier of the protocol, as provided by list_protocols().
            args (str, optional): The arguments to pass to the protocol.
            user_info (minknow_api.protocol_pb2.ProtocolRunUserInfo, optional): User input describing the protocol.

        Returns:
            minknow_api.protocol_pb2.StartProtocolResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.start_protocol,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = StartProtocolRequest()

        if "identifier" in kwargs:
            unused_args.remove("identifier")
            _message.identifier = kwargs['identifier']
        else:
            raise ArgumentError("start_protocol requires a 'identifier' argument")

        if "args" in kwargs:
            unused_args.remove("args")
            _message.args.extend(kwargs['args'])

        if "user_info" in kwargs:
            unused_args.remove("user_info")
            _message.user_info.CopyFrom(kwargs['user_info'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to start_protocol: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.start_protocol,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def stop_protocol(self, _message=None, _timeout=None, **kwargs):
        """Stops the currently running protocol script instance.

        

        Args:
            _message (minknow_api.protocol_pb2.StopProtocolRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            data_action_on_stop (minknow_api.acquisition_pb2.StopRequest.DataAction, optional): Specify how any running acquisition should
                be handled when stopping the protocol.

                Protocol state will enter PROTOCOL_WAITING_FOR_ACQUISITION whilst any running
                acquisition is finished.

                If a script ends on its own any analysis that was started is stopped, and it
                is allowed to catchup. If the caller wants to end catchup they can call stop_protocol
                to end catchup.

                Since 1.15

        Returns:
            minknow_api.protocol_pb2.StopProtocolResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.stop_protocol,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = StopProtocolRequest()

        if "data_action_on_stop" in kwargs:
            unused_args.remove("data_action_on_stop")
            _message.data_action_on_stop = kwargs['data_action_on_stop']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to stop_protocol: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.stop_protocol,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def wait_for_finished(self, _message=None, _timeout=None, **kwargs):
        """Wait for a protocol run to finish.

        The call blocks until the run with the given run ID has finished (or returns immediately if
        it had already finished) and returns information about the protocol run.

        If no run has been started with the provided run ID (or no run ID is given), an error is
        returned.

        If NOTIFY_BEFORE_TERMINATION is specified for state, the protocol end time is an estimate, including
        the allowed timeout.

        Since 1.10

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.protocol_pb2.WaitForFinishedRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            run_id (str): Only consider a specific protocol run.
            state (minknow_api.protocol_pb2.WaitForFinishedRequest.NotificationState, optional): Control what to wait for.

                Specifying NOTIFY_BEFORE_TERMINATION allows a caller to be notified the script will be ended _soon_,
                and do final work to end cleanly.

                Since 1.11
            timeout (float, optional): Timeout to wait for finished, if the timeout expires before the protocol is complete (in the state requested)
                then the response returns.

                By default the timeout will wait forever.

                Since 1.15

        Returns:
            minknow_api.protocol_pb2.ProtocolRunInfo

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.wait_for_finished,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = WaitForFinishedRequest()

        if "run_id" in kwargs:
            unused_args.remove("run_id")
            _message.run_id = kwargs['run_id']
        else:
            raise ArgumentError("wait_for_finished requires a 'run_id' argument")

        if "state" in kwargs:
            unused_args.remove("state")
            _message.state = kwargs['state']

        if "timeout" in kwargs:
            unused_args.remove("timeout")
            _message.timeout = kwargs['timeout']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to wait_for_finished: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.wait_for_finished,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def get_run_info(self, _message=None, _timeout=None, **kwargs):
        """Gets information about a protocol run.

        If no run ID is provided, information about the most recently started protocol run is
        provided.

        Since 1.10

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.protocol_pb2.GetRunInfoRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            run_id (str, optional): The protocol run to get information about.

        Returns:
            minknow_api.protocol_pb2.ProtocolRunInfo

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_run_info,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = GetRunInfoRequest()

        if "run_id" in kwargs:
            unused_args.remove("run_id")
            _message.run_id = kwargs['run_id']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_run_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_run_info,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def list_protocol_runs(self, _message=None, _timeout=None, **kwargs):
        """List previously started protocol run ids (including any current protocol), in order of starting.

        The returned object can be used to find protocol information with get_run_info.

        Since 1.11

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.protocol_pb2.ListProtocolRunsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.protocol_pb2.ListProtocolRunsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_protocol_runs,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = ListProtocolRunsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_protocol_runs: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_protocol_runs,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def get_current_protocol_run(self, _message=None, _timeout=None, **kwargs):
        """Returns the name and run id of the currently running protocol.

        Will fail with FAILED_PRECONDITION if there is no protocol running

        Since 1.11

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.protocol_pb2.GetCurrentProtocolRunRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.protocol_pb2.ProtocolRunInfo

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_current_protocol_run,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = GetCurrentProtocolRunRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_current_protocol_run: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_current_protocol_run,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def watch_current_protocol_run(self, _message=None, _timeout=None, **kwargs):
        """Returns current protocol run info and streams any changes to the current protocol

        This call can be made even if there is no current protocol running. In this case, the next streamed
        response will be the start of a new protocol instance and you will receive updates for that protocol
        until it finishes

        If a protocol finishes this stream will still continue to run and you will be notified when a new protocol starts

        Since 1.12

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.protocol_pb2.WatchCurrentProtocolRunRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
                Note that this is the time until the call ends, not the time between returned
                messages.

        Returns:
            iter of minknow_api.protocol_pb2.ProtocolRunInfo

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.watch_current_protocol_run,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = WatchCurrentProtocolRunRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to watch_current_protocol_run: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.watch_current_protocol_run,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def list_protocols(self, _message=None, _timeout=None, **kwargs):
        """Gives back a list that contains info about each possible protocol script minknow is aware of.
        This will most likely be used to retrieve a suitable protocol script that can be passed on to `start_protocol`

        Since 1.10

        This RPC is idempotent. It may change the state of the system, but if the requested
        change has already happened, it will not fail because of this, make any additional
        changes or return a different value.

        Args:
            _message (minknow_api.protocol_pb2.ListProtocolsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            force_reload (bool, optional): If this is false, then will try to use the cached value of the protocol list where possible
                (still subject to changes in flow cell).
                If this is true, then will force a reload of the protocol list

                Defaults to false

        Returns:
            minknow_api.protocol_pb2.ListProtocolsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_protocols,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = ListProtocolsRequest()

        if "force_reload" in kwargs:
            unused_args.remove("force_reload")
            _message.force_reload = kwargs['force_reload']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_protocols: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_protocols,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def get_context_info(self, _message=None, _timeout=None, **kwargs):
        """Returns string-to-string map of the context tags

        Since 1.11

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.protocol_pb2.GetContextInfoRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.protocol_pb2.GetContextInfoResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_context_info,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = GetContextInfoRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_context_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_context_info,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def set_context_info(self, _message=None, _timeout=None, **kwargs):
        """Store context tags as arbitary string-to-string map

        Since 1.11

        This RPC is idempotent. It may change the state of the system, but if the requested
        change has already happened, it will not fail because of this, make any additional
        changes or return a different value.

        Args:
            _message (minknow_api.protocol_pb2.SetContextInfoRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            context_info (minknow_api.protocol_pb2.SetContextInfoRequest.ContextInfoEntry, optional): 

        Returns:
            minknow_api.protocol_pb2.SetContextInfoResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_context_info,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = SetContextInfoRequest()

        if "context_info" in kwargs:
            unused_args.remove("context_info")
            _message.context_info.update(kwargs['context_info'])
            

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_context_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_context_info,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def get_protocol_purpose(self, _message=None, _timeout=None, **kwargs):
        """Value set by protocol scripts to define the purpose of the script. Gets this value

        Since 1.11

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.protocol_pb2.GetProtocolPurposeRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.protocol_pb2.GetProtocolPurposeResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_protocol_purpose,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = GetProtocolPurposeRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_protocol_purpose: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_protocol_purpose,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def set_protocol_purpose(self, _message=None, _timeout=None, **kwargs):
        """Sets the protocol purpose. See also get_protocol_purpose

        Since 1.11

        This RPC is idempotent. It may change the state of the system, but if the requested
        change has already happened, it will not fail because of this, make any additional
        changes or return a different value.

        Args:
            _message (minknow_api.protocol_pb2.SetProtocolPurposeRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            purpose (str, optional): 

        Returns:
            minknow_api.protocol_pb2.SetProtocolPurposeResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_protocol_purpose,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = SetProtocolPurposeRequest()

        if "purpose" in kwargs:
            unused_args.remove("purpose")
            _message.purpose = kwargs['purpose']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_protocol_purpose: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_protocol_purpose,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def add_epi2me_workflow(self, _message=None, _timeout=None, **kwargs):
        """Links an epi2me workflow reference to a run id.

        Since 1.15

        

        Args:
            _message (minknow_api.protocol_pb2.AddEpi2meWorkflowRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            run_id (str): 
            epi2me_workflow (minknow_api.protocol_pb2.Epi2meWorkflowReference): 

        Returns:
            minknow_api.protocol_pb2.AddEpi2meWorkflowResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.add_epi2me_workflow,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = AddEpi2meWorkflowRequest()

        if "run_id" in kwargs:
            unused_args.remove("run_id")
            _message.run_id = kwargs['run_id']
        else:
            raise ArgumentError("add_epi2me_workflow requires a 'run_id' argument")

        if "epi2me_workflow" in kwargs:
            unused_args.remove("epi2me_workflow")
            _message.epi2me_workflow.CopyFrom(kwargs['epi2me_workflow'])
        else:
            raise ArgumentError("add_epi2me_workflow requires a 'epi2me_workflow' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to add_epi2me_workflow: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.add_epi2me_workflow,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
    def list_protocol_group_ids(self, _message=None, _timeout=None, **kwargs):
        """List all used protocol group ids used in any previous protocol on the box.

        Since 3.2

        This RPC has no side effects. Calling it will have no effect on the state of the
        system. It is safe to call repeatedly, or to retry on failure, although there is no
        guarantee it will return the same information each time.

        Args:
            _message (minknow_api.protocol_pb2.ListProtocolGroupIdsRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.

        Returns:
            minknow_api.protocol_pb2.ListProtocolGroupIdsResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.list_protocol_group_ids,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.protocol.ProtocolService")

        unused_args = set(kwargs.keys())

        _message = ListProtocolGroupIdsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to list_protocol_group_ids: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.list_protocol_group_ids,
                              _message, _timeout,
                              [],
                              "minknow_api.protocol.ProtocolService")
