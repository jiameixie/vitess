# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vtworkerdata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import logutil_pb2 as logutil__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vtworkerdata.proto',
  package='vtworkerdata',
  syntax='proto3',
  serialized_pb=_b('\n\x12vtworkerdata.proto\x12\x0cvtworkerdata\x1a\rlogutil.proto\"-\n\x1d\x45xecuteVtworkerCommandRequest\x12\x0c\n\x04\x61rgs\x18\x01 \x03(\t\"?\n\x1e\x45xecuteVtworkerCommandResponse\x12\x1d\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x0e.logutil.Eventb\x06proto3')
  ,
  dependencies=[logutil__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXECUTEVTWORKERCOMMANDREQUEST = _descriptor.Descriptor(
  name='ExecuteVtworkerCommandRequest',
  full_name='vtworkerdata.ExecuteVtworkerCommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='args', full_name='vtworkerdata.ExecuteVtworkerCommandRequest.args', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=96,
)


_EXECUTEVTWORKERCOMMANDRESPONSE = _descriptor.Descriptor(
  name='ExecuteVtworkerCommandResponse',
  full_name='vtworkerdata.ExecuteVtworkerCommandResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event', full_name='vtworkerdata.ExecuteVtworkerCommandResponse.event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=161,
)

_EXECUTEVTWORKERCOMMANDRESPONSE.fields_by_name['event'].message_type = logutil__pb2._EVENT
DESCRIPTOR.message_types_by_name['ExecuteVtworkerCommandRequest'] = _EXECUTEVTWORKERCOMMANDREQUEST
DESCRIPTOR.message_types_by_name['ExecuteVtworkerCommandResponse'] = _EXECUTEVTWORKERCOMMANDRESPONSE

ExecuteVtworkerCommandRequest = _reflection.GeneratedProtocolMessageType('ExecuteVtworkerCommandRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTEVTWORKERCOMMANDREQUEST,
  __module__ = 'vtworkerdata_pb2'
  # @@protoc_insertion_point(class_scope:vtworkerdata.ExecuteVtworkerCommandRequest)
  ))
_sym_db.RegisterMessage(ExecuteVtworkerCommandRequest)

ExecuteVtworkerCommandResponse = _reflection.GeneratedProtocolMessageType('ExecuteVtworkerCommandResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTEVTWORKERCOMMANDRESPONSE,
  __module__ = 'vtworkerdata_pb2'
  # @@protoc_insertion_point(class_scope:vtworkerdata.ExecuteVtworkerCommandResponse)
  ))
_sym_db.RegisterMessage(ExecuteVtworkerCommandResponse)


import abc
from grpc.beta import implementations as beta_implementations
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
