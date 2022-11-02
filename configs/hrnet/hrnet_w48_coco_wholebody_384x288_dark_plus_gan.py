log_level = 'INFO'
load_from = None
resume_from = None
dist_params = dict(backend='nccl')
workflow = [('train', 1)]
checkpoint_config = dict(interval=50)
evaluation = dict(interval=10, metric='mAP', key_indicator='AP')

optimizer = dict(
    type='Adam',
    lr=5e-3,
)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup=None,
    # warmup='linear',
    # warmup_iters=500,
    # warmup_ratio=0.001,
    step=[70, 300,500,700])
total_epochs = 800
log_config = dict(
    interval=1,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook')
    ])

channel_cfg = dict(
    num_output_channels=18,
    dataset_joints=18,
    dataset_channel=[
        list(range(18)),
    ],
    inference_channel=list(range(18)))

# model settings
model = dict(
    type='TopDown',
    pretrained='https://download.openmmlab.com/mmpose/top_down/'
    'hrnet/hrnet_w48_coco_384x288_dark-741844ba_20200812.pth',
    backbone=dict(
        type='HRNet',
        in_channels=3,
        extra=dict(
            stage1=dict(
                num_modules=1,
                num_branches=1,
                block='BOTTLENECK',
                num_blocks=(4, ),
                num_channels=(64, )),
            stage2=dict(
                num_modules=1,
                num_branches=2,
                block='BASIC',
                num_blocks=(4, 4),
                num_channels=(48, 96)),
            stage3=dict(
                num_modules=4,
                num_branches=3,
                block='BASIC',
                num_blocks=(4, 4, 4),
                num_channels=(48, 96, 192)),
            stage4=dict(
                num_modules=3,
                num_branches=4,
                block='BASIC',
                num_blocks=(4, 4, 4, 4),
                num_channels=(48, 96, 192, 384))),
    ),
    keypoint_head=dict(
        type='TopDownSimpleHead',
        in_channels=48,
        out_channels=channel_cfg['num_output_channels'],
        num_deconv_layers=0,
        extra=dict(final_conv_kernel=1, ),
    ),
    train_cfg=dict(),
    test_cfg=dict(
        flip_test=False,
        post_process=False,
        shift_heatmap=False,
        unbiased_decoding=False,
        modulate_kernel=11),
    loss_pose=dict(type='JointsMSELoss', use_target_weight=True))

data_cfg = dict(
    image_size=[288, 384],
    heatmap_size=[72, 96],
    num_output_channels=channel_cfg['num_output_channels'],
    num_joints=channel_cfg['dataset_joints'],
    dataset_channel=channel_cfg['dataset_channel'],
    inference_channel=channel_cfg['inference_channel'],
    soft_nms=False,
    nms_thr=1.0,
    oks_thr=0.9,
    vis_thr=0.2,
    bbox_thr=1.0,
    use_gt_bbox=True,
    image_thr=0.0,
    bbox_file='data/coco/person_detection_results/'
    'COCO_val2017_detections_AP_H_56_person.json',
)

train_pipeline = [
    dict(type='LoadImageFromFile'),
    # dict(type='TopDownRandomFlip', flip_prob=0.5),
    # dict(
    #     type='TopDownHalfBodyTransform',
    #     num_joints_half_body=8,
    #     prob_half_body=0.3),
    dict(
        type='TopDownGetRandomScaleRotation', rot_factor=40, scale_factor=0.5),
    dict(type='TopDownAffine'),
    dict(type='ToTensor'),
    dict(
        type='NormalizeTensor',
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]),
    dict(type='TopDownGenerateTarget', sigma=3, unbiased_encoding=True),
    dict(
        type='Collect',
        keys=['img', 'target', 'target_weight'],
        meta_keys=[
            'image_file', 'joints_3d', 'joints_3d_visible', 'center', 'scale',
            'rotation', 'bbox_score','flip_pairs'
        ]),
]

val_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='TopDownAffine'),
    dict(type='ToTensor'),
    dict(
        type='NormalizeTensor',
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]),
    dict(
        type='Collect',
        keys=['img'],
        meta_keys=[
            'image_file', 'center', 'scale', 'rotation', 'bbox_score','flip_pairs'

        ]),
]

test_pipeline = val_pipeline


data_root = '/mnt/data/samples/upward/suit540/v3_1_gan'
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type='TopDownCocoWeijingDataset',
        ann_file=f'{data_root}/left_train1.json',
        img_prefix=f'{data_root}/left_train/',
        data_cfg=data_cfg,
        pipeline=train_pipeline),
    val=dict(
        type='TopDownCocoWeijingDataset',
        ann_file=f'{data_root}/left_test.json',
        img_prefix=f'{data_root}/left_test/',
        data_cfg=data_cfg,
        pipeline=train_pipeline),
    test=dict(
        type='TopDownCocoWeijingDataset',
        ann_file=f'{data_root}/12down_train.json',
        img_prefix=f'{data_root}/train_v3_ok_img/',
        data_cfg=data_cfg,
        pipeline=train_pipeline),
)
# load_from = 'demo/hrnet_w48_coco_wholebody_384x288-6e061c6a_20200922.pth'