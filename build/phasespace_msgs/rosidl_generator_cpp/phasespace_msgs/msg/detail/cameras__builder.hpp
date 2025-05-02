// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from phasespace_msgs:msg/Cameras.idl
// generated code does not contain a copyright notice

#ifndef PHASESPACE_MSGS__MSG__DETAIL__CAMERAS__BUILDER_HPP_
#define PHASESPACE_MSGS__MSG__DETAIL__CAMERAS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "phasespace_msgs/msg/detail/cameras__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace phasespace_msgs
{

namespace msg
{

namespace builder
{

class Init_Cameras_cameras
{
public:
  Init_Cameras_cameras()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::phasespace_msgs::msg::Cameras cameras(::phasespace_msgs::msg::Cameras::_cameras_type arg)
  {
    msg_.cameras = std::move(arg);
    return std::move(msg_);
  }

private:
  ::phasespace_msgs::msg::Cameras msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::phasespace_msgs::msg::Cameras>()
{
  return phasespace_msgs::msg::builder::Init_Cameras_cameras();
}

}  // namespace phasespace_msgs

#endif  // PHASESPACE_MSGS__MSG__DETAIL__CAMERAS__BUILDER_HPP_
