# gen-ai-nlp-lab-1

## AYA-23-8B Bfloat16 (No-quantization)
Submission on kaggle: https://www.kaggle.com/competitions/gen-ai-ucu-2024-task-1/leaderboard?#
Roman Kovalchuk: 0.150 on Public Score

### EDA:
In `eda.ipynb` my main idea was not only to check the data, but also to check the number of tokens it has in the `train` dataset for `text` and `entities` fields.
For example `entities` and `text` number of tokens distribution. \
P.S. I used tokenizer for the same model I was about to run inference on (AYA-23-8B Bfloat16)[https://huggingface.co/CohereForAI/aya-23-8B]

![Screenshot 2024-12-11 at 22.23.32.png](images%2FScreenshot%202024-12-11%20at%2022.23.32.png)
![Screenshot 2024-12-11 at 22.23.40.png](images%2FScreenshot%202024-12-11%20at%2022.23.40.png)

And as you can see the text is large, having as much as up to 5k tokens, with a median of 2k;\
And the same goes for output tokens we expect (our target) `entities_tokens`, which goes even further to up to 8k output tokens. So here I decided to split it onto 500 text tokens chunks, predict the labels, and concat them back again, having a precise and not too long and confusing prompt. 

### Data Preprocessing:
For data preprocessing I used two notebooks:
- `preprocessing.ipynb` To split the texts and labels to fit a 500 token window per sample, in order for the model, to achieve better results. 
- `preprocessing_test.ipynb` The same was done for test dataset

### Data Splitting Reasoning:
The data was split and preprocessed as said into a `silver_train` and `silver_test` datasets which included our original
test and train data samples, but expanded, and split both by target and its corresponding test into 500 token chunks.
My logic behind it was to have a prompt with following balanced structure:
- Instruction
- Rules and output format
- Examples (took the most of the prompt space, around 1000-1500 tokens depending on number of examples)
- Input text and field for output labels

So, therefore, the training would be stable, with little oscillations due to differences in sizes of each text in dataset.\
However, due to that splitting, we would have multiple issues, including concating those samples back, along with labels,
in order to have the expected answer back.

### Experiments:
I picked AYA-23-8B model to conduct my experiments, as it's a model trained for 23 languages, including a Ukrainian one.

### Post-processing:
I also included post-processing which is needed due to the fact that this model, if not trained does always (rarely) return
proper list, dict, or even JSON, so I included a following post-processing pipeline, in order to have the results as we expect.
So for each list of entities (due to chunking) we do following:
1. Clean Incomplete Entries: This function would return `[]` if the sample has not closed bracket `{`, due to wrong format, or cut of max tokens
2. `ast.literal_eval` and `list`: Here we transform our `str` list of dicts of entities to an actual Python `str`
3. Filter Unique Dicts: We filter the dicts, which have repeated `text` and `label` (which happens often with this model)
4. Merge all chunks, and Filter for Unique Dicts again, i.e., repeat step 3.
5. Bring back text field for our sample
6. Based on that sample's text field, we only include the `text` in `labels` which is in the text (sometimes model changes word cases or imagines some entitites, or picks them from few-shot examples)

### VLLM Experiment:
Unfortunately with this model, I was unable to run the VLLM with or without quantization, as full precision was not supported on Kaggle T4/P100 GPU, and
there was no quantized version in huggingface of this model; furthermore, P100 GPU did not support `bitsandbytes` for this VLLM version.

### Few-shot experiments:
I've constructed various combination of examples, ranging from 3-5-11-15 shots, but as I've observed, with even 5 shot model, this model started to produce unnecessary words before the output, resulting in broken results. So I've ended-up using 3-shot prompt.
You can check the examples I've used in `src/prompts/examples.py` Optimized by `gpt-o1` model from some examples I gave it from the `train` set.

### Notebooks and Inference:

There's a dozen of notebooks I've used for this lab, however my workflow was to run a Google Colab with either L4 or A100 GPU, in order to save time. However, T4 with longer execution time should work as well, however you'd have to enable a constant in the notebook to quantize it to 4bit.

- `eda.ipynb` Notebook used for EDA
- `preprocessing.ipynb` Notebook used for data splitting for train set
- `preprocessing_test.ipynb` Notebook used for data splitting for test set
- `aya-23-8b-vllm.ipynb` My unsuccessful test to run this model on VLLM
- `aya-23-8b-test.ipynb` My go-to notebook to establish a working pipeline
- `aya-23-8b-final.ipynb` My go-to notebook to submit results, I've preset chunks of samples to run in parallel Google Colab sessions (up to 4) to later merge the results faster. Despite some manual labour with downloading and merging the results programmatically it resulted in speed up in time from 4 hours to 1 hour.
- `aya-23-8b-second-run.ipynb` My notebook to conduct a second run on results in order to lower the number of non-scored samples.
- `aya-23-8b-end-to-end.ipynb` Notebook which includes everything, and can be run by you on Google Colab, but expectedly it would take over 10 hours to complete, irrespective of GPU (the difference between L4 and A100 was nominal, and for P100 you'd have to make quantization adjustments)

### Parameters
Here's my parameters for the run: (take in mind, that we expect our chunks to be really small, as we have subdivided them at the pre-processing stage)
```yml
baseline:
  temperature: 0.3
  top_p: 0.75
  top_k: 0
  max_new_tokens: 800

```

### Second-Run to fit non-scored samples:
The first run resulted in 46 non-scored samples out of 169; and the second run, which was conducted using `aya-23-8b-second-run.ipynb` notebook,
lowered the score to only 36 non-scored samples. It could be the problem with input to the model, or a large and complicated text for this one.
The non-scored samples yields, when the LLM outputs a non-valid output without a bracket, invalid JSON etc.\
Good idea here would be to either change the model, or return wrong outputs, change the prompt to correct them, and run the second-run as described in this sentence. \
But I've had limited time, and would I have more time, I would pick to use other model than this one, specifically tailored to Ukrainian Language, as for example `QWEN`
