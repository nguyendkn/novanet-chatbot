![](./images/describe-en.png)
<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README_CN.md">简体中文</a> |
  <a href="./README_JA.md">日本語</a> |
  <a href="./README_ES.md">Español</a>
</p>

[Web サイト](https://chatbot.ai) • [ドキュメント](https://docs.chatbot.ai) • [Twitter](https://twitter.com/chatbot_ai) • [Discord](https://discord.gg/FngNHpbcY7)


**Chatbot** は、より多くの人々が持続可能な AI ネイティブアプリケーションを作成できるように設計された、使いやすい LLMOps プラットフォームです。様々なアプリケーションタイプに対応したビジュアルオーケストレーションにより Chatbot は Backend-as-a-Service API としても機能する、すぐに使えるアプリケーションを提供します。プラグインやデータセットを統合するための1つの API で開発プロセスを統一し、プロンプトエンジニアリング、ビジュアル分析、継続的な改善のための1つのインターフェイスを使って業務を合理化します。

Chatbotで作成したアプリケーションは以下の通りです:

フォームモードとチャット会話モードをサポートする、すぐに使える Web サイト
プラグイン機能、コンテキストの強化などを網羅する単一の API により、バックエンドのコーディングの手間を省きます。
アプリケーションの視覚的なデータ分析、ログレビュー、アノテーションが可能です。
Chatbot は LangChain と互換性があり、複数の LLM を徐々にサポートします:

- GPT 3 (text-davinci-003)
- GPT 3.5 Turbo(ChatGPT)
- GPT-4

## クラウドサービスの利用

[Chatbot.ai](https://chatbot.ai) をご覧ください

## Community Edition のインストール

### システム要件

Chatbot をインストールする前に、お使いのマシンが以下の最低システム要件を満たしていることを確認してください:

- CPU >= 1 Core
- RAM >= 4GB

### クイックスタート

Chatbot サーバーを起動する最も簡単な方法は、[docker-compose.yml](docker/docker-compose.yaml) ファイルを実行することです。インストールコマンドを実行する前に、[Docker](https://docs.docker.com/get-docker/) と [Docker Compose](https://docs.docker.com/compose/install/) がお使いのマシンにインストールされていることを確認してください:

```bash
cd docker
docker compose up -d
```

実行後、ブラウザで [http://localhost/install](http://localhost/install) にアクセスし、初期化インストール作業を開始することができます。

### Helm Chart

@BorisPolonsky に大感謝します。彼は Chatbot を Kubernetes 上にデプロイするための [Helm Chart](https://helm.sh/) バージョンを提供してくれました。
デプロイ情報については、https://github.com/BorisPolonsky/chatbot-helm をご覧ください。

### 構成

カスタマイズが必要な場合は、[docker-compose.yml](docker/docker-compose.yaml) ファイルのコメントを参照し、手動で環境設定をお願いします。変更後、再度 'docker-compose up -d' を実行してください。

## ロードマップ

開発中の機能:

- **データセット**, Notionやウェブページからのコンテンツ同期など、より多くのデータセットをサポートします
テキスト、ウェブページ、さらには Notion コンテンツなど、より多くのデータセットをサポートする予定です。ユーザーは、自分のデータソースをもとに AI アプリケーションを構築することができます。
- **プラグイン**, アプリケーションに ChatGPT プラグイン標準のプラグインを導入する、または Chatbot 制作のプラグインを利用する
今後、ChatGPT 規格に準拠したプラグインや、ディファイ独自のプラグインを公開し、より多くの機能をアプリケーションで実現できるようにします。
- **オープンソースモデル**, 例えばモデルプロバイダーとして Llama を採用したり、さらにファインチューニングを行う
Llama のような優れたオープンソースモデルを、私たちのプラットフォームのモデルオプションとして提供したり、さらなる微調整のために使用したりすることで、協力していきます。


## Q&A

**Q: Chatbot で何ができるのか？**

A: Chatbot はシンプルでパワフルな LLM 開発・運用ツールです。商用グレードのアプリケーション、パーソナルアシスタントを構築するために使用することができます。独自のアプリケーションを開発したい場合、LangChatbotGenius は OpenAI と統合する際のバックエンド作業を省き、視覚的な操作機能を提供し、GPT モデルを継続的に改善・訓練することが可能です。

**Q: Chatbot を使って、自分のモデルを「トレーニング」するにはどうすればいいのでしょうか？**

A: プロンプトエンジニアリング、コンテキスト拡張、ファインチューニングからなる価値あるアプリケーションです。プロンプトとプログラミング言語を組み合わせたハイブリッドプログラミングアプローチ（テンプレートエンジンのようなもの）で、長文の埋め込みやユーザー入力の YouTube 動画からの字幕取り込みなどを簡単に実現し、これらはすべて LLM が処理するコンテキストとして提出される予定です。また、アプリケーションの操作性を重視し、ユーザーがアプリケーションを使用する際に生成したデータを分析、アノテーション、継続的なトレーニングに利用できるようにしました。適切なツールがなければ、これらのステップに時間がかかることがあります。

**Q: 自分でアプリケーションを作りたい場合、何を準備すればよいですか？**

A: すでに OpenAI API Key をお持ちだと思いますが、お持ちでない場合はご登録ください。もし、すでにトレーニングのコンテキストとなるコンテンツをお持ちでしたら、それは素晴らしいことです！

**Q: インターフェイスにどの言語が使えますか？**

A: 現在、英語と中国語に対応しており、言語パックを寄贈することも可能です。

## Star ヒストリー

[![Star History Chart](https://api.star-history.com/svg?repos=nguyendkn/chatbot&type=Date)](https://star-history.com/#nguyendkn/chatbot&Date)

## お問合せ

ご質問、ご提案、パートナーシップに関するお問い合わせは、以下のチャンネルからお気軽にご連絡ください:

- GitHub Repo で Issue や PR を提出する
- [Discord](https://discord.gg/FngNHpbcY7) コミュニティで議論に参加する。
- hello@chatbot.ai にメールを送信します

私たちは、皆様のお手伝いをさせていただき、より楽しく、より便利な AI アプリケーションを一緒に作っていきたいと思っています！

## コントリビュート

適切なレビューを行うため、コミットへの直接アクセスが可能なコントリビュータを含むすべてのコードコントリビュータは、プルリクエストで提出し、マージされる前にコア開発チームによって承認される必要があります。

私たちはすべてのプルリクエストを歓迎します！協力したい方は、[コントリビューションガイド](CONTRIBUTING.md) をチェックしてみてください。

## セキュリティ

プライバシー保護のため、GitHub へのセキュリティ問題の投稿は避けてください。代わりに、あなたの質問を security@chatbot.ai に送ってください。より詳細な回答を提供します。

## 引用

本ソフトウェアは、以下のオープンソースソフトウェアを使用しています:

- Chase, H. (2022). LangChain [Computer software]. https://github.com/hwchase17/langchain

詳しくは、各ソフトウェアの公式サイトまたはライセンス文をご参照ください。

## ライセンス

このリポジトリは、[Chatbot Open Source License](LICENSE) のもとで利用できます。
