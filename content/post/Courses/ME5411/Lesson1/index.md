---
title: Image presentation
subtitle: ME5411 Robotics Vision and AI

summary: Robotics Vision and AI
projects: [ME5411]

date: '2023-08-15T00:00:00Z'
lastmod: '2023-08-15T00:00:00Z'

draft: false
featureSigma_d: false

authors:
- penway

categories:
- Course Notes
---

example codes in MATLAB:

```matlab
% read image
lenna = imread('lenna_(test_image).png');

% slpit image into 3 channels and show in a grid of 2x2
lenna_r = lenna(:,:,1);
lenna_g = lenna(:,:,2);
lenna_b = lenna(:,:,3);

subplot(2,2,1);
imshow(lenna_r);
title('Red Channel');

subplot(2,2,2);
imshow(lenna_g);
title('Green Channel');

subplot(2,2,3);
imshow(lenna_b);
title('Blue Channel');

subplot(2,2,4);
imshow(lenna);
title('Original Image');

% convolution with a kxk Gaussian kernel
k = 5;
sigma = 1;
kernel = fspecial('gaussian', k, sigma);
kernel % print kernel
lenna_conved = imfilter(lenna, kernel);
figure;
imshow(lenna_conved);
title('Convolved Image');
```