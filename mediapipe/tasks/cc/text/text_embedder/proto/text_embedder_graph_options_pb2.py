# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/text/text_embedder/proto/text_embedder_graph_options.proto
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
from mediapipe.tasks.cc.components.processors.proto import embedder_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_components_dot_processors_dot_proto_dot_embedder__options__pb2
from mediapipe.tasks.cc.core.proto import base_options_pb2 as mediapipe_dot_tasks_dot_cc_dot_core_dot_proto_dot_base__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMmediapipe/tasks/cc/text/text_embedder/proto/text_embedder_graph_options.proto\x12(mediapipe.tasks.text.text_embedder.proto\x1a$mediapipe/framework/calculator.proto\x1a,mediapipe/framework/calculator_options.proto\x1a\x45mediapipe/tasks/cc/components/processors/proto/embedder_options.proto\x1a\x30mediapipe/tasks/cc/core/proto/base_options.proto\"\xa4\x02\n\x18TextEmbedderGraphOptions\x12=\n\x0c\x62\x61se_options\x18\x01 \x01(\x0b\x32\'.mediapipe.tasks.core.proto.BaseOptions\x12V\n\x10\x65mbedder_options\x18\x02 \x01(\x0b\x32<.mediapipe.tasks.components.processors.proto.EmbedderOptions2q\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x84\xe3\xdd\xe3\x01 \x01(\x0b\x32\x42.mediapipe.tasks.text.text_embedder.proto.TextEmbedderGraphOptionsBS\n2com.google.mediapipe.tasks.text.textembedder.protoB\x1dTextEmbedderGraphOptionsProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.tasks.cc.text.text_embedder.proto.text_embedder_graph_options_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TEXTEMBEDDERGRAPHOPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n2com.google.mediapipe.tasks.text.textembedder.protoB\035TextEmbedderGraphOptionsProto'
  _globals['_TEXTEMBEDDERGRAPHOPTIONS']._serialized_start=329
  _globals['_TEXTEMBEDDERGRAPHOPTIONS']._serialized_end=621
# @@protoc_insertion_point(module_scope)
