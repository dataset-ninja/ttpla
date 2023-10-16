from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "TTPLA"
PROJECT_NAME_FULL: str = "TTPLA: An Aerial-Image Dataset for Detection and Segmentation of Transmission Towers and Power Lines"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Apache_2_0(source_url="https://github.com/R3ab/ttpla_dataset/blob/master/LICENSE")
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Energy()]
CATEGORY: Category = Category.EnergyAndUtilities()

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2020

HOMEPAGE_URL: str = "https://github.com/r3ab/ttpla_dataset"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 2001960
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/ttpla"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1Yz59yXCiPKS0_X4K3x9mW22NLnxjvrr0"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "cable": [230, 25, 75],
    "tower_lattice": [60, 180, 75],
    "tower_wooden": [255, 225, 25],
    "tower_tucohy": [0, 130, 200],
    "void": [245, 130, 48],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})
PAPER: Optional[str] = "https://arxiv.org/abs/2010.10032.pdf"
CITATION_URL: Optional[str] = "https://github.com/r3ab/ttpla_dataset#citation"
AUTHORS: Optional[List[str]] = ["Abdelfattah, Rabab", "Wang, Xiaofeng", "Wang, Song"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "University of South Carolina"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://sc.edu/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
