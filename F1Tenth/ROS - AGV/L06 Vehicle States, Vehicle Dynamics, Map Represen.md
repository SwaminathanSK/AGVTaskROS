## Vehicle States
1. Position: Only translation, w.r.t to the coordinate system and the position is the COG of the vehicle.
2. Heading: Angle that displays the direction that the vehicle looks at.
3. Frenet Frame: continuous, differentiable curve in 3d euclidean space. Coordinate system spanned by a **tangential vector t** and **normal vector n**  at any point of the reference line. **s coordinate** is the run length and **d coordinate** is the lateral position relative to the reference path. d is positive to the left of the reference path.
![bfd718f437e8a224ba229695bebce702.png](../_resources/bfd718f437e8a224ba229695bebce702.png)
![898f24c9509477b29e97db38c64fa07d.png](../_resources/898f24c9509477b29e97db38c64fa07d.png)
4. Velocity: The observed speed. Sensor: Pivot sensor.
5. Acceleration: observed acceleration when vehicle changes its state. Measured with IMU sensors.
6. Steering Angle: Angle that displays the direction in which the front wheels currently "looks at"
![86d2577655d2b82e785bf75a99ac2168.png](../_resources/86d2577655d2b82e785bf75a99ac2168.png)
![b0e9c69c9dcb61f6fa68db21a7abfc14.png](../_resources/b0e9c69c9dcb61f6fa68db21a7abfc14.png)

![7ad79b7af0cee0145521ea5b3ad4cd75.png](../_resources/7ad79b7af0cee0145521ea5b3ad4cd75.png)


* * *
### Kinematic Single Track Model - Bicycle Model
![5a1da25a0e40d51b6526d6387377b5c7.png](../_resources/5a1da25a0e40d51b6526d6387377b5c7.png)
![f722f1d8f98b295d833e71a2f10dcc51.png](../_resources/f722f1d8f98b295d833e71a2f10dcc51.png)
![e25773cbb13bf4ecf52962f56c3b4606.png](../_resources/e25773cbb13bf4ecf52962f56c3b4606.png)
* * *
### Linear Single Track Model
1. Plan evasive maneuvers closer to physical limits
2. Consider important effects such as understeer or oversteer
3. Steady-state velocity assumption, rate of change of speed = 0
![21f6dd27024a3e7d97dd9eec3d1196b7.png](../_resources/21f6dd27024a3e7d97dd9eec3d1196b7.png)
![ee88bd108a480ffac32cdc2647e246a1.png](../_resources/ee88bd108a480ffac32cdc2647e246a1.png)
