## Installing Docker:
Source: https://www.simplilearn.com/tutorials/docker-tutorial/how-to-install-docker-on-ubuntu

`sudo apt install docker.io`
`sudo snap install docker` - Installs Dependencies

![59baecf61b8a1ae61db880576c256e52.png](../_resources/59baecf61b8a1ae61db880576c256e52.png)

![fb073bc1c14d1b5523dd6fc5428cd76e.png](../_resources/fb073bc1c14d1b5523dd6fc5428cd76e.png)

![c40a35b04c7ef470233c93cef7a9aadd.png](../_resources/c40a35b04c7ef470233c93cef7a9aadd.png)

Docker+ROS2 Review:
https://docs.google.com/presentation/d/1nzzvHQuBJAqdjlPDUl0l2_rU-MAu8jctu1Gt66vlHHM/edit#slide=id.g10838dd9226_0_25

## f1Tenth LAB 1:

**Running the container from the image (given repository):**
`$ docker run -it -v <absolute_path_to_this_repo>/lab1_ws/src/:/lab1_ws/src/ --name f1tenth_lab1 ros:foxy`


![0049f85ab6962e76e7678c271916a48d.png](../_resources/0049f85ab6962e76e7678c271916a48d.png)

### ROS2:
![4f956a821a6e4a4d0d1f52ce8967d429.png](../_resources/4f956a821a6e4a4d0d1f52ce8967d429.png)

#### Creating the Package:
These dependencies were added to the CMakelists.txt
![2b84dd71741342989984fcd43ee81754.png](../_resources/2b84dd71741342989984fcd43ee81754.png)

Mirroring the same in package.xml too, we have:
![0cfbebfe1d00a02ef64a4fb6716891cc.png](../_resources/0cfbebfe1d00a02ef64a4fb6716891cc.png)

**Due to facing several errors, the build type was later switched to ament_python**

Result after publishing the talker:
![26d27f687508169bcb10676e9b608fd1.png](../_resources/26d27f687508169bcb10676e9b608fd1.png)