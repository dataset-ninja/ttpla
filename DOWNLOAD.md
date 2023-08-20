Dataset **TTPLA** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/H/R/LJ/VTNghXkTHOIZKMYGWsp1qvy1PuUnE2MMcSAGFKIVwoXFhIou6xvP6XRDqQH4aqgojDiKCUmuqZYiTuX65QiUDuWtN1oG7RbvKSmFLsNFqkXTbDQUNDnQP2e7ocvv.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='TTPLA', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1Yz59yXCiPKS0_X4K3x9mW22NLnxjvrr0).