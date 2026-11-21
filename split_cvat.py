
from pathlib import Path
from collections import Counter
from copy import deepcopy
import re
import zipfile
import xml.etree.ElementTree as ET

SOURCE = Path("levietlong-all.zip")

GROUPS = {
    "front": (range(1, 17), "A"),
    "fisheye": (range(1, 13), "B"),
}

def get_slot(filename):
    basename = Path(filename).name
    match = re.match(r"^([AB]\d{2})(?:[_\.]|$)", basename)
    return match.group(1) if match else None

if not SOURCE.exists():
    raise SystemExit(f"Không tìm thấy {SOURCE}")

with zipfile.ZipFile(SOURCE) as z:
    xml_files = [
        n for n in z.namelist()
        if Path(n).name == "annotations.xml"
    ]
    if len(xml_files) != 1:
        raise SystemExit("ZIP phải có đúng một annotations.xml")
    root = ET.fromstring(z.read(xml_files[0]))

images = root.findall("image")
if len(images) != 28:
    raise SystemExit(f"Yêu cầu 28 ảnh, tìm thấy {len(images)}")

slots = [get_slot(im.get("name", "")) for im in images]
expected = (
    {f"A{i:02d}" for i in range(1, 17)}
    | {f"B{i:02d}" for i in range(1, 13)}
)

if None in slots or set(slots) != expected:
    raise SystemExit("Tên ảnh không đúng A01-A16 / B01-B12")
if any(count != 1 for count in Counter(slots).values()):
    raise SystemExit("Có mã ảnh bị trùng")

original_labels = sum(
    len(list(im)) for im in images
)

for group, (numbers, prefix) in GROUPS.items():
    wanted = {f"{prefix}{i:02d}" for i in numbers}
    output_root = deepcopy(root)

    for im in list(output_root.findall("image")):
        if get_slot(im.get("name", "")) not in wanted:
            output_root.remove(im)

    selected = output_root.findall("image")
    for idx, im in enumerate(selected):
        im.set("id", str(idx))

    size = output_root.find("./meta/task/size")
    if size is not None:
        size.text = str(len(selected))

    output = Path(f"levietlong-{group}.zip")
    xml_bytes = ET.tostring(
        output_root, encoding="utf-8",
        xml_declaration=True
    )

    with zipfile.ZipFile(
        output, "w", zipfile.ZIP_DEFLATED
    ) as z:
        z.writestr("annotations.xml", xml_bytes)

    label_count = sum(len(list(im)) for im in selected)
    print(f"{output}: {len(selected)} ảnh, {label_count} nhãn")

print("Tách hoàn tất. File gốc được giữ nguyên.")
