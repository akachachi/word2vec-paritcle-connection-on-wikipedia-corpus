import MeCab


def wakati_for_particle(text):
    mt = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")
    mt.parse('')
    node = mt.parseToNode(text)
    
    """
    今のnodeと次のnodeをみて，
    助詞なら　今と次の語をつなげて　次のnodeへ．
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
    f = open("jawiki.txt", "r")

    text = ""
    for row in f:
        text += wakati_for_particle(row)

    f.close()

    f = open("jawikisep.txt", "w")
    f.write(text)
    f.close()
