#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import os
from collections import namedtuple

import onmt
import onmt.ModelConstructor
import onmt.modules


translate_model_path = os.environ.get('MODEL_PATH', '')

translate_opts = ['model', 'data_type',
                  'alpha', 'beta', 'beam_size', 'batch_size', 'min_length', 'max_length',
                  'replace_unk', 'verbose', 'attn_debug', 'dump_beam', 'n_best', 'gpu', 'cuda', 'tgt']
Options = namedtuple('Options', translate_opts)
opt = Options(translate_model_path, 'text',
              0, -0, 5, 30, 0, 100,
              True, True, True, False, 3, -1, False, None)
dummy_opt = {'src_word_vec_size': 500, 'tgt_word_vec_size': 500, 'word_vec_size': -1, 'share_decoder_embeddings': False, 'share_embeddings': False, 'position_encoding': False, 'feat_merge': 'concat', 'feat_vec_size': -1, 'feat_vec_exponent': 0.7, 'model_type': 'text', 'encoder_type': 'rnn', 'decoder_type': 'rnn', 'layers': -1, 'enc_layers': 2, 'dec_layers': 2, 'rnn_size': 500, 'cnn_kernel_width': 3, 'input_feed': 1, 'rnn_type': 'LSTM', 'brnn': None, 'brnn_merge': 'concat', 'context_gate': None, 'global_attention': 'general', 'copy_attn': False, 'copy_attn_force': False, 'reuse_copy_attn': False, 'coverage_attn': False, 'lambda_coverage': 1}
fields, model, model_opt = onmt.ModelConstructor.load_test_model(opt, dummy_opt)
scorer = onmt.translate.GNMTGlobalScorer(opt.alpha, opt.beta)
translator = onmt.translate.Translator(model, fields,
                                       beam_size=opt.beam_size,
                                       n_best=opt.n_best,
                                       global_scorer=scorer,
                                       max_length=opt.max_length,
                                       copy_attn=model_opt.copy_attn,
                                       cuda=opt.cuda,
                                       beam_trace=opt.dump_beam != "",
                                       min_length=opt.min_length)


def translate(text):
    with io.StringIO(text) as src_file:
        data = onmt.io.build_dataset(
            fields, opt.data_type,
            src_file, opt.tgt, use_filter_pred=False)
        test_data = onmt.io.OrderedIterator(
            dataset=data, device=opt.gpu,
            batch_size=opt.batch_size, train=False, sort=False,
            sort_within_batch=True, shuffle=False)
        builder = onmt.translate.TranslationBuilder(
            data, translator.fields,
            opt.n_best, opt.replace_unk, opt.tgt)

        result = ''
        for batch in test_data:
            batch_data = translator.translate_batch(batch, data)
            translations = builder.from_batch(batch_data)

            for trans in translations:
                # for pred in trans.pred_sents[:opt.n_best]:
                for pred in trans.pred_sents[:1]:
                    result += " ".join(pred)
                    result += '\n'

        return result.strip()
