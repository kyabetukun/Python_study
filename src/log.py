from distutils.debug import DEBUG
from logging import getLogger,StreamHandler,DEBUG,ERROR, Formatter
# ログ出力
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG) #DEBUG以上の重大なログを扱う
logger.setLevel(DEBUG)  #DEBUG以上の重大なログを扱う 
logger.addHandler(handler)
logger.debug("これはデバッグログです")

#ログのレベル
#DEBUG  プログラム内の情報を出力 debug()
#INFO 正常な動きをしている情報 info()
#WARNING 警告をしている waning()
#ERROR 問題が起きた時 error()
#CRITICAL とても重大な問題 critical()


#ログの出力形式 時間とかレベル、どのファイルが分かったら便利
#Formatter
#ログのレベル '%(levelname)s'
#時間 '%(asctime)s'
#%(message)s'
#%(filename)s'
formatter = Formatter('[%(levelname)s]%(asctime)s-%(message)s(%(filename)s)')

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG) #DEBUG以上の重大なログを扱う
logger.setLevel(DEBUG)  #DEBUG以上の重大なログを扱う 
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.debug("これはデバッグログです")
logger.error("ファイルがありません")