
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import yaml

def talker():
    twist_msg = Twist()
    with open("~/Workspaces/task_ws2/bag/cmd_vel.yaml", "r") as file_handle:
        data = yaml.load(file_handle)
        for list_doc in data:
            linear = list_doc["linear"]
            angular = list_doc["angular"]
            twist_msg.linear.x = linear["x"] 
            twist_msg.linear.y = linear["y"] 
            twist_msg.linear.z = linear["z"] 
            twist_msg.angular.x = angular["x"] 
            twist_msg.angular.y = angular["y"] 
            twist_msg.angular.z = angular["z"] 

            pub = rospy.Publisher('noise', Twist, queue_size=10)
            rospy.init_node('talker', anonymous=True)
            rate = rospy.Rate(10) # 10hz
            while not rospy.is_shutdown():
                hello_str = "hello world %s" % rospy.get_time()
                rospy.loginfo(hello_str)
                pub.publish(hello_str)
                rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass