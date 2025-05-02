#include <iostream>
#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <phasespace_msgs/msg/markers.hpp>
#include <phasespace_msgs/msg/cameras.hpp>

using namespace std;

class ListenerNode : public rclcpp::Node
{
public:
  ListenerNode() : Node("listener")
  {

    // marker_sub_ = this->create_subscription<phasespace_msgs::msg::Markers>(
    //   "phasespace_markers", 10, std::bind(&ListenerNode::markerCallback, this, std::placeholders::_1));
    // camera_sub_ = this->create_subscription<phasespace_msgs::msg::Cameras>(
    //   "phasespace_cameras", 10, std::bind(&ListenerNode::cameraCallback, this, std::placeholders::_1));
    error_sub_ = this->create_subscription<std_msgs::msg::String>(
      "phasespace_errors", 10, std::bind(&ListenerNode::errorCallback, this, std::placeholders::_1));
  }

private:
  void errorCallback(const std_msgs::msg::String::SharedPtr msg)
  {
    RCLCPP_INFO(this->get_logger(), "message=%s", msg->data.c_str());
  }

  void cameraCallback(const phasespace_msgs::msg::Cameras::SharedPtr msg)
  {
    for (size_t i = 0; i < msg->cameras.size(); i++)
    {
      RCLCPP_INFO(this->get_logger(), 
        "id=%d pos[%f %f %f] rot[%f %f %f %f] cond=%f",
        msg->cameras[i].id,
        msg->cameras[i].x, msg->cameras[i].y, msg->cameras[i].z,
        msg->cameras[i].qw, msg->cameras[i].qx, msg->cameras[i].qy, msg->cameras[i].qz,
        msg->cameras[i].cond);
    }
  }

  void markerCallback(const phasespace_msgs::msg::Markers::SharedPtr msg)
  {
    for (size_t i = 0; i < msg->markers.size(); i++)
    {
      RCLCPP_INFO(this->get_logger(), 
        "t=%f id=%d [%f %f %f] cond=%f",
        msg->markers[i].time, msg->markers[i].id,
        msg->markers[i].x, msg->markers[i].y, msg->markers[i].z,
        msg->markers[i].cond);
    }
  }


  // rclcpp::Subscription<phasespace_msgs::msg::Markers>::SharedPtr marker_sub_;
  // rclcpp::Subscription<phasespace_msgs::msg::Cameras>::SharedPtr camera_sub_;
  rclcpp::Subscription<std_msgs::msg::String>::SharedPtr error_sub_;
};

int main(int argc, char **argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ListenerNode>());
  rclcpp::shutdown();
  return 0;
}

