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

# 图像形成 Image Formation

## 针孔相机

![针孔相机示意图](E:\Caldron\homepage\content\post\Computer Vision\1 Image Formation\00.png)

假设小孔只能透过一条光线...

## 透镜相机

细透镜方程:

![lens](E:\Caldron\homepage\content\post\Computer Vision\1 Image Formation\02)
$$
\dfrac 1 f = \dfrac 1 u + \dfrac 1 v\\
f:焦距\\
u:物距\\
v:相距
$$
景深与光圈

![depth](E:\Caldron\homepage\content\post\Computer Vision\1 Image Formation\03.png)

光圈（孔径）缩小，即使不在焦点上的物体也可以近似聚焦，所以景深就变大了。

## 3D 到 2D 的坐标变换

### 理想情况

![3d to 2d projection](E:\Caldron\homepage\content\post\Computer Vision\1 Image Formation\01.png)

这是一个3d到2d的投影图，根据相似三角形的关系，可以得到

$$
(x,y,z) \rightarrow(f'\dfrac x z, f'\dfrac y z)
$$

如果想把这个东西用矩阵运算的形式表示，会发现是无法做到的，因为这个不是线性的变换（有除以z的引入）。

$$
\begin{bmatrix} x\\y\\z \end{bmatrix} \rightarrow \begin{bmatrix} f'\dfrac x z \\ f'\dfrac y z \end{bmatrix}
$$

但是可以再加一层变换做到这一点，所以有了坐标的齐次形式：

$$
(x, y)\rightarrow \begin{bmatrix} x\\y\\1 \end{bmatrix}
\ \ \ \ \ \ \ \ 
(x, y, z)\rightarrow \begin{bmatrix} x\\y\\z\\1 \end{bmatrix}
$$

$$
\begin{bmatrix}x\\y\\w\end{bmatrix} \rightarrow(\dfrac x w, \dfrac y w)\ \ \ \ \ \ \ \ \begin{bmatrix}x\\y\\z\\w\end{bmatrix} \rightarrow(\dfrac x w, \dfrac y w, \dfrac z w)
$$
这样就可以进行矩阵运算了：

$$
\begin{bmatrix} 
    1& 0& 0& 0\\ 
    0& 1& 0& 0\\ 
    0& 0& \dfrac 1 {f'}& 0
\end{bmatrix} 
\begin{bmatrix} x\\y\\z\\1 \end{bmatrix} 
= 
\begin{bmatrix} x\\ y\\ \frac z {f'} \end{bmatrix} 
\rightarrow 
(f'\dfrac x z, f'\dfrac y z)
$$

### 实际情况

前面的推导的前提是相机和世界处于同一个坐标系之下，而实际情况并非如此。

