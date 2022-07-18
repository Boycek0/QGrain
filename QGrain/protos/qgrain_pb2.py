# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qgrain.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cqgrain.proto\"=\n\x06Sample\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63lasses\x18\x02 \x03(\x02\x12\x14\n\x0c\x64istribution\x18\x03 \x03(\x02\"{\n\x07\x44\x61taset\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tn_samples\x18\x02 \x01(\x05\x12\x11\n\tn_classes\x18\x03 \x01(\x05\x12\x14\n\x0csample_names\x18\x04 \x03(\t\x12\x0f\n\x07\x63lasses\x18\x05 \x03(\x02\x12\x15\n\rdistributions\x18\x06 \x01(\x0c\"\x15\n\x13ServiceStateRequest\"|\n\x14ServiceStateResponse\x12\x13\n\x0bmax_workers\x18\x01 \x01(\x05\x12\x1a\n\x12max_message_length\x18\x02 \x01(\x05\x12\x19\n\x11\x61vailable_devices\x18\t \x03(\t\x12\x18\n\x10max_dataset_size\x18\n \x01(\x05\"/\n\x12StatisticalRequest\x12\x19\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32\x08.Dataset\"\x8f\x03\n\x15StatisticalParameters\x12\x0e\n\x06method\x18\x01 \x01(\t\x12\x0c\n\x04mean\x18\x02 \x01(\x02\x12\x0b\n\x03std\x18\x03 \x01(\x02\x12\x10\n\x08skewness\x18\x04 \x01(\x02\x12\x10\n\x08kurtosis\x18\x05 \x01(\x02\x12\x13\n\x06median\x18\x06 \x01(\x02H\x00\x88\x01\x01\x12\x11\n\x04mode\x18\x07 \x01(\x02H\x01\x88\x01\x01\x12\r\n\x05modes\x18\x08 \x03(\x02\x12\x1d\n\x10mean_description\x18\t \x01(\tH\x02\x88\x01\x01\x12\x1c\n\x0fstd_description\x18\n \x01(\tH\x03\x88\x01\x01\x12!\n\x14skewness_description\x18\x0b \x01(\tH\x04\x88\x01\x01\x12!\n\x14kurtosis_description\x18\x0c \x01(\tH\x05\x88\x01\x01\x42\t\n\x07_medianB\x07\n\x05_modeB\x13\n\x11_mean_descriptionB\x12\n\x10_std_descriptionB\x17\n\x15_skewness_descriptionB\x17\n\x15_kurtosis_description\"\xac\x05\n\x11StatisticalResult\x12/\n\narithmetic\x18\x01 \x01(\x0b\x32\x16.StatisticalParametersH\x00\x88\x01\x01\x12.\n\tgeometric\x18\x02 \x01(\x0b\x32\x16.StatisticalParametersH\x01\x88\x01\x01\x12\x30\n\x0blogarithmic\x18\x03 \x01(\x0b\x32\x16.StatisticalParametersH\x02\x88\x01\x01\x12\x33\n\x0egeometric_fw57\x18\x04 \x01(\x0b\x32\x16.StatisticalParametersH\x03\x88\x01\x01\x12\x35\n\x10logarithmic_fw57\x18\x05 \x01(\x0b\x32\x16.StatisticalParametersH\x04\x88\x01\x01\x12\x17\n\x0fproportions_gsm\x18\x06 \x03(\x02\x12\x17\n\x0fproportions_ssc\x18\x07 \x03(\x02\x12\x19\n\x11proportions_bgssc\x18\x08 \x03(\x02\x12\x38\n\x0bproportions\x18\t \x03(\x0b\x32#.StatisticalResult.ProportionsEntry\x12\x19\n\x0cgroup_folk54\x18\n \x01(\tH\x05\x88\x01\x01\x12\x1e\n\x11group_bp12_symbol\x18\x0b \x01(\tH\x06\x88\x01\x01\x12\x17\n\ngroup_bp12\x18\x0c \x01(\tH\x07\x88\x01\x01\x1a\x32\n\x10ProportionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x42\r\n\x0b_arithmeticB\x0c\n\n_geometricB\x0e\n\x0c_logarithmicB\x11\n\x0f_geometric_fw57B\x13\n\x11_logarithmic_fw57B\x0f\n\r_group_folk54B\x14\n\x12_group_bp12_symbolB\r\n\x0b_group_bp12\"K\n\x13StatisticalResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12#\n\x07results\x18\x02 \x03(\x0b\x32\x12.StatisticalResult\"\xbb\x02\n\nSSURequest\x12\x17\n\x06sample\x18\x01 \x01(\x0b\x32\x07.Sample\x12,\n\x11\x64istribution_type\x18\x02 \x01(\x0e\x32\x11.DistributionType\x12\x14\n\x0cn_components\x18\x03 \x01(\x05\x12\x0f\n\x02x0\x18\x04 \x01(\x0cH\x00\x88\x01\x01\x12\x0c\n\x04loss\x18\x05 \x01(\t\x12\x11\n\toptimizer\x18\x06 \x01(\t\x12\x12\n\ntry_global\x18\x07 \x01(\x08\x12\x18\n\x10global_max_niter\x18\x08 \x01(\x05\x12\x1c\n\x14global_niter_success\x18\t \x01(\x05\x12\x18\n\x10global_step_size\x18\n \x01(\x02\x12\x1b\n\x13optimizer_max_niter\x18\x0b \x01(\x05\x12\x14\n\x0cneed_history\x18\x0c \x01(\x08\x42\x05\n\x03_x0\"\xf2\x01\n\x0bSSUResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x17\n\ntime_spent\x18\x02 \x01(\x02H\x00\x88\x01\x01\x12\x19\n\x0cn_iterations\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x19\n\x0cn_parameters\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x19\n\x0cn_components\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12\x17\n\nparameters\x18\x06 \x01(\x0cH\x04\x88\x01\x01\x42\r\n\x0b_time_spentB\x0f\n\r_n_iterationsB\x0f\n\r_n_parametersB\x0f\n\r_n_componentsB\r\n\x0b_parameters\"\xda\x02\n\x0b\x45MMARequest\x12\x19\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32\x08.Dataset\x12,\n\x11\x64istribution_type\x18\x02 \x01(\x0e\x32\x11.DistributionType\x12\x11\n\tn_members\x18\x03 \x01(\x05\x12\x0f\n\x02x0\x18\x04 \x01(\x0cH\x00\x88\x01\x01\x12\x0e\n\x06\x64\x65vice\x18\x05 \x01(\t\x12\x0c\n\x04loss\x18\x06 \x01(\t\x12\x17\n\x0fpretrain_epochs\x18\x07 \x01(\x05\x12\x12\n\nmin_epochs\x18\x08 \x01(\x05\x12\x12\n\nmax_epochs\x18\t \x01(\x05\x12\x11\n\tprecision\x18\n \x01(\x02\x12\x15\n\rlearning_rate\x18\x0b \x01(\x02\x12\r\n\x05\x62\x65ta1\x18\x0c \x01(\x02\x12\r\n\x05\x62\x65ta2\x18\r \x01(\x02\x12\x1a\n\x12update_end_members\x18\x0e \x01(\x08\x12\x14\n\x0cneed_history\x18\x0f \x01(\x08\x42\x05\n\x03_x0\"\xc9\x02\n\x0c\x45MMAResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x17\n\ntime_spent\x18\x02 \x01(\x02H\x00\x88\x01\x01\x12\x19\n\x0cn_iterations\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x16\n\tn_samples\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x16\n\tn_members\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12\x16\n\tn_classes\x18\x06 \x01(\x05H\x04\x88\x01\x01\x12\x18\n\x0bproportions\x18\x07 \x01(\x0cH\x05\x88\x01\x01\x12\x18\n\x0b\x65nd_members\x18\x08 \x01(\x0cH\x06\x88\x01\x01\x12\x0e\n\x06losses\x18\t \x03(\x02\x42\r\n\x0b_time_spentB\x0f\n\r_n_iterationsB\x0c\n\n_n_samplesB\x0c\n\n_n_membersB\x0c\n\n_n_classesB\x0e\n\x0c_proportionsB\x0e\n\x0c_end_members\"\xcc\x02\n\nUDMRequest\x12\x19\n\x07\x64\x61taset\x18\x01 \x01(\x0b\x32\x08.Dataset\x12,\n\x11\x64istribution_type\x18\x02 \x01(\x0e\x32\x11.DistributionType\x12\x14\n\x0cn_components\x18\x03 \x01(\x05\x12\x0f\n\x02x0\x18\x04 \x01(\x0cH\x00\x88\x01\x01\x12\x0e\n\x06\x64\x65vice\x18\x05 \x01(\t\x12\x17\n\x0fpretrain_epochs\x18\x06 \x01(\x05\x12\x12\n\nmin_epochs\x18\x07 \x01(\x05\x12\x12\n\nmax_epochs\x18\x08 \x01(\x05\x12\x11\n\tprecision\x18\t \x01(\x02\x12\x15\n\rlearning_rate\x18\n \x01(\x02\x12\r\n\x05\x62\x65ta1\x18\x0b \x01(\x02\x12\r\n\x05\x62\x65ta2\x18\x0c \x01(\x02\x12\x18\n\x10\x63onstraint_level\x18\r \x01(\x02\x12\x14\n\x0cneed_history\x18\x0e \x01(\x08\x42\x05\n\x03_x0\"\xdf\x02\n\x0bUDMResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x17\n\ntime_spent\x18\x02 \x01(\x02H\x00\x88\x01\x01\x12\x19\n\x0cn_iterations\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x16\n\tn_samples\x18\x04 \x01(\x05H\x02\x88\x01\x01\x12\x19\n\x0cn_components\x18\x05 \x01(\x05H\x03\x88\x01\x01\x12\x16\n\tn_classes\x18\x06 \x01(\x05H\x04\x88\x01\x01\x12\x17\n\nparameters\x18\x07 \x01(\x0cH\x05\x88\x01\x01\x12\x1b\n\x13\x64istribution_losses\x18\x08 \x03(\x02\x12\x18\n\x10\x63omponent_losses\x18\t \x03(\x02\x12\x14\n\x0ctotal_losses\x18\n \x03(\x02\x42\r\n\x0b_time_spentB\x0f\n\r_n_iterationsB\x0c\n\n_n_samplesB\x0f\n\r_n_componentsB\x0c\n\n_n_classesB\r\n\x0b_parameters*b\n\x10\x44istributionType\x12\x11\n\rNonparametric\x10\x00\x12\n\n\x06Normal\x10\x01\x12\x0e\n\nSkewNormal\x10\x02\x12\x0b\n\x07Weibull\x10\x03\x12\x12\n\x0eGeneralWeibull\x10\x04\x32\x9b\x02\n\x06QGrain\x12\x42\n\x11get_service_state\x12\x14.ServiceStateRequest\x1a\x15.ServiceStateResponse\"\x00\x12=\n\x0eget_statistics\x12\x13.StatisticalRequest\x1a\x14.StatisticalResponse\"\x00\x12-\n\x0eget_ssu_result\x12\x0b.SSURequest\x1a\x0c.SSUResponse\"\x00\x12\x30\n\x0fget_emma_result\x12\x0c.EMMARequest\x1a\r.EMMAResponse\"\x00\x12-\n\x0eget_udm_result\x12\x0b.UDMRequest\x1a\x0c.UDMResponse\"\x00\x62\x06proto3')

_DISTRIBUTIONTYPE = DESCRIPTOR.enum_types_by_name['DistributionType']
DistributionType = enum_type_wrapper.EnumTypeWrapper(_DISTRIBUTIONTYPE)
Nonparametric = 0
Normal = 1
SkewNormal = 2
Weibull = 3
GeneralWeibull = 4


_SAMPLE = DESCRIPTOR.message_types_by_name['Sample']
_DATASET = DESCRIPTOR.message_types_by_name['Dataset']
_SERVICESTATEREQUEST = DESCRIPTOR.message_types_by_name['ServiceStateRequest']
_SERVICESTATERESPONSE = DESCRIPTOR.message_types_by_name['ServiceStateResponse']
_STATISTICALREQUEST = DESCRIPTOR.message_types_by_name['StatisticalRequest']
_STATISTICALPARAMETERS = DESCRIPTOR.message_types_by_name['StatisticalParameters']
_STATISTICALRESULT = DESCRIPTOR.message_types_by_name['StatisticalResult']
_STATISTICALRESULT_PROPORTIONSENTRY = _STATISTICALRESULT.nested_types_by_name['ProportionsEntry']
_STATISTICALRESPONSE = DESCRIPTOR.message_types_by_name['StatisticalResponse']
_SSUREQUEST = DESCRIPTOR.message_types_by_name['SSURequest']
_SSURESPONSE = DESCRIPTOR.message_types_by_name['SSUResponse']
_EMMAREQUEST = DESCRIPTOR.message_types_by_name['EMMARequest']
_EMMARESPONSE = DESCRIPTOR.message_types_by_name['EMMAResponse']
_UDMREQUEST = DESCRIPTOR.message_types_by_name['UDMRequest']
_UDMRESPONSE = DESCRIPTOR.message_types_by_name['UDMResponse']
Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLE,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:Sample)
  })
_sym_db.RegisterMessage(Sample)

Dataset = _reflection.GeneratedProtocolMessageType('Dataset', (_message.Message,), {
  'DESCRIPTOR' : _DATASET,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:Dataset)
  })
_sym_db.RegisterMessage(Dataset)

ServiceStateRequest = _reflection.GeneratedProtocolMessageType('ServiceStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SERVICESTATEREQUEST,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:ServiceStateRequest)
  })
_sym_db.RegisterMessage(ServiceStateRequest)

ServiceStateResponse = _reflection.GeneratedProtocolMessageType('ServiceStateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SERVICESTATERESPONSE,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:ServiceStateResponse)
  })
_sym_db.RegisterMessage(ServiceStateResponse)

StatisticalRequest = _reflection.GeneratedProtocolMessageType('StatisticalRequest', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICALREQUEST,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:StatisticalRequest)
  })
_sym_db.RegisterMessage(StatisticalRequest)

StatisticalParameters = _reflection.GeneratedProtocolMessageType('StatisticalParameters', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICALPARAMETERS,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:StatisticalParameters)
  })
_sym_db.RegisterMessage(StatisticalParameters)

StatisticalResult = _reflection.GeneratedProtocolMessageType('StatisticalResult', (_message.Message,), {

  'ProportionsEntry' : _reflection.GeneratedProtocolMessageType('ProportionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _STATISTICALRESULT_PROPORTIONSENTRY,
    '__module__' : 'qgrain_pb2'
    # @@protoc_insertion_point(class_scope:StatisticalResult.ProportionsEntry)
    })
  ,
  'DESCRIPTOR' : _STATISTICALRESULT,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:StatisticalResult)
  })
_sym_db.RegisterMessage(StatisticalResult)
_sym_db.RegisterMessage(StatisticalResult.ProportionsEntry)

StatisticalResponse = _reflection.GeneratedProtocolMessageType('StatisticalResponse', (_message.Message,), {
  'DESCRIPTOR' : _STATISTICALRESPONSE,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:StatisticalResponse)
  })
_sym_db.RegisterMessage(StatisticalResponse)

SSURequest = _reflection.GeneratedProtocolMessageType('SSURequest', (_message.Message,), {
  'DESCRIPTOR' : _SSUREQUEST,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:SSURequest)
  })
_sym_db.RegisterMessage(SSURequest)

SSUResponse = _reflection.GeneratedProtocolMessageType('SSUResponse', (_message.Message,), {
  'DESCRIPTOR' : _SSURESPONSE,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:SSUResponse)
  })
_sym_db.RegisterMessage(SSUResponse)

EMMARequest = _reflection.GeneratedProtocolMessageType('EMMARequest', (_message.Message,), {
  'DESCRIPTOR' : _EMMAREQUEST,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:EMMARequest)
  })
_sym_db.RegisterMessage(EMMARequest)

EMMAResponse = _reflection.GeneratedProtocolMessageType('EMMAResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMMARESPONSE,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:EMMAResponse)
  })
_sym_db.RegisterMessage(EMMAResponse)

UDMRequest = _reflection.GeneratedProtocolMessageType('UDMRequest', (_message.Message,), {
  'DESCRIPTOR' : _UDMREQUEST,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:UDMRequest)
  })
_sym_db.RegisterMessage(UDMRequest)

UDMResponse = _reflection.GeneratedProtocolMessageType('UDMResponse', (_message.Message,), {
  'DESCRIPTOR' : _UDMRESPONSE,
  '__module__' : 'qgrain_pb2'
  # @@protoc_insertion_point(class_scope:UDMResponse)
  })
_sym_db.RegisterMessage(UDMResponse)

_QGRAIN = DESCRIPTOR.services_by_name['QGrain']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _STATISTICALRESULT_PROPORTIONSENTRY._options = None
  _STATISTICALRESULT_PROPORTIONSENTRY._serialized_options = b'8\001'
  _DISTRIBUTIONTYPE._serialized_start=3501
  _DISTRIBUTIONTYPE._serialized_end=3599
  _SAMPLE._serialized_start=16
  _SAMPLE._serialized_end=77
  _DATASET._serialized_start=79
  _DATASET._serialized_end=202
  _SERVICESTATEREQUEST._serialized_start=204
  _SERVICESTATEREQUEST._serialized_end=225
  _SERVICESTATERESPONSE._serialized_start=227
  _SERVICESTATERESPONSE._serialized_end=351
  _STATISTICALREQUEST._serialized_start=353
  _STATISTICALREQUEST._serialized_end=400
  _STATISTICALPARAMETERS._serialized_start=403
  _STATISTICALPARAMETERS._serialized_end=802
  _STATISTICALRESULT._serialized_start=805
  _STATISTICALRESULT._serialized_end=1489
  _STATISTICALRESULT_PROPORTIONSENTRY._serialized_start=1300
  _STATISTICALRESULT_PROPORTIONSENTRY._serialized_end=1350
  _STATISTICALRESPONSE._serialized_start=1491
  _STATISTICALRESPONSE._serialized_end=1566
  _SSUREQUEST._serialized_start=1569
  _SSUREQUEST._serialized_end=1884
  _SSURESPONSE._serialized_start=1887
  _SSURESPONSE._serialized_end=2129
  _EMMAREQUEST._serialized_start=2132
  _EMMAREQUEST._serialized_end=2478
  _EMMARESPONSE._serialized_start=2481
  _EMMARESPONSE._serialized_end=2810
  _UDMREQUEST._serialized_start=2813
  _UDMREQUEST._serialized_end=3145
  _UDMRESPONSE._serialized_start=3148
  _UDMRESPONSE._serialized_end=3499
  _QGRAIN._serialized_start=3602
  _QGRAIN._serialized_end=3885
# @@protoc_insertion_point(module_scope)
