# word2vec-paritcle-connection-on-wikipedia-corpus

研究でword2vecを用いる際に，日本語Wikipediaコーパスを助詞に着目して分かち書きして使用するために作成


##例 (6/25修正)
```
隣の客はよく柿喰う客だ
```
という文章は

```
隣の　客は　よく　柿　喰う　客　だ
```
と

```
隣　の客　は　よく　柿　喰う　客　だ
```
に分かち書きされる（はず...）

word2vecで学習する際に，前後の助詞とのつながりを考慮した周辺語を学習できる．
