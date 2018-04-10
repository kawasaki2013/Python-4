## [基本](https://www.blogger.com/null)

<div style="color: #200000;">まず始めに、Pythonのことを疑似コードだと考えてください。これは、ほとん ど事実といえます。変数はタイプを持たないので、あなたはそれの使用を宣言 をする必要がありません。変数は、あなたが代入した時に作られ、そしてこれ 以上使うことがなくなった時に消えます。代入は=演算子によってなされま す。等しいかどうかは==によって確かめられます。いくつもの変数を一 度に代入することもできます。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">x,y,z = 1,2,3

first, second = second, first

a = b = 123
</pre>

<div style="color: #200000;">区切りは、インデントによって表します。インデント"だけ"でです(BEGINも ENDなしです)。一般的な制御構文を見てみるとこうなります。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">if x < 5 or (x > 10 and x < 20):
    print "The value is OK."

if x < 5 or 10 < x < 20:
    print "The value is OK."

for i in [1,2,3,4,5]:
    print "This is iteration number", i

x = 10
while x >= 0:
    print "x is still not negative."
    x = x-1
</pre>

<div style="color: #200000;">最初の二つは、同じ意味です。</div>

<div style="color: #200000;">forループには"リスト"(例で書かれたような)の要素がひとつずつインデック ス変数として与えられます。"普通の"forループ(カウントしていくループのこ とですね)を作るには、ビルト-イン関数のrange()を使います。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;"># Print out the values from 0 to 99 inclusive.
for value in range(100):
    print value
</pre>

<div style="color: #200000;">("#"で始まる行はコメントで、インタプリタはその部分を無視します。)</div>

<div style="color: #200000;">さあ、これであなたは、どんなアルゴリズムでもPythonで実装するのに十分な ことを(理論上は)知ったはずです。では次は、ユーザーとの対話のための"基 本的な"機能の使い方を、知識に加えましょう。ユーザーから(テキストプロン プトで)入力を受けとるには、ビルトイン関数のinputをつかいます。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">x = input("Please enter a number: ")
print "The square of that number is", x*x
</pre>

<div style="color: #200000;">input関数は、指示されたプロンプトを表示し(空の時もある)、ユーザーに Pythonで有効な値を入力させます。この場合は、私たちは数字を期待している んでしょうか?もし(文字列のような)別なものが入力されたなら、プログラム はクラッシュします。それを避けるために、私たちは何らかのエラーチェック が必要でしょう。エラーチェックの話は後にとっておきたいので、もしあなた がユーザーから、一語一語、文字列で(文字列だったら、"なんで"も入力する ことができますしね)入力を受け付けたいなら、raw_inputを代わりに使いましょ う、と言うことだけで今は、満足しておきましょう。もし文字列sを整数に変 換したいのなら、int(s)を使えばできます。</div>

<dl style="color: #200000;">

<dt>**注意:**</dt>

<dd>もし、inputで文字列を受け付けたいなら、ユーザーは引用符で明示的 に文字列を括る必要があります。Pythonでは、文字列は引用符か二重引用符で 括られているからです。  
</dd>

</dl>

<div style="color: #200000;">さあ、私たちはこれで制御構文と入・出力をマスターしたわけです。次に必要 になってくるのは、かっこいいデータ構造ですね。データ構造で一番重要なの は、"リスト"と"辞書"です。リストは大括弧で表されます。そして、(当然)入 れ子にすることができます。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">name = ["Cleese", "John"]

x = [[1,2,3],[y,z],[[[]]]]
</pre>

<div style="color: #200000;">リストの良い所のひとつは、"インデックス"や"スライス"を使って、要素に別々 にでも、まとめてでもアクセスすることができるという所です。インデックス 参照は(その他多くの言語のように)、大括弧で括ったインデックス番号をリス ト名に続けることで使えます。(最初の要素の番号は0であることに注意)</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">print name[1], name[0] # Prints "John Cleese"

name[0] = "Smith"
</pre>

<div style="color: #200000;">スライスは、ほとんどインデックスと同じですが、欲しい位置の最初と終りを コロン":"で分けて、指し示すことができる所が違います。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">x = ["spam","spam","spam","spam","spam","eggs","and","spam"]

print x[5:7] # Prints the list ["eggs","and"]
</pre>

<div style="color: #200000;">スライスの終りの位置は、含まれないことに注意して下さい。もし、インデッ クス番号を指示しなければ、その方向の全ての要素を指示したことになります。 例えば、list[:3]は、listの最初の要素から、インデックス番号3の手前まで の全て、という意味になります(この仕様に関しては、3は0から数えると実際 は4番目になるから、3は含まれないのだ、というふうに主張されています…ふー ん、なるほど)。それに対して、list[3:]というのは、listの3番目(を含む)の 要素から最後(も含む)まで、という意味です。実に面白いやり方として、あな たは、負の数を使うこともできます。list[-3]というのは、リストの最後から 三番めという意味になります…</div>

<div style="color: #200000;">インデックス参照に関連したこととして、lenというリストの長さを返すビル ト-イン関数もあります。</div>

<div style="color: #200000;">さて、次は?辞書って何でしょう?簡単に言うと、順番のないリストのようなも のです。では、どうやって要素を選択すれば良いのでしょう?実は、辞書の全 ての要素は"キー"または、"名前"とも言えるものを持っていて、実際の辞書の ようにそれを要素を探す用途に使えるのです。辞書の例を二つあげると、</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">{ "Alice" : 23452532, "Boris" : 252336,
  "Clarice" : 2352525, "Doris" : 23624643}

person = { 'first name': "Robin", 'last name': "Hood",
           'occupation': "Scoundrel" }
</pre>

<div style="color: #200000;">この場合私たちは、その人(person)の職業を調べるために person["occupation"]という表現を使います。もし彼のラストネームを変えた かったら、以下のように書きます。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">person['last name'] = "of Locksley"
</pre>

<div style="color: #200000;">簡単でしょ?リストと同じく辞書も、他の辞書やリストを要素として持つこと ができます。そして、必然的にリストが辞書を持つこともできます。というこ とは、あなたは簡単に高度なデータ構造を作ることができるという訳です。</div>

## [関数](https://www.blogger.com/null)

<dl style="color: #200000;">

<dt>**次の一歩:**</dt>

<dd>抽象化をしよう。コードひとつひとつに名前を付けて、二つのパラ メーターと一緒に呼び出してみましょう。そのことを他の言い方でいうと?(抽ー 象ー化ー!) 私たちは今、関数(または、"手続き")を定義してみたいです。で、 どうすればいいでしょう?単に、以下のようにdefキーワードーを使えばいいだけ です。</dd>

</dl>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">def square(x):
    return x*x

print square(2) # Prints out 4
</pre>

<div style="color: #200000;">中には、こう言うと理解できる人もいるでしょう: Pythonでは全てのパラメー ターは"参照によって"渡されます。これは、例を挙げるとJavaと同じように働 くということです。では、例を見てみましょう。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">def change(some_list):
    some_list[1] = 4

x = [1,2,3]
change(x)
print x # Prints out [1,4,3]
</pre>

<div style="color: #200000;">見ての通り、関数にはリスト本体が渡され、関数はそれを変更し、その変更は 関数が呼ばれた空間にも適用されました。注意して欲しいのは、以下の例のよ うな振る舞いです。</div>

<pre style="background: rgb(224, 224, 224); color: #200000; padding: 3pt;">def nochange(x):
    x = 0

y = 1
nochange(y)
print y # Prints out 1
</pre>

<div style="color: #200000;">なぜ変更されなかったのでしょう?その理由は、私たちは"値を変えなかったか ら"です!関数に渡された値は1でしたね?実は、私たちは、リストを変えるのと 同じように数字を変えることはできません。数字の1は(いつだって)1です。私 たちが変更"した"のは、ローカル変数(パラメーター)xの中身であって、この 変更は環境に持ち越されません。</div>

<dt style="color: #200000;">**今言ったことを理解できなかった人へ:**</dt>

<dd style="color: #200000;">心配しないで下さい。この事が理解で きないなら、考えなかったらいいだけですよ:)  
Pythonは"キーワード引数"や"デフォルト引数"といった素敵な機能によって、 さまざまな数値を関数に縛り付けておく事ができます。もっと情報が欲しい方 は、 [Pythonチュートリアルのセクション4.7](http://www.python.org/doc/current/tut/node6.html#SECTION006700000000000000000)を見て下さい。  

もしあなたが、関数の一般的な使い方を知っているのなら、Pythonで関数につ いて知らなければいけない基本的な事を、既に知っている事になります。(も ちろん、そうです…returnキーワードは関数の実行を停止して、与えられた値 を返すようになっています。)  

知っておくと便利かもしれない事のひとつは、実は、Pythonでは関数も値だと いう事です。つまり、あなたがsquareという関数を持っていたら、こうする事 ができます。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">queeble = square
print queeble(2) # Prints out 4
</pre>

関数を引数なしで呼び出すには、doit()であってdoitでないという事を覚えて おいて下さい。後者の場合は、例で見たように関数自身が返され、結果が返さ れる訳ではありません。(これはメソッドオブジェクトにも当てはまります… 後の章を見て下さい)  

## [オブジェクトと材料たち](https://www.blogger.com/null)

私はこの章では、あなたが既にオブジェクト指向プログラミングがどういった ものかということを知っている事として話を進めていきます。(もしそうでな いなら、この章の内容はあまりしっくり来ないかもしれません。でも問題ない です…オブジェクトなしで始めたらいいだけの事ですから:))Pythonではクラ スをclassというキーワードで定義します(あまりの自明さに、めまいが…)。 では例を見ましょう。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">class Basket:

    # Always remember the *self* argument
    def __init__(self,contents=None):
        self.contents = contents or []

    def add(self,element):
        self.contents.append(element)

    def print_me(self):
        result = ""
        for element in self.contents:
            result = result + " " + `element`
        print "Contains:"+result
</pre>

<dl>

<dt>**ここでの新事項:**</dt>

<dd> 

*   全てのメソッド(オブジェクトの中の関数)は引数のリストの1番目にオ ブジェクト自身の入った引数を受けとる。(その引数は、習慣的にselfと いう名で呼ばれている)
*   メソッドは、以下のように呼び出す: object.method.(arg1,arg2)
*   __init__のような名前のメソッドは、特別なもので、必ず定義される。__ init__というはクラスの"コンストラクタ"の名前で、例えば、あなたがイ ンスタンスを作る時に呼び出される。
*   関数呼び出しの時に埋めなくてもよい引数を作ることや、引数にデフォ ルトの値を与えたりする事ができる(関数の章で触れたように)。デフォル ト引数を使いたければ以下のようにする。

    <pre style="background: rgb(224, 224, 224); padding: 3pt;">def spam(age=32): ...
    </pre>

    この例では、spamは0から1個のパラメーターとともに呼ばれる。もし何も 与えられなければ、ageパラメーターの値は32になる。
*   この例で使われた"ショート・サーキット・論理"は少し難しいです…後 で説明しましょう。
*   逆引用符(バッククウォート)は、オブジェクトを、説明の文字列に変換 する。(つまり、elementの中身が数字の1なら、`element`というのは、1 と同じことで、'element'というのはただの文字列です。)
*   足し算の記号"+"はリストの結合にも使われる。文字列というのは実は、 文字のリストである。(このことは、文字列にもインデックス参照やスラ イス、len関数を使える事を意味している。クールでしょ?)  

</dd>

</dl>

Pythonでは、どのメソッドも変数も(privateのようには)プロテクトされてい ません。カプセル化はプログラミングスタイル以上のものです。(もしあなた が、"本当に"そういったものを必要としているなら、ネーミング・コンベンショ ン(命名の規則)が同様のプライバシーを提供してくれます:))  

では次は、ショート・サーキット論理についてです…  

Pythonの中の変数は全て、論理値として使う事ができます。[]、0、""、None のような"空"の値は、偽を意味し、その他の値の時([0]、1、"Hello, world" など)は、真を意味します。  

a and bのような論理式は、次のような動作をします。まず、aが真かどうか確 かめます。もしそうで"ない"なら、単純にaを返します。もし"そう"なら、bを 返します(これが式の真の値を返すから)。a or bという式の仕組みは、もしa が真ならそれを返し、そうでないならbを返す。といった風になります。  

この仕組みは、andとorの動作を、Pythonには導入されていないブーリアン演 算子のようにし、また、この機能はあなたが簡潔で魅力的な条件文を書けるよ うにします。たとえば、次の例の様にです。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">if a:
    print a
else:
    print b
</pre>

上の例の代わりに、こう書けます。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">print a or b
</pre>

これはPythonの慣用表現で、あなたはこれをよく使うようになるかも知れませ ん。これは、私たちがBasket.__init__メソッドの中でやったことです。引数 contentsは、デフォルトの値None(偽になる)を持っています。つまり、値を持っ ているかどうかチェックするには、こう書く事もできます。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">if contents:
    self.contents = contents
else:
    self.contents = []
</pre>

もちろん、あなたはこれよりうまい方法を既に知っていますね。では、なぜ最 初の引数にデフォルト値として[]を与えなかったかわかりますか?その理由は、 Pythonの動作の仕方に関係あります。def __init__(self,contents=[]):と 書いた場合、Pythonは"同一の"空リストをデフォルト値として与えます。その リストに何か詰め込まれると、このリストを使う所全てが同じ内容になってし まい、よって、デフォルト値はそれ以降、空でなくなるわけです…これについ てもっと知りたいのなら、ドキュメントを読んで"同一(identity)"と"同じ値 (equality)"の違いを調べるべきでしょう。  

上でやった事を、こういうやり方でもできます。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def __init__(self, contents=[]):
    self.contents = contents[:]
</pre>

何をやっているのか見当はつきますか?どこででも同じ空リストを使う代わり に、contents[:]という文でコピーを作る事ができるのです。(私たちは、単純 に全体をスライスしただけです。)  

これで、名前の通り"かご(Basket)"を作って使う(何かメソッドを呼び出すな ど)事ができるようになったわけです。使い方はこうなります。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">b = Basket(['apple','orange'])
b.add("lemon")
b.print_me()
</pre>

__init__の様な魔法のメソッドは、他にもはあります。そのひとつが、__ str__で、このメソッドではオブジェクトが文字列のように参照されたら、ど ういう振る舞いをするかを定義します。私たちはこれをBasketのprint_meの代 わりに使う事ができます。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def __str__(self):
    result = ""
    for element in self.contents:
        result = result + " " + `element`
    return "Contains:"+result
</pre>

さあこれで、私たちがBasketインスタンスbを表示したければ、こういう風に すればいいだけです。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">print b
</pre>

賢いやり方でしょ?  

サブクラスの作り方は、こうなります。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">class SpamBasket(Basket):
    # ...
</pre>

Pythonは多重継承を認めているので、あなたが望むなら、コンマで区切る事で、 スーパークラスをいくつも括弧の中に入れる事ができます。クラスはx = Basket()のように継承されます。前に書いたように、コンストラクターは、__ init__という特別なメンバー関数を定義する事で作れます。SpamBasketが__ init__(self,type)というコンストラクターを持っているなら、あなたはスパ ムバスケットをy = SpamBasket("apples")のように作る事ができるという わけです。  

もしあなたが、SpamBasketの中で、ひとつまたはそれ以上のスーパークラスの コンストラクターを呼ぶ必要がある場合は、Basket.__init__(self)のように すると呼び出す事ができます。スーパークラスの__init__は、どのインスタン スに対して呼び出されるのかという事を知らないので、selfを明確にパラメー ター中へ追加しておかないといけないという事に注意して下さい。  

Pythonでのオブジェクト指向プログラミングの不思議についてもっと知りたい 方は、[チュートリアル のセクション9](http://www.python.org/doc/tut/classes.html)を見て下さい。  

## [A Jedi Mind Trick](https://www.blogger.com/null)

(この章は、私が個人的にクールだと思ったから追加したわけで、Pythonにつ いて勉強するには、これを読まないといけないというわけでは*ありません*。 Python2.1での変更に関しては章末を見て下さい。)  

あなたは、想像を越えた考えとかは好きな方ですか?もしそうであって、あな たが本当に大胆なら、Guido van Rossum(訳注:知っての通りPythonの創造主) の[メタクラスに関 するエッセイ](http://www.python.org/doc/essays/metaclasses/)を読んでみたいと思うかも知れません。しかし、もしあなた の脳味噌が爆発するような目に会いたく"ない"のなら、この章でお教えする、 ちょっとしたテクニックで我慢しておいた方が良いでしょう…  

Pythonは字句解析ではなく動的(ダイナミック)な名前空間で実装されています。 このことは、以下のような関数を持つ事ができるということです。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def orange_juice():
    return x*2
</pre>

…変数(この場合はx)が、引数にも括り付けられてないし、関数の中でも与え られていません。Pythonは関数が呼ばれた場所によって、そこにある変数を使 うのです。この例の場合、こうできます。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">x = 3
y = orange_juice()
# y is now 6
x = 1
y = orange_juice()
# y is now 2
</pre>

普通、これはあなたが望んだ通りの振る舞いです(あなたは滅多に、こういう 変数へのアクセスの仕方はしないでしょうから、この例は不自然かもしれませ んが)。"しかしながら"、時には静的な名前空間があると、便利なこともあり ます。そういった理由から、関数が作られた時に、環境から値を取り込んでお くという事もできます。この動作はPythonでは、デフォルト引数によって実現 できます。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">x = 4
def apple_juice(x=x):
    return x*2
</pre>

この例では、引数xへ、同じ名前の変数xの値が、関数が定義された時にデフォ ルト値として与えられます。よって、この関数に誰も引数を与えなければ、以 下のように動作します。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">x = 3
y = apple_juice()
# y is now 8
x = 1
y = apple_juice()
# y is now 8
</pre>

つまり、どういうことでしょう?xの値は変わらなかった訳です。もしこれが私 たちの望む動作なら、以下のように書けば良いだけでしょう。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def tomato_juice():
    x = 4
    return x*2
</pre>

なんなら、こう書いたって差し支えありません。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def carrot_juice():
    return 8
</pre>

しかしながら、"重要"な事は、xの値は関数が定義された時に"環境"から取っ て来られるという事です。これは何かに使えそうじゃありませんか?実用例を 見てみましょうか?では、次は二つの関数をひとつにまとめる関数を作ってみ ましょう。  

私たちは、関数がこう動くよう期待しています。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">from math import sin, cos

sincos = compose(sin,cos)

x = sincos(3)
</pre>

composeというのが私たちが作ろうという関数で、xの値は-0.836021861538に なります。これは、sin(cos(3))と同じ事です。では、これを作るには、どう したらよいでしょう?  

(ここで、私たちは関数自身を引数として使っています…これ自体は、ちゃん としたテクニックです。)  

明らかに、composeは二つの関数をパラメーターとして受けとらなくてはなり ません。よって、解答の骨組みは以下のようになります。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def compose(fun1, fun2):
    def inner(x):
        pass # ...
    return inner
</pre>

inner関数の中にreturn fun1(fun2(x))と書いたらいいだけじゃないのかな?と 思うかもしれませんが…それじゃあいけません。それでは、奇妙な動きをして しまいます。次の筋書きを考えてみてください。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">from math import sin, cos

# Wrong version
def compose(fun1, fun2):
    def inner(x):
        return fun1(fun2(x))
    return inner

def fun1(x):
    return x + " world!"

def fun2(x):
    return "Hello,"

sincos = compose(sin,cos)  # Using the wrong version

x = sincos(3)
</pre>

さあ、ではxには何が入っているでしょう?その通り、"Hello, world"ですね。 では、なぜそうなるのでしょう?その理由は、composeが作られた時ではなく、 呼び出された時にfun1とfun2の値を環境から取ってくるからです。これをちゃ んと動かすためには、さっき私が言ったテクニックを使えばいいのです。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def compose(fun1, fun2):
    def inner(x, fun1=fun1, fun2=fun2):
        return fun1(fun2(x))
    return inner
</pre>

これで後は、誰かがわざとこの関数を壊そうとして、ひとつ以上の引数を与え たりしないよう祈るだけです:-)。ついでに言うと、lambdaというキーワード を使う事によって、"匿名"の関数を作る事によって、実は、私たちはinnerと いう名前も必要なくなります。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def compose(f1, f2):
    return lambda x, f1=f1, f2=f2: f1(f2(x))
</pre>

簡潔明瞭ですね。あなたはこれが大好きになるでしょう:-)  

(もしこの章の内容が理解できなくても、心配しないで下さい。少なくとも、 Pythonは"ただのスクリプト言語"以上のものだって事は、あなたに解ってもら えたと信じています:-))  

## [Python2.1と入れ子スコープに関する注意書き](https://www.blogger.com/null)

Python2.1では冒険的に、静的な入れ子状のスコープ、またの呼び名を名前空 間が(オプションとして)導入されています。つまりこれは、あなたが何もトリッ キーなことをしなくても、上の章でしたのと同じ事ができるようになるという ことです。以下のように、簡単に書けばよいのです。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;"># This magic won't be necessary in Python 2.2:
from __future__ import nested_scopes

def compose(fun1, fun2):
    def inner(x):
        return fun1(fun2(x))
    return inner
</pre>

…これで、期待通りに動くことでしょう。  

## [さあ、次は…](https://www.blogger.com/null)

終りを前にして、あと2、3個言っておくことがあります。一番便利な関数やク ラスは、"モジュール"に入っているということです。モジュールというのは、 実際にPythonのコードが入っているテキストファイルの事です。あなたは、そ れをインポートして、自分のプログラムの中で使う事ができます。例えば、ス タンダード・モジュールのstringにあるsplitメソッドを使うには、二通りの やりかたがあります。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">import string

x = string.split(y)
</pre>

もしくは…  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">from string import split

x = split(y)
</pre>

スタンダード・ライブラリー・モジュールに関する情報は、 [www.python.org/doc/lib](http://www.python.org/doc/lib/)を見て 下さい。スタンダード・ライブラリーには便利なものがたくさんあります。  

全てのモジュール/スクリプトは、インポートした時に実行されます。もしあ なたのプログラムをインポート用のモジュール、単独での実行可能なプログラ ムの両方に対応させたいなら、次の様な文をコードの終りに付け加えると良い でしょう。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">if __name__ == "__main__": go()
</pre>

この魔法を唱えると、プログラムは実行可能なスクリプトとして動作します (つまり、このif文の中身は他のスクリプトにインポートされないという訳で す)。もちろん、go関数が直接呼び出された場合はコロンの後に続くものと同 じことをしますよ:-)  

そして、UN*X上でこのスクリプトをファイル名で実行可能にしたければ、次の 文を一番最初の行に書き加えればいいでしょう。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">#!/usr/bin/env python
</pre>

最後に、重要な概念、"例外"について話しましょう。ある操作(何かを0で割る とか、存在しないファイルから読み込むとか)は、エラーまたは"例外"を発生 させます。あなたが自分で、適当な時に"例外"を発生させることもできます。  

もし、例外に対する措置が何もされていないなら、あなたのプログラムは、エ ラーメッセージを表示して終了します。あなたはそれを、try/except文を使っ て避けることができます。例えば、  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">def safe_division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
</pre>

ZeroDivisionErrorは標準的なエラーです。この例であなたは、bが0で割れる かどうか確かめることが"できます"。しかし多くの場合、この行為は成功しな いでしょう。その上、私たちが、safe_divisionのなかでtry文を使わなかった ら、この関数を呼ぶ事は、危険極まりなくなるでしょう。私たちは、次のよう にする事もできます。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">try:
    unsafe_division(a,b)
except ZeroDivisionError:
    print "Something was divided by zero in unsafe_division"
</pre>

"普通なら"特別な問題は起こらないという場合でも、もし起こる"可能性があ る"なら、"例外"を使う事によって、代償の高くつくテストやいろいろな事を 避ける事ができることでしょう。  

どうでした?これでおしまいです。あなたがこの文章で何かを学べたことを願っ てますよ。この後は、[www.python.org](http://www.python.org/)に 行っていろいろ試してみて下さい。そして、Pythonを学ぶ際のモットーは"ルー ク、ソースを使え!(Use the source, Luke.)"だということを、忘れないよう にして下さい(手に入れたコードを全て読め、という意味です:))。始めるに当 たって、ここに[例](http://www.hetland.org/python/quicksort.py) があります。これは、Hoareの有名な"クイックソート"アルゴリズムです。カ ラーバージョンは、[ こちら](http://www.hetland.org/python/quicksort.html)にあります。  

この例について、説明をひとつ付け加えておきましょう。done変数は partitionがリストの要素を走査し終ったかどうかをコントロールします。内 側のループのどちらかが、順序交換を完全に終えたという時に、doneに1がセッ トされbreak文でそこから抜け出します。では、なぜ内側のループのチェック もdoneが使われているのでしょう?その理由は、内側のループひとつ目がbreak で終了したのなら、いずれにせよ、二つ目のループが実行されるかは、メイン ループが終了しているか(doneがセットされているか)という事に依存してくる からです。つまり、doneがセットされた状況で、二つ目のループが実行された としても、doneに1をセットしてbreakするだけだからです。  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">while not done:
    while not done:
        # Iterates until a break

    while not done:
        # Only executed if the first didn't set "done" to 1
</pre>

これと同じ、または、より明確なバージョンはこうなります。(でも、私は上 の方が好きです。)  

<pre style="background: rgb(224, 224, 224); padding: 3pt;">while not done:
    while 1:
        # Iterates until a break

    if not done:
        while 1:
            # Only executed if the first didn't set "done" to 1
</pre>

私が、ひとつ目のループのチェックにdone変数を使っている理由は、ただ、こ の二つのループの対称性を保ちたいがためです。そういうわけで、どっちを使っ てもこのアルゴリズムは動くわけです。</dd>
