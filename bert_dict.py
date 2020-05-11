# coding=utf8
import codecs
import sys
import re
from nstools.zhtools.langconv import *
import emoji


emoji_regex = emoji.get_emoji_regexp()

human_list = ['▲top', '▲topoct', '▲topmay', '▲topapr', '▲topmar', '▲topjun', '▲topdec', '▲topnov', '▲topaug', '▲topjul', '▲topjan', '▲topsep', '▲topfeb', '￥799', '￥2899', '～～', '～～～', '##～6', '##～10', '～10', '##～5', '～5', '##～20', '##～8', '##～17', '##～1', '～4', '##～3', '##～7', '～1', 'ｗedding', '×email', 'ｃｐ', '××', 'ｏｋ', 'ａ', 'ｂ', 'ｃ', 'ｄ', 'ｅ', 'ｆ', 'ｇ', 'ｈ', 'ｉ', 'ｊ', 'ｋ', 'ｌ', 'ｍ', 'ｎ', 'ｏ', 'ｐ', 'ｑ', 'ｒ', 'ｓ', 'ｔ', 'ｕ', 'ｖ', 'ｗ', 'ｘ', 'ｙ', 'ｚ', '##★', '##℃', '##～', '##°', '##☆', '↓↓↓', '##●', '##㎡', '##♪', '##×', '▌♥', '##｜', '##ｄ', '##▲', '##ｏ', '★★', '##→', '#ａ', '⋯⋯', '##▼', '##○', '★★★★★', '##∥', '##◆', '##ω', '★★★', '##ｃ', '##ｓ', '##ｅ', '##ｐ', '##■', '##↑', '##ｋ', '##и', '◆◆', '##ｇ', '##＋', '##а', '±0', '##◎', '##─', '##ｒ', '##＞', '##²', '##ｔ', '★★★★', '##│', '##ｎ', '##ｌ', '##＝', '##ｙ', '☆☆☆', '##ｉ', '##↓', 'ˋ▽ˊ', '##ｖ', '↓↓', '##f2016', '##ｑ', '##₂', '∟∣', '##я', '##←', '##◆◆', '##ｘ', '##cm～', '##ｆ', '##ｈ', '##ｊ', '##ｕ', '##ｗ', '##ｚ']

zhuyin_char = ['ㄅ', 'ㄆ', 'ㆠ', 'ㄇ', 'ㄈ', 'ㄪ', 'ㄉ', 'ㄊ', 'ㄋ', 'ㆹ', 'ㄌ', 'ㄍ', 'ㄎ', 'ㆣ', 'ㄫ', 'ㄏ', 'ㆸ', 'ㄐ', 'ㄑ', 'ㆢ', 'ㄬ', 'ㄒ', 'ㆺ', 'ㄓ', 'ㄔ', 'ㄕ', 'ㄖ', 'ㄗ', 'ㄘ', 'ㆡ', 'ㄙ', 'ㆡ', 'ㆪ', 'ㄨ', 'ㆫ', 'ㆨ', 'ㄩ', 'ㄚ', 'ㆩ', 'ㆦ', 'ㆧ', 'ㄛ', 'ㄜ', 'ㄝ', 'ㆤ', 'ㆥ', 'ㄞ', 'ㆮ', 'ㄟ', 'ㄠ', 'ㆯ', 'ㄡ', 'ㆰ', 'ㆱ', 'ㆬ', 'ㄢ', 'ㄣ', 'ㄯ', 'ㄤ', 'ㆲ', 'ㄥ', 'ㆭ', 'ㄦ', 'ㄭ']

special_token = ['[PAD]', '[UNK]', '[CLS]', '[SEP]', '[MASK]', '<S>', '<T>']

japan_chars = ['ｲ', 'ｸ', 'ｼ', 'ｽ', 'ﾄ', 'ﾉ', 'ﾌ', 'ﾗ', 'ﾙ', 'ﾝ']

korean_chars = ['ᄀ', 'ᄁ', 'ᄂ', 'ᄃ', 'ᄅ', 'ᄆ', 'ᄇ', 'ᄈ', 'ᄉ', 'ᄋ', 'ᄌ', 'ᄎ', 'ᄏ', 'ᄐ', 'ᄑ', 'ᄒ', 'ᅡ', 'ᅢ', 'ᅣ', 'ᅥ', 'ᅦ', 'ᅧ', 'ᅨ', 'ᅩ', 'ᅪ', 'ᅬ', 'ᅭ', 'ᅮ', 'ᅯ', 'ᅲ', 'ᅳ', 'ᅴ', 'ᅵ', 'ᆨ', 'ᆫ', 'ᆯ', 'ᆷ', 'ᆸ', 'ᆺ', 'ᆻ', 'ᆼ', 'ᗜ']

puns = ['“', '‘']

nums = ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '2016', '2017', '2018', '2019', '2020', '2021', '2022']


with codecs.open(sys.argv[1], 'r', 'utf8') as fin,\
    codecs.open(sys.argv[2], 'w', 'utf8') as fout:
    cout_zh = 0
    cout_en = 0
    cout_jp = 0
    cout_em = 0
    cout_zh_res = 0
    cout_zh_tra = 0
    cout_zh_wp = 0
    cout_en_del = 0
    cout_en_res = 0
    cout_num = 0
    cout_num_del = 0
    cout_num_res = 0
    cout_hand_del = 0
    cout_total = 0
    cout_zhuyin = 0
    cout_unused = 0
    cout_special = 0
    cout_jp = 0
    cout_ko = 0

    for line in fin:
        cout_total += 1
        token = line.strip()

        if not token:
            continue

        if token in human_list:
            cout_hand_del += 1  #13
            continue

        # chinese character
        elif re.match(u'[\u4e00-\u9fa5]+', token.replace('##', '')):
            cout_zh += 1  # 14642

            token_simp = Converter('zh-hans').convert(token)
            if token_simp != token:
                cout_zh_tra += 1
                continue
            else:
                if re.match(u'##', token):
                    # print(token)
                    cout_zh_wp += 1
                    continue
                else:
                    cout_zh_res += 1
                    print(token, file=fout)

        # korean character
        elif re.match(u'[\uac00-\ud7ff]+', token.replace('##', '')):
            # print(token)
            cout_ko += 1
            continue

        # japanese character
        elif re.match(u'[\u30a0-\u30ff\u3040-\u309f]+', token.replace('##', '')):
            # print(token)
            cout_jp += 1
            continue

        # english character
        elif re.match(u'[a-z]+', token.replace('##', '')):
            # print(token)
            cout_en += 1
            if re.match(u'##', token):
                # print(token)
                cout_en_res += 1
                print(token, file=fout)
            elif len(token) > 1:
                # print(token)
                cout_en_del += 1
                continue
            else:
                # print(token)
                cout_en_res += 1
                print(token, file=fout)

        # emoji character
        elif re.match(emoji_regex, token.replace('##', '')):
            # print(token)
            cout_em += 1
            continue

        # multi-number characters
        elif re.match(u'(##)?\d', token):
            cout_num += 1
            if len(token.replace('##', '')) == 1:
                # print(token)
                cout_num_res += 1
                print(token, file=fout)
            else:
                cout_num_del += 1
                # print(token)
                continue
        elif token.replace('##', '') in zhuyin_char:
            # print(token, file=fout)
            cout_zhuyin += 1
            continue
        elif token.startswith('[unused'):
            print(token, file=fout)
            cout_unused += 1
        elif token in special_token:
            print(token, file=fout)
            cout_special += 1
            
        elif token.replace('##', '') in japan_chars:
            cout_jp += 1
            continue

        elif token.replace('##', '') in korean_chars:
            cout_ko += 1
            continue
        else:
            # print(token)
            print(token, file=fout)

        # add tokens
        if token == '"':
            for token in puns:
                print(token, file=fout)
        if token == '9':
            for token in nums:
                cout_num_res += 1
                print(token, file=fout)

    print("cout_zh:{}".format(cout_zh))  #14642
    print("cout_zh_tra:{}".format(cout_zh_tra))  #3264
    print("cout_zh_wp:{}".format(cout_zh_wp))  #5689
    print("cout_zh_res:{}".format(cout_zh_res))  #5689
    print("cout_en:{}".format(cout_en))  #3555
    print("cout_en_del:{}".format(cout_en_del))  #2235
    print("cout_en_res:{}".format(cout_en_res))  #1320
    print("cout_num:{}".format(cout_num))  #1179
    print("cout_num_del:{}".format(cout_num_del))  #1137
    print("cout_num_res:{}".format(cout_num_res))  #140
    print("cout_hand_del:{}".format(cout_hand_del))  #132
    print("cout_zhuyin:{}".format(cout_zhuyin))  #36
    print("cout_unused:{}".format(cout_unused))  #99
    print("cout_special:{}".format(cout_special))  #7
    print("cout_jp:{}".format(cout_jp))  #573
    print("cout_ko:{}".format(cout_ko))  #84
    print("cout_em:{}".format(cout_em))  #56









