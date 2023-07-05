Dataset **TTPLA** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/f/6/XX/q1H4bZb8EV44VC6v37CYCPwgptJ7LgIBiaUBwMXDZsj0GgKFKUxMrJBMUntFxdoVlSBdM4H2LGaSbJNp3LhZU4XAJpvMtLug2p8otDD7ZfOzAApNImD6jjKv3xtX.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='TTPLA', dst_path='~/dtools/datasets/TTPLA.tar')
```
The data in original format can be 🔗[downloaded here](https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1Yz59yXCiPKS0_X4K3x9mW22NLnxjvrr0)