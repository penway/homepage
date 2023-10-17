    ---
title: Image presentation
subtitle: ME5411 Robotics Vision and AI

summary: Robotics Vision and AI
projects: [ME5411]

date: '2023-08-15T00:00:00Z'
lastmod: '2023-10-08T00:00:00Z'

draft: false
featureSigma_d: false

authors:
- penway

categories:
- Course Notes
---

> This note is for revision, so I give up telling the story and just write down the key points.

## 1. Image Representation

### Continuous Image Function
f(x,y) or f(x,y,t) for video

The value is intensity that can be determined by illumination, reflection. Or for some other cases, it can be temperature, pressure, distance, etc.

### Image Digitalization
- Sampling: turn continuous x, y into discrete
- Quantization: turn intensity into discrete values
- so it can be represented as a matrix
- each element of this matrix is called a pixel

### Pixel
- smallest unit
- point sample
- has a position
- color capability: bits (or bit-depth) (such as 2-bit for black and white, 8-bit for 256 colors, 24-bit for 16M colors)

## 2. Image Sampling and Quantization

### Sampling
- sampling will make the shape different
- spatial resolution (image resolution): pixel per unit area (pixel / inch, PPI)
- raster dimension (image dimension): the number of pixels in width and height (width x height)
- p(i,j): i is the column, j is the row in the matrix. While in programming, we call image[y, x], either in python or matlab.

### Quantization
- bit-depth: K = 2^n
- index color: 8 bit but encode 256 colors, good for hardware to make a look up table
- this level better be fine enough for human eyes to distinguish, (human do well at 60 gray levels, so we use 8-bit for gray scale)

## 3. Digital Image Properties

### Metric and Topology

- Set
- Metric Space: a set with a distance function
- Topological Space: a mathematical structure that allows formal definition of concepts such as convergence, connectedness, continuity, etc.
- connecivity of a set: a set is connected if it cannot be divided into two disjoint nonempty open sets

distances:
1. Euclidean distance
2. City Block distance (Manhattan distance)
3. Chessboard distance

Typical Connectivity:
1. 4-connectivity
2. 8-connectivity

### Histogram

- a graph showing count of intensity values
- can detect
    - low contrast / high contrast
    - brightness / overexposure / underexposure
- more than one image can have the same histogram
- can remove background by thresholding
- invariant to translation, rotation, scaling, etc
- does not contain spatial information (shape)

### Visual Perception

1. Contrast
    - local change in brightness
    - for human, object from background
2. Acuity
    - the ability to detect detail
    - the resolution of eye
3. perceptual grouping





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

% visualize the kernel in 3D plot
figure;
surf(kernel); % surf is a 3D plot function, it needs a 2D matrix as input
title('Gaussian Kernel');
```

```matlab
% Simple CNNs
gpuInfo = gpuDevice();
disp(gpuInfo);

% 64x3 32x16 16x32 8x64
% use full conv net
net = [ ...
    imageInputLayer([64 64 3])
    convolution2dLayer(3, 16, 'Padding', 1, 'Stride', 2)  % 32x32x16
    batchNormalizationLayer
    leakyReluLayer(0.2)
    convolution2dLayer(3, 32, 'Padding', 1, 'Stride', 2)  % 16x16x32
    batchNormalizationLayer
    leakyReluLayer(0.2)
    convolution2dLayer(3, 64, 'Padding', 1, 'Stride', 2)  % 8x8x64
    batchNormalizationLayer
    leakyReluLayer(0.2)
    convolution2dLayer(3, 128, 'Padding', 1, 'Stride', 2) % 4x4x128
    batchNormalizationLayer
    leakyReluLayer(0.2)
    convolution2dLayer(3, 256, 'Padding', 1, 'Stride', 2) % 2x2x256
    batchNormalizationLayer
    leakyReluLayer(0.2)
    convolution2dLayer(2, 3, 'Padding', 0, 'Stride', 2)   % 1x1x10, 10 classes
    softmaxLayer
    classificationLayer
];

% read in data
imds = imageDatastore('ssb', ...
    'IncludeSubfolders', true, ...
    'LabelSource', 'foldernames');

% split into training and validation
[trainingImds, validationImds] = splitEachLabel(imds, 0.8, 'randomized');

% preprocess into 64x64
inputSize = [64 64 3];
augmentedTrainingImds = augmentedImageDatastore(inputSize, trainingImds);
augmentedValidationImds = augmentedImageDatastore(inputSize, validationImds);

% define training options
options = trainingOptions('sgdm', ...
    'InitialLearnRate', 0.001, ...
    'MaxEpochs', 20, ...
    'Shuffle', 'every-epoch', ...
    'ValidationData', augmentedValidationImds, ...
    'ValidationFrequency', 30, ...
    'Verbose', false, ...
    'Plots', 'training-progress', ...
    'ExecutionEnvironment', 'auto');

% train network
trainedNet = trainNetwork(augmentedTrainingImds, net, options);


```

### Index color
mapping one color to one index, and use the index to represent the color.
such as 0 -> red, 1 -> green, 2 -> blue, 3 -> (0, 3, 6) ...
Good for hardware, like using look up table to save memory and speed up processing.