# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/face_stylizer/proto/face_stylizer_graph_options.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.framework import calculator_options_pb2 as mediapipe_dot_framework_dot_calculator__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2
from mediapipe.tasks.cc.vision.face_landmarker.proto import face_landmarker_graph_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_vision_dot_face__landmarker_dot_proto_dot_face__landmarker__graph__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOmediapipe/tasks/cc/vision/face_stylizer/proto/face_stylizer_graph_options.proto\x12*mediapipe.tasks.vision.face_stylizer.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\x1aSmediapipe/tasks/cc/vision/face_landmarker/proto/face_landmarker_graph_options.proto\"\xbf\x02\n\x18\x46\x61\x63\x65StylizerGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12o\n\x1d\x66\x61\x63\x65_landmarker_graph_options\x18\x02 \x01(\x0b\x32H.mediapipe.tasks.vision.face_landmarker.proto.FaceLandmarkerGraphOptions2s\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xbc\xfa\x86\xf5\x01 \x01(\x0b\x32\x44.mediapipe.tasks.vision.face_stylizer.proto.FaceStylizerGraphOptionsBU\n4com.google.mediapipe.tasks.vision.facestylizer.protoB\x1d\x46\x61\x63\x65StylizerGraphOptionsProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.tasks.cc.vision.face_stylizer.proto.face_stylizer_graph_options_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FACESTYLIZERGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n4com.google.mediapipe.tasks.vision.facestylizer.protoB\035FaceStylizerGraphOptionsProto'
  _globals['_FACESTYLIZERGRAPHOPTIONS']._serialized_start=347
  _globals['_FACESTYLIZERGRAPHOPTIONS']._serialized_end=666
# @@protoc_insertion_point(module_scope)
