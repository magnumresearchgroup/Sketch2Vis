dataDir=raw_data
styleTransferTempImgDir=trans_img_temp
imgDir=imgs


python PhotoSketch/test_pretrained.py \
    --name pretrained \
    --dataset_mode test_dir \
    --dataroot ${dataDir}/${styleTransferTempImgDir} \
    --results_dir ${dataDir}/${imgDir} \
    --checkpoints_dir checkpoints/PhotoSketch \
    --model pix2pix \
    --which_direction AtoB \
    --norm batch \
    --input_nc 3 \
    --output_nc 1 \
    --which_model_netG resnet_9blocks \
    --no_dropout