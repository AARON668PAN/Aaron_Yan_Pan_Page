# generated from rosidl_generator_py/resource/_idl.py.em
# with input from phasespace_msgs:msg/Camera.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Camera(type):
    """Metaclass of message 'Camera'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('phasespace_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'phasespace_msgs.msg.Camera')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__camera
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__camera
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__camera
            cls._TYPE_SUPPORT = module.type_support_msg__msg__camera
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__camera

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Camera(metaclass=Metaclass_Camera):
    """Message class 'Camera'."""

    __slots__ = [
        '_id',
        '_flags',
        '_x',
        '_y',
        '_z',
        '_qw',
        '_qx',
        '_qy',
        '_qz',
        '_cond',
    ]

    _fields_and_field_types = {
        'id': 'uint32',
        'flags': 'uint32',
        'x': 'float',
        'y': 'float',
        'z': 'float',
        'qw': 'float',
        'qx': 'float',
        'qy': 'float',
        'qz': 'float',
        'cond': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.id = kwargs.get('id', int())
        self.flags = kwargs.get('flags', int())
        self.x = kwargs.get('x', float())
        self.y = kwargs.get('y', float())
        self.z = kwargs.get('z', float())
        self.qw = kwargs.get('qw', float())
        self.qx = kwargs.get('qx', float())
        self.qy = kwargs.get('qy', float())
        self.qz = kwargs.get('qz', float())
        self.cond = kwargs.get('cond', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.id != other.id:
            return False
        if self.flags != other.flags:
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.z != other.z:
            return False
        if self.qw != other.qw:
            return False
        if self.qx != other.qx:
            return False
        if self.qy != other.qy:
            return False
        if self.qz != other.qz:
            return False
        if self.cond != other.cond:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property  # noqa: A003
    def id(self):  # noqa: A003
        """Message field 'id'."""
        return self._id

    @id.setter  # noqa: A003
    def id(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'id' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'id' field must be an unsigned integer in [0, 4294967295]"
        self._id = value

    @builtins.property
    def flags(self):
        """Message field 'flags'."""
        return self._flags

    @flags.setter
    def flags(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'flags' field must be of type 'int'"
            assert value >= 0 and value < 4294967296, \
                "The 'flags' field must be an unsigned integer in [0, 4294967295]"
        self._flags = value

    @builtins.property
    def x(self):
        """Message field 'x'."""
        return self._x

    @x.setter
    def x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._x = value

    @builtins.property
    def y(self):
        """Message field 'y'."""
        return self._y

    @y.setter
    def y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._y = value

    @builtins.property
    def z(self):
        """Message field 'z'."""
        return self._z

    @z.setter
    def z(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'z' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._z = value

    @builtins.property
    def qw(self):
        """Message field 'qw'."""
        return self._qw

    @qw.setter
    def qw(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'qw' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'qw' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._qw = value

    @builtins.property
    def qx(self):
        """Message field 'qx'."""
        return self._qx

    @qx.setter
    def qx(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'qx' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'qx' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._qx = value

    @builtins.property
    def qy(self):
        """Message field 'qy'."""
        return self._qy

    @qy.setter
    def qy(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'qy' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'qy' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._qy = value

    @builtins.property
    def qz(self):
        """Message field 'qz'."""
        return self._qz

    @qz.setter
    def qz(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'qz' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'qz' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._qz = value

    @builtins.property
    def cond(self):
        """Message field 'cond'."""
        return self._cond

    @cond.setter
    def cond(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cond' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'cond' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._cond = value
