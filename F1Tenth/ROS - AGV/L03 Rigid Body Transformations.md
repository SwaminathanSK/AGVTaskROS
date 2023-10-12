**Global Map** - Ties submaps together.
### Coordinate frame:
A set of orthogonal axes attached to a body that serves to describe pos of points relative to that body.
![eb70e90b599e72568eb906265981c127.png](../_resources/eb70e90b599e72568eb906265981c127.png)
![a5cb5aecf1443467d3e92faa1a7496d6.png](../_resources/a5cb5aecf1443467d3e92faa1a7496d6.png)
![df94bd149fea5c26b43c1c4c0be9670c.png](../_resources/df94bd149fea5c26b43c1c4c0be9670c.png)

map frame - wrt map
sensor frame - wrt sensor

stattc transform - rigid body
dynamic transform - example: map and car.

![7ff0c10b81d9d71688d10a429670fc8d.png](../_resources/7ff0c10b81d9d71688d10a429670fc8d.png)
![f4c481310a7b688b68b6088e4ef7aaf1.png](../_resources/f4c481310a7b688b68b6088e4ef7aaf1.png)

odom - Not exactly a frame. Describes the history between two frames: base_link and map. 
Odometry_message provides pose estimation and pose is relative to the odom frame.

**An example:**
In TTC only one value of threshold is defined. But depending on what frame we choose on the car, the distance between the car and wall differs with direction.
Thus best way to overcome this is to use the centre of the car as the frame.

Note that LIDAR is at the front of the car. How do we transform measurements from LIDAR to the newer frame?

![94da8233cd8f403bf896feb306ef2070.png](../_resources/94da8233cd8f403bf896feb306ef2070.png)

![2676783441e05f14d429abe6b28c2407.png](../_resources/2676783441e05f14d429abe6b28c2407.png)

![444d75d22d64bbe9854ce3bfa1162d15.png](../_resources/444d75d22d64bbe9854ce3bfa1162d15.png)

![14ab7c5195f3c2ea0bb627f783ded774.png](../_resources/14ab7c5195f3c2ea0bb627f783ded774.png)

![60ea852febb72e1a32314bd0e16550aa.png](../_resources/60ea852febb72e1a32314bd0e16550aa.png)

Note that we are calcuating the point B with respect to the frame A. Now, in case of translation:
![9fbc5fc274a6b93a3f0087ae82221bcc.png](../_resources/9fbc5fc274a6b93a3f0087ae82221bcc.png)
![268f7e8c1e276ae3e94a339ba6964960.png](../_resources/268f7e8c1e276ae3e94a339ba6964960.png)

Now, putting it together:
![f4d9c0ab6e2e8114ba6b6c1467cd97da.png](../_resources/f4d9c0ab6e2e8114ba6b6c1467cd97da.png)

![6983dbf5988f8999ef9dcad1fe323175.png](../_resources/6983dbf5988f8999ef9dcad1fe323175.png)