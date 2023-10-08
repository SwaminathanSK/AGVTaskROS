#include <smb_highlevel_controller/SmbHighlevelController.hpp>
#include<std_msgs/String.h>
#include<sensor_msgs/LaserScan.h>

void scannerCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
{
  ROS_INFO("The mininum range is [%f]", msg->range_min);
}

namespace smb_highlevel_controller {

SmbHighlevelController::SmbHighlevelController(ros::NodeHandle& nodeHandle) :
  nodeHandle_(nodeHandle)
{
  ros::Subscriber subscriber = nodeHandle.subscribe("/scan", 1000, scannerCallback);
}

SmbHighlevelController::~SmbHighlevelController()
{
  
}

} /* namespace */
