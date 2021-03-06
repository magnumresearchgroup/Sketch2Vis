python -m fairseq_cli.train \
  --user-dir models \
  --preproc-dir data/fairseq_data \
  --save-dir saved_model \
  --task captioning \
  --arch simplistic-captioning-arch  \
  --encoder-layers 6 \
  --decoder-layers 6 \
  --optimizer adam \
  --adam-betas "(0.9,0.999)" \
  --lr 0.0003 \
  --lr-scheduler inverse_sqrt \
  --warmup-init-lr 1e-8 \
  --warmup-updates 10000 \
  --weight-decay 0.0001 \
  --dropout 0.3 \
  --max-epoch 200 \
  --max-tokens 1024 \
  --max-source-positions 96 \
  --encoder-embed-dim 512 \
  --save-interval 25 \
  --batch-size 15 \
  --criterion label_smoothed_cross_entropy \
  --arch simplistic-captioning-arch