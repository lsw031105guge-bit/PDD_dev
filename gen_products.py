import datetime
import json
import os
import random


def main() -> None:
    repo = os.path.join(os.path.dirname(__file__), "docs")
    random.seed(7)

    cats = [
        {
            "key": "slippers",
            "category": "居家拖鞋",
            "shortTitle": "静音拖鞋",
            "basePrice": 39,
            "tags": ["宿舍神器", "静音", "防滑"],
            "store": ["宿舍隐身装备店", "楼道轻音铺", "深夜生活馆"],
            "titles": ["凌晨三点拿外卖静音拖鞋", "下楼取快递无声拖鞋", "宿舍楼道轻音拖鞋"],
            "comments": [
                "室友到毕业都不知道我天天点夜宵。",
                "楼下保安都不知道我下来过。",
                "走路像踩棉花，社死概率下降。",
            ],
            "shipping": ["48小时内发货", "现货速发", "次日达"],
        },
        {
            "key": "socks",
            "category": "袜子",
            "shortTitle": "快乐袜子",
            "basePrice": 19,
            "tags": ["舒适", "百搭", "耐穿"],
            "store": ["打工人袜业", "宿舍洗衣房同款", "秋冬保暖铺"],
            "titles": ["一周不想洗的耐穿袜子", "室友看了都想要的快乐袜子", "加班续命不掉跟袜子"],
            "comments": [
                "穿上以后感觉自己更会生活了。",
                "买回来第一件事就是再买两双。",
                "脚不冷了，心态也稳了。",
            ],
            "shipping": ["24小时发货", "48小时内发货", "现货速发"],
        },
        {
            "key": "keyboard",
            "category": "办公键盘",
            "shortTitle": "Excel键盘",
            "basePrice": 199,
            "tags": ["办公室神器", "装忙", "摸鱼"],
            "store": ["摸鱼科技旗舰店", "表面功夫研究所", "工位装备仓"],
            "titles": ["老板来了自动切Excel键盘", "一键进入认真模式键盘", "开会专用装忙键盘"],
            "comments": [
                "老板现在觉得我是部门最努力的人。",
                "我没做事，但键盘看起来很忙。",
                "同事问我效率，我说是键盘带的。",
            ],
            "shipping": ["顺丰包邮", "48小时内发货", "现货当天发"],
        },
        {
            "key": "mirror",
            "category": "家居镜子",
            "shortTitle": "显瘦镜子",
            "basePrice": 129,
            "tags": ["居家好物", "情绪价值", "显瘦"],
            "store": ["夸夸镜旗舰店", "自信加油站", "租房美学馆"],
            "titles": ["可以骗自己减肥成功的镜子", "自带夸夸功能的全身镜", "照一下就想出门的镜子"],
            "comments": ["终于有人夸我瘦了。", "镜子比朋友还会夸人。", "照完很自信，出门五分钟就后悔。"],
            "shipping": ["送运费险", "坏了包赔", "48小时内发货"],
        },
        {
            "key": "cat_bed",
            "category": "宠物用品",
            "shortTitle": "云朵猫窝",
            "basePrice": 89,
            "tags": ["猫咪用品", "四季通用", "软乎乎"],
            "store": ["铲屎官研究所", "猫猫快乐屋", "云朵猫窝旗舰店"],
            "titles": ["猫不睡但一定会买的猫窝", "猫不进但你会坐的猫窝", "看着就想买的云朵猫窝"],
            "comments": ["猫没睡，我天天坐。", "猫不进，但我心安。", "买了以后我觉得自己很会养猫。"],
            "shipping": ["次日达", "48小时内发货", "现货速发"],
        },
        {
            "key": "umbrella",
            "category": "雨具伞具",
            "shortTitle": "透明雨伞",
            "basePrice": 59,
            "tags": ["颜值担当", "通勤", "耐用"],
            "store": ["雨天也要好看", "通勤小物店", "氛围感伞铺"],
            "titles": ["会发光的透明雨伞", "下雨也想出门的透明伞", "夜路回头率拉满的雨伞"],
            "comments": ["下雨终于不是坏事。", "撑着像MV主角。", "朋友问链接，我没敢发。"],
            "shipping": ["满2件包邮", "48小时内发货", "现货当天发"],
        },
        {
            "key": "humidifier",
            "category": "桌面小家电",
            "shortTitle": "迷你加湿器",
            "basePrice": 69,
            "tags": ["桌面", "养生", "氛围感"],
            "store": ["养生但熬夜旗舰店", "桌面小电器馆", "打工人补水站"],
            "titles": ["桌面迷你加湿器", "假装很养生的加湿器", "办公室补水小加湿器"],
            "comments": ["一开就像在认真生活。", "雾一出来，精神状态就高级了。", "加湿没加到多少，氛围加到了。"],
            "shipping": ["24小时内发货", "48小时内发货", "现货速发"],
        },
        {
            "key": "projector",
            "category": "数码家电",
            "shortTitle": "迷你投影",
            "basePrice": 399,
            "tags": ["宿舍神器", "数码", "追剧"],
            "store": ["宿舍电影院", "影音生活", "投影旗舰店"],
            "titles": ["宿舍迷你投影仪", "躺着追剧的投影仪", "租房小客厅投影仪"],
            "comments": ["宿舍直接变电影院。", "墙上放电影，心情立刻变好。", "本来没想买，刷着刷着就买了。"],
            "shipping": ["赠运费险", "48小时内发货", "顺丰包邮"],
        },
        {
            "key": "mouse_pad",
            "category": "电脑配件",
            "shortTitle": "暖手鼠标垫",
            "basePrice": 49,
            "tags": ["冬日限定", "发热", "办公"],
            "store": ["冬日工坊", "工位取暖站", "数码配件城"],
            "titles": ["USB暖手鼠标垫", "冬天办公续命发热鼠标垫", "写作业不冻手鼠标垫"],
            "comments": ["冬天写代码续命神器。", "手暖了以后人也没那么烦。", "办公室唯一的温暖。"],
            "shipping": ["次日发货", "48小时内发货", "现货速发"],
        },
        {
            "key": "alarm_clock",
            "category": "闹钟时钟",
            "shortTitle": "鼓励闹钟",
            "basePrice": 59,
            "tags": ["早八求生", "宿舍", "起床"],
            "store": ["早八商店", "起床困难户救援队", "闹钟旗舰店"],
            "titles": ["会说加油的闹钟", "早八起床情绪支持闹钟", "听了还是起不来的闹钟"],
            "comments": ["虽然还是起不来。", "它很努力，我也很努力。", "闹钟骂我两句我就醒了。"],
            "shipping": ["限时秒杀", "48小时内发货", "现货速发"],
        },
    ]

    batches = ["A", "B", "C"]
    items = []
    idx = 1
    for c in cats:
        for j in range(30):
            img = f"images/{c['key']}/{(j % 3) + 1:03d}.jpg"
            title = random.choice(c["titles"]) + random.choice([" 宿舍爆款", " 深夜剁手", " 网红同款", " 真的能买", " 离谱但好用"])
            price = round(c["basePrice"] + random.choice([-6, -3, 0, 3, 6]), 1)
            origin = round(price + random.choice([10, 20, 30, 40]), 1)
            item = {
                "id": f"p{idx:04d}",
                "batchLabel": batches[(idx - 1) % 3],
                "category": c["category"],
                "title": title,
                "shortTitle": c["shortTitle"],
                "coverUrl": img,
                "price": price,
                "originPrice": origin,
                "salesText": random.choice(["1.2万+", "2.8万+", "4.5万+", "5.8万+", "7.9万+", "10万+", "12万+", "18万+", "25万+", "33万+"]),
                "storeName": random.choice(c["store"]),
                "tags": c["tags"],
                "comment": random.choice(c["comments"]),
                "description": f"{c['category']}类真实风格商品图，标题离谱但图必须对得上。",
                "shippingText": random.choice(c["shipping"]),
            }
            items.append(item)
            idx += 1

    catalog = {
        "version": 1,
        "pageSize": 30,
        "batches": batches,
        "items": items,
        "generatedAt": datetime.datetime.utcnow().isoformat() + "Z",
    }

    os.makedirs(repo, exist_ok=True)
    with open(os.path.join(repo, "products.json"), "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, separators=(",", ":"))

    print("items", len(items))


if __name__ == "__main__":
    main()
