// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from phasespace_msgs:msg/Rigids.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "phasespace_msgs/msg/detail/rigids__struct.h"
#include "phasespace_msgs/msg/detail/rigids__functions.h"

#include "rosidl_runtime_c/primitives_sequence.h"
#include "rosidl_runtime_c/primitives_sequence_functions.h"

// Nested array functions includes
#include "phasespace_msgs/msg/detail/rigid__functions.h"
// end nested array functions include
bool phasespace_msgs__msg__rigid__convert_from_py(PyObject * _pymsg, void * _ros_message);
PyObject * phasespace_msgs__msg__rigid__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool phasespace_msgs__msg__rigids__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[35];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("phasespace_msgs.msg._rigids.Rigids", full_classname_dest, 34) == 0);
  }
  phasespace_msgs__msg__Rigids * ros_message = _ros_message;
  {  // rigids
    PyObject * field = PyObject_GetAttrString(_pymsg, "rigids");
    if (!field) {
      return false;
    }
    PyObject * seq_field = PySequence_Fast(field, "expected a sequence in 'rigids'");
    if (!seq_field) {
      Py_DECREF(field);
      return false;
    }
    Py_ssize_t size = PySequence_Size(field);
    if (-1 == size) {
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    if (!phasespace_msgs__msg__Rigid__Sequence__init(&(ros_message->rigids), size)) {
      PyErr_SetString(PyExc_RuntimeError, "unable to create phasespace_msgs__msg__Rigid__Sequence ros_message");
      Py_DECREF(seq_field);
      Py_DECREF(field);
      return false;
    }
    phasespace_msgs__msg__Rigid * dest = ros_message->rigids.data;
    for (Py_ssize_t i = 0; i < size; ++i) {
      if (!phasespace_msgs__msg__rigid__convert_from_py(PySequence_Fast_GET_ITEM(seq_field, i), &dest[i])) {
        Py_DECREF(seq_field);
        Py_DECREF(field);
        return false;
      }
    }
    Py_DECREF(seq_field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * phasespace_msgs__msg__rigids__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Rigids */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("phasespace_msgs.msg._rigids");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Rigids");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  phasespace_msgs__msg__Rigids * ros_message = (phasespace_msgs__msg__Rigids *)raw_ros_message;
  {  // rigids
    PyObject * field = NULL;
    size_t size = ros_message->rigids.size;
    field = PyList_New(size);
    if (!field) {
      return NULL;
    }
    phasespace_msgs__msg__Rigid * item;
    for (size_t i = 0; i < size; ++i) {
      item = &(ros_message->rigids.data[i]);
      PyObject * pyitem = phasespace_msgs__msg__rigid__convert_to_py(item);
      if (!pyitem) {
        Py_DECREF(field);
        return NULL;
      }
      int rc = PyList_SetItem(field, i, pyitem);
      (void)rc;
      assert(rc == 0);
    }
    assert(PySequence_Check(field));
    {
      int rc = PyObject_SetAttrString(_pymessage, "rigids", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
