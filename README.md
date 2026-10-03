# Simorgh Channels

The curated registry of public Telegram channels that post free proxy
configurations, consumed by the **Simorgh** server-discovery harvest in
[HELBOYCODER/simorgh-servers](https://github.com/HELBOYCODER/simorgh-servers).
The seed list is taken from [zeghostwriter/ZeroNet](https://github.com/zeghostwriter/ZeroNet)
(MIT; see [NOTICE](NOTICE)).

## The registry

[`channels.json`](channels.json) is a JSON array; every entry has exactly:

| key | meaning |
| --- | --- |
| `id` | unique short name, the channel's t.me username |
| `name` | display name |
| `url` | `https://t.me/<username>` — read through the public web preview |
| `tier` | `1` priority (harvested every 10 min by the `fresh` workflow), `2` directory (lists other channels; crawled for new ones), `3` general channel |
| `language` | primary language tag of the channel, `fa` for Persian |

The `channels-lint` workflow validates the schema on every PR and push, so
the harvest can always read this file from a commit that lints clean. Raw
URL the harvest and other tools fetch:

```
https://raw.githubusercontent.com/HELBOYCODER/simorgh-channels/main/channels.json
https://cdn.jsdelivr.net/gh/HELBOYCODER/simorgh-channels@main/channels.json
```

Note: the simorgh-servers harvest currently reads its own seed file
`deploy/crowd/telegram-channels.json` (upstream's layout, kept working). This
registry is the curated, linted source of truth; adopting it on the harvest
side is a one-line change to its `--telegram` argument later.

## Adding or removing a channel

Open a pull request editing `channels.json`:

- one channel per entry, keys exactly as in the table above,
- `id` unique and equal to the channel's public t.me username,
- a channel counts as a source only if its page is in Persian and it posts
  configs; the harvest drops channels that have posted nothing for two
  weeks, so stale entries can simply be deleted.

Nothing here endorses a channel or any configuration posted in one; every
config found is tested before it can reach a user, and only encrypted
transports are kept.

---

## بخش فارسی (فارسی)

<div dir="rtl">

### این مخزن چیست؟

فهرست انتخاب‌شده‌ی کانال‌های عمومی تلگرام که کانفیگ‌های رایگان منتشر می‌کنند و
برداشت سرور سیمورغ آن‌ها را می‌خواند. فایل `channels.json` یک آرایه‌ی JSON است و
هر ورودی پنج کلید دارد: `id` (نام کاربری عمومی کانال)، `name` (نام نمایشی)،
`url` (نشانی `https://t.me/…`)، `tier` (۱ اولویت: هر ۱۰ دقیقه خوانده می‌شود؛ ۲
فهرست‌ساز: کانال‌های دیگر را معرفی می‌کند؛ ۳ کانال عمومی) و `language`. گردش
کاری `channels-lint` در هر pull request شکل فایل را بررسی می‌کند تا برداشت همیشه
از یک نسخه‌ی سالم بخواند.

### چطور کانالی اضافه یا حذف کنیم؟

یک PR برای ویرایش `channels.json` بزنید؛ `id` باید همان نام کاربری عمومی کانال و
یکتا باشد. کانالی که دو هفته کانفیگ نگذارد، توسط برداشت نادیده گرفته می‌شود و
می‌توانید خودِ آن را از فهرست حذف کنید. افزودن کانال به معنای تأیید آن نیست: هر کانفیگ
پیش از رسیدن به کاربر آزمایش می‌شود و فقط ترافیک رمزنگاری‌شده نگه داشته می‌شود.

### اعتبار

این فهرست از پروژه‌ی zeghostwriter/ZeroNet (با مجوز MIT) برداشته شده و در
NOTICE توضیح داده شده است. کانال‌های تلگرام اشخاص ثالث‌اند و پروژه‌ی سیمورغ
هیچ کانالی را بهره‌برداری یا تأیید نمی‌کند.

</div>
