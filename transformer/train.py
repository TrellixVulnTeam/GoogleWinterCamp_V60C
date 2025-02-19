import tensorflow as tf
import tensorflow_datasets as tfds

import os
import re
import numpy as np
import pickle
from argparse import ArgumentParser

import config
from util import get_dataset, get_args
from model import transformer, CustomSchedule, loss_function, accuracy


def train(inputs, outputs, args):
    tf.keras.backend.clear_session()
    dataset, VOCAB_SIZE, _ = get_dataset(inputs, outputs, args)
    cur_model = transformer(
        vocab_size=VOCAB_SIZE,
        num_layers=config.NUM_LAYERS,
        units=config.UNITS,
        d_model=config.D_MODEL,
        num_heads=config.NUM_HEADS,
        dropout=config.DROPOUT)
    learning_rate = CustomSchedule(config.D_MODEL)

    optimizer = tf.keras.optimizers.Adam(
        learning_rate, beta_1=0.9, beta_2=0.98, epsilon=1e-9)

    cur_model.compile(optimizer=optimizer, loss=loss_function, metrics=[accuracy])
    if args.pre_train:
        # cur_model = tf.keras.models.load_model(args.pre_train_model_path)
        cur_model.load_weights(args.pre_train_model_path)
        print('load pre train model success!')
    print('build model success, start training...')
    cur_model.fit(dataset, epochs=args.epochs)

    cur_model.save_weights(args.save_model_path)


if __name__ == "__main__":
    # 读入
    args = get_args()
    questions_infile = open(args.input_path, 'rb')
    answers_infile = open(args.output_path, 'rb')
    questions = pickle.load(questions_infile)
    answers = pickle.load(answers_infile)
    print('load data success, from ' + args.input_path)
    train(questions, answers, args)

