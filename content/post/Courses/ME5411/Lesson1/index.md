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