**TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Lines** is a dataset for instance segmentation, semantic segmentation, and object detection tasks. It is used in the energy industry. 

The dataset consists of 1234 images with 11447 labeled objects belonging to 5 different classes including *cable*, *tower_lattice*, *tower_wooden*, and other: *tower_tucohy* and *void*.

Images in the TTPLA dataset have pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into a semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There are 3 splits in the dataset: *test* (220 images), *train* (905 images), and *val* (109 images). The dataset was released in 2020 by the University of South Carolina.

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/ttpla/raw/main/visualizations/side_annotations_grid.png">
