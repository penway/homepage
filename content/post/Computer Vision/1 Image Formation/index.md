---
title: 图像形成
subtitle: 

summary: 计算机视觉 图像形成
date: "2022-1-10T00:00:00Z"
lastmod: "2021-1-10T00:00:00Z"

tags: -计算机
categories: 计算机视觉

image:
  caption: 'Image credit: [**The Creation of Adam**](./featured.jpg)'
  focal_point: ""
  placement: 2
  preview_only: false
---

## 针孔相机

![针孔相机示意图](https://penway.cn/post/computer-vision/1-image-formation/00.png)

假设小孔只能透过一条光线...

## 透镜相机

细透镜方程:

![lens](https://penway.cn/post/computer-vision/1-image-formation/02)
$$ \dfrac 1 f = \dfrac 1 u + \dfrac 1 v\\f:焦距\\u:物距\\v:相距 $$
景深与光圈

![depth](https://penway.cn/post/computer-vision/1-image-formation/03.png)

光圈（孔径）缩小，即使不在焦点上的物体也可以近似聚焦，所以景深就变大了。

### 视场（FOV, Field of view，视角）

即相机能拍摄到的最大范围，单位是角度

焦距越小，FOV越大，反之亦然。

## 几何模型

相机的内部参数是指相机本身的特性，外部参数是指相机在世界中的位置。

### 内部参数

#### 理想情况

![3d to 2d projection](https://penway.cn/post/computer-vision/1-image-formation/01.png)

这是一个3d到2d的投影图，根据相似三角形的关系，可以得到

$$(x,y,z) \rightarrow(f'\dfrac x z, f'\dfrac y z)$$

如果想把这个东西用矩阵运算的形式表示，会发现是无法做到的，因为这个不是线性的变换（有除以z的引入）。

$$\begin{bmatrix} x \\\\ y \\\\ z \end{bmatrix} \rightarrow \begin{bmatrix} f'\dfrac x z \\ f'\dfrac y z \end{bmatrix}$$

但是可以再加一层变换做到这一点，所以有了坐标的齐次形式：

$$
(x, y) \rightarrow 
\begin{bmatrix} 
x \\\\ y \\\\ 1
\end{bmatrix}
\ \ \ \ \ \ \ \ 
(x, y, z) \rightarrow
\begin{bmatrix} 
x \\\\ y \\\\ z \\\\ 1
\end{bmatrix}
$$
$$
\begin{bmatrix}
x \\\\ y \\\\ w
\end{bmatrix}
\rightarrow (\dfrac x w, \dfrac y w) \ \ \ \ \ \ \ \ 
\begin{bmatrix}
x \\\\ y \\\\ z \\\\ w
\end{bmatrix}
\rightarrow(\dfrac x w, \dfrac y w, \dfrac z w)
$$

这样就可以进行矩阵运算了：

$$
\begin{bmatrix}     1& 0& 0& 0 \\\\ 0& 1& 0& 0 \\\\ 0& 0& \dfrac 1 {f'}& 0\end{bmatrix} 
\begin{bmatrix} x \\\\ y \\\\ z \\\\ 1 \end{bmatrix} 
= 
\begin{bmatrix} x \\ y\\ \frac z {f'} \end{bmatrix} 
\rightarrow 
(f'\dfrac x z, f'\dfrac y z)
$$

#### 实际情况

前面的推导的前提是相机和世界处于同一个坐标系之下，而实际情况并非如此。

原先的点是：$(f'\dfrac x z, f'\dfrac y z)$

但是，像素（光屏）不一定是在焦距处：$(\alpha\dfrac x z, \alpha\dfrac y z)$

并且像素不一定是正方形：$(\alpha\dfrac x z, \beta\dfrac y z)$

加上相机的平移（也就是相机坐标系的原点未知），得到的点应该是这样的：$ (\dfrac {\alpha x} z + c_x, \dfrac{\beta y} z + c_y) \rightarrow \begin{bmatrix} \alpha x + c_x z\\ \beta y + c_y z\\ z \end{bmatrix} $

因此整个方程可以写成：
$$
\begin{bmatrix}
\alpha& 1& c_x& 0\\\\
0& \beta& c_x& 0\\0& 0& 1& 0\\\\
\end{bmatrix}
\begin{bmatrix}
x \\\\ y \\\\ z \\\\ 1
\end{bmatrix}
=
\begin{bmatrix}
\alpha x + c_x \\\\ \beta y + c_y \\\\ 1
\end{bmatrix}
$$
其中$\begin{bmatrix}\alpha& 1& c_x\\0& \beta& c_x\\0& 0& 1\\\end{bmatrix}$叫做相机矩阵$K$，里面的参数即为内部参数，所以目前整个方程可以改写成
$$P'=MP=K\begin{bmatrix}I& 0\end{bmatrix}P$$
其中 $\alpha\ \beta$ 和相机的焦距以及像素大小有关；$c_x\ c_y$ 和相机的相机的成像平面的位置有关。

### 外部参数

世界坐标系是绝对不变的，SLAM中的视觉里程计就是求解相机在世界坐标系下的运动轨迹。

因此这里的变换是在三维空间中的直接变换，因此齐次变换矩阵是四维的。

下面用三维的情况举例：

外部的平移和内部是相同的所以矩阵的形式也是一样的：

$$\begin{bmatrix}\alpha& 1& c_x& 0\\0& \beta& c_x& 0\\0& 0& 1& 0\\\end{bmatrix}$$

相机的旋转比较复杂，假设相点$P'=(u',v')$，旋转之前的是$(u_0,v_0)$
$$v'sin(\theta)=v_0\\u'=u-cos(\theta)v'=u-cot(\theta)v$$
整理得
$$u = \alpha \frac x z - \alpha cot(\theta) \dfrac y z + u_0\\v = \dfrac \beta {sin(\theta)} \dfrac y z + v_0$$
因此整个方程可以写成：
$$\begin{bmatrix}\alpha& -\alpha cot(\theta)& c_x& 0\\0& \dfrac\beta{sin(\theta)}& c_x& 0\\0& 0& 1& 0\\\end{bmatrix}\begin{bmatrix}x\\y\\z\\1\end{bmatrix}=\begin{bmatrix} u \\ v \\ 1 \end{bmatrix}= P'$$

$$\begin{bmatrix}R_{2 \times 2}& T\\0& 1\end{bmatrix}_{3\times 3}$$

四维的情况也是同理：
$$\begin{bmatrix}R_{3 \times 3}& T\\0& 1\end{bmatrix}_{4 \times 4}$$

### 相机参数

所有的参数合起来就是下面的方程：
$$
P'_{3 \times 1} = M_{3 \times 4}P_w = K_{3 \times 3} \begin{bmatrix}R&T\end{bmatrix}_{3 \times 4} P_{w\ 4 \times 1}
$$
令 $M=\begin{bmatrix}m_1\\m_2\\m_3\end{bmatrix}$，可以得到
$$
P'=(\dfrac{m_1P_w}{m_3P_w}, \dfrac{m_2P_w}{m_3P_w})
$$

### 透视类型

#### 基本假设

假设世界坐标系和相机坐标系相同，即没有旋转和平移；相机内部没有倾斜，感光芯片为方块像素，没有失真，像平面中心为原点。
$$
M = 
\begin{bmatrix} 
f&0&0&0\\
0&f&0&0\\
0&0&1&0
\end{bmatrix}
$$

#### 基本透视投影

焦距归一化为1
$$P'=\begin{bmatrix} 1&0&0&0\\0&1&0&0\\0&0&1&0\end{bmatrix}\begin{bmatrix}x\\y\\z\\1\end{bmatrix}\begin{bmatrix}x\\y\\z\end{bmatrix} \\ \rightarrow P'=(\frac x z, \frac y z)$$

#### 弱透视投影 perspective

景深相对于场景到相机的距离较小，即当场景目标很小或距离远时，适用于图像识别。

![perspective](E:\Caldron\homepage\content\post\Computer Vision\1 Image Formation\04.png)
$$
P'=(\frac {f'} {z_0}x, \frac {f'} {z_0}y)
$$

$$
M = K\begin{bmatrix}R&T\end{bmatrix}=\begin{bmatrix}A&b\\0&1\end{bmatrix}
$$

#### 透视投影 projective

适用于3D-2D映射，用于运动恢复结构、SLAM。
$$
M = K\begin{bmatrix}R&T\end{bmatrix}=\begin{bmatrix}A&b\\v&1\end{bmatrix}
$$


#### 正交投影

$$
P'=P
$$

## 相机标定

通过已知外部参数求出内部参数。

