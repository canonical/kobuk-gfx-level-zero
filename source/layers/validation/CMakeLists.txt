# Copyright (C) 2020-2023 Intel Corporation
# SPDX-License-Identifier: MIT
set(TARGET_NAME ze_validation_layer)

configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/ZeValidationLayerVersion.rc.in
    ${CMAKE_CURRENT_BINARY_DIR}/ZeValidationLayerVersion.rc
    @ONLY)

add_library(${TARGET_NAME}
    SHARED
        ${CMAKE_CURRENT_SOURCE_DIR}/ze_validation_layer.h
        ${CMAKE_CURRENT_SOURCE_DIR}/ze_validation_layer.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/ze_valddi.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/zet_valddi.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/zes_valddi.cpp
        ${CMAKE_CURRENT_BINARY_DIR}/ZeValidationLayerVersion.rc
)

target_include_directories(${TARGET_NAME}
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CMAKE_CURRENT_SOURCE_DIR}/common
        ${CMAKE_CURRENT_SOURCE_DIR}/handle_lifetime_tracking
        ${CMAKE_CURRENT_SOURCE_DIR}/checkers/parameter_validation
        ${CMAKE_CURRENT_SOURCE_DIR}/checkers/template
        ${CMAKE_CURRENT_SOURCE_DIR}/../../utils
)

target_link_libraries(${TARGET_NAME} PRIVATE level_zero_utils)

if(UNIX)
    set(GCC_COVERAGE_COMPILE_FLAGS "-fvisibility=hidden -fvisibility-inlines-hidden")
    set(CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} ${GCC_COVERAGE_COMPILE_FLAGS}")
endif()

set_target_properties(${TARGET_NAME} PROPERTIES
    VERSION "${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}.${PROJECT_VERSION_PATCH}"
    SOVERSION  "${PROJECT_VERSION_MAJOR}"
)

install(TARGETS ze_validation_layer
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR} COMPONENT level-zero-devel
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR} COMPONENT level-zero
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR} COMPONENT level-zero
    NAMELINK_COMPONENT level-zero-devel
)

add_subdirectory(handle_lifetime_tracking)
add_subdirectory(checkers)
