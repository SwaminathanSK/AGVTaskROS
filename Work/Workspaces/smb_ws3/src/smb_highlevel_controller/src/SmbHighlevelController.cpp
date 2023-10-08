#include <smb_highlevel_controller/SmbHighlevelController.hpp>
#include<std_msgs/String.h>
#include<geometry_msgs/Twist.h>
#include<sensor_msgs/LaserScan.h>

void scannerCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
{
  for(int i = 0; i<360; i++){
    ROS_INFO("[%f] ", msg->ranges[i]);
  }
}

namespace smb_highlevel_controller {

SmbHighlevelController::SmbHighlevelController(ros::NodeHandle& nodeHandle) :
  nodeHandle_(nodeHandle)
{
  ros::Subscriber subscriber = nodeHandle.subscribe("/scan", 1000, scannerCallback);
  ros::Publisher publisher = nodeHandle.advertise<geometry_msgs::Twist>("/cmd_vel", 1000);
}

SmbHighlevelController::~SmbHighlevelController()
{
  
}

} /* namespace */
