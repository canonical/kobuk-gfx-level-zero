"""
 Copyright (C) 2019-2021 Intel Corporation

 SPDX-License-Identifier: MIT

 @file zet.py
 @version v1.12-r1.12.15

 """
import platform
from ctypes import *
from enum import *

###############################################################################
__version__ = "1.0"

###############################################################################
## @brief Handle to a driver instance
class zet_driver_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of device object
class zet_device_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of context object
class zet_context_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of command list object
class zet_command_list_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of module object
class zet_module_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of function object
class zet_kernel_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of metric group's object
class zet_metric_group_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of metric's object
class zet_metric_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of metric streamer's object
class zet_metric_streamer_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of metric query pool's object
class zet_metric_query_pool_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of metric query's object
class zet_metric_query_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of tracer object
class zet_tracer_exp_handle_t(c_void_p):
    pass

###############################################################################
## @brief Debug session handle
class zet_debug_session_handle_t(c_void_p):
    pass

###############################################################################
## @brief Defines structure types
class zet_structure_type_v(IntEnum):
    METRIC_GROUP_PROPERTIES = 0x1                                           ## ::zet_metric_group_properties_t
    METRIC_PROPERTIES = 0x2                                                 ## ::zet_metric_properties_t
    METRIC_STREAMER_DESC = 0x3                                              ## ::zet_metric_streamer_desc_t
    METRIC_QUERY_POOL_DESC = 0x4                                            ## ::zet_metric_query_pool_desc_t
    PROFILE_PROPERTIES = 0x5                                                ## ::zet_profile_properties_t
    DEVICE_DEBUG_PROPERTIES = 0x6                                           ## ::zet_device_debug_properties_t
    DEBUG_MEMORY_SPACE_DESC = 0x7                                           ## ::zet_debug_memory_space_desc_t
    DEBUG_REGSET_PROPERTIES = 0x8                                           ## ::zet_debug_regset_properties_t
    GLOBAL_METRICS_TIMESTAMPS_EXP_PROPERTIES = 0x9                          ## ::zet_metric_global_timestamps_resolution_exp_t. Deprecated, use
                                                                            ## ::ZET_STRUCTURE_TYPE_METRIC_GLOBAL_TIMESTAMPS_RESOLUTION_EXP.
    METRIC_GLOBAL_TIMESTAMPS_RESOLUTION_EXP = 0x9                           ## ::zet_metric_global_timestamps_resolution_exp_t
    TRACER_EXP_DESC = 0x00010001                                            ## ::zet_tracer_exp_desc_t
    METRICS_CALCULATE_EXP_DESC = 0x00010002                                 ## ::zet_metric_calculate_exp_desc_t. Deprecated, use
                                                                            ## ::ZET_STRUCTURE_TYPE_METRIC_CALCULATE_EXP_DESC.
    METRIC_CALCULATE_EXP_DESC = 0x00010002                                  ## ::zet_metric_calculate_exp_desc_t
    METRIC_PROGRAMMABLE_EXP_PROPERTIES = 0x00010003                         ## ::zet_metric_programmable_exp_properties_t
    METRIC_PROGRAMMABLE_PARAM_INFO_EXP = 0x00010004                         ## ::zet_metric_programmable_param_info_exp_t
    METRIC_PROGRAMMABLE_PARAM_VALUE_INFO_EXP = 0x00010005                   ## ::zet_metric_programmable_param_value_info_exp_t
    METRIC_GROUP_TYPE_EXP = 0x00010006                                      ## ::zet_metric_group_type_exp_t
    EXPORT_DMA_EXP_PROPERTIES = 0x00010007                                  ## ::zet_export_dma_buf_exp_properties_t
    METRIC_TRACER_EXP_DESC = 0x00010008                                     ## ::zet_metric_tracer_exp_desc_t

class zet_structure_type_t(c_int):
    def __str__(self):
        return str(zet_structure_type_v(self.value))


###############################################################################
## @brief Base for all properties types
class zet_base_properties_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p)                                             ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
    ]

###############################################################################
## @brief Base for all descriptor types
class zet_base_desc_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p)                                             ## [in][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
    ]

###############################################################################
## @brief Supported value types
class zet_value_type_v(IntEnum):
    UINT32 = 0                                                              ## 32-bit unsigned-integer
    UINT64 = 1                                                              ## 64-bit unsigned-integer
    FLOAT32 = 2                                                             ## 32-bit floating-point
    FLOAT64 = 3                                                             ## 64-bit floating-point
    BOOL8 = 4                                                               ## 8-bit boolean
    STRING = 5                                                              ## C string
    UINT8 = 6                                                               ## 8-bit unsigned-integer
    UINT16 = 7                                                              ## 16-bit unsigned-integer

class zet_value_type_t(c_int):
    def __str__(self):
        return str(zet_value_type_v(self.value))


###############################################################################
## @brief Union of values
class zet_value_t(Structure):
    _fields_ = [
        ("ui32", c_ulong),                                              ## [out] 32-bit unsigned-integer
        ("ui64", c_ulonglong),                                          ## [out] 64-bit unsigned-integer
        ("fp32", c_float),                                              ## [out] 32-bit floating-point
        ("fp64", c_double),                                             ## [out] 64-bit floating-point
        ("b8", ze_bool_t)                                               ## [out] 8-bit boolean
    ]

###############################################################################
## @brief Typed value
class zet_typed_value_t(Structure):
    _fields_ = [
        ("type", zet_value_type_t),                                     ## [out] type of value
        ("value", zet_value_t)                                          ## [out] value
    ]

###############################################################################
## @brief Enables driver instrumentation and dependencies for device metrics

###############################################################################
## @brief Enables driver instrumentation and dependencies for program
##        instrumentation

###############################################################################
## @brief Enables driver instrumentation and dependencies for program debugging

###############################################################################
## @brief Supported module debug info formats.
class zet_module_debug_info_format_v(IntEnum):
    ELF_DWARF = 0                                                           ## Format is ELF/DWARF

class zet_module_debug_info_format_t(c_int):
    def __str__(self):
        return str(zet_module_debug_info_format_v(self.value))


###############################################################################
## @brief Supported device debug property flags
class zet_device_debug_property_flags_v(IntEnum):
    ATTACH = ZE_BIT(0)                                                      ## the device supports attaching for debug

class zet_device_debug_property_flags_t(c_int):
    def __str__(self):
        return hex(self.value)


###############################################################################
## @brief Device debug properties queried using ::zetDeviceGetDebugProperties.
class zet_device_debug_properties_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("flags", zet_device_debug_property_flags_t)                    ## [out] returns 0 (none) or a valid combination of
                                                                        ## ::zet_device_debug_property_flag_t
    ]

###############################################################################
## @brief Debug configuration provided to ::zetDebugAttach
class zet_debug_config_t(Structure):
    _fields_ = [
        ("pid", c_ulong)                                                ## [in] the host process identifier
    ]

###############################################################################
## @brief Supported debug event flags.
class zet_debug_event_flags_v(IntEnum):
    NEED_ACK = ZE_BIT(0)                                                    ## The event needs to be acknowledged by calling
                                                                            ## ::zetDebugAcknowledgeEvent.

class zet_debug_event_flags_t(c_int):
    def __str__(self):
        return hex(self.value)


###############################################################################
## @brief Supported debug event types.
class zet_debug_event_type_v(IntEnum):
    INVALID = 0                                                             ## The event is invalid
    DETACHED = 1                                                            ## The tool was detached
    PROCESS_ENTRY = 2                                                       ## The debuggee process created command queues on the device
    PROCESS_EXIT = 3                                                        ## The debuggee process destroyed all command queues on the device
    MODULE_LOAD = 4                                                         ## An in-memory module was loaded onto the device
    MODULE_UNLOAD = 5                                                       ## An in-memory module is about to get unloaded from the device
    THREAD_STOPPED = 6                                                      ## The thread stopped due to a device exception
    THREAD_UNAVAILABLE = 7                                                  ## The thread is not available to be stopped
    PAGE_FAULT = 8                                                          ## A page request could not be completed on the device

class zet_debug_event_type_t(c_int):
    def __str__(self):
        return str(zet_debug_event_type_v(self.value))


###############################################################################
## @brief Supported debug detach reasons.
class zet_debug_detach_reason_v(IntEnum):
    INVALID = 0                                                             ## The detach reason is not valid
    HOST_EXIT = 1                                                           ## The host process exited

class zet_debug_detach_reason_t(c_int):
    def __str__(self):
        return str(zet_debug_detach_reason_v(self.value))


###############################################################################
## @brief Event information for ::ZET_DEBUG_EVENT_TYPE_DETACHED
class zet_debug_event_info_detached_t(Structure):
    _fields_ = [
        ("reason", zet_debug_detach_reason_t)                           ## [out] the detach reason
    ]

###############################################################################
## @brief Event information for ::ZET_DEBUG_EVENT_TYPE_MODULE_LOAD and
##        ::ZET_DEBUG_EVENT_TYPE_MODULE_UNLOAD
class zet_debug_event_info_module_t(Structure):
    _fields_ = [
        ("format", zet_module_debug_info_format_t),                     ## [out] the module format
        ("moduleBegin", c_ulonglong),                                   ## [out] the begin address of the in-memory module (inclusive)
        ("moduleEnd", c_ulonglong),                                     ## [out] the end address of the in-memory module (exclusive)
        ("load", c_ulonglong)                                           ## [out] the load address of the module on the device
    ]

###############################################################################
## @brief Event information for ::ZET_DEBUG_EVENT_TYPE_THREAD_STOPPED and
##        ::ZET_DEBUG_EVENT_TYPE_THREAD_UNAVAILABLE
class zet_debug_event_info_thread_stopped_t(Structure):
    _fields_ = [
        ("thread", ze_device_thread_t)                                  ## [out] the stopped/unavailable thread
    ]

###############################################################################
## @brief Page fault reasons.
class zet_debug_page_fault_reason_v(IntEnum):
    INVALID = 0                                                             ## The page fault reason is not valid
    MAPPING_ERROR = 1                                                       ## The address is not mapped
    PERMISSION_ERROR = 2                                                    ## Invalid access permissions

class zet_debug_page_fault_reason_t(c_int):
    def __str__(self):
        return str(zet_debug_page_fault_reason_v(self.value))


###############################################################################
## @brief Event information for ::ZET_DEBUG_EVENT_TYPE_PAGE_FAULT
class zet_debug_event_info_page_fault_t(Structure):
    _fields_ = [
        ("address", c_ulonglong),                                       ## [out] the faulting address
        ("mask", c_ulonglong),                                          ## [out] the alignment mask
        ("reason", zet_debug_page_fault_reason_t)                       ## [out] the page fault reason
    ]

###############################################################################
## @brief Event type-specific information
class zet_debug_event_info_t(Structure):
    _fields_ = [
        ("detached", zet_debug_event_info_detached_t),                  ## [out] type == ::ZET_DEBUG_EVENT_TYPE_DETACHED
        ("module", zet_debug_event_info_module_t),                      ## [out] type == ::ZET_DEBUG_EVENT_TYPE_MODULE_LOAD or
                                                                        ## ::ZET_DEBUG_EVENT_TYPE_MODULE_UNLOAD
        ("thread", zet_debug_event_info_thread_stopped_t),              ## [out] type == ::ZET_DEBUG_EVENT_TYPE_THREAD_STOPPED or
                                                                        ## ::ZET_DEBUG_EVENT_TYPE_THREAD_UNAVAILABLE
        ("page_fault", zet_debug_event_info_page_fault_t)               ## [out] type == ::ZET_DEBUG_EVENT_TYPE_PAGE_FAULT
    ]

###############################################################################
## @brief A debug event on the device.
class zet_debug_event_t(Structure):
    _fields_ = [
        ("type", zet_debug_event_type_t),                               ## [out] the event type
        ("flags", zet_debug_event_flags_t),                             ## [out] returns 0 (none) or a combination of ::zet_debug_event_flag_t
        ("info", zet_debug_event_info_t)                                ## [out] event type specific information
    ]

###############################################################################
## @brief Supported device memory space types.
class zet_debug_memory_space_type_v(IntEnum):
    DEFAULT = 0                                                             ## default memory space (attribute may be omitted)
    SLM = 1                                                                 ## shared local memory space (GPU-only)
    ELF = 2                                                                 ## ELF file memory space

class zet_debug_memory_space_type_t(c_int):
    def __str__(self):
        return str(zet_debug_memory_space_type_v(self.value))


###############################################################################
## @brief Device memory space descriptor
class zet_debug_memory_space_desc_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("type", zet_debug_memory_space_type_t),                        ## [in] type of memory space
        ("address", c_ulonglong)                                        ## [in] the virtual address within the memory space
    ]

###############################################################################
## @brief Supported general register set flags.
class zet_debug_regset_flags_v(IntEnum):
    READABLE = ZE_BIT(0)                                                    ## register set is readable
    WRITEABLE = ZE_BIT(1)                                                   ## register set is writeable

class zet_debug_regset_flags_t(c_int):
    def __str__(self):
        return hex(self.value)


###############################################################################
## @brief Device register set properties queried using
##        ::zetDebugGetRegisterSetProperties.
class zet_debug_regset_properties_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("type", c_ulong),                                              ## [out] device-specific register set type
        ("version", c_ulong),                                           ## [out] device-specific version of this register set
        ("generalFlags", zet_debug_regset_flags_t),                     ## [out] general register set flags
        ("deviceFlags", c_ulong),                                       ## [out] device-specific register set flags
        ("count", c_ulong),                                             ## [out] number of registers in the set
        ("bitSize", c_ulong),                                           ## [out] the size of a register in bits
        ("byteSize", c_ulong)                                           ## [out] the size required for reading or writing a register in bytes
    ]

###############################################################################
## @brief Maximum metric group name string size
ZET_MAX_METRIC_GROUP_NAME = 256

###############################################################################
## @brief Maximum metric group description string size
ZET_MAX_METRIC_GROUP_DESCRIPTION = 256

###############################################################################
## @brief Metric group sampling type
class zet_metric_group_sampling_type_flags_v(IntEnum):
    EVENT_BASED = ZE_BIT(0)                                                 ## Event based sampling
    TIME_BASED = ZE_BIT(1)                                                  ## Time based sampling
    EXP_TRACER_BASED = ZE_BIT(2)                                            ## Experimental Tracer based sampling

class zet_metric_group_sampling_type_flags_t(c_int):
    def __str__(self):
        return hex(self.value)


###############################################################################
## @brief Metric group properties queried using ::zetMetricGroupGetProperties
class zet_metric_group_properties_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("name", c_char * ZET_MAX_METRIC_GROUP_NAME),                   ## [out] metric group name
        ("description", c_char * ZET_MAX_METRIC_GROUP_DESCRIPTION),     ## [out] metric group description
        ("samplingType", zet_metric_group_sampling_type_flags_t),       ## [out] metric group sampling type.
                                                                        ## returns a combination of ::zet_metric_group_sampling_type_flag_t.
        ("domain", c_ulong),                                            ## [out] metric group domain number. Cannot use multiple, simultaneous
                                                                        ## metric groups from the same domain.
        ("metricCount", c_ulong)                                        ## [out] metric count belonging to this group
    ]

###############################################################################
## @brief Metric types
class zet_metric_type_v(IntEnum):
    DURATION = 0                                                            ## Metric type: duration
    EVENT = 1                                                               ## Metric type: event
    EVENT_WITH_RANGE = 2                                                    ## Metric type: event with range
    THROUGHPUT = 3                                                          ## Metric type: throughput
    TIMESTAMP = 4                                                           ## Metric type: timestamp
    FLAG = 5                                                                ## Metric type: flag
    RATIO = 6                                                               ## Metric type: ratio
    RAW = 7                                                                 ## Metric type: raw
    EVENT_EXP_TIMESTAMP = 0x7ffffff9                                        ## Metric type: event with only timestamp and value has no meaning
    EVENT_EXP_START = 0x7ffffffa                                            ## Metric type: the first event of a start/end event pair
    EVENT_EXP_END = 0x7ffffffb                                              ## Metric type: the second event of a start/end event pair
    EVENT_EXP_MONOTONIC_WRAPS_VALUE = 0x7ffffffc                            ## Metric type: value of the event is a monotonically increasing value
                                                                            ## that can wrap around
    EXP_EXPORT_DMA_BUF = 0x7ffffffd                                         ## Metric which exports linux dma_buf, which could be imported/mapped to
                                                                            ## the host process
    IP_EXP = 0x7ffffffe                                                     ## Metric type: instruction pointer. Deprecated, use
                                                                            ## ::ZET_METRIC_TYPE_IP.
    IP = 0x7ffffffe                                                         ## Metric type: instruction pointer

class zet_metric_type_t(c_int):
    def __str__(self):
        return str(zet_metric_type_v(self.value))


###############################################################################
## @brief Metric group calculation type
class zet_metric_group_calculation_type_v(IntEnum):
    METRIC_VALUES = 0                                                       ## Calculated metric values from raw data.
    MAX_METRIC_VALUES = 1                                                   ## Maximum metric values.

class zet_metric_group_calculation_type_t(c_int):
    def __str__(self):
        return str(zet_metric_group_calculation_type_v(self.value))


###############################################################################
## @brief Maximum metric name string size
ZET_MAX_METRIC_NAME = 256

###############################################################################
## @brief Maximum metric description string size
ZET_MAX_METRIC_DESCRIPTION = 256

###############################################################################
## @brief Maximum metric component string size
ZET_MAX_METRIC_COMPONENT = 256

###############################################################################
## @brief Maximum metric result units string size
ZET_MAX_METRIC_RESULT_UNITS = 256

###############################################################################
## @brief Metric properties queried using ::zetMetricGetProperties
class zet_metric_properties_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("name", c_char * ZET_MAX_METRIC_NAME),                         ## [out] metric name
        ("description", c_char * ZET_MAX_METRIC_DESCRIPTION),           ## [out] metric description
        ("component", c_char * ZET_MAX_METRIC_COMPONENT),               ## [out] metric component
        ("tierNumber", c_ulong),                                        ## [out] number of tier
        ("metricType", zet_metric_type_t),                              ## [out] metric type
        ("resultType", zet_value_type_t),                               ## [out] metric result type
        ("resultUnits", c_char * ZET_MAX_METRIC_RESULT_UNITS)           ## [out] metric result units
    ]

###############################################################################
## @brief Metric streamer descriptor
class zet_metric_streamer_desc_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("notifyEveryNReports", c_ulong),                               ## [in,out] number of collected reports after which notification event
                                                                        ## will be signaled. If the requested value is not supported exactly,
                                                                        ## then the driver may use a value that is the closest supported
                                                                        ## approximation and shall update this member during ::zetMetricStreamerOpen.
        ("samplingPeriod", c_ulong)                                     ## [in,out] streamer sampling period in nanoseconds. If the requested
                                                                        ## value is not supported exactly, then the driver may use a value that
                                                                        ## is the closest supported approximation and shall update this member
                                                                        ## during ::zetMetricStreamerOpen.
    ]

###############################################################################
## @brief Metric query pool types
class zet_metric_query_pool_type_v(IntEnum):
    PERFORMANCE = 0                                                         ## Performance metric query pool.
    EXECUTION = 1                                                           ## Skips workload execution between begin/end calls.

class zet_metric_query_pool_type_t(c_int):
    def __str__(self):
        return str(zet_metric_query_pool_type_v(self.value))


###############################################################################
## @brief Metric query pool description
class zet_metric_query_pool_desc_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("type", zet_metric_query_pool_type_t),                         ## [in] Query pool type.
        ("count", c_ulong)                                              ## [in] Internal slots count within query pool object.
    ]

###############################################################################
## @brief Supportted profile features
class zet_profile_flags_v(IntEnum):
    REGISTER_REALLOCATION = ZE_BIT(0)                                       ## request the compiler attempt to minimize register usage as much as
                                                                            ## possible to allow for instrumentation
    FREE_REGISTER_INFO = ZE_BIT(1)                                          ## request the compiler generate free register info

class zet_profile_flags_t(c_int):
    def __str__(self):
        return hex(self.value)


###############################################################################
## @brief Profiling meta-data for instrumentation
class zet_profile_properties_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("flags", zet_profile_flags_t),                                 ## [out] indicates which flags were enabled during compilation.
                                                                        ## returns 0 (none) or a combination of ::zet_profile_flag_t
        ("numTokens", c_ulong)                                          ## [out] number of tokens immediately following this structure
    ]

###############################################################################
## @brief Supported profile token types
class zet_profile_token_type_v(IntEnum):
    FREE_REGISTER = 0                                                       ## GRF info

class zet_profile_token_type_t(c_int):
    def __str__(self):
        return str(zet_profile_token_type_v(self.value))


###############################################################################
## @brief Profile free register token detailing unused registers in the current
##        function
class zet_profile_free_register_token_t(Structure):
    _fields_ = [
        ("type", zet_profile_token_type_t),                             ## [out] type of token
        ("size", c_ulong),                                              ## [out] total size of the token, in bytes
        ("count", c_ulong)                                              ## [out] number of register sequences immediately following this
                                                                        ## structure
    ]

###############################################################################
## @brief Profile register sequence detailing consecutive bytes, all of which
##        are unused
class zet_profile_register_sequence_t(Structure):
    _fields_ = [
        ("start", c_ulong),                                             ## [out] starting byte in the register table, representing the start of
                                                                        ## unused bytes in the current function
        ("count", c_ulong)                                              ## [out] number of consecutive bytes in the sequence, starting from start
    ]

###############################################################################
## @brief API Tracing Experimental Extension Name
ZET_API_TRACING_EXP_NAME = "ZET_experimental_api_tracing"

###############################################################################
## @brief API Tracing Experimental Extension Version(s)
class zet_api_tracing_exp_version_v(IntEnum):
    _1_0 = ZE_MAKE_VERSION( 1, 0 )                                          ## version 1.0
    CURRENT = ZE_MAKE_VERSION( 1, 0 )                                       ## latest known version

class zet_api_tracing_exp_version_t(c_int):
    def __str__(self):
        return str(zet_api_tracing_exp_version_v(self.value))


###############################################################################
## @brief Alias the existing callbacks definition for 'core' callbacks
class zet_core_callbacks_t(ze_callbacks_t):
    pass

###############################################################################
## @brief Tracer descriptor
class zet_tracer_exp_desc_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("pUserData", c_void_p)                                         ## [in] pointer passed to every tracer's callbacks
    ]

###############################################################################
## @brief Concurrent Metric Groups Experimental Extension Name
ZET_CONCURRENT_METRIC_GROUPS_EXP_NAME = "ZET_experimental_concurrent_metric_groups"

###############################################################################
## @brief Concurrent Metric Groups Experimental Extension Version(s)
class zet_concurrent_metric_groups_exp_version_v(IntEnum):
    _1_0 = ZE_MAKE_VERSION( 1, 0 )                                          ## version 1.0
    CURRENT = ZE_MAKE_VERSION( 1, 0 )                                       ## latest known version

class zet_concurrent_metric_groups_exp_version_t(c_int):
    def __str__(self):
        return str(zet_concurrent_metric_groups_exp_version_v(self.value))


###############################################################################
## @brief Metric Tracer Experimental Extension Name
ZET_METRICS_TRACER_EXP_NAME = "ZET_experimental_metric_tracer"

###############################################################################
## @brief Metric Tracer Experimental Extension Version(s)
class zet_metric_tracer_exp_version_v(IntEnum):
    _1_0 = ZE_MAKE_VERSION( 1, 0 )                                          ## version 1.0
    CURRENT = ZE_MAKE_VERSION( 1, 0 )                                       ## latest known version

class zet_metric_tracer_exp_version_t(c_int):
    def __str__(self):
        return str(zet_metric_tracer_exp_version_v(self.value))


###############################################################################
## @brief Handle of metric tracer's object
class zet_metric_tracer_exp_handle_t(c_void_p):
    pass

###############################################################################
## @brief Handle of metric decoder's object
class zet_metric_decoder_exp_handle_t(c_void_p):
    pass

###############################################################################
## @brief Metric tracer descriptor
class zet_metric_tracer_exp_desc_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("notifyEveryNBytes", c_ulong)                                  ## [in,out] number of collected bytes after which notification event will
                                                                        ## be signaled. If the requested value is not supported exactly, then the
                                                                        ## driver may use a value that is the closest supported approximation and
                                                                        ## shall update this member during ::zetMetricTracerCreateExp.
    ]

###############################################################################
## @brief Decoded metric entry
class zet_metric_entry_exp_t(Structure):
    _fields_ = [
        ("value", zet_value_t),                                         ## [out] value of the decodable metric entry or event. Number is
                                                                        ## meaningful based on the metric type.
        ("timeStamp", c_ulonglong),                                     ## [out] timestamp at which the event happened.
        ("metricIndex", c_ulong),                                       ## [out] index to the decodable metric handle in the input array
                                                                        ## (phMetric) in ::zetMetricTracerDecodeExp().
        ("onSubdevice", ze_bool_t),                                     ## [out] True if the event occurred on a sub-device; false means the
                                                                        ## device on which the metric tracer was opened does not have
                                                                        ## sub-devices.
        ("subdeviceId", c_ulong)                                        ## [out] If onSubdevice is true, this gives the ID of the sub-device.
    ]

###############################################################################
## @brief Metric group type
class zet_metric_group_type_exp_flags_v(IntEnum):
    EXPORT_DMA_BUF = ZE_BIT(0)                                              ## Metric group and metrics exports memory using linux dma-buf, which
                                                                            ## could be imported/mapped to the host process. Properties of the
                                                                            ## dma_buf could be queried using ::zet_export_dma_buf_exp_properties_t.
    USER_CREATED = ZE_BIT(1)                                                ## Metric group created using ::zetDeviceCreateMetricGroupsFromMetricsExp
    OTHER = ZE_BIT(2)                                                       ## Metric group which has a collection of metrics

class zet_metric_group_type_exp_flags_t(c_int):
    def __str__(self):
        return hex(self.value)


###############################################################################
## @brief Query the metric group type using `pNext` of
##        ::zet_metric_group_properties_t
class zet_metric_group_type_exp_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("type", zet_metric_group_type_exp_flags_t)                     ## [out] metric group type.
                                                                        ## returns a combination of ::zet_metric_group_type_exp_flags_t.
    ]

###############################################################################
## @brief Exported dma_buf properties queried using `pNext` of
##        ::zet_metric_group_properties_t or ::zet_metric_properties_t
class zet_export_dma_buf_exp_properties_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("fd", c_int),                                                  ## [out] the file descriptor handle that could be used to import the
                                                                        ## memory by the host process.
        ("size", c_size_t)                                              ## [out] size in bytes of the dma_buf
    ]

###############################################################################
## @brief Calculating Multiple Metrics Experimental Extension Name
ZET_MULTI_METRICS_EXP_NAME = "ZET_experimental_calculate_multiple_metrics"

###############################################################################
## @brief Calculating Multiple Metrics Experimental Extension Version(s)
class ze_calculate_multiple_metrics_exp_version_v(IntEnum):
    _1_0 = ZE_MAKE_VERSION( 1, 0 )                                          ## version 1.0
    CURRENT = ZE_MAKE_VERSION( 1, 0 )                                       ## latest known version

class ze_calculate_multiple_metrics_exp_version_t(c_int):
    def __str__(self):
        return str(ze_calculate_multiple_metrics_exp_version_v(self.value))


###############################################################################
## @brief Global Metric Timestamps Experimental Extension Name
ZET_GLOBAL_METRICS_TIMESTAMPS_EXP_NAME = "ZET_experimental_global_metric_timestamps"

###############################################################################
## @brief Global Metric Timestamps Experimental Extension Version(s)
class ze_metric_global_timestamps_exp_version_v(IntEnum):
    _1_0 = ZE_MAKE_VERSION( 1, 0 )                                          ## version 1.0
    CURRENT = ZE_MAKE_VERSION( 1, 0 )                                       ## latest known version

class ze_metric_global_timestamps_exp_version_t(c_int):
    def __str__(self):
        return str(ze_metric_global_timestamps_exp_version_v(self.value))


###############################################################################
## @brief Metric timestamps resolution
## 
## @details
##     - This structure may be returned from ::zetMetricGroupGetProperties via
##       the `pNext` member of ::zet_metric_group_properties_t.
##     - Used for mapping metric timestamps to other timers.
class zet_metric_global_timestamps_resolution_exp_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("timerResolution", c_ulonglong),                               ## [out] Returns the resolution of metrics timer (used for timestamps) in
                                                                        ## cycles/sec.
        ("timestampValidBits", c_ulonglong)                             ## [out] Returns the number of valid bits in the timestamp value.
    ]

###############################################################################
## @brief Exporting Metrics Data Experimental Extension Name
ZET_EXPORT_METRICS_DATA_EXP_NAME = "ZET_experimental_metric_export_data"

###############################################################################
## @brief Exporting Metrics Data Experimental Extension Version(s)
class zet_export_metric_data_exp_version_v(IntEnum):
    _1_0 = ZE_MAKE_VERSION( 1, 0 )                                          ## version 1.0
    CURRENT = ZE_MAKE_VERSION( 1, 0 )                                       ## latest known version

class zet_export_metric_data_exp_version_t(c_int):
    def __str__(self):
        return str(zet_export_metric_data_exp_version_v(self.value))


###############################################################################
## @brief Maximum count of characters in export data element name
ZET_MAX_METRIC_EXPORT_DATA_ELEMENT_NAME_EXP = 256

###############################################################################
## @brief Maximum export data element description string size
ZET_MAX_METRIC_EXPORT_DATA_ELEMENT_DESCRIPTION_EXP = 256

###############################################################################
## @brief Metrics calculation descriptor
class zet_metric_calculate_exp_desc_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("rawReportSkipCount", c_ulong)                                 ## [in] number of reports to skip during calculation
    ]

###############################################################################
## @brief Programmable Metrics Experimental Extension Name
ZET_PROGRAMMABLE_METRICS_EXP_NAME = "ZET_experimental_programmable_metrics"

###############################################################################
## @brief Programmable Metrics Experimental Extension Version(s)
class zet_metric_programmable_exp_version_v(IntEnum):
    _1_1 = ZE_MAKE_VERSION( 1, 1 )                                          ## version 1.1
    CURRENT = ZE_MAKE_VERSION( 1, 1 )                                       ## latest known version

class zet_metric_programmable_exp_version_t(c_int):
    def __str__(self):
        return str(zet_metric_programmable_exp_version_v(self.value))


###############################################################################
## @brief Maximum count of characters in export data element name
ZET_MAX_PROGRAMMABLE_METRICS_ELEMENT_NAME_EXP = 256

###############################################################################
## @brief Maximum export data element description string size
ZET_MAX_PROGRAMMABLE_METRICS_ELEMENT_DESCRIPTION_EXP = 256

###############################################################################
## @brief Maximum count of characters in metric group name prefix
ZET_MAX_METRIC_GROUP_NAME_PREFIX_EXP = 64

###############################################################################
## @brief Maximum metric programmable name string size
ZET_MAX_METRIC_PROGRAMMABLE_NAME_EXP = 128

###############################################################################
## @brief Maximum metric programmable description string size
ZET_MAX_METRIC_PROGRAMMABLE_DESCRIPTION_EXP = 128

###############################################################################
## @brief Maximum metric programmable component string size
ZET_MAX_METRIC_PROGRAMMABLE_COMPONENT_EXP = 128

###############################################################################
## @brief Maximum metric programmable parameter string size
ZET_MAX_METRIC_PROGRAMMABLE_PARAMETER_NAME_EXP = 128

###############################################################################
## @brief Maximum value for programmable value description
ZET_MAX_METRIC_PROGRAMMABLE_VALUE_DESCRIPTION_EXP = 128

###############################################################################
## @brief Maximum value metric group name prefix
ZE_MAX_METRIC_GROUP_NAME_PREFIX = 64

###############################################################################
## @brief Handle of metric programmable's object
class zet_metric_programmable_exp_handle_t(c_void_p):
    pass

###############################################################################
## @brief Metric Programmable properties queried using
##        ::zetMetricProgrammableGetPropertiesExp
class zet_metric_programmable_exp_properties_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("name", c_char * ZET_MAX_METRIC_PROGRAMMABLE_NAME_EXP),        ## [out] metric programmable name
        ("description", c_char * ZET_MAX_METRIC_PROGRAMMABLE_DESCRIPTION_EXP),  ## [out] metric programmable description
        ("component", c_char * ZET_MAX_METRIC_PROGRAMMABLE_COMPONENT_EXP),  ## [out] metric programmable component
        ("tierNumber", c_ulong),                                        ## [out] tier number
        ("domain", c_ulong),                                            ## [out] metric domain number.
        ("parameterCount", c_ulong),                                    ## [out] number of parameters in the programmable
        ("samplingType", zet_metric_group_sampling_type_flags_t),       ## [out] metric sampling type.
                                                                        ## returns a combination of ::zet_metric_group_sampling_type_flag_t.
        ("sourceId", c_ulong)                                           ## [out] unique metric source identifier(within platform)to identify the
                                                                        ## HW block where the metric is collected.
    ]

###############################################################################
## @brief Metric Programmable Parameter types
class zet_metric_programmable_param_type_exp_v(IntEnum):
    DISAGGREGATION = 0                                                      ## Metric is disaggregated.
    LATENCY = 1                                                             ## Metric for latency measurement.
    NORMALIZATION_UTILIZATION = 2                                           ## Produces normalization in percent using raw_metric * 100 / cycles / HW
                                                                            ## instance_count.
    NORMALIZATION_AVERAGE = 3                                               ## Produces normalization using raw_metric / HW instance_count.
    NORMALIZATION_RATE = 4                                                  ## Produces normalization average using raw_metric / timestamp.
    NORMALIZATION_BYTES = 5                                                 ## Produces normalization average using raw_metric * n bytes.
    GENERIC = 6                                                             ## Generic Parameter type. Please refer the parameter's description.

class zet_metric_programmable_param_type_exp_t(c_int):
    def __str__(self):
        return str(zet_metric_programmable_param_type_exp_v(self.value))


###############################################################################
## @brief Supported value info types
class zet_value_info_type_exp_v(IntEnum):
    UINT32 = 0                                                              ## 32-bit unsigned-integer
    UINT64 = 1                                                              ## 64-bit unsigned-integer
    FLOAT32 = 2                                                             ## 32-bit floating-point
    FLOAT64 = 3                                                             ## 64-bit floating-point
    BOOL8 = 4                                                               ## 8-bit boolean
    UINT8 = 5                                                               ## 8-bit unsigned-integer
    UINT16 = 6                                                              ## 16-bit unsigned-integer
    UINT64_RANGE = 7                                                        ## 64-bit unsigned-integer range (minimum and maximum)
    FLOAT64_RANGE = 8                                                       ## 64-bit floating point range (minimum and maximum)

class zet_value_info_type_exp_t(c_int):
    def __str__(self):
        return str(zet_value_info_type_exp_v(self.value))


###############################################################################
## @brief Value info of type uint64_t range
class zet_value_uint64_range_exp_t(Structure):
    _fields_ = [
        ("ui64Min", c_ulonglong),                                       ## [out] minimum value of the range
        ("ui64Max", c_ulonglong)                                        ## [out] maximum value of the range
    ]

###############################################################################
## @brief Value info of type float64 range
class zet_value_fp64_range_exp_t(Structure):
    _fields_ = [
        ("fp64Min", c_double),                                          ## [out] minimum value of the range
        ("fp64Max", c_double)                                           ## [out] maximum value of the range
    ]

###############################################################################
## @brief Union of value information
class zet_value_info_exp_t(Structure):
    _fields_ = [
        ("ui32", c_ulong),                                              ## [out] 32-bit unsigned-integer
        ("ui64", c_ulonglong),                                          ## [out] 64-bit unsigned-integer
        ("fp32", c_float),                                              ## [out] 32-bit floating-point
        ("fp64", c_double),                                             ## [out] 64-bit floating-point
        ("b8", ze_bool_t),                                              ## [out] 8-bit boolean
        ("ui8", c_ubyte),                                               ## [out] 8-bit unsigned integer
        ("ui16", c_ushort),                                             ## [out] 16-bit unsigned integer
        ("ui64Range", zet_value_uint64_range_exp_t),                    ## [out] minimum and maximum value of the range
        ("fp64Range", zet_value_fp64_range_exp_t)                       ## [out] minimum and maximum value of the range
    ]

###############################################################################
## @brief Metric Programmable parameter information
class zet_metric_programmable_param_info_exp_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("type", zet_metric_programmable_param_type_exp_t),             ## [out] programmable parameter type
        ("name", c_char * ZET_MAX_METRIC_PROGRAMMABLE_PARAMETER_NAME_EXP),  ## [out] metric programmable parameter name
        ("valueInfoType", zet_value_info_type_exp_t),                   ## [out] value info type
        ("defaultValue", zet_value_t),                                  ## [out] default value for the parameter
        ("valueInfoCount", c_ulong)                                     ## [out] count of ::zet_metric_programmable_param_value_info_exp_t
    ]

###############################################################################
## @brief Metric Programmable parameter value information
class zet_metric_programmable_param_value_info_exp_t(Structure):
    _fields_ = [
        ("stype", zet_structure_type_t),                                ## [in] type of this structure
        ("pNext", c_void_p),                                            ## [in,out][optional] must be null or a pointer to an extension-specific
                                                                        ## structure (i.e. contains stype and pNext).
        ("valueInfo", zet_value_info_exp_t),                            ## [out] information about the parameter value
        ("description", c_char * ZET_MAX_METRIC_PROGRAMMABLE_VALUE_DESCRIPTION_EXP) ## [out] description about the value
    ]

###############################################################################
## @brief Metric Programmable parameter value
class zet_metric_programmable_param_value_exp_t(Structure):
    _fields_ = [
        ("value", zet_value_t)                                          ## [in] parameter value
    ]

###############################################################################
__use_win_types = "Windows" == platform.uname()[0]

###############################################################################
## @brief Function-pointer for zetMetricProgrammableGetExp
if __use_win_types:
    _zetMetricProgrammableGetExp_t = WINFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(c_ulong), POINTER(zet_metric_programmable_exp_handle_t) )
else:
    _zetMetricProgrammableGetExp_t = CFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(c_ulong), POINTER(zet_metric_programmable_exp_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricProgrammableGetPropertiesExp
if __use_win_types:
    _zetMetricProgrammableGetPropertiesExp_t = WINFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, POINTER(zet_metric_programmable_exp_properties_t) )
else:
    _zetMetricProgrammableGetPropertiesExp_t = CFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, POINTER(zet_metric_programmable_exp_properties_t) )

###############################################################################
## @brief Function-pointer for zetMetricProgrammableGetParamInfoExp
if __use_win_types:
    _zetMetricProgrammableGetParamInfoExp_t = WINFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, POINTER(c_ulong), POINTER(zet_metric_programmable_param_info_exp_t) )
else:
    _zetMetricProgrammableGetParamInfoExp_t = CFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, POINTER(c_ulong), POINTER(zet_metric_programmable_param_info_exp_t) )

###############################################################################
## @brief Function-pointer for zetMetricProgrammableGetParamValueInfoExp
if __use_win_types:
    _zetMetricProgrammableGetParamValueInfoExp_t = WINFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, c_ulong, POINTER(c_ulong), POINTER(zet_metric_programmable_param_value_info_exp_t) )
else:
    _zetMetricProgrammableGetParamValueInfoExp_t = CFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, c_ulong, POINTER(c_ulong), POINTER(zet_metric_programmable_param_value_info_exp_t) )


###############################################################################
## @brief Table of MetricProgrammableExp functions pointers
class _zet_metric_programmable_exp_dditable_t(Structure):
    _fields_ = [
        ("pfnGetExp", c_void_p),                                        ## _zetMetricProgrammableGetExp_t
        ("pfnGetPropertiesExp", c_void_p),                              ## _zetMetricProgrammableGetPropertiesExp_t
        ("pfnGetParamInfoExp", c_void_p),                               ## _zetMetricProgrammableGetParamInfoExp_t
        ("pfnGetParamValueInfoExp", c_void_p)                           ## _zetMetricProgrammableGetParamValueInfoExp_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricTracerCreateExp
if __use_win_types:
    _zetMetricTracerCreateExp_t = WINFUNCTYPE( ze_result_t, zet_context_handle_t, zet_device_handle_t, c_ulong, POINTER(zet_metric_group_handle_t), POINTER(zet_metric_tracer_exp_desc_t), ze_event_handle_t, POINTER(zet_metric_tracer_exp_handle_t) )
else:
    _zetMetricTracerCreateExp_t = CFUNCTYPE( ze_result_t, zet_context_handle_t, zet_device_handle_t, c_ulong, POINTER(zet_metric_group_handle_t), POINTER(zet_metric_tracer_exp_desc_t), ze_event_handle_t, POINTER(zet_metric_tracer_exp_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricTracerDestroyExp
if __use_win_types:
    _zetMetricTracerDestroyExp_t = WINFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t )
else:
    _zetMetricTracerDestroyExp_t = CFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t )

###############################################################################
## @brief Function-pointer for zetMetricTracerEnableExp
if __use_win_types:
    _zetMetricTracerEnableExp_t = WINFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t, ze_bool_t )
else:
    _zetMetricTracerEnableExp_t = CFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t, ze_bool_t )

###############################################################################
## @brief Function-pointer for zetMetricTracerDisableExp
if __use_win_types:
    _zetMetricTracerDisableExp_t = WINFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t, ze_bool_t )
else:
    _zetMetricTracerDisableExp_t = CFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t, ze_bool_t )

###############################################################################
## @brief Function-pointer for zetMetricTracerReadDataExp
if __use_win_types:
    _zetMetricTracerReadDataExp_t = WINFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t, POINTER(c_size_t), POINTER(c_ubyte) )
else:
    _zetMetricTracerReadDataExp_t = CFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t, POINTER(c_size_t), POINTER(c_ubyte) )

###############################################################################
## @brief Function-pointer for zetMetricTracerDecodeExp
if __use_win_types:
    _zetMetricTracerDecodeExp_t = WINFUNCTYPE( ze_result_t, zet_metric_decoder_exp_handle_t, POINTER(c_size_t), POINTER(c_ubyte), c_ulong, POINTER(zet_metric_handle_t), POINTER(c_ulong), POINTER(c_ulong), POINTER(c_ulong), POINTER(zet_metric_entry_exp_t) )
else:
    _zetMetricTracerDecodeExp_t = CFUNCTYPE( ze_result_t, zet_metric_decoder_exp_handle_t, POINTER(c_size_t), POINTER(c_ubyte), c_ulong, POINTER(zet_metric_handle_t), POINTER(c_ulong), POINTER(c_ulong), POINTER(c_ulong), POINTER(zet_metric_entry_exp_t) )


###############################################################################
## @brief Table of MetricTracerExp functions pointers
class _zet_metric_tracer_exp_dditable_t(Structure):
    _fields_ = [
        ("pfnCreateExp", c_void_p),                                     ## _zetMetricTracerCreateExp_t
        ("pfnDestroyExp", c_void_p),                                    ## _zetMetricTracerDestroyExp_t
        ("pfnEnableExp", c_void_p),                                     ## _zetMetricTracerEnableExp_t
        ("pfnDisableExp", c_void_p),                                    ## _zetMetricTracerDisableExp_t
        ("pfnReadDataExp", c_void_p),                                   ## _zetMetricTracerReadDataExp_t
        ("pfnDecodeExp", c_void_p)                                      ## _zetMetricTracerDecodeExp_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricDecoderCreateExp
if __use_win_types:
    _zetMetricDecoderCreateExp_t = WINFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t, POINTER(zet_metric_decoder_exp_handle_t) )
else:
    _zetMetricDecoderCreateExp_t = CFUNCTYPE( ze_result_t, zet_metric_tracer_exp_handle_t, POINTER(zet_metric_decoder_exp_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricDecoderDestroyExp
if __use_win_types:
    _zetMetricDecoderDestroyExp_t = WINFUNCTYPE( ze_result_t, zet_metric_decoder_exp_handle_t )
else:
    _zetMetricDecoderDestroyExp_t = CFUNCTYPE( ze_result_t, zet_metric_decoder_exp_handle_t )

###############################################################################
## @brief Function-pointer for zetMetricDecoderGetDecodableMetricsExp
if __use_win_types:
    _zetMetricDecoderGetDecodableMetricsExp_t = WINFUNCTYPE( ze_result_t, zet_metric_decoder_exp_handle_t, POINTER(c_ulong), POINTER(zet_metric_handle_t) )
else:
    _zetMetricDecoderGetDecodableMetricsExp_t = CFUNCTYPE( ze_result_t, zet_metric_decoder_exp_handle_t, POINTER(c_ulong), POINTER(zet_metric_handle_t) )


###############################################################################
## @brief Table of MetricDecoderExp functions pointers
class _zet_metric_decoder_exp_dditable_t(Structure):
    _fields_ = [
        ("pfnCreateExp", c_void_p),                                     ## _zetMetricDecoderCreateExp_t
        ("pfnDestroyExp", c_void_p),                                    ## _zetMetricDecoderDestroyExp_t
        ("pfnGetDecodableMetricsExp", c_void_p)                         ## _zetMetricDecoderGetDecodableMetricsExp_t
    ]

###############################################################################
## @brief Function-pointer for zetDeviceGetDebugProperties
if __use_win_types:
    _zetDeviceGetDebugProperties_t = WINFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(zet_device_debug_properties_t) )
else:
    _zetDeviceGetDebugProperties_t = CFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(zet_device_debug_properties_t) )


###############################################################################
## @brief Table of Device functions pointers
class _zet_device_dditable_t(Structure):
    _fields_ = [
        ("pfnGetDebugProperties", c_void_p)                             ## _zetDeviceGetDebugProperties_t
    ]

###############################################################################
## @brief Function-pointer for zetDeviceGetConcurrentMetricGroupsExp
if __use_win_types:
    _zetDeviceGetConcurrentMetricGroupsExp_t = WINFUNCTYPE( ze_result_t, zet_device_handle_t, c_ulong, *, *, * )
else:
    _zetDeviceGetConcurrentMetricGroupsExp_t = CFUNCTYPE( ze_result_t, zet_device_handle_t, c_ulong, *, *, * )

###############################################################################
## @brief Function-pointer for zetDeviceCreateMetricGroupsFromMetricsExp
if __use_win_types:
    _zetDeviceCreateMetricGroupsFromMetricsExp_t = WINFUNCTYPE( ze_result_t, zet_device_handle_t, c_ulong, *, *, *, *, POINTER(zet_metric_group_handle_t) )
else:
    _zetDeviceCreateMetricGroupsFromMetricsExp_t = CFUNCTYPE( ze_result_t, zet_device_handle_t, c_ulong, *, *, *, *, POINTER(zet_metric_group_handle_t) )


###############################################################################
## @brief Table of DeviceExp functions pointers
class _zet_device_exp_dditable_t(Structure):
    _fields_ = [
        ("pfnGetConcurrentMetricGroupsExp", c_void_p),                  ## _zetDeviceGetConcurrentMetricGroupsExp_t
        ("pfnCreateMetricGroupsFromMetricsExp", c_void_p)               ## _zetDeviceCreateMetricGroupsFromMetricsExp_t
    ]

###############################################################################
## @brief Function-pointer for zetContextActivateMetricGroups
if __use_win_types:
    _zetContextActivateMetricGroups_t = WINFUNCTYPE( ze_result_t, zet_context_handle_t, zet_device_handle_t, c_ulong, POINTER(zet_metric_group_handle_t) )
else:
    _zetContextActivateMetricGroups_t = CFUNCTYPE( ze_result_t, zet_context_handle_t, zet_device_handle_t, c_ulong, POINTER(zet_metric_group_handle_t) )


###############################################################################
## @brief Table of Context functions pointers
class _zet_context_dditable_t(Structure):
    _fields_ = [
        ("pfnActivateMetricGroups", c_void_p)                           ## _zetContextActivateMetricGroups_t
    ]

###############################################################################
## @brief Function-pointer for zetCommandListAppendMetricStreamerMarker
if __use_win_types:
    _zetCommandListAppendMetricStreamerMarker_t = WINFUNCTYPE( ze_result_t, zet_command_list_handle_t, zet_metric_streamer_handle_t, c_ulong )
else:
    _zetCommandListAppendMetricStreamerMarker_t = CFUNCTYPE( ze_result_t, zet_command_list_handle_t, zet_metric_streamer_handle_t, c_ulong )

###############################################################################
## @brief Function-pointer for zetCommandListAppendMetricQueryBegin
if __use_win_types:
    _zetCommandListAppendMetricQueryBegin_t = WINFUNCTYPE( ze_result_t, zet_command_list_handle_t, zet_metric_query_handle_t )
else:
    _zetCommandListAppendMetricQueryBegin_t = CFUNCTYPE( ze_result_t, zet_command_list_handle_t, zet_metric_query_handle_t )

###############################################################################
## @brief Function-pointer for zetCommandListAppendMetricQueryEnd
if __use_win_types:
    _zetCommandListAppendMetricQueryEnd_t = WINFUNCTYPE( ze_result_t, zet_command_list_handle_t, zet_metric_query_handle_t, ze_event_handle_t, c_ulong, POINTER(ze_event_handle_t) )
else:
    _zetCommandListAppendMetricQueryEnd_t = CFUNCTYPE( ze_result_t, zet_command_list_handle_t, zet_metric_query_handle_t, ze_event_handle_t, c_ulong, POINTER(ze_event_handle_t) )

###############################################################################
## @brief Function-pointer for zetCommandListAppendMetricMemoryBarrier
if __use_win_types:
    _zetCommandListAppendMetricMemoryBarrier_t = WINFUNCTYPE( ze_result_t, zet_command_list_handle_t )
else:
    _zetCommandListAppendMetricMemoryBarrier_t = CFUNCTYPE( ze_result_t, zet_command_list_handle_t )


###############################################################################
## @brief Table of CommandList functions pointers
class _zet_command_list_dditable_t(Structure):
    _fields_ = [
        ("pfnAppendMetricStreamerMarker", c_void_p),                    ## _zetCommandListAppendMetricStreamerMarker_t
        ("pfnAppendMetricQueryBegin", c_void_p),                        ## _zetCommandListAppendMetricQueryBegin_t
        ("pfnAppendMetricQueryEnd", c_void_p),                          ## _zetCommandListAppendMetricQueryEnd_t
        ("pfnAppendMetricMemoryBarrier", c_void_p)                      ## _zetCommandListAppendMetricMemoryBarrier_t
    ]

###############################################################################
## @brief Function-pointer for zetModuleGetDebugInfo
if __use_win_types:
    _zetModuleGetDebugInfo_t = WINFUNCTYPE( ze_result_t, zet_module_handle_t, zet_module_debug_info_format_t, POINTER(c_size_t), POINTER(c_ubyte) )
else:
    _zetModuleGetDebugInfo_t = CFUNCTYPE( ze_result_t, zet_module_handle_t, zet_module_debug_info_format_t, POINTER(c_size_t), POINTER(c_ubyte) )


###############################################################################
## @brief Table of Module functions pointers
class _zet_module_dditable_t(Structure):
    _fields_ = [
        ("pfnGetDebugInfo", c_void_p)                                   ## _zetModuleGetDebugInfo_t
    ]

###############################################################################
## @brief Function-pointer for zetKernelGetProfileInfo
if __use_win_types:
    _zetKernelGetProfileInfo_t = WINFUNCTYPE( ze_result_t, zet_kernel_handle_t, POINTER(zet_profile_properties_t) )
else:
    _zetKernelGetProfileInfo_t = CFUNCTYPE( ze_result_t, zet_kernel_handle_t, POINTER(zet_profile_properties_t) )


###############################################################################
## @brief Table of Kernel functions pointers
class _zet_kernel_dditable_t(Structure):
    _fields_ = [
        ("pfnGetProfileInfo", c_void_p)                                 ## _zetKernelGetProfileInfo_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricGet
if __use_win_types:
    _zetMetricGet_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t, POINTER(c_ulong), POINTER(zet_metric_handle_t) )
else:
    _zetMetricGet_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t, POINTER(c_ulong), POINTER(zet_metric_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricGetProperties
if __use_win_types:
    _zetMetricGetProperties_t = WINFUNCTYPE( ze_result_t, zet_metric_handle_t, POINTER(zet_metric_properties_t) )
else:
    _zetMetricGetProperties_t = CFUNCTYPE( ze_result_t, zet_metric_handle_t, POINTER(zet_metric_properties_t) )


###############################################################################
## @brief Table of Metric functions pointers
class _zet_metric_dditable_t(Structure):
    _fields_ = [
        ("pfnGet", c_void_p),                                           ## _zetMetricGet_t
        ("pfnGetProperties", c_void_p)                                  ## _zetMetricGetProperties_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricCreateFromProgrammableExp
if __use_win_types:
    _zetMetricCreateFromProgrammableExp_t = WINFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, POINTER(zet_metric_programmable_param_value_exp_t), c_ulong, c_char_p, c_char_p, POINTER(c_ulong), POINTER(zet_metric_handle_t) )
else:
    _zetMetricCreateFromProgrammableExp_t = CFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, POINTER(zet_metric_programmable_param_value_exp_t), c_ulong, c_char_p, c_char_p, POINTER(c_ulong), POINTER(zet_metric_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricDestroyExp
if __use_win_types:
    _zetMetricDestroyExp_t = WINFUNCTYPE( ze_result_t, zet_metric_handle_t )
else:
    _zetMetricDestroyExp_t = CFUNCTYPE( ze_result_t, zet_metric_handle_t )

###############################################################################
## @brief Function-pointer for zetMetricCreateFromProgrammableExp2
if __use_win_types:
    _zetMetricCreateFromProgrammableExp2_t = WINFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, c_ulong, POINTER(zet_metric_programmable_param_value_exp_t), c_char_p, c_char_p, POINTER(c_ulong), POINTER(zet_metric_handle_t) )
else:
    _zetMetricCreateFromProgrammableExp2_t = CFUNCTYPE( ze_result_t, zet_metric_programmable_exp_handle_t, c_ulong, POINTER(zet_metric_programmable_param_value_exp_t), c_char_p, c_char_p, POINTER(c_ulong), POINTER(zet_metric_handle_t) )


###############################################################################
## @brief Table of MetricExp functions pointers
class _zet_metric_exp_dditable_t(Structure):
    _fields_ = [
        ("pfnCreateFromProgrammableExp", c_void_p),                     ## _zetMetricCreateFromProgrammableExp_t
        ("pfnDestroyExp", c_void_p),                                    ## _zetMetricDestroyExp_t
        ("pfnCreateFromProgrammableExp2", c_void_p)                     ## _zetMetricCreateFromProgrammableExp2_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricGroupGet
if __use_win_types:
    _zetMetricGroupGet_t = WINFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(c_ulong), POINTER(zet_metric_group_handle_t) )
else:
    _zetMetricGroupGet_t = CFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(c_ulong), POINTER(zet_metric_group_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricGroupGetProperties
if __use_win_types:
    _zetMetricGroupGetProperties_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t, POINTER(zet_metric_group_properties_t) )
else:
    _zetMetricGroupGetProperties_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t, POINTER(zet_metric_group_properties_t) )

###############################################################################
## @brief Function-pointer for zetMetricGroupCalculateMetricValues
if __use_win_types:
    _zetMetricGroupCalculateMetricValues_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t, zet_metric_group_calculation_type_t, c_size_t, POINTER(c_ubyte), POINTER(c_ulong), POINTER(zet_typed_value_t) )
else:
    _zetMetricGroupCalculateMetricValues_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t, zet_metric_group_calculation_type_t, c_size_t, POINTER(c_ubyte), POINTER(c_ulong), POINTER(zet_typed_value_t) )


###############################################################################
## @brief Table of MetricGroup functions pointers
class _zet_metric_group_dditable_t(Structure):
    _fields_ = [
        ("pfnGet", c_void_p),                                           ## _zetMetricGroupGet_t
        ("pfnGetProperties", c_void_p),                                 ## _zetMetricGroupGetProperties_t
        ("pfnCalculateMetricValues", c_void_p)                          ## _zetMetricGroupCalculateMetricValues_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricGroupCalculateMultipleMetricValuesExp
if __use_win_types:
    _zetMetricGroupCalculateMultipleMetricValuesExp_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t, zet_metric_group_calculation_type_t, c_size_t, POINTER(c_ubyte), POINTER(c_ulong), POINTER(c_ulong), POINTER(c_ulong), POINTER(zet_typed_value_t) )
else:
    _zetMetricGroupCalculateMultipleMetricValuesExp_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t, zet_metric_group_calculation_type_t, c_size_t, POINTER(c_ubyte), POINTER(c_ulong), POINTER(c_ulong), POINTER(c_ulong), POINTER(zet_typed_value_t) )

###############################################################################
## @brief Function-pointer for zetMetricGroupGetGlobalTimestampsExp
if __use_win_types:
    _zetMetricGroupGetGlobalTimestampsExp_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t, ze_bool_t, POINTER(c_ulonglong), POINTER(c_ulonglong) )
else:
    _zetMetricGroupGetGlobalTimestampsExp_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t, ze_bool_t, POINTER(c_ulonglong), POINTER(c_ulonglong) )

###############################################################################
## @brief Function-pointer for zetMetricGroupGetExportDataExp
if __use_win_types:
    _zetMetricGroupGetExportDataExp_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t, POINTER(c_ubyte), c_size_t, POINTER(c_size_t), * )
else:
    _zetMetricGroupGetExportDataExp_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t, POINTER(c_ubyte), c_size_t, POINTER(c_size_t), * )

###############################################################################
## @brief Function-pointer for zetMetricGroupCalculateMetricExportDataExp
if __use_win_types:
    _zetMetricGroupCalculateMetricExportDataExp_t = WINFUNCTYPE( ze_result_t, ze_driver_handle_t, zet_metric_group_calculation_type_t, c_size_t, POINTER(c_ubyte), POINTER(zet_metric_calculate_exp_desc_t), POINTER(c_ulong), POINTER(c_ulong), POINTER(c_ulong), POINTER(zet_typed_value_t) )
else:
    _zetMetricGroupCalculateMetricExportDataExp_t = CFUNCTYPE( ze_result_t, ze_driver_handle_t, zet_metric_group_calculation_type_t, c_size_t, POINTER(c_ubyte), POINTER(zet_metric_calculate_exp_desc_t), POINTER(c_ulong), POINTER(c_ulong), POINTER(c_ulong), POINTER(zet_typed_value_t) )

###############################################################################
## @brief Function-pointer for zetMetricGroupCreateExp
if __use_win_types:
    _zetMetricGroupCreateExp_t = WINFUNCTYPE( ze_result_t, zet_device_handle_t, c_char_p, c_char_p, zet_metric_group_sampling_type_flags_t, POINTER(zet_metric_group_handle_t) )
else:
    _zetMetricGroupCreateExp_t = CFUNCTYPE( ze_result_t, zet_device_handle_t, c_char_p, c_char_p, zet_metric_group_sampling_type_flags_t, POINTER(zet_metric_group_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricGroupAddMetricExp
if __use_win_types:
    _zetMetricGroupAddMetricExp_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t, zet_metric_handle_t, *, c_char_p )
else:
    _zetMetricGroupAddMetricExp_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t, zet_metric_handle_t, *, c_char_p )

###############################################################################
## @brief Function-pointer for zetMetricGroupRemoveMetricExp
if __use_win_types:
    _zetMetricGroupRemoveMetricExp_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t, zet_metric_handle_t )
else:
    _zetMetricGroupRemoveMetricExp_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t, zet_metric_handle_t )

###############################################################################
## @brief Function-pointer for zetMetricGroupCloseExp
if __use_win_types:
    _zetMetricGroupCloseExp_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t )
else:
    _zetMetricGroupCloseExp_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t )

###############################################################################
## @brief Function-pointer for zetMetricGroupDestroyExp
if __use_win_types:
    _zetMetricGroupDestroyExp_t = WINFUNCTYPE( ze_result_t, zet_metric_group_handle_t )
else:
    _zetMetricGroupDestroyExp_t = CFUNCTYPE( ze_result_t, zet_metric_group_handle_t )


###############################################################################
## @brief Table of MetricGroupExp functions pointers
class _zet_metric_group_exp_dditable_t(Structure):
    _fields_ = [
        ("pfnCalculateMultipleMetricValuesExp", c_void_p),              ## _zetMetricGroupCalculateMultipleMetricValuesExp_t
        ("pfnGetGlobalTimestampsExp", c_void_p),                        ## _zetMetricGroupGetGlobalTimestampsExp_t
        ("pfnGetExportDataExp", c_void_p),                              ## _zetMetricGroupGetExportDataExp_t
        ("pfnCalculateMetricExportDataExp", c_void_p),                  ## _zetMetricGroupCalculateMetricExportDataExp_t
        ("pfnCreateExp", c_void_p),                                     ## _zetMetricGroupCreateExp_t
        ("pfnAddMetricExp", c_void_p),                                  ## _zetMetricGroupAddMetricExp_t
        ("pfnRemoveMetricExp", c_void_p),                               ## _zetMetricGroupRemoveMetricExp_t
        ("pfnCloseExp", c_void_p),                                      ## _zetMetricGroupCloseExp_t
        ("pfnDestroyExp", c_void_p)                                     ## _zetMetricGroupDestroyExp_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricStreamerOpen
if __use_win_types:
    _zetMetricStreamerOpen_t = WINFUNCTYPE( ze_result_t, zet_context_handle_t, zet_device_handle_t, zet_metric_group_handle_t, POINTER(zet_metric_streamer_desc_t), ze_event_handle_t, POINTER(zet_metric_streamer_handle_t) )
else:
    _zetMetricStreamerOpen_t = CFUNCTYPE( ze_result_t, zet_context_handle_t, zet_device_handle_t, zet_metric_group_handle_t, POINTER(zet_metric_streamer_desc_t), ze_event_handle_t, POINTER(zet_metric_streamer_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricStreamerClose
if __use_win_types:
    _zetMetricStreamerClose_t = WINFUNCTYPE( ze_result_t, zet_metric_streamer_handle_t )
else:
    _zetMetricStreamerClose_t = CFUNCTYPE( ze_result_t, zet_metric_streamer_handle_t )

###############################################################################
## @brief Function-pointer for zetMetricStreamerReadData
if __use_win_types:
    _zetMetricStreamerReadData_t = WINFUNCTYPE( ze_result_t, zet_metric_streamer_handle_t, c_ulong, POINTER(c_size_t), POINTER(c_ubyte) )
else:
    _zetMetricStreamerReadData_t = CFUNCTYPE( ze_result_t, zet_metric_streamer_handle_t, c_ulong, POINTER(c_size_t), POINTER(c_ubyte) )


###############################################################################
## @brief Table of MetricStreamer functions pointers
class _zet_metric_streamer_dditable_t(Structure):
    _fields_ = [
        ("pfnOpen", c_void_p),                                          ## _zetMetricStreamerOpen_t
        ("pfnClose", c_void_p),                                         ## _zetMetricStreamerClose_t
        ("pfnReadData", c_void_p)                                       ## _zetMetricStreamerReadData_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricQueryPoolCreate
if __use_win_types:
    _zetMetricQueryPoolCreate_t = WINFUNCTYPE( ze_result_t, zet_context_handle_t, zet_device_handle_t, zet_metric_group_handle_t, POINTER(zet_metric_query_pool_desc_t), POINTER(zet_metric_query_pool_handle_t) )
else:
    _zetMetricQueryPoolCreate_t = CFUNCTYPE( ze_result_t, zet_context_handle_t, zet_device_handle_t, zet_metric_group_handle_t, POINTER(zet_metric_query_pool_desc_t), POINTER(zet_metric_query_pool_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricQueryPoolDestroy
if __use_win_types:
    _zetMetricQueryPoolDestroy_t = WINFUNCTYPE( ze_result_t, zet_metric_query_pool_handle_t )
else:
    _zetMetricQueryPoolDestroy_t = CFUNCTYPE( ze_result_t, zet_metric_query_pool_handle_t )


###############################################################################
## @brief Table of MetricQueryPool functions pointers
class _zet_metric_query_pool_dditable_t(Structure):
    _fields_ = [
        ("pfnCreate", c_void_p),                                        ## _zetMetricQueryPoolCreate_t
        ("pfnDestroy", c_void_p)                                        ## _zetMetricQueryPoolDestroy_t
    ]

###############################################################################
## @brief Function-pointer for zetMetricQueryCreate
if __use_win_types:
    _zetMetricQueryCreate_t = WINFUNCTYPE( ze_result_t, zet_metric_query_pool_handle_t, c_ulong, POINTER(zet_metric_query_handle_t) )
else:
    _zetMetricQueryCreate_t = CFUNCTYPE( ze_result_t, zet_metric_query_pool_handle_t, c_ulong, POINTER(zet_metric_query_handle_t) )

###############################################################################
## @brief Function-pointer for zetMetricQueryDestroy
if __use_win_types:
    _zetMetricQueryDestroy_t = WINFUNCTYPE( ze_result_t, zet_metric_query_handle_t )
else:
    _zetMetricQueryDestroy_t = CFUNCTYPE( ze_result_t, zet_metric_query_handle_t )

###############################################################################
## @brief Function-pointer for zetMetricQueryReset
if __use_win_types:
    _zetMetricQueryReset_t = WINFUNCTYPE( ze_result_t, zet_metric_query_handle_t )
else:
    _zetMetricQueryReset_t = CFUNCTYPE( ze_result_t, zet_metric_query_handle_t )

###############################################################################
## @brief Function-pointer for zetMetricQueryGetData
if __use_win_types:
    _zetMetricQueryGetData_t = WINFUNCTYPE( ze_result_t, zet_metric_query_handle_t, POINTER(c_size_t), POINTER(c_ubyte) )
else:
    _zetMetricQueryGetData_t = CFUNCTYPE( ze_result_t, zet_metric_query_handle_t, POINTER(c_size_t), POINTER(c_ubyte) )


###############################################################################
## @brief Table of MetricQuery functions pointers
class _zet_metric_query_dditable_t(Structure):
    _fields_ = [
        ("pfnCreate", c_void_p),                                        ## _zetMetricQueryCreate_t
        ("pfnDestroy", c_void_p),                                       ## _zetMetricQueryDestroy_t
        ("pfnReset", c_void_p),                                         ## _zetMetricQueryReset_t
        ("pfnGetData", c_void_p)                                        ## _zetMetricQueryGetData_t
    ]

###############################################################################
## @brief Function-pointer for zetTracerExpCreate
if __use_win_types:
    _zetTracerExpCreate_t = WINFUNCTYPE( ze_result_t, zet_context_handle_t, POINTER(zet_tracer_exp_desc_t), POINTER(zet_tracer_exp_handle_t) )
else:
    _zetTracerExpCreate_t = CFUNCTYPE( ze_result_t, zet_context_handle_t, POINTER(zet_tracer_exp_desc_t), POINTER(zet_tracer_exp_handle_t) )

###############################################################################
## @brief Function-pointer for zetTracerExpDestroy
if __use_win_types:
    _zetTracerExpDestroy_t = WINFUNCTYPE( ze_result_t, zet_tracer_exp_handle_t )
else:
    _zetTracerExpDestroy_t = CFUNCTYPE( ze_result_t, zet_tracer_exp_handle_t )

###############################################################################
## @brief Function-pointer for zetTracerExpSetPrologues
if __use_win_types:
    _zetTracerExpSetPrologues_t = WINFUNCTYPE( ze_result_t, zet_tracer_exp_handle_t, POINTER(zet_core_callbacks_t) )
else:
    _zetTracerExpSetPrologues_t = CFUNCTYPE( ze_result_t, zet_tracer_exp_handle_t, POINTER(zet_core_callbacks_t) )

###############################################################################
## @brief Function-pointer for zetTracerExpSetEpilogues
if __use_win_types:
    _zetTracerExpSetEpilogues_t = WINFUNCTYPE( ze_result_t, zet_tracer_exp_handle_t, POINTER(zet_core_callbacks_t) )
else:
    _zetTracerExpSetEpilogues_t = CFUNCTYPE( ze_result_t, zet_tracer_exp_handle_t, POINTER(zet_core_callbacks_t) )

###############################################################################
## @brief Function-pointer for zetTracerExpSetEnabled
if __use_win_types:
    _zetTracerExpSetEnabled_t = WINFUNCTYPE( ze_result_t, zet_tracer_exp_handle_t, ze_bool_t )
else:
    _zetTracerExpSetEnabled_t = CFUNCTYPE( ze_result_t, zet_tracer_exp_handle_t, ze_bool_t )


###############################################################################
## @brief Table of TracerExp functions pointers
class _zet_tracer_exp_dditable_t(Structure):
    _fields_ = [
        ("pfnCreate", c_void_p),                                        ## _zetTracerExpCreate_t
        ("pfnDestroy", c_void_p),                                       ## _zetTracerExpDestroy_t
        ("pfnSetPrologues", c_void_p),                                  ## _zetTracerExpSetPrologues_t
        ("pfnSetEpilogues", c_void_p),                                  ## _zetTracerExpSetEpilogues_t
        ("pfnSetEnabled", c_void_p)                                     ## _zetTracerExpSetEnabled_t
    ]

###############################################################################
## @brief Function-pointer for zetDebugAttach
if __use_win_types:
    _zetDebugAttach_t = WINFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(zet_debug_config_t), POINTER(zet_debug_session_handle_t) )
else:
    _zetDebugAttach_t = CFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(zet_debug_config_t), POINTER(zet_debug_session_handle_t) )

###############################################################################
## @brief Function-pointer for zetDebugDetach
if __use_win_types:
    _zetDebugDetach_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t )
else:
    _zetDebugDetach_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t )

###############################################################################
## @brief Function-pointer for zetDebugReadEvent
if __use_win_types:
    _zetDebugReadEvent_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, c_ulonglong, POINTER(zet_debug_event_t) )
else:
    _zetDebugReadEvent_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, c_ulonglong, POINTER(zet_debug_event_t) )

###############################################################################
## @brief Function-pointer for zetDebugAcknowledgeEvent
if __use_win_types:
    _zetDebugAcknowledgeEvent_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, POINTER(zet_debug_event_t) )
else:
    _zetDebugAcknowledgeEvent_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, POINTER(zet_debug_event_t) )

###############################################################################
## @brief Function-pointer for zetDebugInterrupt
if __use_win_types:
    _zetDebugInterrupt_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t )
else:
    _zetDebugInterrupt_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t )

###############################################################################
## @brief Function-pointer for zetDebugResume
if __use_win_types:
    _zetDebugResume_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t )
else:
    _zetDebugResume_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t )

###############################################################################
## @brief Function-pointer for zetDebugReadMemory
if __use_win_types:
    _zetDebugReadMemory_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, POINTER(zet_debug_memory_space_desc_t), c_size_t, c_void_p )
else:
    _zetDebugReadMemory_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, POINTER(zet_debug_memory_space_desc_t), c_size_t, c_void_p )

###############################################################################
## @brief Function-pointer for zetDebugWriteMemory
if __use_win_types:
    _zetDebugWriteMemory_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, POINTER(zet_debug_memory_space_desc_t), c_size_t, c_void_p )
else:
    _zetDebugWriteMemory_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, POINTER(zet_debug_memory_space_desc_t), c_size_t, c_void_p )

###############################################################################
## @brief Function-pointer for zetDebugGetRegisterSetProperties
if __use_win_types:
    _zetDebugGetRegisterSetProperties_t = WINFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(c_ulong), POINTER(zet_debug_regset_properties_t) )
else:
    _zetDebugGetRegisterSetProperties_t = CFUNCTYPE( ze_result_t, zet_device_handle_t, POINTER(c_ulong), POINTER(zet_debug_regset_properties_t) )

###############################################################################
## @brief Function-pointer for zetDebugReadRegisters
if __use_win_types:
    _zetDebugReadRegisters_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, c_ulong, c_ulong, c_ulong, c_void_p )
else:
    _zetDebugReadRegisters_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, c_ulong, c_ulong, c_ulong, c_void_p )

###############################################################################
## @brief Function-pointer for zetDebugWriteRegisters
if __use_win_types:
    _zetDebugWriteRegisters_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, c_ulong, c_ulong, c_ulong, c_void_p )
else:
    _zetDebugWriteRegisters_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, c_ulong, c_ulong, c_ulong, c_void_p )

###############################################################################
## @brief Function-pointer for zetDebugGetThreadRegisterSetProperties
if __use_win_types:
    _zetDebugGetThreadRegisterSetProperties_t = WINFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, POINTER(c_ulong), POINTER(zet_debug_regset_properties_t) )
else:
    _zetDebugGetThreadRegisterSetProperties_t = CFUNCTYPE( ze_result_t, zet_debug_session_handle_t, ze_device_thread_t, POINTER(c_ulong), POINTER(zet_debug_regset_properties_t) )


###############################################################################
## @brief Table of Debug functions pointers
class _zet_debug_dditable_t(Structure):
    _fields_ = [
        ("pfnAttach", c_void_p),                                        ## _zetDebugAttach_t
        ("pfnDetach", c_void_p),                                        ## _zetDebugDetach_t
        ("pfnReadEvent", c_void_p),                                     ## _zetDebugReadEvent_t
        ("pfnAcknowledgeEvent", c_void_p),                              ## _zetDebugAcknowledgeEvent_t
        ("pfnInterrupt", c_void_p),                                     ## _zetDebugInterrupt_t
        ("pfnResume", c_void_p),                                        ## _zetDebugResume_t
        ("pfnReadMemory", c_void_p),                                    ## _zetDebugReadMemory_t
        ("pfnWriteMemory", c_void_p),                                   ## _zetDebugWriteMemory_t
        ("pfnGetRegisterSetProperties", c_void_p),                      ## _zetDebugGetRegisterSetProperties_t
        ("pfnReadRegisters", c_void_p),                                 ## _zetDebugReadRegisters_t
        ("pfnWriteRegisters", c_void_p),                                ## _zetDebugWriteRegisters_t
        ("pfnGetThreadRegisterSetProperties", c_void_p)                 ## _zetDebugGetThreadRegisterSetProperties_t
    ]

###############################################################################
class _zet_dditable_t(Structure):
    _fields_ = [
        ("MetricProgrammableExp", _zet_metric_programmable_exp_dditable_t),
        ("MetricTracerExp", _zet_metric_tracer_exp_dditable_t),
        ("MetricDecoderExp", _zet_metric_decoder_exp_dditable_t),
        ("Device", _zet_device_dditable_t),
        ("DeviceExp", _zet_device_exp_dditable_t),
        ("Context", _zet_context_dditable_t),
        ("CommandList", _zet_command_list_dditable_t),
        ("Module", _zet_module_dditable_t),
        ("Kernel", _zet_kernel_dditable_t),
        ("Metric", _zet_metric_dditable_t),
        ("MetricExp", _zet_metric_exp_dditable_t),
        ("MetricGroup", _zet_metric_group_dditable_t),
        ("MetricGroupExp", _zet_metric_group_exp_dditable_t),
        ("MetricStreamer", _zet_metric_streamer_dditable_t),
        ("MetricQueryPool", _zet_metric_query_pool_dditable_t),
        ("MetricQuery", _zet_metric_query_dditable_t),
        ("TracerExp", _zet_tracer_exp_dditable_t),
        ("Debug", _zet_debug_dditable_t)
    ]

###############################################################################
## @brief zet device-driver interfaces
class ZET_DDI:
    def __init__(self, version : ze_api_version_t):
        # load the ze_loader library
        if "Windows" == platform.uname()[0]:
            self.__dll = WinDLL("ze_loader.dll")
        else:
            self.__dll = CDLL("ze_loader.so")

        # fill the ddi tables
        self.__dditable = _zet_dditable_t()

        # call driver to get function pointers
        _MetricProgrammableExp = _zet_metric_programmable_exp_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricProgrammableExpProcAddrTable(version, byref(_MetricProgrammableExp)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricProgrammableExp = _MetricProgrammableExp

        # attach function interface to function address
        self.zetMetricProgrammableGetExp = _zetMetricProgrammableGetExp_t(self.__dditable.MetricProgrammableExp.pfnGetExp)
        self.zetMetricProgrammableGetPropertiesExp = _zetMetricProgrammableGetPropertiesExp_t(self.__dditable.MetricProgrammableExp.pfnGetPropertiesExp)
        self.zetMetricProgrammableGetParamInfoExp = _zetMetricProgrammableGetParamInfoExp_t(self.__dditable.MetricProgrammableExp.pfnGetParamInfoExp)
        self.zetMetricProgrammableGetParamValueInfoExp = _zetMetricProgrammableGetParamValueInfoExp_t(self.__dditable.MetricProgrammableExp.pfnGetParamValueInfoExp)

        # call driver to get function pointers
        _MetricTracerExp = _zet_metric_tracer_exp_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricTracerExpProcAddrTable(version, byref(_MetricTracerExp)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricTracerExp = _MetricTracerExp

        # attach function interface to function address
        self.zetMetricTracerCreateExp = _zetMetricTracerCreateExp_t(self.__dditable.MetricTracerExp.pfnCreateExp)
        self.zetMetricTracerDestroyExp = _zetMetricTracerDestroyExp_t(self.__dditable.MetricTracerExp.pfnDestroyExp)
        self.zetMetricTracerEnableExp = _zetMetricTracerEnableExp_t(self.__dditable.MetricTracerExp.pfnEnableExp)
        self.zetMetricTracerDisableExp = _zetMetricTracerDisableExp_t(self.__dditable.MetricTracerExp.pfnDisableExp)
        self.zetMetricTracerReadDataExp = _zetMetricTracerReadDataExp_t(self.__dditable.MetricTracerExp.pfnReadDataExp)
        self.zetMetricTracerDecodeExp = _zetMetricTracerDecodeExp_t(self.__dditable.MetricTracerExp.pfnDecodeExp)

        # call driver to get function pointers
        _MetricDecoderExp = _zet_metric_decoder_exp_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricDecoderExpProcAddrTable(version, byref(_MetricDecoderExp)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricDecoderExp = _MetricDecoderExp

        # attach function interface to function address
        self.zetMetricDecoderCreateExp = _zetMetricDecoderCreateExp_t(self.__dditable.MetricDecoderExp.pfnCreateExp)
        self.zetMetricDecoderDestroyExp = _zetMetricDecoderDestroyExp_t(self.__dditable.MetricDecoderExp.pfnDestroyExp)
        self.zetMetricDecoderGetDecodableMetricsExp = _zetMetricDecoderGetDecodableMetricsExp_t(self.__dditable.MetricDecoderExp.pfnGetDecodableMetricsExp)

        # call driver to get function pointers
        _Device = _zet_device_dditable_t()
        r = ze_result_v(self.__dll.zetGetDeviceProcAddrTable(version, byref(_Device)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.Device = _Device

        # attach function interface to function address
        self.zetDeviceGetDebugProperties = _zetDeviceGetDebugProperties_t(self.__dditable.Device.pfnGetDebugProperties)

        # call driver to get function pointers
        _DeviceExp = _zet_device_exp_dditable_t()
        r = ze_result_v(self.__dll.zetGetDeviceExpProcAddrTable(version, byref(_DeviceExp)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.DeviceExp = _DeviceExp

        # attach function interface to function address
        self.zetDeviceGetConcurrentMetricGroupsExp = _zetDeviceGetConcurrentMetricGroupsExp_t(self.__dditable.DeviceExp.pfnGetConcurrentMetricGroupsExp)
        self.zetDeviceCreateMetricGroupsFromMetricsExp = _zetDeviceCreateMetricGroupsFromMetricsExp_t(self.__dditable.DeviceExp.pfnCreateMetricGroupsFromMetricsExp)

        # call driver to get function pointers
        _Context = _zet_context_dditable_t()
        r = ze_result_v(self.__dll.zetGetContextProcAddrTable(version, byref(_Context)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.Context = _Context

        # attach function interface to function address
        self.zetContextActivateMetricGroups = _zetContextActivateMetricGroups_t(self.__dditable.Context.pfnActivateMetricGroups)

        # call driver to get function pointers
        _CommandList = _zet_command_list_dditable_t()
        r = ze_result_v(self.__dll.zetGetCommandListProcAddrTable(version, byref(_CommandList)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.CommandList = _CommandList

        # attach function interface to function address
        self.zetCommandListAppendMetricStreamerMarker = _zetCommandListAppendMetricStreamerMarker_t(self.__dditable.CommandList.pfnAppendMetricStreamerMarker)
        self.zetCommandListAppendMetricQueryBegin = _zetCommandListAppendMetricQueryBegin_t(self.__dditable.CommandList.pfnAppendMetricQueryBegin)
        self.zetCommandListAppendMetricQueryEnd = _zetCommandListAppendMetricQueryEnd_t(self.__dditable.CommandList.pfnAppendMetricQueryEnd)
        self.zetCommandListAppendMetricMemoryBarrier = _zetCommandListAppendMetricMemoryBarrier_t(self.__dditable.CommandList.pfnAppendMetricMemoryBarrier)

        # call driver to get function pointers
        _Module = _zet_module_dditable_t()
        r = ze_result_v(self.__dll.zetGetModuleProcAddrTable(version, byref(_Module)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.Module = _Module

        # attach function interface to function address
        self.zetModuleGetDebugInfo = _zetModuleGetDebugInfo_t(self.__dditable.Module.pfnGetDebugInfo)

        # call driver to get function pointers
        _Kernel = _zet_kernel_dditable_t()
        r = ze_result_v(self.__dll.zetGetKernelProcAddrTable(version, byref(_Kernel)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.Kernel = _Kernel

        # attach function interface to function address
        self.zetKernelGetProfileInfo = _zetKernelGetProfileInfo_t(self.__dditable.Kernel.pfnGetProfileInfo)

        # call driver to get function pointers
        _Metric = _zet_metric_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricProcAddrTable(version, byref(_Metric)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.Metric = _Metric

        # attach function interface to function address
        self.zetMetricGet = _zetMetricGet_t(self.__dditable.Metric.pfnGet)
        self.zetMetricGetProperties = _zetMetricGetProperties_t(self.__dditable.Metric.pfnGetProperties)

        # call driver to get function pointers
        _MetricExp = _zet_metric_exp_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricExpProcAddrTable(version, byref(_MetricExp)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricExp = _MetricExp

        # attach function interface to function address
        self.zetMetricCreateFromProgrammableExp = _zetMetricCreateFromProgrammableExp_t(self.__dditable.MetricExp.pfnCreateFromProgrammableExp)
        self.zetMetricDestroyExp = _zetMetricDestroyExp_t(self.__dditable.MetricExp.pfnDestroyExp)
        self.zetMetricCreateFromProgrammableExp2 = _zetMetricCreateFromProgrammableExp2_t(self.__dditable.MetricExp.pfnCreateFromProgrammableExp2)

        # call driver to get function pointers
        _MetricGroup = _zet_metric_group_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricGroupProcAddrTable(version, byref(_MetricGroup)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricGroup = _MetricGroup

        # attach function interface to function address
        self.zetMetricGroupGet = _zetMetricGroupGet_t(self.__dditable.MetricGroup.pfnGet)
        self.zetMetricGroupGetProperties = _zetMetricGroupGetProperties_t(self.__dditable.MetricGroup.pfnGetProperties)
        self.zetMetricGroupCalculateMetricValues = _zetMetricGroupCalculateMetricValues_t(self.__dditable.MetricGroup.pfnCalculateMetricValues)

        # call driver to get function pointers
        _MetricGroupExp = _zet_metric_group_exp_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricGroupExpProcAddrTable(version, byref(_MetricGroupExp)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricGroupExp = _MetricGroupExp

        # attach function interface to function address
        self.zetMetricGroupCalculateMultipleMetricValuesExp = _zetMetricGroupCalculateMultipleMetricValuesExp_t(self.__dditable.MetricGroupExp.pfnCalculateMultipleMetricValuesExp)
        self.zetMetricGroupGetGlobalTimestampsExp = _zetMetricGroupGetGlobalTimestampsExp_t(self.__dditable.MetricGroupExp.pfnGetGlobalTimestampsExp)
        self.zetMetricGroupGetExportDataExp = _zetMetricGroupGetExportDataExp_t(self.__dditable.MetricGroupExp.pfnGetExportDataExp)
        self.zetMetricGroupCalculateMetricExportDataExp = _zetMetricGroupCalculateMetricExportDataExp_t(self.__dditable.MetricGroupExp.pfnCalculateMetricExportDataExp)
        self.zetMetricGroupCreateExp = _zetMetricGroupCreateExp_t(self.__dditable.MetricGroupExp.pfnCreateExp)
        self.zetMetricGroupAddMetricExp = _zetMetricGroupAddMetricExp_t(self.__dditable.MetricGroupExp.pfnAddMetricExp)
        self.zetMetricGroupRemoveMetricExp = _zetMetricGroupRemoveMetricExp_t(self.__dditable.MetricGroupExp.pfnRemoveMetricExp)
        self.zetMetricGroupCloseExp = _zetMetricGroupCloseExp_t(self.__dditable.MetricGroupExp.pfnCloseExp)
        self.zetMetricGroupDestroyExp = _zetMetricGroupDestroyExp_t(self.__dditable.MetricGroupExp.pfnDestroyExp)

        # call driver to get function pointers
        _MetricStreamer = _zet_metric_streamer_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricStreamerProcAddrTable(version, byref(_MetricStreamer)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricStreamer = _MetricStreamer

        # attach function interface to function address
        self.zetMetricStreamerOpen = _zetMetricStreamerOpen_t(self.__dditable.MetricStreamer.pfnOpen)
        self.zetMetricStreamerClose = _zetMetricStreamerClose_t(self.__dditable.MetricStreamer.pfnClose)
        self.zetMetricStreamerReadData = _zetMetricStreamerReadData_t(self.__dditable.MetricStreamer.pfnReadData)

        # call driver to get function pointers
        _MetricQueryPool = _zet_metric_query_pool_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricQueryPoolProcAddrTable(version, byref(_MetricQueryPool)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricQueryPool = _MetricQueryPool

        # attach function interface to function address
        self.zetMetricQueryPoolCreate = _zetMetricQueryPoolCreate_t(self.__dditable.MetricQueryPool.pfnCreate)
        self.zetMetricQueryPoolDestroy = _zetMetricQueryPoolDestroy_t(self.__dditable.MetricQueryPool.pfnDestroy)

        # call driver to get function pointers
        _MetricQuery = _zet_metric_query_dditable_t()
        r = ze_result_v(self.__dll.zetGetMetricQueryProcAddrTable(version, byref(_MetricQuery)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.MetricQuery = _MetricQuery

        # attach function interface to function address
        self.zetMetricQueryCreate = _zetMetricQueryCreate_t(self.__dditable.MetricQuery.pfnCreate)
        self.zetMetricQueryDestroy = _zetMetricQueryDestroy_t(self.__dditable.MetricQuery.pfnDestroy)
        self.zetMetricQueryReset = _zetMetricQueryReset_t(self.__dditable.MetricQuery.pfnReset)
        self.zetMetricQueryGetData = _zetMetricQueryGetData_t(self.__dditable.MetricQuery.pfnGetData)

        # call driver to get function pointers
        _TracerExp = _zet_tracer_exp_dditable_t()
        r = ze_result_v(self.__dll.zetGetTracerExpProcAddrTable(version, byref(_TracerExp)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.TracerExp = _TracerExp

        # attach function interface to function address
        self.zetTracerExpCreate = _zetTracerExpCreate_t(self.__dditable.TracerExp.pfnCreate)
        self.zetTracerExpDestroy = _zetTracerExpDestroy_t(self.__dditable.TracerExp.pfnDestroy)
        self.zetTracerExpSetPrologues = _zetTracerExpSetPrologues_t(self.__dditable.TracerExp.pfnSetPrologues)
        self.zetTracerExpSetEpilogues = _zetTracerExpSetEpilogues_t(self.__dditable.TracerExp.pfnSetEpilogues)
        self.zetTracerExpSetEnabled = _zetTracerExpSetEnabled_t(self.__dditable.TracerExp.pfnSetEnabled)

        # call driver to get function pointers
        _Debug = _zet_debug_dditable_t()
        r = ze_result_v(self.__dll.zetGetDebugProcAddrTable(version, byref(_Debug)))
        if r != ze_result_v.SUCCESS:
            raise Exception(r)
        self.__dditable.Debug = _Debug

        # attach function interface to function address
        self.zetDebugAttach = _zetDebugAttach_t(self.__dditable.Debug.pfnAttach)
        self.zetDebugDetach = _zetDebugDetach_t(self.__dditable.Debug.pfnDetach)
        self.zetDebugReadEvent = _zetDebugReadEvent_t(self.__dditable.Debug.pfnReadEvent)
        self.zetDebugAcknowledgeEvent = _zetDebugAcknowledgeEvent_t(self.__dditable.Debug.pfnAcknowledgeEvent)
        self.zetDebugInterrupt = _zetDebugInterrupt_t(self.__dditable.Debug.pfnInterrupt)
        self.zetDebugResume = _zetDebugResume_t(self.__dditable.Debug.pfnResume)
        self.zetDebugReadMemory = _zetDebugReadMemory_t(self.__dditable.Debug.pfnReadMemory)
        self.zetDebugWriteMemory = _zetDebugWriteMemory_t(self.__dditable.Debug.pfnWriteMemory)
        self.zetDebugGetRegisterSetProperties = _zetDebugGetRegisterSetProperties_t(self.__dditable.Debug.pfnGetRegisterSetProperties)
        self.zetDebugReadRegisters = _zetDebugReadRegisters_t(self.__dditable.Debug.pfnReadRegisters)
        self.zetDebugWriteRegisters = _zetDebugWriteRegisters_t(self.__dditable.Debug.pfnWriteRegisters)
        self.zetDebugGetThreadRegisterSetProperties = _zetDebugGetThreadRegisterSetProperties_t(self.__dditable.Debug.pfnGetThreadRegisterSetProperties)

        # success!
