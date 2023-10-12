## The wall following problem
**Two objectives:**
* Parallel to the walls
* roughly move along the centre line

**Control objective:**
1) y = 0
2) Lsin(theta) = 0
![8643a7e943b8186d808a4f4c788baea0.png](../_resources/8643a7e943b8186d808a4f4c788baea0.png)
Note that we will keep L constant here. (It is a parameter). Reducing the L makes it jerkier. and Increasing it makes the converging rate small.

Since y and theta are opposite. The error at any time will be
![bb1e0112b261c6da7adbc4d48612217e.png](../_resources/bb1e0112b261c6da7adbc4d48612217e.png)


![fc45653781d8ef926f6605968b49dfbf.png](../_resources/fc45653781d8ef926f6605968b49dfbf.png)
![93bf85491d04ce4933179b8ffa172602.png](../_resources/93bf85491d04ce4933179b8ffa172602.png)

![f90d5418833fa54007bafbacd64d452b.png](../_resources/f90d5418833fa54007bafbacd64d452b.png)

![85dc1a800ecd211e9f92cba003375004.png](../_resources/85dc1a800ecd211e9f92cba003375004.png)

![b15f27d57e9d7e02997eca9b40d0ea7c.png](../_resources/b15f27d57e9d7e02997eca9b40d0ea7c.png)  

![4abde0d6f2223d00b3c61a3cebf201ac.png](../_resources/4abde0d6f2223d00b3c61a3cebf201ac.png)

The problem of overshooting can be fixed by either making the integral term work only after the error has come into a small margin, or by bounding the integral error accumulation.

![e129c32ad55314ed9155bfdb9588c2ff.png](../_resources/e129c32ad55314ed9155bfdb9588c2ff.png)

We cannot immediately consider this for the error. Since, by the time we calculate AB, we might have gone further on the track.
![153d42bf141109bce5655ceaf17c2392.png](../_resources/153d42bf141109bce5655ceaf17c2392.png)