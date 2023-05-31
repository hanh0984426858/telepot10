# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/image/image_transformation_calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.calculators.image import rotation_mode_pb2 as mediapipe_dot_calculators_dot_image_dot_rotation__mode__pb2
from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2
from mediapipe.gpu import scale_mode_pb2 as mediapipe_dot_gpu_dot_scale__mode__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAmediapipe/calculators/image/image_transformation_calculator.proto\x12\tmediapipe\x1a/mediapipe/calculators/image/rotation_mode.proto\x1a$mediapipe/framework/calculator.proto\x1a\x1emediapipe/gpu/scale_mode.proto\"\x88\x04\n$ImageTransformationCalculatorOptions\x12\x17\n\x0coutput_width\x18\x01 \x01(\x05:\x01\x30\x12\x18\n\routput_height\x18\x02 \x01(\x05:\x01\x30\x12\x33\n\rrotation_mode\x18\x03 \x01(\x0e\x32\x1c.mediapipe.RotationMode.Mode\x12\x1e\n\x0f\x66lip_vertically\x18\x04 \x01(\x08:\x05\x66\x61lse\x12 \n\x11\x66lip_horizontally\x18\x05 \x01(\x08:\x05\x66\x61lse\x12-\n\nscale_mode\x18\x06 \x01(\x0e\x32\x19.mediapipe.ScaleMode.Mode\x12\x1e\n\x10\x63onstant_padding\x18\x07 \x01(\x08:\x04true\x12L\n\rpadding_color\x18\x08 \x01(\x0b\x32\x35.mediapipe.ImageTransformationCalculatorOptions.Color\x1a:\n\x05\x43olor\x12\x0e\n\x03red\x18\x01 \x01(\x05:\x01\x30\x12\x10\n\x05green\x18\x02 \x01(\x05:\x01\x30\x12\x0f\n\x04\x62lue\x18\x03 \x01(\x05:\x01\x30\x32]\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xbe\xfd\x91x \x01(\x0b\x32/.mediapipe.ImageTransformationCalculatorOptionsBR\n%com.google.mediapipe.calculator.protoB)ImageTransformationCalculatorOptionsProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.calculators.image.image_transformation_calculator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_IMAGETRANSFORMATIONCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%com.google.mediapipe.calculator.protoB)ImageTransformationCalculatorOptionsProto'
  _globals['_IMAGETRANSFORMATIONCALCULATOROPTIONS']._serialized_start=200
  _globals['_IMAGETRANSFORMATIONCALCULATOROPTIONS']._serialized_end=720
  _globals['_IMAGETRANSFORMATIONCALCULATOROPTIONS_COLOR']._serialized_start=567
  _globals['_IMAGETRANSFORMATIONCALCULATOROPTIONS_COLOR']._serialized_end=625
# @@protoc_insertion_point(module_scope)
