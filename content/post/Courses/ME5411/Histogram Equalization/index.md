---
title: Histogram Equalization
subtitle: ME5411 Robotics Vision and AI

summary: Robotics Vision and AI
projects: [ME5411]

date: '2023-09-16T00:00:00Z'
lastmod: '2023-09-16T00:00:00Z'

draft: false
featureSigma_d: false

authors:
- penway

categories:
- Course Notes
---

## Histogram Equalization Naively Explained

Sometimes, one image can be too dark, too bright or have really low contract, which can be all seen in the histogram of the image. We can see from below that these histograms are not evenly distributed or not spread out enough.

So we can develop a method to spread out the histogram of the image, i.e. make every intensity value (histogram bin) have similar (better the same) number of pixels. This is called histogram equalization.

### Histogram

The following code snippet shows how to plot a histogram of an image, and to plot a histogram of an image with a certain bin size.

```python
import cv2 as cv
import numpy as np

def cal_hist(image: np.ndarray) -> np.ndarray:
    # we need gray image as input
    hist = np.zeros(256, np.int32)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            hist[image[i, j]] += 1
    return hist
```

These three images are preprocessed by phone app by changing the exposure and lowing the contrast. We can see that the histogram is not evenly distributed. But we can imagine that the "information" is not very different, just that the histogram is not spread out enough.

![Histogram of the three images](./Figure_1_hist.png)
![image](./Figure_2_three_oranges.png)