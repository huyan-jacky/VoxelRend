# Med-PointRend

 A modified PointRend for medical image, both 2D and 3D are supported.

## File description

```bash
Med-PointRend/
    data/
        images/
            case_0001.nii.gz
            ...
        labels/
            case_0001.nii.gz
            ...
        preds/
            case_0001.nii.gz
            ...
    utils/
        getBoundary.py
    tools/
        train.py
        inference.py
    configs/
        MLP-3-64.json
        MLP-4-64-64.json
        ...
    models/
        MLP.py
    checkpoints/
        MLP-3-64
            2020-04-01-20-30.checkpoint
            ...
        MLP-4-64-64
            ...
    results/
```

## Train

```bash
python.py tools/train.py configs/MLP-3-64.json
```

## Inference

```bash
python.py tools/inference.py configs/MLP-3-64.json checkpoints/MLP-3-64/2020-04-01-20-30.checkpoint --out==results/test1/
```
