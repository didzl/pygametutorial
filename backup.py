# -*- coding: utf-8 -*-
#
#  migration.py
#
#  Usage: python migration.py src_subdomain src_space_id src_app_id src_api_token tar_subdomain tar_space_id tar_app_id tar_api_token
#  ※ Setting space_id 0, normal space processing
#
import csv, sys, subprocess
  
params = sys.argv # コマンドライン引数
  
argc = len(params)
if (argc != 9):
    print('Usage: python migration.py src_subdomain src_space_id src_app_id src_api_token tar_subdomain tar_space_id tar_app_id tar_api_token')
    quit()
  
BUILTIN_LIST = ['$id', 'レコード番号', '$revision', '作成者', '作成日時', '更新者', '更新日時', 'ステータス'] # ビルトインフィールド
CLI_KINTONE = './cli-kintone' # コマンドラインツール
WORK_DIR = './work1' # 作業用ディレクトリ
DL_CSV = 'backup.csv' # ダウンロードCSVのファイル名
UL_CSV = 'upload.csv' # アップロード用CSVのファイル名
  
# コピー元アプリ情報
src_subdomain = 'md8zrpp7fb4p' # サブドメイン
src_space_id = 0 # ゲストスペースのID（0の時には通常のスペース）
src_app_id = 13 # アプリID
src_api_token = '' # APIトークン
  
# コピー先アプリ情報
tar_subdomain = params[5] # サブドメイン
tar_space_id = params[6] # ゲストスペースのID（0の時には通常のスペース）
tar_app_id = params[7] # アプリID
tar_api_token = params[8] # APIトークン
  
## 作業用ディレクトリ作成
mkdir_cmd = 'mkdir {}'.format(WORK_DIR) # コマンド生成
subprocess.call(mkdir_cmd, shell=True) # コマンド実行
  
## バックアップコマンド（ファイルとCSVをダウンロード）
dl_cmd = '{} -a {} -d {} -t {} -q {} -b {} &gt; {}/{}'.format(CLI_KINTONE, src_app_id, src_subdomain, src_api_token, '"order by \$id asc"', WORK_DIR, WORK_DIR, DL_CSV)
print(dl_cmd)
if src_space_id is not '0':
    dl_cmd = dl_cmd + ' -g {}'.format(src_space_id) # コマンド生成
subprocess.call(dl_cmd, shell=True) # コマンド実行
  
## ファイル処理（ビルトインフィールドを削除してアップロード用ファイルを作成）
with open(WORK_DIR + '/' + DL_CSV, 'r') as fin: # ファイルを読込モードでオープン
  reader = csv.reader(fin) # readerオブジェクトを作成
  reader_t = list(map(list, list(zip(*reader)))) # ビルトインフィールド削除前に、読込CSVの転置
  i=0
  for x in reader_t: # ビルトインフィールドの行を削除
    if reader_t[i][0] in BUILTIN_LIST:
        reader_t.pop(i)
        continue
    i += 1
  body = list(map(list, list(zip(*reader_t)))) # ビルトインフィールド削除後に、書込CSV用に転置
  with open(WORK_DIR + '/' + UL_CSV, 'w') as fout: # ファイルを書込モードでオープン
    writer = csv.writer(fout)  # writerオブジェクトを作成
    writer.writerows(body)  # アップロード用CSVを書き込む
      
## アップロードコマンド（ファイルとCSVをアップロード）
ul_cmd = '{} -a {} -d {} -t {} -b {} -f {}/{}'.format(CLI_KINTONE, tar_app_id, tar_subdomain, tar_api_token, WORK_DIR, WORK_DIR, UL_CSV)
print(ul_cmd)
if tar_space_id is not '0':
    ul_cmd = ul_cmd + ' -g {}'.format(tar_space_id) # コマンド生成
subprocess.call(ul_cmd, shell=True) # コマンド実行