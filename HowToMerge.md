# Pull Request があった場合の手順(あるといいなあ)

1. Bugzilla に報告して Bug ID を取る
2. レビューして、必要に応じてコメントを出す
3. テストする
4. Ready to merge になったら以下の手順でマージする

### マージ手順

1. Install [hub](https://github.com/github/hub)
2. Pull Request のURLを取得する。https://github.com/HeapStats/heapstats/pull/番号 の形式。
3. ローカルのリポジトリの master ブランチで `git am -3 <2.のURL>` を実行する。コンフリクトが発生したら修正して `git am -continue`
4. ローカル作業で修正する。主な修正点は以下の通り。
 * ChangeLog
5. 以下のどちらかの手順で Commit message を Bug XXX: YYY に修正し、bugzilla URL、Closes ＃番号を入力する。[参考](https://github.com/ykubota/HowManageCommitsWithHG/commit/ca0cebac33f0792a7509a199ece114e7fc85b9a1)
 1. 1 つのコミットの場合： `git commit --amend` でオリジナルのコミットを修正する
 2. 複数のコミットの場合： `git rebase -i origin/master` で一つのコミットに整理する
6. master へ push する

参考情報： [GitHubでの”Merge pull request”の弊害](http://postd.cc/merge-pull-request-considered-harmful/)

### mercurial sync 手順

1. 上の内容にコミットメッセージ "Contributed-by: XXX <YYY@example.com>, Reviewed-by: ZZZ, <github issue url>" をつけて push.

自動化は追々。

