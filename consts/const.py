from datetime import timedelta, timezone

# timezone
JST = timezone(timedelta(hours=+9), "JST")

# datetime <-> String の変換フォーマット(ISO)
LONG_DT_FORMAT = "%Y-%m-%d %H:%M:%S"
SHORT_DT_FORMAT = "%Y-%m-%d"
