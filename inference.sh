python inference.py \
--user-dir models \
--tokenizer moses \
--bpe subword_nmt \
--bpe-codes data/fairseq_data/codes.txt \
--preproc-dir data/fairseq_data  \
--path saved_model/checkpoint_best.pt \
--input data/fairseq_data/test-ids.txt \
--beam 5 \

