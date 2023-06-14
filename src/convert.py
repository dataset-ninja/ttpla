# https://github.com/r3ab/ttpla_dataset

import os
import numpy as np
import supervisely as sly
from supervisely.io.fs import (
    get_file_name_with_ext,
    get_file_name,
    get_file_ext,
    file_exists,
    get_file_size,
)
import xml.etree.ElementTree as ET
from supervisely.io.json import load_json_file
from dotenv import load_dotenv


# if sly.is_development():
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# api = sly.Api.from_env()
# team_id = sly.env.team_id()
# workspace_id = sly.env.workspace_id()


# project_name = "TTPLA"
dataset_path = "./APP_DATA/data_original_size"
batch_size = 30
ds_name = "ds"
images_ext = ".jpg"
ann_ext = ".json"


qwertyy = load_json_file(
    "./APP_DATA/data_original_size/1_00217.json"
)


def create_ann(image_path):
    labels = []

    image_np = sly.imaging.image.read(image_path)[:, :, 0]
    img_height = image_np.shape[0]
    img_wight = image_np.shape[1]

    file_name = get_file_name(image_path)

    ann_path = os.path.join(dataset_path, file_name + ann_ext)
    if file_exists(ann_path):
        ann_data = load_json_file(ann_path)
        poly_data = ann_data["shapes"]
        for curr_poly in poly_data:
            class_name = curr_poly["label"].lower()
            obj_class = name_to_obj_class[class_name]
            polygons_coords = curr_poly["points"]
            exterior = []
            for coords in polygons_coords:
                for i in range(0, len(coords), 2):
                    exterior.append([int(coords[i + 1]), int(coords[i])])
            poligon = sly.Polygon(exterior)
            label_poly = sly.Label(poligon, obj_class)
            labels.append(label_poly)

    return sly.Annotation(img_size=(img_height, img_wight), labels=labels)


obj_class_tower_lattice = sly.ObjClass("tower_lattice", sly.Polygon)
obj_class_cable = sly.ObjClass("cable", sly.Polygon)
obj_class_tower_wooden = sly.ObjClass("tower_wooden", sly.Polygon)
obj_class_void = sly.ObjClass("void", sly.Polygon)
obj_class_tower_tucohy = sly.ObjClass("tower_tucohy", sly.Polygon)

name_to_obj_class = {
    "tower_lattice": obj_class_tower_lattice,
    "cable": obj_class_cable,
    "tower_wooden": obj_class_tower_wooden,
    "void": obj_class_void,
    "tower_tucohy": obj_class_tower_tucohy,
}



def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    project = api.project.create(workspace_id, project_name, change_name_if_conflict=True)
    meta = sly.ProjectMeta(obj_classes=list(name_to_obj_class.values()))
    api.project.update_meta(project.id, meta.to_json())

    images_names = [
        im_name for im_name in os.listdir(dataset_path) if get_file_ext(im_name) == images_ext
    ]

    dataset = api.dataset.create(project.id, ds_name, change_name_if_conflict=True)

    progress = sly.Progress("Create dataset {}".format(ds_name), len(images_names))

    for img_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [os.path.join(dataset_path, im_name) for im_name in img_names_batch]

        img_infos = api.image.upload_paths(dataset.id, img_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        anns = [create_ann(image_path) for image_path in img_pathes_batch]
        api.annotation.upload_anns(img_ids, anns)

        progress.iters_done_report(len(img_names_batch))

    return project