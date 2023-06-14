**TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Lines** is a dataset for semantic segmentation, object detection, and instance segmentation tasks. It is used in the energy industry.

The dataset consists of 1242 images with 11468 labeled objects belonging to 5 different classes including *cable*, *tower_lattice*, *tower_wooden*, and other: *tower_tucohy* and *void*.

Each image in the TTPLA dataset has pixel-level instance segmentation annotations. Due to the nature of the instance segmentation task, it can be automatically transformed into semantic segmentation (only one mask for every class) or object detection (bounding boxes for every object) tasks. All images are labeled (i.e. with annotations). There is 1 split in the dataset: *ds* (1242 images). The dataset was released in 2020 by the [University of South Carolina](https://sc.edu/).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/ttpla/raw/main/visualizations/side_annotations_grid.png">
