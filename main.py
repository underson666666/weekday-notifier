#!/usr/bin/python3
import datetime
import os

import requests

import const


def get_WeekNum_and_DayOfWeek(date_: datetime.date) -> tuple:
    """
    Return
    ------
    week_num: int
        対象の日付が第X週
    DayOfWeek: str
        曜日
    """
    # weekday()で取得した数値を曜日に変換するためのリスト
    lists = ["月", "火", "水", "木", "金", "土", "日"]
    divmod_ = divmod(date_.day, 7)  # 日付を７で割って商と余りを取得

    # 商が0＝日付が6日以下の場合は第一週
    if divmod_[0] == 0:
        week_num = 1
    # 余りが0＝7の倍数の日数は商＝第X週
    elif divmod_[1] == 0:
        week_num = divmod_[0]
    # それ以外＝商が1以上かつあまりもある⇒商＋1＝第X週
    else:
        week_num = divmod_[0] + 1

    # 戻り値は第X週と曜日の二つ
    return (week_num, lists[date_.weekday()])


def main():
    today = datetime.date.today()
    tommorow = today + datetime.timedelta(days=1)
    # こんな感じで変数を戻り値分用意すればそれぞれの変数に直性代入できる
    week_num, DayOfWeek = get_WeekNum_and_DayOfWeek(tommorow)

    # print(f"{today}は第{week_num}{DayOfWeek}曜日")

    messages = build_message(week_num, DayOfWeek)
    if not messages:
        return

    message = str()
    msg = f"\n明日 {tommorow} は\n"
    for message in messages:
        msg += message + "\n"
    else:
        msg += "です。"

    notify_line(msg)


def build_message(week_num, day_of_week):
    """
    Returns
    -------
    str
    """
    m = list()

    # search data
    a = set(
        filter(lambda x: x[0] == week_num and x[1] == day_of_week, const.WEEK_DAY_SCHED)
    )
    if a:
        m.append(f"第{week_num}{day_of_week}曜日 なので")
    for s in a:
        # _ = f"- 明日 {tommorow} は 第{s[0]}{s[1]}曜日 なので {s[2]} 日"
        _ = f"  {s[2]} 日"
        m.append(_)

    # searhc every week data
    b = set(filter(lambda x: x[0] == 0 and x[1] == day_of_week, const.WEEK_DAY_SCHED))
    if b:
        m.append(f"{day_of_week}曜日 なので")
    for s in b:
        _ = f"  {s[2]}"
        m.append(_)

    return m


def notify_line(message: str):
    """notify to line notify

    Parameters
    ----------
    message: str
        通知するメッセージ
    """
    api_token = os.getenv("LINE_API_TOKEN")
    headers = {"Authorization": f"Bearer {api_token}"}
    data = {"message": message}
    res = requests.post(const.LINE_NOTIFY_API, headers=headers, data=data)

    if res.status_code != requests.codes.ok:
        print("failed to send message.")


if __name__ == "__main__":
    main()
