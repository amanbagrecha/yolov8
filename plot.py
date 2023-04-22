import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches

from datasets import load_dataset


data = load_dataset("Francesco/solar-panels-taxvb")
split_name = "train"
index_value = 9
img_no = data[split_name]["image_id"].index(index_value)

_, _, bboxs, labels = data[split_name]["objects"][img_no].values()
image_id = data[split_name]["image_id"][img_no]

with Image.open(f"datasets/images/{split_name}/{image_id}.png") as f:

    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(f)

    for idx, (bbox, label) in enumerate(zip(bboxs, labels)):
        print(f"{label=} and {bbox=}")
        ax.add_patch(
            patches.Rectangle(
                (bbox[0], bbox[1]), bbox[2], bbox[3], fill=False, edgecolor="blue", lw=3
            )
        )
        ax.text(
            bbox[0] + 10,
            (bbox[1] + 10),
            str(label),
            verticalalignment="top",
            color="white",
            fontsize=10,
            weight="bold",
        )

    plt.show()
