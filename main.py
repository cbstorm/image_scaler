import cv2
import os
import sys

assert_argv_map = dict()
assert_argv_map['-p'] = 0
assert_argv_map['-sr'] = 0
assert_argv_map['-mw'] = 0
assert_argv_map['-mh'] = 0

def max(a, b):
    return a if a > b else b


def scale_img(img_path, scale_rate=0, max_width=320, max_height=320):
    img = cv2.imread(os.path.join(os.getcwd(), img_path), cv2.COLOR_BGR2RGB)
    print("original.width: ", img.shape[1], "original.height: ", img.shape[0])
    w_scale = 0
    h_scale = 0
    if scale_rate > 0:
        h_scale = int(img.shape[0] * scale_rate)
        w_scale = int(img.shape[1] * scale_rate)
    elif max_height > 0 and max_width > 0:
        h_scale_rate = int(img.shape[0] / max_height)
        w_scale_rate = int(img.shape[1] / max_width)
        scale_rate = 1 / max(w_scale_rate, h_scale_rate)
        w_scale = int(img.shape[1] * scale_rate)
        h_scale = int(img.shape[0] * scale_rate)
    elif max_height > 0 and max_width <= 0:
        h_scale_rate = int(img.shape[0] / max_height)
        scale_rate = 1 / h_scale_rate
        w_scale = int(img.shape[1] * scale_rate)
        h_scale = int(img.shape[0] * scale_rate)
    elif max_width > 0 and max_height <= 0:
        w_scale_rate = int(img.shape[1] / max_width)
        scale_rate = 1 / w_scale_rate
        w_scale = int(img.shape[1] * scale_rate)
        h_scale = int(img.shape[0] * scale_rate)
    print("w_scale: ", w_scale, "h_scale: ", h_scale)
    resized_img = cv2.resize(img, (w_scale, h_scale))
    image_name = img_path.split('/')[-1]
    dest_path = os.path.join(os.getcwd(), 'out', image_name)
    cv2.imwrite(dest_path, resized_img)
    print(dest_path)
    return


def main():
    argv_map = dict()
    argv = sys.argv[1:]
    for i, v in enumerate(argv):
        if i % 2 == 0:
            assert_argv_map[v] = 1
            argv_map[v] = None
        else:
            argv_map[argv[i-1]] = v

    img_path = argv_map['-p']
    sr = 0
    max_width = 0
    max_height = 0
    if assert_argv_map['-sr'] == 1:
        sr = 1/int(argv_map['-sr'])

    if (assert_argv_map['-mw'] == 1):
        max_width = int(argv_map['-mw'])

    if (assert_argv_map['-mh'] == 1):
        max_height = int(argv_map['-mh'])

    scale_img(img_path, scale_rate=sr,
              max_width=max_width, max_height=max_height)
    return


main()
