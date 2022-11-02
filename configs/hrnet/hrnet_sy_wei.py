_base_ = './faster_rcnn_hrnetv2p_w40_2x_coco.py'
# The new config inherits a base config to highlight the necessary modification


# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1)))
        # "sytrain_nomark_wr": ("/mnt/data/samples/upward/suit540/train_v2_2", "/mnt/data/samples/upward/suit540/train_v2_2.json"),
        # "sytest_nomark_wr": ("/mnt/data/samples/upward/suit540/test_v2_2", "/mnt/data/samples/upward/suit540/test_v2_2.json"),
# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('person',)
data = dict(
    train=dict(
        img_prefix='/mnt/data/samples/upward/suit540/train_v2_2/',
        classes=classes,
        ann_file='/mnt/data/samples/upward/suit540/train_v2_2.json'),
    val=dict(
        img_prefix='/mnt/data/samples/upward/suit540/test_v2_2',
        classes=classes,
        ann_file='/mnt/data/samples/upward/suit540/test_v2_2.json'),
    test=dict(
        img_prefix='balloon/val/',
        classes=classes,
        ann_file='balloon/val/annotation_coco.json')
        )

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = '/home/sy/working/otherCodes/mmdetection/models/faster_rcnn_hrnetv2p_w40_2x_coco_20200512_161033-0f236ef4.pth'