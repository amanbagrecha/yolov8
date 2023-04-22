import os

from datasets import load_dataset


data = load_dataset("Francesco/solar-panels-taxvb")


os.makedirs("datasets/labels/train/", exist_ok=True)
os.makedirs("datasets/labels/val/", exist_ok=True)
os.makedirs("datasets/images/train/", exist_ok=True)
os.makedirs("datasets/images/val/", exist_ok=True)
os.makedirs("datasets/labels/test/", exist_ok=True)
os.makedirs("datasets/images/test/", exist_ok=True)

for train_dict in data["train"]:

    train_dict["image"].save(f"datasets/images/train/{train_dict['image_id']}.png")

    with open(f"datasets/labels/train/{train_dict['image_id']}.txt", "w") as f:
        _, _, bboxs, labels = train_dict["objects"].values()
        for bbox, label in zip(bboxs, labels):
            print(bbox, label)
            img_width = train_dict["width"]
            img_height = train_dict["height"]
            x_center = (bbox[0] + bbox[2] / 2) / img_width
            y_center = (bbox[1] + bbox[3] / 2) / img_height
            width = bbox[2] / img_width
            height = bbox[3] / img_height
            f.write(f"{label} {x_center} {y_center} {width} {height}\n")


for train_dict in data["validation"]:

    train_dict["image"].save(f"datasets/images/val/{train_dict['image_id']}.png")

    with open(f"datasets/labels/val/{train_dict['image_id']}.txt", "w") as f:
        _, _, bboxs, labels = train_dict["objects"].values()
        for bbox, label in zip(bboxs, labels):
            print(bbox, label)
            img_width = train_dict["width"]
            img_height = train_dict["height"]
            x_center = (bbox[0] + (bbox[2]) / 2) / img_width
            y_center = (bbox[1] + (bbox[3]) / 2) / img_height
            width = bbox[2] / img_width
            height = bbox[3] / img_height
            f.write(f"{label} {x_center} {y_center} {width} {height}\n")

for train_dict in data["test"]:

    train_dict["image"].save(f"datasets/images/test/{train_dict['image_id']}.png")

    with open(f"datasets/labels/test/{train_dict['image_id']}.txt", "w") as f:
        _, _, bboxs, labels = train_dict["objects"].values()
        for bbox, label in zip(bboxs, labels):
            print(bbox, label)
            img_width = train_dict["width"]
            img_height = train_dict["height"]
            x_center = (bbox[0] + (bbox[2]) / 2) / img_width
            y_center = (bbox[1] + (bbox[3]) / 2) / img_height
            width = bbox[2] / img_width
            height = bbox[3] / img_height
            f.write(f"{label} {x_center} {y_center} {width} {height}\n")
