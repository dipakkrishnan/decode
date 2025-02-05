from datasets import load_dataset
import tensorflow as tf


def build_dataset(batch_size: int = 32, shuffle_buffer: int = 10000):
    # Load dataset
    dataset = load_dataset("wikitext", "wikitext-2-raw-v1")

    # Convert to tensorflow format
    tf_dataset = tf.data.Dataset.from_tensor_slices(dataset["train"]["text"])

    tf_dataset = tf_dataset.shuffle(shuffle_buffer)
    tf_dataset = tf_dataset.filter(lambda x: tf.strings.length(x) > 0)
    tf_dataset = tf_dataset.batch(batch_size, drop_remainder=True)
    tf_dataset = tf_dataset.prefetch(tf.data.AUTOTUNE)

    return tf_dataset
