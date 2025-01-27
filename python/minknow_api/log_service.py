### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from minknow_api.log_pb2_grpc import *
import minknow_api.log_pb2 as log_pb2
from minknow_api.log_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging
import sys

__all__ = [
    "LogService",
    "GetUserMessagesRequest",
    "UserMessage",
    "SendUserMessageRequest",
    "SendUserMessageResponse",
    "SendPingRequest",
    "SendPingResponse",
    "Severity",
    "MESSAGE_SEVERITY_TRACE",
    "MESSAGE_SEVERITY_INFO",
    "MESSAGE_SEVERITY_WARNING",
    "MESSAGE_SEVERITY_ERROR",
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


class LogService(object):
    def __init__(self, channel):
        self._stub = LogServiceStub(channel)
        self._pb = log_pb2
    def get_user_messages(self, _message=None, _timeout=None, **kwargs):
        """Get a stream of user messages, updated with new messages as the are emitted in minknow.

        Since 1.11

        

        Args:
            _message (minknow_api.log_pb2.GetUserMessagesRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
                Note that this is the time until the call ends, not the time between returned
                messages.
            include_old_messages (bool, optional): If set, any messages which have already been sent to listeners
                will be sent to the new stream again, before new messages are sent.

                If not specified - the default will not send messages that were sent previously.

                note: there is a limit on how many messages are recorded for replay.

        Returns:
            iter of minknow_api.log_pb2.UserMessage

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_user_messages,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.log.LogService")

        unused_args = set(kwargs.keys())

        _message = GetUserMessagesRequest()

        if "include_old_messages" in kwargs:
            unused_args.remove("include_old_messages")
            _message.include_old_messages = kwargs['include_old_messages']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_user_messages: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_user_messages,
                              _message, _timeout,
                              [],
                              "minknow_api.log.LogService")
    def send_user_message(self, _message=None, _timeout=None, **kwargs):
        """Send a log message to any listeners of messages (see get_user_messages)

        Any historical user messages are first sent to the caller,

        Since 1.11

        

        Args:
            _message (minknow_api.log_pb2.SendUserMessageRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            severity (minknow_api.log_pb2.Severity): The severity of the message to send

                note: TRACE messages cannot be sent using this interface (will throw an error).
            identifier (str, optional): A short unique textual identifier for the message
                Used to identify the message for translation purposes
            user_message (str): The user message to send to any listeners.
            extra_data (minknow_api.log_pb2.SendUserMessageRequest.ExtraDataEntry, optional): Any extra data associated with the user message, as a map from key to data.

        Returns:
            minknow_api.log_pb2.SendUserMessageResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.send_user_message,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.log.LogService")

        unused_args = set(kwargs.keys())

        _message = SendUserMessageRequest()

        if "severity" in kwargs:
            unused_args.remove("severity")
            _message.severity = kwargs['severity']
        else:
            raise ArgumentError("send_user_message requires a 'severity' argument")

        if "identifier" in kwargs:
            unused_args.remove("identifier")
            _message.identifier = kwargs['identifier']

        if "user_message" in kwargs:
            unused_args.remove("user_message")
            _message.user_message = kwargs['user_message']
        else:
            raise ArgumentError("send_user_message requires a 'user_message' argument")

        if "extra_data" in kwargs:
            unused_args.remove("extra_data")
            _message.extra_data.update(kwargs['extra_data'])
            

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to send_user_message: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.send_user_message,
                              _message, _timeout,
                              [],
                              "minknow_api.log.LogService")
    def send_ping(self, _message=None, _timeout=None, **kwargs):
        """Send a ping to the configured ping server (see system config for ping server url)

        The tracking_id and context_data section of the ping are filled in automatically by MinKNOW.

        The ping is queued internally for sending immediately, if MinKNOW fails to send the message it
        stores the message to send when possible.

        Since 1.11

        

        Args:
            _message (minknow_api.log_pb2.SendPingRequest, optional): The message to send.
                This can be passed instead of the keyword arguments.
            _timeout (float, optional): The call will be cancelled after this number of seconds
                if it has not been completed.
            ping_data (str): The json data to send as a ping.

                note: if this string is not a valid json object, an error will be raised.

        Returns:
            minknow_api.log_pb2.SendPingResponse

        Note that the returned messages are actually wrapped in a type that collapses
        submessages for fields marked with ``[rpc_unwrap]``.
        """
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.send_ping,
                                  _message, _timeout,
                                  [],
                                  "minknow_api.log.LogService")

        unused_args = set(kwargs.keys())

        _message = SendPingRequest()

        if "ping_data" in kwargs:
            unused_args.remove("ping_data")
            _message.ping_data = kwargs['ping_data']
        else:
            raise ArgumentError("send_ping requires a 'ping_data' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to send_ping: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.send_ping,
                              _message, _timeout,
                              [],
                              "minknow_api.log.LogService")
