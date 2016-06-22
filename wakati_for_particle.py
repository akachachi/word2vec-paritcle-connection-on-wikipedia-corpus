import MeCab


def wakati_for_particle(text):
    mt = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")
    mt.parse('')
    node = mt.parseToNode(text)
    
    """
    今のnodeと次のnodeをみて，
    次のnodeが助詞なら　今と次の語をつなげて　次のnodeへ．
    今のnodeが助詞なら　今と次の語をつなげて　次の次のnodeへ．
    """
    wakati_txt = ""
    try:
        while node:
            current_feature = node.feature.split(',')
            next_feature = node.next.feature.split(',')

            if current_feature[0] == "助詞":
                wakati_txt += " " + node.surface + node.next.surface 
                node = node.next
            elif next_feature[0] == "助詞":
                wakati_txt += " " + node.surface + node.next.surface
                node = node.next
            else:
                wakati_txt += " " + node.surface
                node = node.next
    except:
        print("テキストの終わり")

    return wakati_txt





if __name__ == '__main__':
    wakati_for_particle("中居正広のタイトルはキンタマ")
