import MeCab


def wakati_meisi_josi(text):
    mt = MeCab.Tagger("")
    mt.parse('')
    node = mt.parseToNode(text)

    wakati_txt = ""
    try:
        while node:
            current_feature = node.feature.split(',')
            next_feature = node.next.feature.split(',')

            if current_feature[0] == "名詞" and current_feature [1] != "サ変接続" and next_feature[0] == "助詞":
                wakati_txt += " " + node.surface + node.next.surface
                node = node.next.next
            else:
                wakati_txt += " " + node.surface
                node = node.next

    except:
        pass

    return wakati_txt


def wakati_josi_dousi(text):
    mt = MeCab.Tagger("")
    mt.parse('')
    node = mt.parseToNode(text)

    wakati_txt = ""
    try:
        while node:
            current_feature = node.feature.split(',')
            next_feature = node.next.feature.split(',')

            if current_feature[0] == "助詞" and (next_feature[0] == "動詞" or (next_feature[0] == "名詞" and next_feature[1] == "サ変接続")):
                wakati_txt += " " + node.surface + node.next.surface
                node = node.next.next
            else:
                wakati_txt += " " + node.surface
                node = node.next

    except:
        pass

    return wakati_txt
