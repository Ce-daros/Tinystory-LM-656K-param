from transformers import LlamaTokenizerFast

tokenizer = LlamaTokenizerFast(
    bos_token="[BOS]",  # 设置开始标记
    eos_token="[EOS]",  # 设置结束标记
    unk_token="[UNK]"
)

print(tokenizer)